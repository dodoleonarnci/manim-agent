"""
Fourier Transform Epicycles - SVG Tracing Animation

This module implements a three-scene animation demonstrating how Fourier Transform
can decompose any closed curve into rotating circles (epicycles).

Scenes:
1. Fourier Transform Basics (~8 seconds) - Frequency decomposition concept
2. Epicycle Mechanics (~10 seconds) - Rotating circles demonstration
3. SVG Tracing (~30 seconds) - Full epicycle drawing of custom SVG
"""

from manim import *
import numpy as np
import cmath
import params  # Import all configurable parameters


# ============================================================================
# UTILITY FUNCTIONS FOR FOURIER ANALYSIS
# ============================================================================

def compute_dft(signal):
    """
    Compute Discrete Fourier Transform of a complex signal.

    Args:
        signal: List or array of complex numbers representing 2D points

    Returns:
        Array of complex Fourier coefficients
    """
    N = len(signal)
    coefficients = []

    for k in range(N):
        sum_val = 0 + 0j
        for n in range(N):
            angle = -2 * PI * k * n / N
            sum_val += signal[n] * cmath.exp(1j * angle)
        coefficients.append(sum_val / N)

    return np.array(coefficients)


def compute_dft_fast(signal):
    """
    Fast DFT using NumPy FFT.

    Args:
        signal: List or array of complex numbers

    Returns:
        Array of complex Fourier coefficients (shifted so k=0 is at center)
    """
    coeffs = np.fft.fft(signal) / len(signal)
    coeffs = np.fft.fftshift(coeffs)  # Shift zero frequency to center
    return coeffs


def extract_svg_points(svg_mobject, num_samples=200):
    """
    Extract evenly spaced points from SVG path.

    Args:
        svg_mobject: Manim SVGMobject
        num_samples: Number of points to sample

    Returns:
        Array of complex numbers representing the path
    """
    # Get the submobject with the most points (main shape)
    # This handles complex SVGs with multiple paths
    if len(svg_mobject.submobjects) > 0:
        # Find submobject with most points
        largest_submobject = max(svg_mobject.submobjects, key=lambda s: len(s.points))
        path = largest_submobject

        # Debug info
        print(f"SVG has {len(svg_mobject.submobjects)} submobjects")
        print(f"Using submobject with {len(path.points)} points (largest)")
    else:
        path = svg_mobject

    # Get evenly spaced points along the path
    points = []
    for alpha in np.linspace(0, 1, num_samples, endpoint=False):
        point = path.point_from_proportion(alpha)
        points.append(point)

    # Convert to complex numbers (z = x + iy)
    complex_points = np.array([p[0] + 1j * p[1] for p in points])

    # Center the curve at origin
    mean = np.mean(complex_points)
    complex_points -= mean

    return complex_points


def create_simple_shape_points(shape_type="circle", num_samples=200, radius=2):
    """
    Create points for simple test shapes.

    Args:
        shape_type: "circle", "square", "heart", or "star"
        num_samples: Number of points to sample
        radius: Size of the shape

    Returns:
        Array of complex numbers
    """
    t = np.linspace(0, 1, num_samples, endpoint=False)

    if shape_type == "circle":
        points = radius * np.exp(2j * PI * t)

    elif shape_type == "square":
        # Parametric square
        x = np.where(t < 0.25, 4*t,
            np.where(t < 0.5, 1,
            np.where(t < 0.75, 1 - 4*(t-0.5), -1)))
        y = np.where(t < 0.25, -1,
            np.where(t < 0.5, -1 + 4*(t-0.25),
            np.where(t < 0.75, 1, 1 - 4*(t-0.75))))
        points = radius * (x + 1j * y)

    elif shape_type == "heart":
        # Heart curve using parametric equations
        angle = 2 * PI * t
        x = 16 * np.sin(angle)**3
        y = 13 * np.cos(angle) - 5 * np.cos(2*angle) - 2 * np.cos(3*angle) - np.cos(4*angle)
        points = (x + 1j * y) * radius / 20

    elif shape_type == "star":
        # 5-pointed star
        angle = 2 * PI * t
        r = np.where(np.mod(angle, 2*PI/5) < PI/5, radius, radius * 0.4)
        points = r * np.exp(1j * angle)

    else:
        # Default to circle
        points = radius * np.exp(2j * PI * t)

    return points


# ============================================================================
# SCENE 1: FOURIER TRANSFORM BASICS
# ============================================================================

class Scene1_FourierBasics(Scene):
    """
    Introduces Fourier Transform concept by decomposing a composite wave
    into its frequency components.

    Duration: ~8 seconds
    """

    def construct(self):
        self.scene1_animation()

    def scene1_animation(self):
        """Scene 1 animation logic (can be called from combined scene)"""
        # Title
        title = Text("Fourier Transform: Decomposing Signals", font_size=params.TITLE_FONT_SIZE)
        self.play(Write(title), run_time=params.SCENE1_TITLE_WRITE_TIME)
        self.play(title.animate.scale(params.MEDIUM_TITLE_SCALE).to_edge(UP), run_time=params.SCENE1_TITLE_SCALE_TIME)

        # Create axes for the signal
        axes = Axes(
            x_range=[params.AXES_X_RANGE[0] * PI, params.AXES_X_RANGE[1] * PI, params.AXES_X_RANGE[2] * PI],
            y_range=params.AXES_Y_RANGE,
            x_length=params.AXES_X_LENGTH,
            y_length=params.AXES_Y_LENGTH,
            axis_config={"include_tip": False}
        ).shift(DOWN * params.SCENE1_AXES_SHIFT_DOWN)

        # Combined wave function using parameters
        def combined_wave(x):
            return (params.WAVE_AMPLITUDES[0] * np.sin(params.WAVE_FREQUENCIES[0] * x) +
                    params.WAVE_AMPLITUDES[1] * np.sin(params.WAVE_FREQUENCIES[1] * x) +
                    params.WAVE_AMPLITUDES[2] * np.sin(params.WAVE_FREQUENCIES[2] * x))

        combined = axes.plot(combined_wave, color=WHITE, stroke_width=params.COMBINED_WAVE_STROKE_WIDTH)

        # Animate the combined wave
        self.play(Create(axes), run_time=params.SCENE1_AXES_CREATE_TIME)
        self.play(Create(combined), run_time=params.SCENE1_WAVE_CREATE_TIME)

        # Decompose into components using parameters
        wave_colors = [globals()[c] for c in params.WAVE_COLORS]  # Convert string names to colors
        waves = [
            axes.plot(
                lambda x, i=i: params.WAVE_AMPLITUDES[i] * np.sin(params.WAVE_FREQUENCIES[i] * x),
                color=wave_colors[i]
            )
            for i in range(3)
        ]

        # Labels for components
        labels = [
            Text(f"ω{params.WAVE_FREQUENCIES[i]}", color=wave_colors[i], font_size=params.LABEL_FONT_SIZE).next_to(waves[i], RIGHT)
            for i in range(3)
        ]

        # Shift waves vertically for separation
        for wave, label in zip(waves, labels):
            wave.shift(UP * params.SCENE1_WAVE_SEPARATION_SHIFT)
            label.shift(UP * params.SCENE1_WAVE_SEPARATION_SHIFT)

        # Transform to components
        self.play(
            *[TransformFromCopy(combined, wave) for wave in waves],
            *[Write(label) for label in labels],
            combined.animate.set_opacity(params.SCENE1_FADED_OPACITY),
            axes.animate.set_opacity(params.SCENE1_FADED_OPACITY),
            run_time=params.SCENE1_DECOMPOSE_TIME
        )

        self.wait(params.SCENE1_WAIT_TIME)

        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=params.SCENE1_FADEOUT_TIME
        )


# ============================================================================
# SCENE 1.5: ROTATION TO WAVES CONNECTION
# ============================================================================

class Scene1_5_RotationToWaves(Scene):
    """
    Brief transition scene showing how rotating vectors create sinusoidal waves.
    Connects the Fourier decomposition from Scene 1 to epicycles in Scene 2.

    Duration: ~5 seconds
    """

    def construct(self):
        self.scene1_5_animation()

    def scene1_5_animation(self):
        """Scene 1.5 animation logic (can be called from combined scene)"""
        # Title
        title = Text("Rotation = Sinusoidal Motion", font_size=params.TITLE_FONT_SIZE - 4)
        self.play(Write(title), run_time=params.SCENE1_5_TITLE_WRITE_TIME)
        self.play(title.animate.scale(params.MEDIUM_TITLE_SCALE).to_edge(UP), run_time=params.SCENE1_5_TITLE_SCALE_TIME)

        # Create a rotating arrow/vector on the left
        radius = params.SCENE1_5_ARROW_RADIUS
        circle_color = globals()[params.SCENE1_5_CIRCLE_COLOR]
        circle = Circle(radius=radius, color=circle_color, stroke_width=params.SCENE1_5_CIRCLE_STROKE_WIDTH)
        circle.shift(LEFT * params.SCENE1_5_CIRCLE_SHIFT)

        arrow = Arrow(
            start=circle.get_center(),
            end=circle.get_center() + radius * RIGHT,
            color=circle_color,
            buff=0,
            stroke_width=params.SCENE1_5_ARROW_STROKE_WIDTH,
            max_tip_length_to_length_ratio=params.SCENE1_5_ARROW_TIP_RATIO
        )

        # Axes for wave projection on the right
        axes = Axes(
            x_range=[0, 2*PI, PI],
            y_range=params.SCENE1_5_AXES_Y_RANGE,
            x_length=params.SCENE1_5_AXES_X_LENGTH,
            y_length=params.SCENE1_5_AXES_Y_LENGTH,
            axis_config={"include_tip": False}
        ).shift(RIGHT * params.SCENE1_5_AXES_SHIFT_X + DOWN * params.SCENE1_5_AXES_SHIFT_Y)

        # Show circle and arrow
        self.play(Create(circle), GrowArrow(arrow), run_time=params.SCENE1_5_CIRCLE_CREATE_TIME)

        # Show axes
        self.play(Create(axes), run_time=params.SCENE1_5_AXES_CREATE_TIME)

        # ValueTracker for rotation
        time_tracker = ValueTracker(0)

        # Wave path that will be traced
        wave_points = []

        def get_wave_point():
            """Get current point on the wave based on rotation angle"""
            t = time_tracker.get_value()
            x = t
            y = radius * np.sin(t)
            if x <= 2*PI:
                return axes.c2p(x, y)
            else:
                return axes.c2p(2*PI, y)

        # Traced path for the wave
        wave_trace = TracedPath(
            get_wave_point,
            stroke_width=params.SCENE1_5_WAVE_STROKE_WIDTH,
            stroke_color=circle_color,
            dissipating_time=None
        )
        self.add(wave_trace)

        # Dot at the tip of the arrow
        tip_dot_color = globals()[params.SCENE1_5_TIP_DOT_COLOR]
        tip_dot = Dot(arrow.get_end(), color=tip_dot_color, radius=params.SCENE1_5_TIP_DOT_RADIUS)
        self.add(tip_dot)

        # Projection line from arrow tip to wave
        projection_line_color = globals()[params.SCENE1_5_PROJECTION_LINE_COLOR]
        projection_line = always_redraw(
            lambda: DashedLine(
                arrow.get_end(),
                get_wave_point(),
                color=projection_line_color,
                stroke_width=params.SCENE1_5_PROJECTION_STROKE_WIDTH,
                dash_length=params.SCENE1_5_PROJECTION_DASH_LENGTH
            )
        )
        self.add(projection_line)

        # Updater for rotating arrow
        def update_arrow(mob):
            angle = time_tracker.get_value()
            center = circle.get_center()
            new_end = center + radius * np.array([np.cos(angle), np.sin(angle), 0])
            arrow.put_start_and_end_on(center, new_end)
            tip_dot.move_to(arrow.get_end())

        arrow.add_updater(update_arrow)

        # Animate one full rotation
        self.play(
            time_tracker.animate.set_value(2 * PI),
            run_time=params.SCENE1_5_ROTATION_DURATION,
            rate_func=linear
        )

        arrow.remove_updater(update_arrow)

        self.wait(params.SCENE1_5_WAIT_TIME)

        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=params.SCENE1_5_FADEOUT_TIME
        )


# ============================================================================
# SCENE 2: EPICYCLE MECHANICS
# ============================================================================

class Scene2_EpicycleMechanics(Scene):
    """
    Demonstrates how epicycles (circles upon circles) work with rotating arrows.
    Shows 3-4 epicycles connected head-to-tail.

    Duration: ~10 seconds
    """

    def construct(self):
        self.scene2_animation()

    def scene2_animation(self):
        """Scene 2 animation logic (can be called from combined scene)"""
        # Title
        title = Text("Epicycles: Circles Upon Circles", font_size=params.TITLE_FONT_SIZE)
        self.play(Write(title), run_time=params.SCENE2_TITLE_WRITE_TIME)
        self.play(title.animate.scale(params.MEDIUM_TITLE_SCALE).to_edge(UP), run_time=params.SCENE2_TITLE_SCALE_TIME)

        # Epicycle parameters
        radii = params.SCENE2_RADII
        frequencies = params.SCENE2_FREQUENCIES
        colors = [globals()[c] for c in params.SCENE2_COLORS]

        # Create circles and arrows with correct initial positions (head-to-tail at t=0)
        circles = VGroup()
        arrows = VGroup()

        current_pos = ORIGIN
        for i, (r, freq, color) in enumerate(zip(radii, frequencies, colors)):
            # Initial angle at t=0
            angle = 0  # Start all at zero rotation

            # Calculate arrow end position
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            new_end = current_pos + r * direction

            # Create circle centered at current position
            circle = Circle(radius=r, color=color, stroke_width=params.SCENE2_CIRCLE_STROKE_WIDTH)
            circle.move_to(current_pos)

            # Create arrow from current position to new end
            arrow = Arrow(
                start=current_pos,
                end=new_end,
                color=color,
                buff=0,
                stroke_width=params.SCENE2_ARROW_STROKE_WIDTH,
                max_tip_length_to_length_ratio=params.SCENE2_ARROW_TIP_RATIO
            )

            circles.add(circle)
            arrows.add(arrow)

            # Next epicycle starts at the tip of this arrow
            current_pos = new_end

        # Show first epicycle
        self.play(
            Create(circles[0]),
            GrowArrow(arrows[0]),
            run_time=params.SCENE2_FIRST_EPICYCLE_CREATE_TIME
        )

        # Add remaining epicycles one by one
        for i in range(1, len(radii)):
            self.play(
                Create(circles[i]),
                GrowArrow(arrows[i]),
                run_time=params.SCENE2_REMAINING_EPICYCLE_CREATE_TIME
            )

        # Setup traced path
        trace_color = globals()[params.SCENE2_TRACE_COLOR]
        trace = TracedPath(
            lambda: arrows[-1].get_end(),
            stroke_width=params.SCENE2_TRACE_STROKE_WIDTH,
            stroke_color=trace_color,
            dissipating_time=None
        )
        self.add(trace)

        # Use ValueTracker for explicit time control
        time_tracker = ValueTracker(0)

        # Animation function for rotating epicycles
        def update_epicycles(mob):
            """Update positions of all epicycles"""
            time = time_tracker.get_value()

            for i, (arrow, freq, radius) in enumerate(zip(arrows, frequencies, radii)):
                # Calculate rotation angle
                angle = freq * 2 * PI * time

                # Determine center (tip of previous arrow or origin)
                if i == 0:
                    center = ORIGIN
                else:
                    center = arrows[i-1].get_end()

                # Calculate new arrow position
                direction = np.array([np.cos(angle), np.sin(angle), 0])
                new_end = center + radius * direction

                # Update arrow
                arrow.put_start_and_end_on(center, new_end)

                # Update circle position
                circles[i].move_to(center)

        # Add updater only once to avoid redundant calls
        # The update function already updates all arrows and circles
        arrows[0].add_updater(update_epicycles)

        # Animate rotation
        self.play(
            time_tracker.animate.set_value(params.SCENE2_NUM_ROTATIONS),
            run_time=params.SCENE2_ROTATION_DURATION,
            rate_func=linear
        )

        # Remove updater
        arrows[0].remove_updater(update_epicycles)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=params.SCENE2_FADEOUT_TIME
        )


# ============================================================================
# SCENE 3: SVG TRACING WITH FULL EPICYCLES
# ============================================================================

class Scene3_SVGTracing(Scene):
    """
    Full demonstration: Load SVG (or use default shape), compute DFT,
    and animate epicycles tracing the shape.

    Duration: ~30 seconds

    Args:
        svg_path: Path to SVG file (optional, uses default heart shape if not provided)
        num_epicycles: Number of epicycles to use (default: 50)
        num_samples: Number of points to sample from curve (default: 200)
    """

    def __init__(self, **kwargs):
        self.svg_path = params.DEFAULT_SVG_PATH
        self.num_epicycles = params.NUM_EPICYCLES
        self.num_samples = params.NUM_SAMPLES
        super().__init__(**kwargs)

    def construct(self):
        self.scene3_animation()

    def scene3_animation(self):
        """Scene 3 animation logic (can be called from combined scene)"""
        # Title
        title = Text("Fourier Epicycles: Drawing with Math", font_size=params.TITLE_FONT_SIZE)
        self.play(Write(title), run_time=params.SCENE3_TITLE_WRITE_TIME)
        self.play(title.animate.scale(params.SMALL_TITLE_SCALE).to_edge(UP), run_time=params.SCENE3_TITLE_SCALE_TIME)

        # Load or create shape
        if self.svg_path:
            try:
                svg_mob = SVGMobject(self.svg_path)
                svg_mob.scale(params.SCENE3_SVG_SCALE)
                complex_points = extract_svg_points(svg_mob, self.num_samples)
            except:
                # Fallback to default shape if SVG fails
                complex_points = create_simple_shape_points("heart", self.num_samples, radius=params.SCENE3_DEFAULT_SHAPE_RADIUS)
                svg_mob = self.create_reference_shape_from_points(complex_points)
        else:
            # Use default heart shape
            complex_points = create_simple_shape_points("heart", self.num_samples, radius=params.SCENE3_DEFAULT_SHAPE_RADIUS)
            svg_mob = self.create_reference_shape_from_points(complex_points)

        # Show reference shape
        reference_color = globals()[params.SCENE3_REFERENCE_COLOR]
        svg_mob.set_color(reference_color).set_opacity(params.SCENE3_REFERENCE_OPACITY)
        self.play(Create(svg_mob), run_time=params.SCENE3_REFERENCE_CREATE_TIME)
        self.wait(params.SCENE3_REFERENCE_WAIT_TIME)

        # Show sample points if enabled
        if params.SCENE3_SHOW_SAMPLE_POINTS:
            # Create dots for each sample point
            sample_point_color = globals()[params.SCENE3_SAMPLE_POINT_COLOR]
            sample_dots = VGroup(*[
                Dot(
                    point=[p.real, p.imag, 0],
                    radius=params.SCENE3_SAMPLE_POINT_RADIUS,
                    color=sample_point_color
                )
                for p in complex_points
            ])

            # Animate sample points appearing
            self.play(
                LaggedStart(*[FadeIn(dot) for dot in sample_dots], lag_ratio=0.001),
                run_time=params.SCENE3_SAMPLE_POINTS_CREATE_TIME
            )
            self.wait(params.SCENE3_SAMPLE_POINTS_WAIT_TIME)

            # Fade out sample points before showing epicycles
            self.play(
                FadeOut(sample_dots),
                run_time=params.SCENE3_SAMPLE_POINTS_FADEOUT_TIME
            )

        # Compute DFT
        coefficients = compute_dft_fast(complex_points)
        N = len(coefficients)

        # Create frequency indices centered around 0
        freqs = np.arange(-N//2, N//2)

        # Pair coefficients with frequencies and sort by magnitude
        coeff_freq_pairs = list(zip(coefficients, freqs))
        sorted_pairs = sorted(coeff_freq_pairs, key=lambda x: abs(x[0]), reverse=True)

        # Use top N epicycles
        top_pairs = sorted_pairs[:self.num_epicycles]

        # Separate back into coefficients and frequencies
        top_coeffs = [c for c, f in top_pairs]
        top_freqs = [f for c, f in top_pairs]

        # Create epicycle visualization
        circles, arrows = self.create_epicycle_system(top_coeffs, top_freqs)

        # Check if we have epicycles to display
        if len(circles) == 0 or len(arrows) == 0:
            print("⚠️ Warning: No epicycles to display (all filtered out due to small radius)")
            print("   Try decreasing SCENE3_MIN_EPICYCLE_RADIUS in params.py")
            # Just show the reference shape and exit
            self.wait(2)
            self.play(FadeOut(svg_mob), run_time=1)
            return

        # Add epicycles in batches of 100 for efficient initialization
        # This ensures proper updater tracking while keeping animation smooth
        batch_size = 100
        num_batches = (len(circles) + batch_size - 1) // batch_size  # Ceiling division

        for batch_idx in range(num_batches):
            start_idx = batch_idx * batch_size
            end_idx = min(start_idx + batch_size, len(circles))

            # Create animations for this batch
            batch_circles = [Create(circles[i]) for i in range(start_idx, end_idx)]
            batch_arrows = [GrowArrow(arrows[i]) for i in range(start_idx, end_idx)]

            # Show all epicycles in this batch together
            self.play(
                *batch_circles,
                *batch_arrows,
                run_time=params.SCENE3_EPICYCLE_CREATE_TIME / num_batches
            )

        # Setup traced path
        traced_path_color = globals()[params.SCENE3_TRACED_PATH_COLOR]
        traced_path = TracedPath(
            lambda: arrows[-1].get_end(),
            stroke_width=params.SCENE3_TRACED_PATH_STROKE_WIDTH,
            stroke_color=traced_path_color,
            dissipating_time=None
        )
        self.add(traced_path)

        # Use ValueTracker for explicit time control
        time_tracker = ValueTracker(0)

        # Updater for epicycle rotation
        def update_epicycles(mob):
            """Update all epicycle positions based on time tracker"""
            # Get current time from tracker
            time = time_tracker.get_value()

            for i, (arrow, coeff, freq) in enumerate(zip(arrows, top_coeffs, top_freqs)):
                # Rotate coefficient by frequency
                rotated = coeff * cmath.exp(1j * freq * 2 * PI * time)

                # Determine center (tip of previous arrow or origin)
                if i == 0:
                    center = ORIGIN
                else:
                    center = arrows[i-1].get_end()

                # Convert to 2D coordinates
                new_pos = center + np.array([rotated.real, rotated.imag, 0])

                # Update arrow
                arrow.put_start_and_end_on(center, new_pos)

                # Update circle - move to current position
                circles[i].move_to(center)

        # Add updater only once to avoid redundant calls
        # The update function already updates all arrows and circles
        arrows[0].add_updater(update_epicycles)

        # Animate time tracker to create rotation
        # Use SCENE3_NUM_ROTATIONS and SCENE3_ROTATION_DURATION from params
        # This will create smooth continuous rotation
        self.play(
            time_tracker.animate.set_value(params.SCENE3_NUM_ROTATIONS),
            run_time=params.SCENE3_ROTATION_DURATION,
            rate_func=linear
        )

        # Remove updater
        arrows[0].remove_updater(update_epicycles)

        # Finale: fade epicycles, highlight traced path
        finale_color = globals()[params.SCENE3_FINALE_PATH_COLOR]
        self.play(
            *[FadeOut(c) for c in circles],
            *[FadeOut(a) for a in arrows],
            FadeOut(svg_mob),
            traced_path.animate.set_stroke(width=params.SCENE3_FINALE_PATH_STROKE_WIDTH, color=finale_color),
            run_time=params.SCENE3_FINALE_TIME
        )

        self.wait(params.SCENE3_FINALE_WAIT_TIME)

    def create_reference_shape_from_points(self, complex_points):
        """Create a VMobject from complex points for reference"""
        points_2d = [[p.real, p.imag, 0] for p in complex_points]
        # Close the path
        points_2d.append(points_2d[0])

        path = VMobject()
        path.set_points_as_corners(points_2d)
        return path

    def create_epicycle_system(self, coefficients, frequencies):
        """
        Create circles and arrows for epicycles positioned head-to-tail at t=0.

        Args:
            coefficients: Complex Fourier coefficients
            frequencies: Corresponding frequency indices

        Returns:
            (circles, arrows): VGroups of Circle and Arrow mobjects
        """
        circles = VGroup()
        arrows = VGroup()

        # Start at origin and position each epicycle head-to-tail
        current_pos = ORIGIN

        for i, (coeff, freq) in enumerate(zip(coefficients, frequencies)):
            radius = abs(coeff)
            phase = cmath.phase(coeff)

            # Skip if radius is too small
            if radius < params.SCENE3_MIN_EPICYCLE_RADIUS:
                continue

            # Color based on frequency magnitude (blue = low, red = high)
            freq_ratio = min(abs(freq) / params.SCENE3_FREQ_NORMALIZE_DIVISOR, 1.0)  # Normalize frequency
            low_freq_color = globals()[params.SCENE3_LOW_FREQ_COLOR]
            high_freq_color = globals()[params.SCENE3_HIGH_FREQ_COLOR]
            color = interpolate_color(low_freq_color, high_freq_color, freq_ratio)

            # At t=0, rotation angle is just the phase
            # (freq * 0 = 0, so e^(i*freq*0) = 1, leaving just e^(i*phase))
            arrow_direction = np.array([np.cos(phase), np.sin(phase), 0])
            new_pos = current_pos + radius * arrow_direction

            # Create circle centered at current position
            circle = Circle(
                radius=radius,
                color=color,
                stroke_width=params.SCENE3_EPICYCLE_CIRCLE_STROKE_WIDTH,
                stroke_opacity=params.SCENE3_EPICYCLE_CIRCLE_OPACITY
            )
            circle.move_to(current_pos)

            # Create arrow from current position to new position
            arrow = Arrow(
                start=current_pos,
                end=new_pos,
                color=color,
                buff=0,
                stroke_width=params.SCENE3_EPICYCLE_ARROW_STROKE_WIDTH,
                max_tip_length_to_length_ratio=params.SCENE3_EPICYCLE_ARROW_TIP_RATIO
            )

            circles.add(circle)
            arrows.add(arrow)

            # Next epicycle starts at the tip of this arrow
            current_pos = new_pos

        return circles, arrows

# ============================================================================
# COMBINED SCENE: ALL THREE SCENES IN SEQUENCE
# ============================================================================

class CombinedScenes(Scene):
    """
    Complete animation combining all four scenes.

    Total duration: ~55 seconds
    - Scene 1: Fourier basics (8s)
    - Scene 1.5: Rotation to waves connection (5s)
    - Scene 2: Epicycle mechanics (10s)
    - Scene 3: SVG tracing (30s)
    """

    def __init__(self, svg_path=None, num_epicycles=60, **kwargs):
        self.svg_path = svg_path
        self.num_epicycles = num_epicycles
        super().__init__(**kwargs)

    def construct(self):
        # Scene 1: Fourier Transform Basics
        Scene1_FourierBasics.scene1_animation(self)
        self.wait(0.5)

        # Scene 1.5: Rotation to Waves Connection
        Scene1_5_RotationToWaves.scene1_5_animation(self)
        self.wait(0.5)

        # Scene 2: Epicycle Mechanics
        Scene2_EpicycleMechanics.scene2_animation(self)
        self.wait(0.5)

        # Scene 3: SVG Tracing
        # Pass parameters to scene 3
        scene3 = Scene3_SVGTracing()
        scene3.renderer = self.renderer
        scene3.scene3_animation()

        self.wait(1)


# ============================================================================
# CONVENIENCE CLASSES FOR DIFFERENT SHAPES
# ============================================================================

class FourierEpicyclesHeart(CombinedScenes):
    """Fourier epicycles with heart shape (default)"""
    def __init__(self, **kwargs):
        super().__init__(svg_path=None, num_epicycles=60, **kwargs)


class FourierEpicyclesCustom(CombinedScenes):
    """
    Fourier epicycles with custom SVG file.

    Usage:
        Place your SVG file in the project directory and pass the path:
        manim -pql fourier_epicycles.py FourierEpicyclesCustom

    To specify a custom SVG, modify the __init__ method with your file path.
    """
    def __init__(self, **kwargs):
        # Change this path to your SVG file
        custom_svg_path = "woman_flower.svg"
        super().__init__(svg_path=custom_svg_path, num_epicycles=80, **kwargs)
