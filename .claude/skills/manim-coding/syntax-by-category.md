# Manim Syntax Organized by Category

Quick lookup reference for Manim commands organized by functionality.

---

## SCENE STRUCTURE

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Your code here
        pass
```

**Other Scene Types**:
- `Scene` - Standard 2D scene
- `ThreeDScene` - 3D scene with camera controls
- `MovingCameraScene` - Scene with movable camera
- `ZoomedScene` - Scene with zoom functionality
- `VectorScene` - Linear algebra scene

---

## SCENE METHODS

```python
# Animation control
self.play(animation)                    # Execute animation
self.play(anim1, anim2)                # Multiple simultaneous animations
self.wait()                            # Pause 1 second
self.wait(3)                           # Pause 3 seconds

# Object management
self.add(mobject)                      # Add to scene (no animation)
self.remove(mobject)                   # Remove from scene (no animation)
self.add(obj1, obj2, obj3)            # Add multiple objects

# Camera (MovingCameraScene)
self.camera.frame.animate.scale(0.5)
self.camera.frame.animate.move_to(position)
```

---

## SHAPES - BASIC

```python
# Circles and curves
Circle(radius=1.0)
Dot(point=ORIGIN, radius=0.08)
Ellipse(width=2, height=1)
Arc(radius=1.0, start_angle=0, angle=PI/2)
Annulus(inner_radius=1, outer_radius=2)

# Polygons
Square(side_length=2.0)
Rectangle(width=4.0, height=2.0)
Triangle()
RegularPolygon(n=6)                    # n-sided polygon
Star(n=5, outer_radius=1)
RoundedRectangle(corner_radius=0.2)

# Lines
Line(start=LEFT, end=RIGHT)
Arrow(start=LEFT, end=RIGHT)
Vector(direction=RIGHT)
DashedLine(start, end)
```

---

## TEXT AND MATH

```python
# Text
Text("Hello World")
Text("Colored", color=BLUE)
Text("Custom Font", font="Arial")
Text("Large", font_size=72)

# LaTeX math
MathTex(r"\int_0^1 f(x) dx")
MathTex(r"E = mc^2")
MathTex(r"\frac{a}{b}")
MathTex(r"\sum_{i=1}^{n} i^2")

# LaTeX text
Tex(r"This is \LaTeX\ text")

# Multi-part math (for selective animation)
MathTex(r"f(x)", "=", r"x^2", "+", "1")
# Access parts: [0], [1], [2], [3], [4]

# Numbered equations
MathTex(r"f(x) = x^2").add_background_rectangle()
```

---

## COORDINATE SYSTEMS

```python
# 2D Axes
Axes(
    x_range=[-10, 10, 1],              # [min, max, step]
    y_range=[-5, 5, 1],
    x_length=10,
    y_length=6
)

# Number plane (with grid)
NumberPlane(
    x_range=[-10, 10, 1],
    y_range=[-5, 5, 1],
    background_line_style={"stroke_opacity": 0.5}
)

# 3D Axes
ThreeDAxes()

# Complex plane
ComplexPlane()

# Polar plane
PolarPlane(radius_max=5)

# Methods
axes.plot(lambda x: x**2, color=BLUE)
axes.plot(np.sin, x_range=[0, TAU])
axes.get_axis_labels(x_label="x", y_label="y")
axes.get_graph_label(graph, label="f(x)")
axes.c2p(x, y)                        # Coordinate to point
axes.p2c(point)                       # Point to coordinate
```

---

## POSITIONING

```python
# Absolute positioning
obj.move_to(ORIGIN)
obj.move_to(other_obj)
obj.move_to([x, y, z])

# Relative positioning
obj.shift(UP)
obj.shift(RIGHT * 2)
obj.shift(UP * 2 + LEFT * 3)
obj.next_to(other_obj, RIGHT)
obj.next_to(other_obj, UP, buff=0.5)  # Custom spacing

# Edge and corner positioning
obj.to_edge(UP)
obj.to_edge(LEFT, buff=0.5)
obj.to_corner(UL)                     # Upper-left corner

# Alignment
obj.align_to(other_obj, UP)           # Align top edges
obj.align_to(other_obj, LEFT)         # Align left edges

# Centering
obj.center()
obj.to_edge(ORIGIN)
```

**Direction Constants**:
```python
UP, DOWN, LEFT, RIGHT
UL, UR, DL, DR                        # Corners
ORIGIN                                # [0, 0, 0]
```

---

## STYLING

```python
# Color
obj.set_color(BLUE)
obj.set_fill(RED, opacity=0.5)
obj.set_stroke(WHITE, width=3)
obj.set_stroke(color=WHITE, width=2, opacity=0.8)

# Opacity
obj.set_opacity(0.5)                  # 0.0 = transparent, 1.0 = opaque

# Size
obj.scale(2)                          # 2x larger
obj.scale(0.5)                        # Half size
obj.set_width(3)
obj.set_height(2)

# Rotation
obj.rotate(PI / 4)                    # Rotate 45 degrees
obj.rotate(TAU / 8)                   # Same as PI/4
obj.rotate(angle, about_point=ORIGIN)

# Background
obj.add_background_rectangle()
obj.add_background_rectangle(color=BLACK, opacity=0.8)
```

**Common Colors**:
```python
RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE
PINK, WHITE, BLACK, GRAY, GREY
LIGHT_GRAY, DARK_GRAY, LIGHT_BLUE, DARK_BLUE
TEAL, MAROON, GOLD, LIGHT_PINK
```

---

## ANIMATIONS - CREATION

```python
# Basic creation
Create(obj)                           # Draw progressively
FadeIn(obj)                           # Fade in
Write(text)                           # Handwriting effect
DrawBorderThenFill(obj)              # Draw outline, then fill

# Creation with effects
FadeIn(obj, shift=DOWN)
FadeIn(obj, scale=0.5)
GrowFromCenter(obj)
GrowFromEdge(obj, DOWN)
GrowFromPoint(obj, point)
SpinInFromNothing(obj)

# Text-specific
AddTextLetterByLetter(text)
AddTextWordByWord(text)
TypeWithCursor(text)

# Progressive
ShowIncreasingSubsets(group)
ShowSubmobjectsOneByOne(group)
SpiralIn(obj)
```

---

## ANIMATIONS - REMOVAL

```python
# Basic removal
FadeOut(obj)
Uncreate(obj)                         # Reverse of Create
Unwrite(obj)                          # Reverse of Write

# Removal with effects
FadeOut(obj, shift=UP)
FadeOut(obj, scale=1.5)
ShrinkToCenter(obj)

# Text removal
RemoveTextLetterByLetter(text)
UntypeWithCursor(text)
```

---

## ANIMATIONS - TRANSFORMATION

```python
# Basic transforms
Transform(obj1, obj2)                 # Morph obj1 into obj2
ReplacementTransform(obj1, obj2)      # Replace obj1 with obj2
TransformFromCopy(source, target)     # Transform a copy
ClockwiseTransform(obj1, obj2)
CounterclockwiseTransform(obj1, obj2)

# Fade transforms
FadeTransform(obj1, obj2)
FadeTransformPieces(obj1, obj2)

# Method-based
ApplyMethod(obj.method, args)
ApplyFunction(func, obj)
ApplyMatrix(matrix, obj)

# Target-based
obj.generate_target()
obj.target.shift(UP).rotate(PI/4)
MoveToTarget(obj)

# Cyclic
CyclicReplace(obj1, obj2, obj3)
```

---

## ANIMATIONS - MOVEMENT

```python
# Rotation
Rotate(obj, angle=PI)
Rotate(obj, angle=TAU, about_point=ORIGIN)

# Movement along path
path = Line(LEFT*3, RIGHT*3)
MoveAlongPath(obj, path)

# Shifting (use .animate)
obj.animate.shift(UP * 2)
```

---

## ANIMATIONS - INDICATION

```python
# Emphasis
Indicate(obj)                         # Brief emphasis
Circumscribe(obj)                     # Draw circle around
FocusOn(obj)                          # Focus attention
Flash(point)                          # Flash effect
ShowPassingFlash(obj)                 # Passing light
Wiggle(obj)                           # Wiggle
```

---

## THE .animate SYNTAX

```python
# Animate any method call
self.play(obj.animate.shift(UP))
self.play(obj.animate.rotate(PI/4))
self.play(obj.animate.set_color(RED))
self.play(obj.animate.scale(2))
self.play(obj.animate.move_to(ORIGIN))

# Chain transformations
self.play(
    obj.animate
    .shift(UP * 2)
    .rotate(PI / 4)
    .set_color(BLUE)
    .scale(1.5)
)

# Multiple objects
self.play(
    obj1.animate.shift(LEFT),
    obj2.animate.shift(RIGHT),
    obj3.animate.scale(2)
)
```

---

## GROUPING

```python
# Create group
group = VGroup(obj1, obj2, obj3)
group = VGroup(*list_of_objects)

# Arrange
group.arrange(RIGHT)                  # Horizontal
group.arrange(DOWN)                   # Vertical
group.arrange(RIGHT, buff=1)          # With spacing
group.arrange_in_grid(rows=2, cols=3)
group.arrange_in_grid(rows=2, cols=3, buff=0.5)

# Access elements
group[0]                              # First element
group[1:3]                            # Slice
len(group)                            # Number of elements

# Operations
group.shift(UP)                       # Shift all
group.set_color(BLUE)                # Color all
self.play(FadeIn(group))             # Animate all
```

---

## ANIMATION TIMING

```python
# Duration
self.play(Create(obj), run_time=3)    # 3 seconds
self.play(FadeIn(obj), run_time=0.5) # Fast

# Rate functions (easing)
self.play(
    Create(obj),
    rate_func=linear                  # Constant speed
)
self.play(
    Create(obj),
    rate_func=smooth                  # Ease in/out (default)
)

# Other rate functions
rate_func=rush_into                   # Fast start, slow end
rate_func=rush_from                   # Slow start, fast end
rate_func=there_and_back             # Go and return
rate_func=running_start              # Acceleration
```

---

## MULTIPLE ANIMATIONS

```python
# Simultaneous
self.play(
    Create(circle),
    FadeIn(square),
    Write(text)
)

# Sequential with lag
self.play(
    LaggedStart(
        Create(obj1),
        Create(obj2),
        Create(obj3),
        lag_ratio=0.5                 # 0.0-1.0
    )
)

# Succession (one after another)
self.play(
    Succession(
        Create(circle),
        FadeIn(square),
        Write(text)
    )
)

# Animation group
self.play(
    AnimationGroup(
        Create(obj1),
        Create(obj2),
        lag_ratio=0.3
    )
)
```

---

## UPDATERS

```python
# Add updater
def update_func(mobject, dt):
    mobject.rotate(dt * PI / 2)

obj.add_updater(update_func)
self.add(obj)
self.wait(2)                          # Updates during wait
obj.remove_updater(update_func)

# Lambda updater
obj.add_updater(lambda m, dt: m.rotate(dt))

# Clear all updaters
obj.clear_updaters()

# Always updater (no dt parameter)
obj.add_updater(lambda m: m.move_to(other_obj))
```

---

## VALUE TRACKER

```python
# Create tracker
tracker = ValueTracker(0)

# Get/set value
value = tracker.get_value()
tracker.set_value(10)

# Animate value
self.play(tracker.animate.set_value(10), run_time=3)

# Use with updater
number = DecimalNumber(0)
number.add_updater(
    lambda m: m.set_value(tracker.get_value())
)

self.add(number)
self.play(tracker.animate.set_value(100), run_time=5)
```

---

## TABLES

```python
# Basic table
Table(
    [["1", "2", "3"],
     ["4", "5", "6"]],
    row_labels=[Text("A"), Text("B")],
    col_labels=[Text("X"), Text("Y"), Text("Z")]
)

# Math table
MathTable(
    [[1, 2, 3],
     [4, 5, 6]]
)

# Number tables
IntegerTable([[1, 2], [3, 4]])
DecimalTable([[1.5, 2.3], [4.7, 5.1]])

# Methods
table.add_highlighted_cell((row, col), color=YELLOW)
table.get_cell((row, col))
```

---

## 3D SCENES

```python
class My3DScene(ThreeDScene):
    def construct(self):
        # 3D axes
        axes = ThreeDAxes()

        # 3D shapes
        sphere = Sphere(radius=1)
        cube = Cube()
        cylinder = Cylinder(radius=1, height=2)
        cone = Cone()

        # Camera control
        self.set_camera_orientation(
            phi=75 * DEGREES,
            theta=30 * DEGREES
        )

        # Rotate camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # Move camera
        self.move_camera(
            phi=60 * DEGREES,
            theta=45 * DEGREES,
            run_time=2
        )
```

---

## MOBJECT METHODS

```python
# Copying
copy = obj.copy()

# Size queries
obj.get_width()
obj.get_height()
obj.get_center()

# Position queries
obj.get_top()
obj.get_bottom()
obj.get_left()
obj.get_right()
obj.get_corner(UL)

# Submobjects
obj.submobjects                       # List
obj.add(child_obj)
obj.remove(child_obj)

# Become (replace with another)
obj.become(other_obj)
```

---

## COMMON PARAMETERS

```python
# Color parameters
color=BLUE
fill_color=RED
stroke_color=WHITE
fill_opacity=0.5
stroke_opacity=0.8
stroke_width=3

# Size parameters
radius=1.0
width=4.0
height=2.0
side_length=2.0

# Text parameters
font_size=48
font="Arial"

# Animation parameters
run_time=2.0
rate_func=smooth
lag_ratio=0.5

# Positioning parameters
buff=0.5                              # Spacing
aligned_edge=UP                       # Alignment edge
```

---

## MATHEMATICAL CONSTANTS

```python
PI          # 3.14159...
TAU         # 2*PI = 6.28318...
E           # 2.71828...
DEGREES     # PI/180 (for degree conversion)

# Usage
obj.rotate(45 * DEGREES)
obj.rotate(PI / 4)
obj.rotate(TAU / 8)
```

---

## COMMAND LINE FLAGS

```bash
# Quality presets
-ql, --quality l         # Low (480p, 15fps)
-qm, --quality m         # Medium (720p, 30fps)
-qh, --quality h         # High (1080p, 60fps)
-qk, --quality k         # 4K (2160p, 60fps)

# Preview
-p, --preview            # Open video after rendering

# Rendering
-s, --save_last_frame    # Render last frame only
-a                       # Render all scenes

# Format
--format=gif             # Render as GIF
--format=png             # Render as PNG sequence

# Common combinations
manim -pql file.py Scene      # Preview low quality
manim -pqh file.py Scene      # Preview high quality
manim -s file.py Scene        # Save last frame
```

---

## DEBUGGING

```python
# Add dot at position
self.add(Dot(position, color=RED))

# Print coordinates
print(obj.get_center())

# Background rectangle (to see bounds)
obj.add_background_rectangle()

# Color submobjects differently
for i, submob in enumerate(obj.submobjects):
    submob.set_color([RED, GREEN, BLUE][i % 3])

# Show axes for reference
self.add(Axes())

# Render only last frame
# manim -s script.py SceneName
```

---

## BEST PRACTICES

1. **Use `.animate` for simple transformations**
   ```python
   self.play(obj.animate.shift(UP))  # Good
   self.play(ApplyMethod(obj.shift, UP))  # Verbose
   ```

2. **Use VGroup for related objects**
   ```python
   group = VGroup(obj1, obj2, obj3)
   group.arrange(RIGHT)
   ```

3. **Use raw strings for LaTeX**
   ```python
   MathTex(r"\frac{1}{2}")  # Good
   MathTex("\\frac{1}{2}")   # Works but messy
   ```

4. **Break complex formulas into parts**
   ```python
   eq = MathTex("E", "=", "m", "c^2")
   # Can animate parts separately
   ```

5. **Use run_time for pacing**
   ```python
   self.play(animation, run_time=2)  # Control speed
   ```
