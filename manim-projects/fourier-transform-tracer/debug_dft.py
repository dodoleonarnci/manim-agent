"""
Debug script to verify DFT reconstruction matches original points
"""
import numpy as np
import cmath
from manim import PI, TAU

def compute_dft_fast(signal):
    """Fast DFT using NumPy FFT."""
    coeffs = np.fft.fft(signal) / len(signal)
    coeffs = np.fft.fftshift(coeffs)  # Shift zero frequency to center
    return coeffs

def create_simple_shape_points(shape_type="circle", num_samples=200, radius=2):
    """Create points for simple test shapes."""
    t = np.linspace(0, 1, num_samples, endpoint=False)

    if shape_type == "circle":
        points = radius * np.exp(2j * PI * t)
    elif shape_type == "heart":
        angle = 2 * PI * t
        x = 16 * np.sin(angle)**3
        y = 13 * np.cos(angle) - 5 * np.cos(2*angle) - 2 * np.cos(3*angle) - np.cos(4*angle)
        points = (x + 1j * y) * radius / 20
    else:
        points = radius * np.exp(2j * PI * t)

    return points

def reconstruct_from_dft(coefficients, frequencies, t_values, num_epicycles=None):
    """Reconstruct signal from DFT coefficients at given time values."""
    N = len(coefficients)

    # If num_epicycles specified, use only top coefficients
    if num_epicycles is not None and num_epicycles < N:
        # Sort by magnitude and take top N
        coeff_freq_pairs = list(zip(coefficients, frequencies))
        sorted_pairs = sorted(coeff_freq_pairs, key=lambda x: abs(x[0]), reverse=True)
        top_pairs = sorted_pairs[:num_epicycles]
        coefficients = [c for c, f in top_pairs]
        frequencies = [f for c, f in top_pairs]

    reconstructed = []
    for t in t_values:
        # Sum up all rotating phasors
        point = 0 + 0j
        for coeff, freq in zip(coefficients, frequencies):
            # Rotate coefficient by frequency and time
            point += coeff * cmath.exp(1j * freq * t)
        reconstructed.append(point)

    return np.array(reconstructed)

# Test with a simple circle
print("Testing with CIRCLE shape...")
print("=" * 60)

num_samples = 100
original_points = create_simple_shape_points("circle", num_samples=num_samples, radius=2)

# Compute DFT
coefficients = compute_dft_fast(original_points)
N = len(coefficients)

# Create frequency indices centered around 0
frequencies = np.arange(-N//2, N//2)

print(f"Number of sample points: {num_samples}")
print(f"Number of DFT coefficients: {len(coefficients)}")
print(f"Frequency range: {frequencies[0]} to {frequencies[-1]}")

# Test reconstruction at t values corresponding to original sampling
# Original samples were at t ∈ [0, 1), so we use t ∈ [0, 2π)
t_values = np.linspace(0, 2*PI, num_samples, endpoint=False)

# Reconstruct with ALL coefficients
reconstructed_full = reconstruct_from_dft(coefficients, frequencies, t_values)

# Compute error
error_full = np.abs(original_points - reconstructed_full)
max_error_full = np.max(error_full)
mean_error_full = np.mean(error_full)

print(f"\nReconstruction with ALL {len(coefficients)} coefficients:")
print(f"  Max error: {max_error_full:.2e}")
print(f"  Mean error: {mean_error_full:.2e}")

# Test with reduced epicycles
for num_epi in [50, 20, 10]:
    reconstructed_partial = reconstruct_from_dft(coefficients, frequencies, t_values, num_epicycles=num_epi)
    error_partial = np.abs(original_points - reconstructed_partial)
    max_error_partial = np.max(error_partial)
    mean_error_partial = np.mean(error_partial)
    print(f"\nReconstruction with {num_epi} epicycles:")
    print(f"  Max error: {max_error_partial:.2e}")
    print(f"  Mean error: {mean_error_partial:.2e}")

# Now test with HEART shape
print("\n" + "=" * 60)
print("Testing with HEART shape...")
print("=" * 60)

original_points_heart = create_simple_shape_points("heart", num_samples=num_samples, radius=2)

# Compute DFT
coefficients_heart = compute_dft_fast(original_points_heart)
frequencies_heart = np.arange(-N//2, N//2)

# Reconstruct with ALL coefficients
reconstructed_full_heart = reconstruct_from_dft(coefficients_heart, frequencies_heart, t_values)

# Compute error
error_full_heart = np.abs(original_points_heart - reconstructed_full_heart)
max_error_full_heart = np.max(error_full_heart)
mean_error_full_heart = np.mean(error_full_heart)

print(f"\nReconstruction with ALL {len(coefficients_heart)} coefficients:")
print(f"  Max error: {max_error_full_heart:.2e}")
print(f"  Mean error: {mean_error_full_heart:.2e}")

# Check if the issue is with time parametrization
print("\n" + "=" * 60)
print("Testing TIME PARAMETRIZATION...")
print("=" * 60)

# The animation uses time_tracker going from 0 to 3*TAU
# Let's see what happens at different time ranges
for time_range_name, time_end in [("0 to 2π", 2*PI), ("0 to 2*TAU (4π)", 2*TAU), ("0 to 3*TAU (6π)", 3*TAU)]:
    t_test = np.linspace(0, time_end, num_samples, endpoint=False)
    reconstructed_test = reconstruct_from_dft(coefficients, frequencies, t_test)

    print(f"\nTime range {time_range_name}:")
    print(f"  First 3 points: {reconstructed_test[:3]}")
    print(f"  Last 3 points: {reconstructed_test[-3:]}")

    # Check if it traces the circle once, twice, or three times
    # For a circle, we expect it to return to start after one full period
    distance_from_start = np.abs(reconstructed_test[-1] - reconstructed_test[0])
    print(f"  Distance from start to end: {distance_from_start:.4f}")

print("\n" + "=" * 60)
print("DIAGNOSIS:")
print("=" * 60)
print("The DFT assumes the signal is PERIODIC with period N samples.")
print("When we animate from t=0 to t=3*TAU, we're tracing the shape 3 times.")
print("The key is that frequencies are in units of 2π/N, not 2π.")
