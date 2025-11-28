"""
Test script to verify epicycle rotation is actually happening
"""

from manim import *
import numpy as np
import cmath


class TestEpicycleRotation(Scene):
    """Test that epicycles rotate and move together"""

    def construct(self):
        # Simple test with 2 epicycles
        radii = [1.5, 0.8]
        frequencies = [1, -2]
        colors = [BLUE, RED]

        # Create circles and arrows
        circles = VGroup()
        arrows = VGroup()

        current_pos = ORIGIN
        for i, (r, freq, color) in enumerate(zip(radii, frequencies, colors)):
            angle = 0
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            new_end = current_pos + r * direction

            circle = Circle(radius=r, color=color, stroke_width=3)
            circle.move_to(current_pos)

            arrow = Arrow(
                start=current_pos,
                end=new_end,
                color=color,
                buff=0,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.2
            )

            circles.add(circle)
            arrows.add(arrow)
            current_pos = new_end

        # Add to scene
        self.add(circles, arrows)

        # Add position markers at key points
        start_dot = Dot(arrows[0].get_end(), color=GREEN, radius=0.1)
        end_dot = Dot(arrows[-1].get_end(), color=YELLOW, radius=0.1)
        self.add(start_dot, end_dot)

        # Add traced path
        trace = TracedPath(
            lambda: arrows[-1].get_end(),
            stroke_width=3,
            stroke_color=WHITE,
            dissipating_time=None
        )
        self.add(trace)

        self.wait(0.5)

        # Test 1: Manual position updates to verify basic movement works
        title = Text("Test 1: Manual Updates", font_size=24).to_edge(UP)
        self.play(Write(title))

        # Manually rotate 90 degrees in 4 steps
        for step in range(4):
            time_val = (step + 1) * PI / 4  # 45 degrees per step

            current_pos = ORIGIN
            for i, (arrow, circle, freq, radius) in enumerate(zip(arrows, circles, frequencies, radii)):
                angle = freq * time_val

                if i == 0:
                    center = ORIGIN
                else:
                    center = arrows[i-1].get_end()

                direction = np.array([np.cos(angle), np.sin(angle), 0])
                new_end = center + radius * direction

                # Update positions
                arrow.put_start_and_end_on(center, new_end)
                circle.move_to(center)

                # Update dot positions
                if i == 0:
                    start_dot.move_to(arrow.get_end())
                if i == len(arrows) - 1:
                    end_dot.move_to(arrow.get_end())

                current_pos = new_end

            self.wait(0.5)

        self.play(FadeOut(title))
        self.wait(0.5)

        # Test 2: Using ValueTracker with updater
        title2 = Text("Test 2: ValueTracker", font_size=24).to_edge(UP)
        self.play(Write(title2))

        # Reset to origin
        current_pos = ORIGIN
        for i, (r, freq, color) in enumerate(zip(radii, frequencies, colors)):
            angle = 0
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            new_end = current_pos + r * direction

            arrows[i].put_start_and_end_on(current_pos, new_end)
            circles[i].move_to(current_pos)
            current_pos = new_end

        start_dot.move_to(arrows[0].get_end())
        end_dot.move_to(arrows[-1].get_end())

        # ValueTracker
        time_tracker = ValueTracker(0)

        # Add text to show current time value
        time_text = always_redraw(
            lambda: Text(
                f"t = {time_tracker.get_value():.2f}",
                font_size=20
            ).to_corner(UL).shift(DOWN * 0.5)
        )
        self.add(time_text)

        # Position text for arrow tips
        pos_text = always_redraw(
            lambda: Text(
                f"Tip: ({arrows[-1].get_end()[0]:.2f}, {arrows[-1].get_end()[1]:.2f})",
                font_size=18
            ).to_corner(UL).shift(DOWN)
        )
        self.add(pos_text)

        def update_epicycles(mob):
            time = time_tracker.get_value()

            current_pos = ORIGIN
            for i, (arrow, circle, freq, radius) in enumerate(zip(arrows, circles, frequencies, radii)):
                angle = freq * time

                if i == 0:
                    center = ORIGIN
                else:
                    center = arrows[i-1].get_end()

                direction = np.array([np.cos(angle), np.sin(angle), 0])
                new_end = center + radius * direction

                arrow.put_start_and_end_on(center, new_end)
                circle.move_to(center)

                # Update dots
                if i == 0:
                    start_dot.move_to(arrow.get_end())
                if i == len(arrows) - 1:
                    end_dot.move_to(arrow.get_end())

        # Add updater to each arrow and circle individually
        for arrow in arrows:
            arrow.add_updater(update_epicycles)
        for circle in circles:
            circle.add_updater(update_epicycles)

        # Animate
        self.play(
            time_tracker.animate.set_value(2 * TAU),
            run_time=8,
            rate_func=linear
        )

        # Remove updaters
        for arrow in arrows:
            arrow.remove_updater(update_epicycles)
        for circle in circles:
            circle.remove_updater(update_epicycles)

        self.wait(1)


class TestSimpleRotation(Scene):
    """Ultra-simple test: single rotating arrow"""

    def construct(self):
        # Single arrow
        arrow = Arrow(ORIGIN, 2*RIGHT, color=BLUE, buff=0, stroke_width=5)
        circle = Circle(radius=2, color=BLUE, stroke_width=3)

        self.add(circle, arrow)

        # Dot at tip
        dot = Dot(arrow.get_end(), color=YELLOW, radius=0.15)
        self.add(dot)

        # Trace
        trace = TracedPath(lambda: arrow.get_end(), stroke_width=3, stroke_color=WHITE)
        self.add(trace)

        # ValueTracker
        time_tracker = ValueTracker(0)

        # Time display
        time_text = always_redraw(
            lambda: Text(f"t = {time_tracker.get_value():.2f}", font_size=24).to_corner(UL)
        )
        self.add(time_text)

        # Updater
        def rotate_arrow(mob):
            angle = time_tracker.get_value()
            new_end = 2 * np.array([np.cos(angle), np.sin(angle), 0])
            arrow.put_start_and_end_on(ORIGIN, new_end)
            dot.move_to(arrow.get_end())

        arrow.add_updater(rotate_arrow)

        # Animate
        self.play(
            time_tracker.animate.set_value(2 * TAU),
            run_time=6,
            rate_func=linear
        )

        arrow.remove_updater(rotate_arrow)
        self.wait(1)
