from manim import *
import numpy as np
from scipy.integrate import solve_ivp


class LorenzAttractor(ThreeDScene):
    """
    Animated visualization of the Lorenz attractor with rotating 3D view.
    Total duration: ~18-20 seconds
    """

    def construct(self):
        # Scene 1: Brief introduction (3 seconds)
        self.intro_scene()

        # Scene 2: 3D attractor with rotation (15-17 seconds)
        self.lorenz_3d_scene()

    def intro_scene(self):
        """Display title and brief description."""
        # Title
        title = Text("Lorenz Attractor", font_size=48, color=BLUE)
        subtitle = Text("Chaotic System", font_size=28, color=GREY_B)
        subtitle.next_to(title, DOWN, buff=0.3)

        # Group title and subtitle
        intro_group = VGroup(title, subtitle)
        intro_group.move_to(ORIGIN)

        # Animate intro
        self.play(FadeIn(intro_group), run_time=1)
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(intro_group), run_time=0.5)

    def lorenz_system(self, t, state, sigma, rho, beta):
        """
        Lorenz differential equations.

        Args:
            t: Time (not used in autonomous system)
            state: [x, y, z] current state
            sigma, rho, beta: System parameters

        Returns:
            [dx/dt, dy/dt, dz/dt]
        """
        x, y, z = state
        dx_dt = sigma * (y - x)
        dy_dt = x * (rho - z) - y
        dz_dt = x * y - beta * z
        return [dx_dt, dy_dt, dz_dt]

    def compute_lorenz_trajectory(self, t_max=40, num_points=5000):
        """
        Numerically integrate Lorenz equations.

        Args:
            t_max: Maximum time to integrate
            num_points: Number of points in trajectory

        Returns:
            Array of [x, y, z] points
        """
        # Standard Lorenz parameters
        sigma = 10
        rho = 28
        beta = 8/3

        # Initial condition
        initial_state = [0.1, 0, 0]

        # Time span
        t_span = (0, t_max)
        t_eval = np.linspace(0, t_max, num_points)

        # Solve ODE
        solution = solve_ivp(
            self.lorenz_system,
            t_span,
            initial_state,
            args=(sigma, rho, beta),
            t_eval=t_eval,
            method='RK45'
        )

        # Extract trajectory points
        x, y, z = solution.y

        # Stack into Nx3 array
        points = np.column_stack([x, y, z])

        return points

    def lorenz_3d_scene(self):
        """Main 3D scene with rotating Lorenz attractor."""
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-25, 25, 5],
            y_range=[-35, 35, 5],
            z_range=[0, 55, 5],
            x_length=6,
            y_length=6,
            z_length=5,
            axis_config={"color": GREY_A, "stroke_width": 1}
        )

        # Compute Lorenz trajectory
        trajectory_points = self.compute_lorenz_trajectory(t_max=40, num_points=5000)

        # Scale and center the trajectory for better visualization
        # Lorenz attractor typically has range: x∈[-20,20], y∈[-30,30], z∈[0,50]
        scaled_points = []
        for point in trajectory_points:
            x, y, z = point
            # Scale to fit nicely in the scene
            scaled_x = x * 0.12
            scaled_y = y * 0.12
            scaled_z = (z - 25) * 0.12  # Center z around middle
            scaled_points.append([scaled_x, scaled_y, scaled_z])

        # Create the trajectory curve
        trajectory = VMobject()
        trajectory.set_points_as_corners(scaled_points)
        trajectory.set_stroke(color=BLUE, width=2)

        # Apply gradient color (blue to purple)
        trajectory.set_color_by_gradient(BLUE, PURPLE, PINK)

        # Set camera position
        self.set_camera_orientation(
            phi=70 * DEGREES,
            theta=-45 * DEGREES,
            distance=8
        )

        # Add axes
        self.add(axes)
        self.wait(0.3)

        # Start camera rotation
        self.begin_ambient_camera_rotation(rate=0.15)

        # Trace the attractor
        self.play(
            Create(trajectory),
            run_time=14,
            rate_func=linear
        )

        # Continue rotating with complete trajectory visible
        self.wait(2)

        # Stop rotation and fade out
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(trajectory), FadeOut(axes), run_time=0.5)
