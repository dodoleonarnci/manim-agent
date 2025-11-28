"""
Golden Ratio Spiral Animation

Visual parameters are externalized in params.py
Edit that file to customize:
- Colors (gold, segment colors, backgrounds)
- Text content (titles, labels, equations)
- Dimensions (line widths, segment lengths)
- Positions (coordinates for all elements)
- Timing (animation speeds, pauses)
- Font sizes

No code changes needed for aesthetic adjustments!
"""

from manim import *
import numpy as np

# Import visual parameters
from params import (
    COLORS, TEXT, DIMENSIONS, POSITIONS, TIMING, SIZES,
    OPACITY, MATH_CONSTANTS, FIBONACCI
)

# Mathematical constants
PHI = MATH_CONSTANTS["phi"]


class IntroScene(Scene):
    """
    Scene 1: Introduction to the Golden Ratio

    Introduces φ (phi), shows the line segment division,
    and demonstrates the fundamental equation (a+b)/a = a/b = φ
    """

    def construct(self):
        self.intro_animation()

    def intro_animation(self):
        # Title
        title = Text(TEXT["intro_title"], font_size=SIZES["title_font"], color=COLORS["gold"], weight=BOLD)
        title.to_edge(UP)

        # Display the symbol φ
        phi_symbol = Text(TEXT["phi_symbol"], font_size=SIZES["phi_symbol_font"], color=COLORS["gold"], weight=BOLD)
        phi_value = Text(TEXT["phi_value"], font_size=SIZES["phi_value_font"])
        phi_value.next_to(phi_symbol, DOWN)

        # Animate title and symbol
        self.play(FadeIn(title, shift=DOWN), run_time=TIMING["intro_title_fadein"])
        self.play(Write(phi_symbol), run_time=TIMING["phi_symbol_write"])
        self.wait(TIMING["phi_value_wait"])
        self.play(FadeIn(phi_value, shift=UP))
        self.wait(TIMING["default_wait"])

        # Clear for line segment demonstration
        self.play(FadeOut(phi_symbol), FadeOut(phi_value))

        # Create line segment division
        segment_length = DIMENSIONS["segment_total_length"]
        a_length = segment_length / PHI
        b_length = segment_length - a_length

        # Create the line segments
        start_point = LEFT * 3
        end_point = RIGHT * 3
        division_point = start_point + RIGHT * a_length

        # Full line
        full_line = Line(start_point, end_point, color=COLORS["whole"], stroke_width=DIMENSIONS["line_stroke"])

        # Mark the division point
        division_dot = Dot(division_point, color=COLORS["gold"], radius=DIMENSIONS["dot_radius"])

        # Label the segments
        a_brace = BraceBetweenPoints(start_point, division_point, direction=DOWN)
        a_label = Text(TEXT["segment_a_label"], color=COLORS["segment_a"], font_size=SIZES["label_font"]).next_to(a_brace, DOWN)

        b_brace = BraceBetweenPoints(division_point, end_point, direction=DOWN)
        b_label = Text(TEXT["segment_b_label"], color=COLORS["segment_b"], font_size=SIZES["label_font"]).next_to(b_brace, DOWN)

        whole_brace = BraceBetweenPoints(start_point, end_point, direction=UP)
        whole_label = Text(TEXT["segment_whole_label"], font_size=SIZES["label_font"]).next_to(whole_brace, UP)

        # Animate line segment
        self.play(Create(full_line))
        self.play(FadeIn(division_dot))
        self.wait(TIMING["segment_wait"])

        # Show segment labels
        self.play(GrowFromCenter(a_brace), Write(a_label))
        self.play(GrowFromCenter(b_brace), Write(b_label))
        self.wait(TIMING["segment_wait"])

        self.play(GrowFromCenter(whole_brace), Write(whole_label))
        self.wait(TIMING["default_wait"])

        # Show the golden ratio equation
        eq_line1 = Text("(a + b)", color=COLORS["property_2"], font_size=SIZES["equation_font"])
        eq_div1 = Text("/", font_size=SIZES["equation_font"])
        eq_a1 = Text("a", font_size=SIZES["equation_font"])
        eq_equals1 = Text("=", font_size=SIZES["equation_font"])
        eq_a2 = Text("a", font_size=SIZES["equation_font"])
        eq_div2 = Text("/", font_size=SIZES["equation_font"])
        eq_b = Text("b", font_size=SIZES["equation_font"])
        eq_equals2 = Text("=", font_size=SIZES["equation_font"])
        eq_phi = Text(TEXT["phi_symbol"], color=COLORS["gold"], font_size=SIZES["equation_font"])

        equation = VGroup(
            eq_line1, eq_div1, eq_a1, eq_equals1,
            eq_a2, eq_div2, eq_b, eq_equals2, eq_phi
        ).arrange(RIGHT, buff=0.15)
        equation.move_to(DOWN * POSITIONS["equation_y"])

        self.play(Write(equation))
        self.wait(TIMING["equation_wait"])

        # Transform to algebraic form
        algebraic_eq = Text(TEXT["algebraic_equation"], font_size=SIZES["equation_font"] + 4, color=COLORS["gold"])
        algebraic_eq.move_to(equation)

        self.play(
            FadeOut(full_line), FadeOut(division_dot),
            FadeOut(a_brace), FadeOut(a_label),
            FadeOut(b_brace), FadeOut(b_label),
            FadeOut(whole_brace), FadeOut(whole_label)
        )
        self.play(Transform(equation, algebraic_eq))
        self.wait(TIMING["transform_wait"])

        # Show the solution
        solution_phi = Text(TEXT["phi_symbol"], color=COLORS["gold"], font_size=SIZES["equation_font"])
        solution_eq = Text("=", font_size=SIZES["equation_font"])
        solution_frac = Text("(1 + √5) / 2", font_size=SIZES["equation_font"])
        solution = VGroup(solution_phi, solution_eq, solution_frac).arrange(RIGHT, buff=0.15)
        solution.next_to(equation, DOWN, buff=0.8)

        self.play(Write(solution))
        self.wait(TIMING["solution_wait"])

        # Fade out
        self.play(FadeOut(title), FadeOut(equation), FadeOut(solution))
        self.wait(TIMING["fadeout_wait"])


class PropertiesScene(Scene):
    """
    Scene 2: Unique Properties of φ

    Demonstrates:
    1. φ² = φ + 1 (squaring property)
    2. 1/φ = φ - 1 (reciprocal property)
    """

    def construct(self):
        self.properties_animation()

    def properties_animation(self):
        # Title
        title = Text(TEXT["properties_title"], font_size=SIZES["subtitle_font"], color=COLORS["gold"], weight=BOLD)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))
        self.wait(TIMING["default_wait"])

        # Property 1: Squaring property
        prop1_title = Text(TEXT["prop1_title"], font_size=SIZES["property_title_font"], color=COLORS["property_1"], weight=BOLD)
        prop1_title.move_to(UP * POSITIONS["prop_title_y"])

        # Create equation: φ² = φ + 1
        phi_sq = Text("φ²", color=COLORS["gold"], font_size=SIZES["property_font"])
        eq1 = Text("=", font_size=SIZES["property_font"])
        phi_plus = Text("φ + 1", font_size=SIZES["property_font"])
        prop1_eq = VGroup(phi_sq, eq1, phi_plus).arrange(RIGHT, buff=0.2)
        prop1_eq.next_to(prop1_title, DOWN, buff=0.5)

        # Numerical verification
        prop1_num = Text(TEXT["prop1_numerical"], font_size=SIZES["numerical_font"])
        prop1_num.next_to(prop1_eq, DOWN, buff=0.4)

        self.play(FadeIn(prop1_title, shift=RIGHT))
        self.play(Write(prop1_eq))
        self.wait(TIMING["property_wait"])
        self.play(FadeIn(prop1_num, shift=UP))
        self.wait(TIMING["numerical_wait"])

        # Visual representation: rectangle decomposition
        rect_width = DIMENSIONS["rect_width"]
        rect_height = rect_width / PHI

        # φ² rectangle
        phi_squared_rect = Rectangle(
            width=rect_width,
            height=rect_width / PHI,
            color=COLORS["gold"],
            stroke_width=DIMENSIONS["rect_stroke"],
            fill_opacity=OPACITY["rect_fill"]
        )
        phi_squared_rect.shift(RIGHT * POSITIONS["rect_x"])

        phi_sq_label = Text("φ²", color=COLORS["gold"], font_size=SIZES["rect_label_font"]).next_to(
            phi_squared_rect, LEFT, buff=0.3
        )

        self.play(Create(phi_squared_rect), Write(phi_sq_label))
        self.wait(TIMING["visual_wait"])

        # Decompose into φ rectangle and 1 square
        phi_rect = Rectangle(
            width=rect_width / PHI,
            height=rect_width / PHI,
            color=COLORS["phi_rect"],
            stroke_width=DIMENSIONS["rect_stroke"],
            fill_opacity=OPACITY["rect_fill"]
        )
        phi_rect.align_to(phi_squared_rect, LEFT)
        phi_rect.align_to(phi_squared_rect, UP)

        unit_square = Square(
            side_length=rect_width / PHI,
            color=COLORS["unit_square"],
            stroke_width=DIMENSIONS["rect_stroke"],
            fill_opacity=OPACITY["rect_fill"]
        )
        unit_square.next_to(phi_rect, RIGHT, buff=0)

        phi_rect_label = Text("φ", color=COLORS["phi_rect"], font_size=SIZES["rect_label_font"]).move_to(
            phi_rect.get_center()
        )
        unit_square_label = Text("1", color=COLORS["unit_square"], font_size=SIZES["rect_label_font"]).move_to(
            unit_square.get_center()
        )

        self.play(FadeOut(phi_squared_rect), FadeOut(phi_sq_label))
        self.play(
            Create(phi_rect), Create(unit_square),
            Write(phi_rect_label), Write(unit_square_label)
        )
        self.wait(TIMING["visual_decompose_wait"])

        # Clear for property 2
        self.play(
            FadeOut(prop1_title), FadeOut(prop1_eq), FadeOut(prop1_num),
            FadeOut(phi_rect), FadeOut(unit_square),
            FadeOut(phi_rect_label), FadeOut(unit_square_label)
        )

        # Property 2: Reciprocal property
        prop2_title = Text(TEXT["prop2_title"], font_size=SIZES["property_title_font"], color=COLORS["property_2"], weight=BOLD)
        prop2_title.move_to(UP * POSITIONS["prop_title_y"])

        # Create equation: 1/φ = φ - 1
        one_over = Text("1/φ", font_size=SIZES["property_font"])
        eq2 = Text("=", font_size=SIZES["property_font"])
        phi_minus = Text("φ - 1", color=COLORS["gold"], font_size=SIZES["property_font"])
        prop2_eq = VGroup(one_over, eq2, phi_minus).arrange(RIGHT, buff=0.2)
        prop2_eq.next_to(prop2_title, DOWN, buff=0.5)

        # Numerical verification
        prop2_num = Text(TEXT["prop2_numerical"], font_size=SIZES["numerical_font"])
        prop2_num.next_to(prop2_eq, DOWN, buff=0.4)

        self.play(FadeIn(prop2_title, shift=RIGHT))
        self.play(Write(prop2_eq))
        self.wait(TIMING["property_wait"])
        self.play(FadeIn(prop2_num, shift=UP))
        self.wait(TIMING["numerical_wait"])

        # Visual representation: golden rectangle with unit square
        golden_rect = Rectangle(
            width=rect_width,
            height=rect_width / PHI,
            color=COLORS["gold"],
            stroke_width=DIMENSIONS["rect_stroke"],
            fill_opacity=OPACITY["rect_fill"]
        )
        golden_rect.shift(RIGHT * POSITIONS["rect_x"])

        gr_label = Text("φ", color=COLORS["gold"], font_size=SIZES["rect_label_font"]).next_to(
            golden_rect, UP, buff=0.2
        )

        self.play(Create(golden_rect), Write(gr_label))
        self.wait(TIMING["visual_wait"])

        # Unit square inside
        unit_sq = Square(
            side_length=rect_width / PHI,
            color=COLORS["phi_rect"],
            stroke_width=DIMENSIONS["rect_stroke"],
            fill_opacity=OPACITY["rect_fill"]
        )
        unit_sq.align_to(golden_rect, LEFT)
        unit_sq.align_to(golden_rect, UP)

        unit_label = Text("1", color=COLORS["phi_rect"], font_size=SIZES["rect_label_font"]).move_to(
            unit_sq.get_center()
        )

        # Remaining rectangle
        remaining = Rectangle(
            width=rect_width - rect_width / PHI,
            height=rect_width / PHI,
            color=COLORS["unit_square"],
            stroke_width=DIMENSIONS["rect_stroke"],
            fill_opacity=OPACITY["rect_fill"]
        )
        remaining.next_to(unit_sq, RIGHT, buff=0)

        remaining_label = Text("φ - 1", color=COLORS["unit_square"], font_size=24).move_to(
            remaining.get_center()
        )

        self.play(Create(unit_sq), Write(unit_label))
        self.wait(TIMING["visual_wait"])
        self.play(Create(remaining), Write(remaining_label))
        self.wait(TIMING["visual_decompose_wait"])

        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(TIMING["fadeout_wait"])


class FibonacciConnection(Scene):
    """
    Scene 3: Fibonacci Sequence Connection

    Shows the Fibonacci sequence and demonstrates how
    the ratio of consecutive terms converges to φ
    """

    def construct(self):
        self.fibonacci_animation()

    def fibonacci_animation(self):
        # Title
        title = Text(TEXT["fibonacci_title"], font_size=SIZES["subtitle_font"], color=COLORS["gold"], weight=BOLD)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))
        self.wait(TIMING["default_wait"])

        # Fibonacci sequence
        fib_numbers = FIBONACCI["sequence"]

        # Display Fibonacci sequence
        fib_text = Text(TEXT["fib_sequence_label"], font_size=SIZES["fib_title_font"], weight=BOLD)
        fib_text.next_to(title, DOWN, buff=POSITIONS["fib_text_y_offset"])
        self.play(Write(fib_text))
        self.wait(TIMING["default_wait"])

        # Create sequence display
        fib_mobjects = []
        for i, num in enumerate(fib_numbers):
            num_text = Text(str(num), font_size=SIZES["fib_sequence_font"], color=COLORS["fib_numbers"])
            if i == 0:
                num_text.next_to(fib_text, DOWN, buff=0.5)
                num_text.shift(LEFT * abs(POSITIONS["fib_start_x"]))
            else:
                num_text.next_to(fib_mobjects[-1], RIGHT, buff=0.3)

            fib_mobjects.append(num_text)

        # Add commas between numbers
        comma_mobjects = []
        for i in range(len(fib_mobjects) - 1):
            comma = Text(",", font_size=SIZES["fib_sequence_font"])
            comma.next_to(fib_mobjects[i], RIGHT, buff=0.1)
            comma_mobjects.append(comma)

        # Animate sequence building up
        for i in range(len(fib_numbers)):
            if i < 2:
                # First two numbers appear
                self.play(FadeIn(fib_mobjects[i], shift=UP), run_time=TIMING["fib_number_fadein"])
            else:
                # Show addition for subsequent numbers
                if i < len(comma_mobjects):
                    self.play(FadeIn(comma_mobjects[i-1]), run_time=TIMING["fib_comma"])

                # Highlight the two previous numbers
                self.play(
                    fib_mobjects[i-2].animate.set_color(COLORS["fib_highlight"]),
                    fib_mobjects[i-1].animate.set_color(COLORS["fib_highlight"]),
                    run_time=TIMING["fib_addition_highlight"]
                )

                # Show the new number
                self.play(FadeIn(fib_mobjects[i], shift=DOWN), run_time=TIMING["fib_number_fadein"])

                # Reset colors
                self.play(
                    fib_mobjects[i-2].animate.set_color(COLORS["fib_numbers"]),
                    fib_mobjects[i-1].animate.set_color(COLORS["fib_numbers"]),
                    run_time=TIMING["fib_addition_highlight"]
                )

        # Add remaining commas
        for comma in comma_mobjects[len(fib_mobjects)-2:]:
            self.play(FadeIn(comma), run_time=TIMING["fib_comma"])

        self.wait(TIMING["default_wait"])

        # Move sequence up to make room for ratios
        all_fib = VGroup(*fib_mobjects, *comma_mobjects, fib_text)
        self.play(all_fib.animate.shift(UP * POSITIONS["convergence_shift_up"]), run_time=TIMING["fib_sequence_shift"])
        self.wait(TIMING["default_wait"])

        # Show convergence to φ
        convergence_title = Text(TEXT["ratio_label"], font_size=SIZES["ratio_font"], weight=BOLD)
        convergence_title.next_to(all_fib, DOWN, buff=0.8)
        self.play(Write(convergence_title))
        self.wait(TIMING["default_wait"])

        # Calculate and display ratios
        ratios_data = []
        for i in range(1, len(fib_numbers)):
            ratio = fib_numbers[i] / fib_numbers[i-1]
            ratios_data.append((fib_numbers[i], fib_numbers[i-1], ratio))

        # Display select ratios to show convergence
        display_indices = FIBONACCI["ratio_display_indices"]

        ratio_mobjects = []
        for idx, i in enumerate(display_indices):
            n_plus_1, n, ratio = ratios_data[i]

            # Create ratio text
            ratio_text = Text(
                f"{n_plus_1}/{n} = {ratio:.3f}",
                font_size=SIZES["ratio_font"]
            )

            if idx == 0:
                ratio_text.next_to(convergence_title, DOWN, buff=0.4)
            else:
                ratio_text.next_to(ratio_mobjects[-1], DOWN, buff=0.2)

            # Color code based on closeness to PHI
            diff = abs(ratio - PHI)
            if diff < FIBONACCI["ratio_exact_threshold"]:
                ratio_text.set_color(COLORS["ratio_exact"])
            elif diff < FIBONACCI["ratio_close_threshold"]:
                ratio_text.set_color(COLORS["ratio_close"])
            else:
                ratio_text.set_color(COLORS["whole"])

            ratio_mobjects.append(ratio_text)
            self.play(Write(ratio_text), run_time=TIMING["ratio_write"])

        self.wait(TIMING["ratio_wait"])

        # Show φ value for comparison
        phi_comparison = Text(
            TEXT["phi_comparison"],
            font_size=SIZES["fib_sequence_font"],
            color=COLORS["gold"],
            weight=BOLD
        )
        phi_comparison.next_to(ratio_mobjects[-1], DOWN, buff=0.5)

        self.play(Write(phi_comparison))
        self.wait(TIMING["ratio_wait"])

        # Add convergence statement
        convergence_statement = Text(
            TEXT["convergence_statement"],
            font_size=SIZES["convergence_font"],
            color=COLORS["convergence"],
            weight=BOLD
        )
        convergence_statement.next_to(phi_comparison, DOWN, buff=0.4)

        self.play(FadeIn(convergence_statement, shift=UP))
        self.wait(TIMING["convergence_wait"])

        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(TIMING["fadeout_wait"])


class GoldenRectangles(Scene):
    """
    Scene 4: Golden Rectangles with Fibonacci Squares

    Builds golden rectangles with Fibonacci squares showing
    the recursive subdivision pattern.
    """

    def construct(self):
        self.golden_rectangles_animation()

    def golden_rectangles_animation(self):
        # Title
        title = Text(TEXT["rectangles_title"], font_size=SIZES["subtitle_font"], color=COLORS["gold"], weight=BOLD)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))
        self.wait(TIMING["default_wait"])

        # TODO: Implement golden rectangles with Fibonacci squares
        # This will be implemented in the next iteration

        placeholder = Text("Coming soon: Golden Rectangles", font_size=SIZES["label_font"])
        self.play(Write(placeholder))
        self.wait(2)
        self.play(FadeOut(placeholder), FadeOut(title))


class SpiralBuilding(Scene):
    """
    Scene 5: Building the Golden Spiral

    Draws the spiral using quarter-circle arcs in Fibonacci squares
    and overlays the true golden spiral.
    """

    def construct(self):
        self.spiral_building_animation()

    def spiral_building_animation(self):
        # Title
        title = Text(TEXT["spiral_title"], font_size=SIZES["subtitle_font"], color=COLORS["gold"], weight=BOLD)
        title.to_edge(UP)
        self.play(FadeIn(title, shift=DOWN))
        self.wait(TIMING["default_wait"])

        # TODO: Implement spiral building
        # This will be implemented in the next iteration

        placeholder = Text("Coming soon: Golden Spiral", font_size=SIZES["label_font"])
        self.play(Write(placeholder))
        self.wait(2)
        self.play(FadeOut(placeholder), FadeOut(title))


class CombinedScenes(Scene):
    """Combines all scenes in the correct order for a single video."""

    def construct(self):
        # Scene 1: Introduction
        IntroScene.intro_animation(self)
        self.clear()

        # Scene 2: Properties
        PropertiesScene.properties_animation(self)
        self.clear()

        # Scene 3: Fibonacci Connection
        FibonacciConnection.fibonacci_animation(self)
        self.clear()

        # Scene 4: Golden Rectangles
        GoldenRectangles.golden_rectangles_animation(self)
        self.clear()

        # Scene 5: Spiral Building
        SpiralBuilding.spiral_building_animation(self)
