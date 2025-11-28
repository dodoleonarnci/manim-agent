"""
Rotating 3D Lorenz Attractor Animation

This animation visualizes the famous Lorenz attractor, a set of chaotic solutions
to the Lorenz system of differential equations:
    dx/dt = σ(y - x)
    dy/dt = x(ρ - z) - y
    dz/dt = xy - βz

Standard parameters: σ=10, ρ=28, β=8/3
"""

from manim import *
import numpy as np


class LorenzAttractor(ThreeDScene):
    """3D visualization of the Lorenz attractor with rotating camera"""

    def construct(self):
        self.lorenz_attractor_animation()

    def lorenz_attractor_animation(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-30, 30, 10],
            y_range=[-30, 30, 10],
            z_range=[0, 50, 10],
            x_length=8,
            y_length=8,
            z_length=6,
        )

        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = axes.get_z_axis_label("z", rotation=0)

        # Title
        title = Text("Lorenz Attractor", font_size=48).to_edge(UP)

        # Lorenz system parameters
        sigma = 10.0
        rho = 28.0
        beta = 8.0 / 3.0

        # Function to compute derivatives
        def lorenz_deriv(state, t=0):
            x, y, z = state
            return np.array([
                sigma * (y - x),
                x * (rho - z) - y,
                x * y - beta * z
            ])

        # Numerical integration using Runge-Kutta 4th order
        def runge_kutta_4(f, y0, t):
            """RK4 integration"""
            n = len(t)
            y = np.zeros((n, len(y0)))
            y[0] = y0

            for i in range(n - 1):
                h = t[i+1] - t[i]
                k1 = f(y[i], t[i])
                k2 = f(y[i] + k1 * h / 2., t[i] + h / 2.)
                k3 = f(y[i] + k2 * h / 2., t[i] + h / 2.)
                k4 = f(y[i] + k3 * h, t[i] + h)
                y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)

            return y

        # Generate trajectory
        t = np.linspace(0, 40, 8000)
        initial_state = [1.0, 1.0, 1.0]
        trajectory = runge_kutta_4(lorenz_deriv, initial_state, t)

        # Scale trajectory for better visualization
        scale_factor = 0.15

        # Create points for the curve
        points = [
            axes.c2p(
                trajectory[i, 0] * scale_factor,
                trajectory[i, 1] * scale_factor,
                trajectory[i, 2] * scale_factor
            )
            for i in range(len(trajectory))
        ]

        # Create the attractor curve with gradient coloring
        # Split into segments for color gradient
        num_segments = 20
        segment_size = len(points) // num_segments

        curves = VGroup()
        colors = color_gradient([BLUE, PURPLE, RED, ORANGE, YELLOW], num_segments)

        for i in range(num_segments):
            start_idx = i * segment_size
            end_idx = min((i + 1) * segment_size, len(points))

            if end_idx - start_idx < 2:
                continue

            segment_points = points[start_idx:end_idx]
            curve = VMobject()
            curve.set_points_smoothly(segment_points)
            curve.set_stroke(colors[i], width=2, opacity=0.8)
            curves.add(curve)

        # Add a small sphere at the starting point
        start_dot = Dot3D(
            point=points[0],
            radius=0.08,
            color=GREEN
        )

        # Set initial camera orientation
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, zoom=0.8)

        # Animation sequence
        # 1. Show title
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(0.5)

        # 2. Create axes
        self.play(Create(axes), run_time=2)
        self.play(
            Write(x_label),
            Write(y_label),
            Write(z_label),
            run_time=1
        )
        self.wait(0.5)

        # 3. Draw the attractor with starting point
        self.play(FadeIn(start_dot))

        # Draw the curves sequentially
        self.play(
            *[Create(curve, run_time=3) for curve in curves],
            rate_func=smooth
        )
        self.wait(1)

        # 4. Rotate camera around the attractor
        # First rotation
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(8)

        # Change rotation rate for variety
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=60 * DEGREES, theta=60 * DEGREES, run_time=3)
        self.wait(1)

        # Resume rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(8)

        # Final view
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, run_time=3)
        self.wait(2)

        # Fade out
        self.play(
            FadeOut(curves),
            FadeOut(start_dot),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(z_label),
            FadeOut(title),
            run_time=2
        )
        self.wait(0.5)


class LorenzAttractorTracing(ThreeDScene):
    """Alternative version showing the trajectory being traced in real-time"""

    def construct(self):
        self.lorenz_attractor_tracing_animation()

    def lorenz_attractor_tracing_animation(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-30, 30, 10],
            y_range=[-30, 30, 10],
            z_range=[0, 50, 10],
            x_length=8,
            y_length=8,
            z_length=6,
        )

        # Title
        title = Text("Lorenz Attractor - Live Tracing", font_size=48).to_edge(UP)

        # Lorenz system parameters
        sigma = 10.0
        rho = 28.0
        beta = 8.0 / 3.0

        def lorenz_deriv(state, t=0):
            x, y, z = state
            return np.array([
                sigma * (y - x),
                x * (rho - z) - y,
                x * y - beta * z
            ])

        def runge_kutta_4(f, y0, t):
            n = len(t)
            y = np.zeros((n, len(y0)))
            y[0] = y0

            for i in range(n - 1):
                h = t[i+1] - t[i]
                k1 = f(y[i], t[i])
                k2 = f(y[i] + k1 * h / 2., t[i] + h / 2.)
                k3 = f(y[i] + k2 * h / 2., t[i] + h / 2.)
                k4 = f(y[i] + k3 * h, t[i] + h)
                y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)

            return y

        # Generate trajectory
        t = np.linspace(0, 40, 4000)
        initial_state = [1.0, 1.0, 1.0]
        trajectory = runge_kutta_4(lorenz_deriv, initial_state, t)

        scale_factor = 0.15

        # Create parametric function for the trajectory
        def get_point(i):
            idx = int(i)
            if idx >= len(trajectory):
                idx = len(trajectory) - 1
            return axes.c2p(
                trajectory[idx, 0] * scale_factor,
                trajectory[idx, 1] * scale_factor,
                trajectory[idx, 2] * scale_factor
            )

        # Set initial camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES, zoom=0.8)

        # Add title
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # Create axes
        self.play(Create(axes), run_time=1.5)
        self.wait(0.5)

        # Create a moving dot
        dot = Dot3D(point=get_point(0), radius=0.1, color=YELLOW)
        self.add(dot)

        # Create the traced path
        path = VMobject(color=BLUE)
        path.set_stroke(width=2)
        path.set_points([get_point(0)])
        self.add(path)

        # Trace the attractor
        def update_path(mob, alpha):
            idx = int(alpha * (len(trajectory) - 1))
            new_point = get_point(idx)
            mob.add_line_to(new_point)
            dot.move_to(new_point)

        # Start camera rotation
        self.begin_ambient_camera_rotation(rate=0.1)

        # Animate tracing
        self.play(
            UpdateFromAlphaFunc(path, update_path),
            run_time=12,
            rate_func=linear
        )

        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.wait(1)


class CombinedScenes(ThreeDScene):
    """Combines all scenes in the correct order for a single video."""

    def construct(self):
        # Scene 1: Main Lorenz Attractor
        LorenzAttractor.lorenz_attractor_animation(self)

        # Clear the scene
        self.clear()
        self.renderer.camera.reset()

        # Scene 2: Live Tracing
        LorenzAttractorTracing.lorenz_attractor_tracing_animation(self)
