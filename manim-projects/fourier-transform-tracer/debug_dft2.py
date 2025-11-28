"""
Debug script - Testing the EXACT formula used in the animation
"""
import numpy as np
import cmath
from manim import PI, TAU

def compute_dft_fast(signal):
    """Fast DFT using NumPy FFT - EXACT copy from animation.py"""
    coeffs = np.fft.fft(signal) / len(signal)
    coeffs = np.fft.fftshift(coeffs)  # Shift zero frequency to center
    return coeffs

def create_simple_shape_points(shape_type="circle", num_samples=200, radius=2):
    """Create points - EXACT copy from animation.py"""
    t = np.linspace(0, 1, num_samples, endpoint=False)

    if shape_type == "circle":
        points = radius * np.exp(2j * PI * t)
    else:
        angle = 2 * PI * t
        x = 16 * np.sin(angle)**3
        y = 13 * np.cos(angle) - 5 * np.cos(2*angle) - 2 * np.cos(3*angle) - np.cos(4*angle)
        points = (x + 1j * y) * radius / 20

    return points

# Create the shape EXACTLY as the animation does
num_samples = 1000  # From params.py NUM_SAMPLES
original_points = create_simple_shape_points("heart", num_samples=num_samples, radius=2.0)

# Compute DFT EXACTLY as animation does
coefficients = compute_dft_fast(original_points)
N = len(coefficients)

# Create frequency indices EXACTLY as animation does
freqs = np.arange(-N//2, N//2)

print(f"Original shape: HEART with {num_samples} sample points")
print(f"DFT coefficients: {len(coefficients)}")
print(f"Frequency range: {freqs[0]} to {freqs[-1]}")
print()

# Sort by magnitude and take top epicycles EXACTLY as animation does
num_epicycles = 50  # Reasonable number for testing
coeff_freq_pairs = list(zip(coefficients, freqs))
sorted_pairs = sorted(coeff_freq_pairs, key=lambda x: abs(x[0]), reverse=True)
top_pairs = sorted_pairs[:num_epicycles]

top_coeffs = [c for c, f in top_pairs]
top_freqs = [f for c, f in top_pairs]

print(f"Using top {num_epicycles} epicycles")
print(f"Top 5 frequencies: {top_freqs[:5]}")
print(f"Top 5 magnitudes: {[abs(c) for c in top_coeffs[:5]]}")
print()

# NOW: Reconstruct using the EXACT formula from animation.py line 627
# rotated = coeff * cmath.exp(1j * freq * time)
# where time goes from 0 to 3*TAU

def reconstruct_exact_animation_formula(coeffs, freqs, num_points=100):
    """Use EXACT formula from animation update_epicycles function"""
    # Animation uses time from 0 to 3*TAU
    time_values = np.linspace(0, 3*TAU, num_points, endpoint=False)

    reconstructed = []
    for time in time_values:
        # Sum all epicycles (line 623-639 in animation.py)
        current_pos = 0 + 0j
        for coeff, freq in zip(coeffs, freqs):
            # Line 627: rotated = coeff * cmath.exp(1j * freq * time)
            rotated = coeff * cmath.exp(1j * freq * time)
            current_pos += rotated
        reconstructed.append(current_pos)

    return np.array(reconstructed), time_values

# Test reconstruction
reconstructed, time_vals = reconstruct_exact_animation_formula(top_coeffs, top_freqs, num_points=num_samples)

print("=" * 70)
print("ISSUE DIAGNOSIS:")
print("=" * 70)
print()
print("The problem is in the TIME PARAMETRIZATION!")
print()
print("The DFT formula assumes frequencies are INTEGER multiples of 2π/N,")
print("where N is the number of sample points.")
print()
print(f"For N={num_samples} samples:")
print(f"  - Frequency k={top_freqs[0]} corresponds to {top_freqs[0]} cycles over 2π")
print(f"  - But we're animating time from 0 to 3*TAU = 6π")
print()
print("CORRECT formula should be:")
print("  rotated = coeff * exp(i * freq * 2π * time)")
print("  where time goes from 0 to 1 (or 0 to 3 for 3 rotations)")
print()
print("CURRENT formula in animation.py line 627:")
print("  rotated = coeff * exp(i * freq * time)")
print("  where time goes from 0 to 3*TAU")
print()
print("This causes FREQUENCY MISMATCH because:")
print(f"  - Frequency {top_freqs[0]} rotates at {top_freqs[0]}*3*TAU = {top_freqs[0]*3*2*PI:.1f} rad")
print(f"  - Instead of {top_freqs[0]}*2π*3 = {top_freqs[0]*2*PI*3:.1f} rad")
print()

# Test the CORRECT formula
def reconstruct_correct_formula(coeffs, freqs, num_rotations=3):
    """Use CORRECT DFT reconstruction formula"""
    # Time should go from 0 to num_rotations (for full rotations)
    # We need to sample at the same rate as original
    num_points_per_rotation = len(original_points)
    total_points = num_points_per_rotation * num_rotations
    time_values = np.linspace(0, num_rotations, total_points, endpoint=False)

    reconstructed = []
    for time in time_values:
        current_pos = 0 + 0j
        for coeff, freq in zip(coeffs, freqs):
            # CORRECT: rotated = coeff * cmath.exp(1j * freq * 2*PI * time)
            rotated = coeff * cmath.exp(1j * freq * 2*PI * time)
            current_pos += rotated
        reconstructed.append(current_pos)

    return np.array(reconstructed), time_values

reconstructed_correct, time_vals_correct = reconstruct_correct_formula(top_coeffs, top_freqs, num_rotations=3)

# Compare with original points (repeating 3 times for 3 rotations)
original_repeated = np.tile(original_points, 3)

error_correct = np.abs(original_repeated - reconstructed_correct)
print(f"Error with CORRECT formula (using top {num_epicycles} epicycles):")
print(f"  Max error: {np.max(error_correct):.4f}")
print(f"  Mean error: {np.mean(error_correct):.4f}")
print()

print("=" * 70)
print("SOLUTION:")
print("=" * 70)
print()
print("Change line 627 in animation.py from:")
print("    rotated = coeff * cmath.exp(1j * freq * time)")
print()
print("To:")
print("    rotated = coeff * cmath.exp(1j * freq * 2 * PI * time)")
print()
print("And change line 649 from:")
print("    time_tracker.animate.set_value(3 * TAU)")
print()
print("To:")
print("    time_tracker.animate.set_value(3)  # 3 full rotations")
