"""
Common Manim Code Examples
Run with: manim -pql examples.py SceneName
"""

from manim import *


class BasicShapes(Scene):
    """Example: Creating and styling basic shapes"""
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        circle.set_stroke(WHITE, width=3)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        square.next_to(circle, RIGHT, buff=1)

        triangle = Triangle()
        triangle.set_fill(GREEN, opacity=0.5)
        triangle.next_to(square, RIGHT, buff=1)

        self.play(Create(circle), Create(square), Create(triangle))
        self.wait()


class AnimateSyntax(Scene):
    """Example: Using the .animate syntax"""
    def construct(self):
        square = Square()
        self.play(Create(square))

        # Animate various transformations
        self.play(square.animate.rotate(PI / 4))
        self.play(square.animate.shift(UP * 2))
        self.play(square.animate.scale(2))
        self.play(square.animate.set_fill(BLUE, opacity=0.5))

        # Chain multiple transformations
        self.play(
            square.animate
            .shift(DOWN * 2)
            .rotate(-PI / 4)
            .scale(0.5)
            .set_color(RED)
        )
        self.wait()


class TransformExample(Scene):
    """Example: Transform vs ReplacementTransform"""
    def construct(self):
        # Transform
        circle = Circle()
        square = Square()
        self.play(Create(circle))
        self.wait()
        self.play(Transform(circle, square))
        self.wait()
        # Note: 'circle' is still the object reference
        self.play(FadeOut(circle))

        # ReplacementTransform
        circle2 = Circle()
        square2 = Square()
        circle2.shift(DOWN * 2)
        square2.shift(DOWN * 2)
        self.play(Create(circle2))
        self.wait()
        self.play(ReplacementTransform(circle2, square2))
        self.wait()
        # Note: 'square2' is now the object reference
        self.play(FadeOut(square2))


class TextAndMath(Scene):
    """Example: Text and mathematical formulas"""
    def construct(self):
        # Regular text
        title = Text("Mathematical Animations", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))

        # Math formula
        formula = MathTex(r"E = mc^2")
        formula.scale(2)
        self.play(Write(formula))
        self.wait()

        # Multi-part formula for selective animation
        equation = MathTex(
            r"\int_0^1", r"x^2", r"dx", "=", r"\frac{1}{3}"
        )
        equation.shift(DOWN * 2)

        self.play(Write(equation[0:3]))  # Integral part
        self.wait()
        self.play(Write(equation[3:]))   # Result
        self.wait()

        # Highlight specific part
        self.play(Indicate(equation[1]))
        self.wait()


class GraphExample(Scene):
    """Example: Plotting functions on axes"""
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=6,
        )

        # Add labels
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Plot a function
        graph = axes.plot(lambda x: 0.1 * x**2, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="y=0.1x^2")

        # Animate
        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.play(Write(graph_label))
        self.wait()


class GroupExample(Scene):
    """Example: Using VGroup to organize objects"""
    def construct(self):
        # Create multiple shapes
        shapes = VGroup(
            Circle().set_fill(RED, opacity=0.5),
            Square().set_fill(GREEN, opacity=0.5),
            Triangle().set_fill(BLUE, opacity=0.5),
            Star().set_fill(YELLOW, opacity=0.5),
        )

        # Arrange them
        shapes.arrange(RIGHT, buff=0.5)

        # Animate with lag
        self.play(
            LaggedStart(*[Create(shape) for shape in shapes], lag_ratio=0.3)
        )
        self.wait()

        # Transform the entire group
        self.play(shapes.animate.arrange(DOWN, buff=0.5))
        self.wait()

        # Rotate all at different speeds
        self.play(
            shapes[0].animate.rotate(PI),
            shapes[1].animate.rotate(PI / 2),
            shapes[2].animate.rotate(PI / 4),
            shapes[3].animate.rotate(PI / 3),
        )
        self.wait()


class UpdaterExample(Scene):
    """Example: Using updaters for dynamic animations"""
    def construct(self):
        # Create a rotating square
        square = Square()

        # Add rotation updater
        square.add_updater(lambda m, dt: m.rotate(dt * PI / 2))

        self.add(square)
        self.wait(4)  # Square rotates during wait

        # Remove updater
        square.clear_updaters()
        self.wait()


class ValueTrackerExample(Scene):
    """Example: Using ValueTracker for animated values"""
    def construct(self):
        # Create a number display
        tracker = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=2)
        number.add_updater(lambda m: m.set_value(tracker.get_value()))

        # Create a circle that scales with the value
        circle = Circle()
        circle.add_updater(
            lambda m: m.become(Circle(radius=0.5 + tracker.get_value() * 0.3))
        )

        self.add(number, circle)
        number.to_corner(UL)

        # Animate the value
        self.play(tracker.animate.set_value(5), run_time=3)
        self.wait()
        self.play(tracker.animate.set_value(0), run_time=2)
        self.wait()


class NumberPlaneExample(Scene):
    """Example: Using NumberPlane for coordinate visualization"""
    def construct(self):
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
        )

        # Create points
        point1 = Dot(plane.c2p(2, 3), color=RED)
        point2 = Dot(plane.c2p(-3, -2), color=BLUE)

        # Create labels
        label1 = MathTex("(2, 3)", color=RED).next_to(point1, UR)
        label2 = MathTex("(-3, -2)", color=BLUE).next_to(point2, DL)

        # Animate
        self.play(Create(plane))
        self.play(FadeIn(point1), FadeIn(point2))
        self.play(Write(label1), Write(label2))
        self.wait()


class MultipleAnimationsExample(Scene):
    """Example: Running multiple animations"""
    def construct(self):
        circle = Circle().shift(LEFT * 2)
        square = Square().shift(RIGHT * 2)

        # Simultaneous animations
        self.play(
            Create(circle),
            Create(square),
        )
        self.wait()

        # With different timing
        self.play(
            circle.animate.shift(UP * 2),
            square.animate.shift(DOWN * 2),
            run_time=2
        )
        self.wait()

        # Sequential with LaggedStart
        triangle1 = Triangle().shift(UP * 2 + LEFT)
        triangle2 = Triangle().shift(UP * 2)
        triangle3 = Triangle().shift(UP * 2 + RIGHT)

        self.play(
            LaggedStart(
                Create(triangle1),
                Create(triangle2),
                Create(triangle3),
                lag_ratio=0.5
            )
        )
        self.wait()


class TableExample(Scene):
    """Example: Creating tables"""
    def construct(self):
        # Simple table
        table = Table(
            [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]],
            row_labels=[Text("A"), Text("B"), Text("C")],
            col_labels=[Text("X"), Text("Y"), Text("Z")]
        )

        table.scale(0.5)
        self.play(Create(table))
        self.wait()

        # Highlight a cell
        table.add_highlighted_cell((2, 3), color=YELLOW)
        self.wait()


class ThreeDExample(ThreeDScene):
    """Example: 3D Scene with camera movement"""
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, resolution=(20, 20))
        sphere.set_color(BLUE)
        sphere.set_opacity(0.8)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Create(axes))
        self.play(Create(sphere))
        self.wait()

        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()
