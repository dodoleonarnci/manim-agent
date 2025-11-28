"""
Verification test: Check that circles move with arrows in both Scene 2 and Scene 3 patterns
"""
from manim import *
import numpy as np
import cmath

class VerifyScene2Pattern(Scene):
    """Test Scene 2 update pattern with 2 epicycles"""

    def construct(self):
        # Title
        title = Text("Scene 2 Pattern: Circles Moving", font_size=28)
        self.play(Write(title))
        self.play(title.animate.scale(0.7).to_edge(UP))

        # Scene 2 pattern: Simple epicycles
        radii = [1.5, 0.8]
        frequencies = [1, -2]
        colors = [BLUE, GREEN]

        # Create circles and arrows
        circles = VGroup()
        arrows = VGroup()

        current_pos = ORIGIN
        for i, (r, freq, color) in enumerate(zip(radii, frequencies, colors)):
            angle = 0
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            new_end = current_pos + r * direction

            circle = Circle(radius=r, color=color, stroke_width=2)
            circle.move_to(current_pos)

            arrow = Arrow(start=current_pos, end=new_end, color=color, buff=0, stroke_width=3)

            circles.add(circle)
            arrows.add(arrow)
            current_pos = new_end

        self.play(*[Create(c) for c in circles], *[GrowArrow(a) for a in arrows])

        # Updater pattern from Scene 2
        time_tracker = ValueTracker(0)

        def update_epicycles(mob):
            time = time_tracker.get_value()
            for i, (arrow, freq, radius) in enumerate(zip(arrows, frequencies, radii)):
                angle = freq * 2 * PI * time

                if i == 0:
                    center = ORIGIN
                else:
                    center = arrows[i-1].get_end()

                direction = np.array([np.cos(angle), np.sin(angle), 0])
                new_end = center + radius * direction

                arrow.put_start_and_end_on(center, new_end)
                circles[i].move_to(center)  # KEY LINE: Move circle with arrow

        arrows[0].add_updater(update_epicycles)

        # Animate
        self.play(time_tracker.animate.set_value(2), run_time=4, rate_func=linear)

        arrows[0].remove_updater(update_epicycles)
        self.wait(0.5)


class VerifyScene3Pattern(Scene):
    """Test Scene 3 update pattern with DFT coefficients"""

    def construct(self):
        # Title
        title = Text("Scene 3 Pattern: Circles Moving", font_size=28)
        self.play(Write(title))
        self.play(title.animate.scale(0.7).to_edge(UP))

        # Scene 3 pattern: DFT-based epicycles
        # Simulate simple DFT coefficients for a circle
        num_epicycles = 3
        top_coeffs = [1.0+0j, 0.3+0.2j, 0.2-0.1j]
        top_freqs = [1, 2, -1]
        colors_list = [BLUE, GREEN, RED]

        # Create circles and arrows
        circles = VGroup()
        arrows = VGroup()

        current_pos = ORIGIN
        for i, (coeff, freq, color) in enumerate(zip(top_coeffs, top_freqs, colors_list)):
            radius = abs(coeff)
            phase = cmath.phase(coeff)

            arrow_direction = np.array([np.cos(phase), np.sin(phase), 0])
            new_pos = current_pos + radius * arrow_direction

            circle = Circle(radius=radius, color=color, stroke_width=2)
            circle.move_to(current_pos)

            arrow = Arrow(start=current_pos, end=new_pos, color=color, buff=0, stroke_width=3)

            circles.add(circle)
            arrows.add(arrow)
            current_pos = new_pos

        self.play(*[Create(c) for c in circles], *[GrowArrow(a) for a in arrows])

        # Traced path
        traced_path = TracedPath(lambda: arrows[-1].get_end(), stroke_color=YELLOW, stroke_width=3)
        self.add(traced_path)

        # Updater pattern from Scene 3
        time_tracker = ValueTracker(0)

        def update_epicycles(mob):
            time = time_tracker.get_value()
            current_pos = ORIGIN

            for i, (arrow, circle, coeff, freq) in enumerate(zip(arrows, circles, top_coeffs, top_freqs)):
                # Rotate coefficient by frequency
                rotated = coeff * cmath.exp(1j * freq * 2 * PI * time)

                # Convert to 2D coordinates
                new_pos = current_pos + np.array([rotated.real, rotated.imag, 0])

                # Update arrow
                arrow.put_start_and_end_on(current_pos, new_pos)

                # Update circle - KEY LINE: Move circle with arrow
                circle.move_to(current_pos)

                # Next circle starts at this tip
                current_pos = new_pos

        arrows[0].add_updater(update_epicycles)

        # Animate
        self.play(time_tracker.animate.set_value(1), run_time=4, rate_func=linear)

        arrows[0].remove_updater(update_epicycles)
        self.wait(0.5)
