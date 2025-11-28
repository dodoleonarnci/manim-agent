---
name: manim-coding
description: Expert knowledge of Manim Community Edition for creating programmatic mathematical animations. Use when writing Manim code, creating animations, working with mathematical visualizations, or helping debug Manim scripts.
allowed-tools: Read, Write, Bash, Grep, Glob
---

# Manim Community Edition Coding Skill

This skill provides comprehensive reference for Manim Community Edition (ManimCE), a Python library for creating programmatic animations of mathematical and technical concepts.

**Official Documentation**: https://docs.manim.community/en/stable/

---

## SECTION 0: PROJECT DIRECTORY SETUP (CRITICAL - DO THIS FIRST!)

**IMPORTANT**: Before starting any Manim project, you MUST set up the correct working directory.

### Directory Management Rules

1. **Create a project subdirectory** in `/manim-projects/`
2. **Work exclusively within that subdirectory** for all file operations
3. **Use descriptive project names** (e.g., `fourier-epicycles`, `calculus-derivatives`, `linear-algebra-transforms`)

### Setup Steps

When starting a new Manim project:

```bash
# Step 1: Create project directory
mkdir -p /manim-projects/your-project-name

# Step 2: Navigate to project directory
cd /manim-projects/your-project-name

# Step 3: Create your animation file
# (Use Write tool to create the .py file in this directory)

# Step 4: Run manim from within the project directory
manim -pql animation.py SceneName
```

### Example Workflow

```bash
# For a Fourier Transform project:
mkdir -p /manim-projects/fourier-epicycles
cd /manim-projects/fourier-epicycles

# Now create fourier_animation.py in this directory
# Then run:
manim -pql fourier_animation.py FourierScene
```

### File Paths

- **Animation files**: `/manim-projects/your-project-name/animation.py`
- **Asset files** (SVGs, images): `/manim-projects/your-project-name/assets/`
- **Output videos**: `/manim-projects/your-project-name/media/videos/...`
- **Research reports**: `/manim-projects/your-project-name/research-reports/` (if needed)

### Before Every File Operation

**Always verify you're in the correct directory**:

```bash
pwd  # Should show /manim-projects/your-project-name
```

### Important Notes

- **DO NOT** work in the root directory or home directory
- **DO NOT** create Manim files outside of `/manim-projects/`
- **ALWAYS** use absolute paths starting with `/manim-projects/your-project-name/` when using Write, Read, or other file tools
- The `/manim-projects/` directory should already exist on the system

---

## SECTION 1: ESSENTIAL BASICS (Most Commonly Used)

These are the fundamental commands and patterns used in virtually every Manim project.

### Basic Scene Structure

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # All animation code goes here
        pass
```

**Key Points**:
- Import everything from manim: `from manim import *`
- Create a class that inherits from `Scene`
- All animation logic goes in the `construct()` method

### Multi-Scene Projects with Combined Scene

**IMPORTANT**: When creating projects with multiple scenes, use helper methods to enable scene combination:

```python
from manim import *

class Scene1(Scene):
    def construct(self):
        self.scene1_animation()

    def scene1_animation(self):
        """First scene animation - can be called from any scene"""
        text = Text("Scene 1")
        self.play(Write(text))
        self.wait()

class Scene2(Scene):
    def construct(self):
        self.scene2_animation()

    def scene2_animation(self):
        """Second scene animation - can be called from any scene"""
        text = Text("Scene 2")
        self.play(Write(text))
        self.wait()

class CombinedScenes(Scene):
    def construct(self):
        """Combines all scenes in the correct order for a single video."""
        # Play Scene 1
        Scene1.scene1_animation(self)
        self.clear()

        # Play Scene 2
        Scene2.scene2_animation(self)
```

**Note**:
- Each scene's logic goes in a separate method (e.g., `scene1_animation`)
- Individual scenes call their own method from `construct()`
- `CombinedScenes` calls all scene methods with `self` as the context
- Use `self.clear()` between scenes to clear the screen
- The helper method must use `self` for all Manim operations (`self.play()`, `self.add()`, etc.)

### Core Scene Methods

```python
self.play(animation)           # Execute an animation
self.wait()                    # Pause for 1 second
self.wait(2)                   # Pause for 2 seconds
self.add(mobject)              # Add object to scene (instantly, no animation)
self.remove(mobject)           # Remove object from scene
```

### Essential Animations

**Creation Animations** (making objects appear):
```python
self.play(Create(circle))              # Draw the object progressively
self.play(FadeIn(square))              # Fade in
self.play(Write(text))                 # Handwriting effect (for text/VMobjects)
self.play(DrawBorderThenFill(shape))   # Draw outline then fill
```

**Removal Animations**:
```python
self.play(FadeOut(mobject))            # Fade out
self.play(Uncreate(mobject))           # Reverse of Create
self.play(Unwrite(mobject))            # Reverse of Write
```

**Transformation Animations**:
```python
self.play(Transform(obj1, obj2))                # Morph obj1 into obj2
self.play(ReplacementTransform(obj1, obj2))     # Replace obj1 with obj2
self.play(TransformFromCopy(source, target))    # Transform a copy
```

### The `.animate` Syntax (Very Common)

The `.animate` property allows you to animate any method call:

```python
# Instead of calling methods directly, use .animate to animate the change
self.play(square.animate.rotate(PI / 4))
self.play(square.animate.shift(UP * 2))
self.play(circle.animate.set_fill(PINK, opacity=0.5))
self.play(text.animate.scale(2))

# Chain multiple transformations
self.play(mobject.animate.shift(UP).rotate(PI/2).set_color(BLUE))
```

### Most Common Shapes

```python
# Basic shapes
circle = Circle()
square = Square()
triangle = Triangle()
rectangle = Rectangle(width=4, height=2)
line = Line(start=LEFT, end=RIGHT)
arrow = Arrow(start=LEFT, end=RIGHT)
dot = Dot()

# Polygons
polygon = Polygon(point1, point2, point3, ...)
regular_poly = RegularPolygon(n=6)  # hexagon
star = Star(n=5)
```

### Essential Text and Math

```python
# Regular text (non-LaTeX)
text = Text("Hello World")
text = Text("Colored Text", color=BLUE)

# LaTeX math
math = MathTex(r"\int_0^1 f(x) dx")
equation = MathTex(r"E = mc^2")

# LaTeX text
latex_text = Tex(r"This is \LaTeX text")

# Multi-part math for selective animation
formula = MathTex(r"f(x)", "=", r"x^2", "+", r"2x", "+", "1")
# Can access parts: formula[0], formula[2], etc.
```

### Basic Positioning Methods

```python
# Positioning
mobject.shift(UP)                          # Move relative to current position
mobject.shift(RIGHT * 2)                   # Move 2 units right
mobject.move_to(ORIGIN)                    # Move to absolute position
mobject.move_to(other_obj)                 # Move to position of another object
mobject.next_to(other_obj, RIGHT)          # Position next to another object
mobject.next_to(other_obj, UP, buff=0.5)   # With custom spacing

# Alignment
mobject.align_to(other_obj, UP)            # Align edges
mobject.to_edge(UP)                        # Move to edge of screen
mobject.to_corner(UL)                      # Move to corner (UL, UR, DL, DR)
```

### Direction and Position Constants

```python
# Directional vectors
UP, DOWN, LEFT, RIGHT
UL, UR, DL, DR        # Corners (Up-Left, etc.)
ORIGIN                # Center of screen (0, 0, 0)

# Common usage
mobject.shift(UP * 2 + RIGHT * 3)
```

### Basic Styling Methods

```python
# Color
mobject.set_color(BLUE)
mobject.set_fill(RED, opacity=0.5)         # Fill color and opacity
mobject.set_stroke(WHITE, width=3)         # Border color and width

# Opacity
mobject.set_opacity(0.5)                   # 0.0 = transparent, 1.0 = opaque

# Scale and Rotate
mobject.scale(2)                           # Make 2x larger
mobject.rotate(PI / 4)                     # Rotate by 45 degrees
mobject.rotate(TAU / 8)                    # TAU = 2*PI
```

### Common Colors

```python
# Basic colors
RED, GREEN, BLUE
YELLOW, ORANGE, PURPLE
PINK, WHITE, BLACK, GRAY, GREY

# Extended colors
LIGHT_GRAY, DARK_GRAY
LIGHT_BLUE, DARK_BLUE
TEAL, MAROON, GOLD

# Gradients
color_gradient([RED, BLUE, GREEN], 100)
```

### Running Manim from Command Line

```bash
# Basic rendering
manim script.py SceneName

# With preview (opens video after rendering)
manim -p script.py SceneName

# Quality settings
manim -pql script.py SceneName    # Low quality (preview)
manim -pqm script.py SceneName    # Medium quality
manim -pqh script.py SceneName    # High quality (1080p)
manim -pqk script.py SceneName    # 4K quality

# Render last frame only
manim -s script.py SceneName      # Save last frame as image

# Multiple flags
manim -pqh --format=gif script.py SceneName  # Render as GIF
```

**Common flags**:
- `-p`: Preview (play video after rendering)
- `-q`: Quality (`l`=low, `m`=medium, `h`=high, `k`=4K)
- `-s`: Save last frame only
- `--format=gif`: Render as GIF instead of video

---

## SECTION 2: INTERMEDIATE FEATURES (Commonly Used)

These features are frequently used in more complex animations.

### Advanced Text Animations

```python
# Letter by letter
self.play(AddTextLetterByLetter(text))
self.play(RemoveTextLetterByLetter(text))

# Word by word
self.play(AddTextWordByWord(text))

# Typing effect with cursor
self.play(TypeWithCursor(text))
self.play(UntypeWithCursor(text))
```

### Grouping and VGroups

```python
# Create a group
group = VGroup(circle, square, triangle)

# Operate on the entire group
group.arrange(RIGHT, buff=0.5)             # Arrange horizontally
group.arrange(DOWN, buff=1.0)              # Arrange vertically
group.arrange_in_grid(rows=2, cols=3)      # Arrange in grid

# Transform groups
self.play(group.animate.shift(UP))
self.play(FadeIn(group))                   # Animate all at once

# Access individual elements
group[0]  # First element
group[1]  # Second element
```

### Coordinate Systems and Graphing

```python
# Create axes
axes = Axes(
    x_range=[-10, 10, 1],        # [min, max, step]
    y_range=[-5, 5, 1],
    x_length=10,
    y_length=6
)

# Number plane (with grid)
plane = NumberPlane(
    x_range=[-10, 10, 1],
    y_range=[-5, 5, 1]
)

# Plot functions
graph = axes.plot(lambda x: x**2, color=BLUE)
graph = axes.plot(np.sin, x_range=[0, 2*PI], color=RED)

# Add labels
labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
graph_label = axes.get_graph_label(graph, label="y=x^2")

# Get coordinates
point = axes.c2p(2, 4)  # Convert coordinate (2,4) to pixel position
coords = axes.p2c(point)  # Convert pixel position to coordinates
```

### Movement Animations

```python
# Rotation
self.play(Rotate(mobject, angle=PI))
self.play(Rotate(mobject, angle=TAU, about_point=ORIGIN))

# Moving along a path
path = Line(LEFT * 3, RIGHT * 3)
self.play(MoveAlongPath(dot, path))

# Complex movement (using .animate)
self.play(mobject.animate.shift(UP * 2).rotate(PI / 2))
```

### Fading with Effects

```python
# Fade with movement
self.play(FadeIn(mobject, shift=DOWN))
self.play(FadeOut(mobject, shift=UP, scale=0.5))

# Fade transform between objects
self.play(FadeTransform(obj1, obj2))
self.play(FadeTransformPieces(obj1, obj2))  # Animates submobjects
```

### Updaters (Dynamic Animations)

```python
# Add an updater function
def update_func(mobject, dt):
    mobject.rotate(dt * PI / 2)  # Rotate continuously

mobject.add_updater(update_func)
self.add(mobject)
self.wait(2)  # Mobject will update during wait
mobject.remove_updater(update_func)

# Value tracker for animated values
tracker = ValueTracker(0)
decimal = DecimalNumber(0)
decimal.add_updater(lambda m: m.set_value(tracker.get_value()))

self.play(tracker.animate.set_value(10), run_time=3)
```

### Animation Timing and Run Time

```python
# Control animation speed
self.play(Create(circle), run_time=3)      # Takes 3 seconds
self.play(FadeIn(square), run_time=0.5)    # Fast animation

# Multiple animations with different timing
self.play(
    Create(circle),
    FadeIn(square),
    run_time=2
)

# Rate functions (easing)
from manim import rate_functions as rf
self.play(
    Create(circle),
    rate_func=rf.smooth,        # Smooth ease in/out
    run_time=2
)
```

### Rate Functions (Easing)

```python
# Common easing functions
rate_func=linear                    # Constant speed
rate_func=smooth                    # Ease in and out (default)
rate_func=rush_into                 # Fast start, slow end
rate_func=rush_from                 # Slow start, fast end
rate_func=there_and_back            # Go and return
rate_func=running_start             # Acceleration from start

# Example usage
self.play(circle.animate.shift(RIGHT * 4), rate_func=smooth)
```

### Animation Lag and Succession

```python
# Animate submobjects with lag
self.play(
    LaggedStart(*[Create(obj) for obj in objects], lag_ratio=0.5)
)

# Animate in succession
self.play(
    Succession(
        Create(circle),
        FadeIn(square),
        Write(text)
    )
)

# AnimationGroup
self.play(
    AnimationGroup(
        Create(circle),
        FadeIn(square),
        lag_ratio=0.3
    )
)
```

### Tables and Matrices

```python
# Basic table
table = Table(
    [["1", "2", "3"],
     ["4", "5", "6"]],
    row_labels=[Text("Row 1"), Text("Row 2")],
    col_labels=[Text("A"), Text("B"), Text("C")]
)

# Math table (with LaTeX)
math_table = MathTable(
    [[1, 2, 3],
     [4, 5, 6]],
    element_to_mobject=lambda x: MathTex(str(x))
)

# Integer/Decimal tables
int_table = IntegerTable([[1, 2], [3, 4]])
dec_table = DecimalTable([[1.5, 2.3], [4.7, 5.1]])

# Highlight cells
table.add_highlighted_cell((2, 3), color=YELLOW)
```

### 3D Scenes

```python
from manim import ThreeDScene

class My3DScene(ThreeDScene):
    def construct(self):
        # Create 3D axes
        axes = ThreeDAxes()

        # Create 3D objects
        sphere = Sphere(radius=1)
        cube = Cube()

        # Camera controls
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        self.add(axes, sphere)
        self.wait(2)

        self.stop_ambient_camera_rotation()
```

### Common Mobject Methods

```python
# Copying
copy = mobject.copy()
mobject2 = mobject.deepcopy()

# Sizing
mobject.get_width()
mobject.get_height()
mobject.set_width(3)
mobject.set_height(2)

# Position queries
mobject.get_center()
mobject.get_top()
mobject.get_bottom()
mobject.get_left()
mobject.get_right()
mobject.get_corner(UL)

# Submobjects
mobject.submobjects              # List of submobjects
len(mobject)                     # Number of submobjects
mobject[0]                       # Access first submobject
```

---

## SECTION 3: ADVANCED FEATURES (Less Common)

These are specialized features for advanced use cases.

### Custom Animations

```python
class MyAnimation(Animation):
    def __init__(self, mobject, **kwargs):
        super().__init__(mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        # alpha goes from 0 to 1
        # Define how the mobject changes
        self.mobject.scale(1 + alpha)
```

### Specialized Shapes

```python
# Arcs and sectors
arc = Arc(radius=1, start_angle=0, angle=PI/2)
sector = Sector(radius=2, start_angle=0, angle=PI/3)
annulus = Annulus(inner_radius=1, outer_radius=2)
annular_sector = AnnularSector(inner_radius=1, outer_radius=2)

# Bezier curves
curve = CubicBezier(start, control1, control2, end)
arc_between = ArcBetweenPoints(point1, point2)
arc_polygon = ArcPolygon(point1, point2, point3, ...)

# Rounded shapes
rounded_rect = RoundedRectangle(corner_radius=0.5)

# Labeled shapes
labeled_dot = LabeledDot(Text("A"))
annotation_dot = AnnotationDot()
```

### Complex Plane and Polar Coordinates

```python
# Complex plane
plane = ComplexPlane()
point = plane.n2p(complex(2, 3))  # Convert complex number to point

# Polar plane
polar = PolarPlane(radius_max=5)
```

### Matrix Transformations

```python
# Apply matrix transformation
matrix = [[1, 2], [3, 4]]
self.play(ApplyMatrix(matrix, mobject))

# Apply custom function to points
def custom_func(point):
    x, y, z = point
    return np.array([x**2, y**2, z])

self.play(ApplyFunction(custom_func, mobject))
self.play(ApplyPointwiseFunction(custom_func, mobject))
```

### Indication Animations

```python
# Highlight and indicate
self.play(Indicate(mobject))                    # Brief emphasis
self.play(Flash(mobject))                       # Flash effect
self.play(FocusOn(mobject))                     # Focus attention
self.play(Circumscribe(mobject))                # Draw circle around
self.play(ShowPassingFlash(mobject))            # Passing light effect
self.play(Wiggle(mobject))                      # Wiggle effect
```

### Transform Variants

```python
# Cyclic replacement
self.play(CyclicReplace(mob1, mob2, mob3))

# Clockwise transform
self.play(ClockwiseTransform(source, target))
self.play(CounterclockwiseTransform(source, target))

# Move to target (requires setting target first)
mobject.generate_target()
mobject.target.shift(UP * 2).rotate(PI / 4)
self.play(MoveToTarget(mobject))

# Scale in place
self.play(ScaleInPlace(mobject, scale_factor=2))
self.play(ShrinkToCenter(mobject))
```

### Advanced Text Manipulation

```python
# Text with different fonts
text = Text("Custom Font", font="Arial")

# Text with colors and gradients
text = Text("Gradient", gradient=(RED, BLUE))
text = Text("Multi", t2c={"Multi": BLUE})  # Text2color

# Math with color mapping
formula = MathTex(
    r"x^2", "+", r"y^2", "=", r"r^2",
    substrings_to_isolate=["x", "y", "r"]
)
formula.set_color_by_tex("x", RED)
formula.set_color_by_tex("y", BLUE)
```

### Custom Colors

```python
# Create custom colors
from manim import ManimColor
custom = ManimColor("#FF5733")

# Color palettes
from manim import XKCD, X11
color = XKCD.AVOCADO
color = X11.NAVY_BLUE

# Interpolate between colors
interpolate_color(RED, BLUE, alpha=0.5)
color_gradient([RED, GREEN, BLUE], 10)
```

### Scene Variants

```python
# Moving camera scene
class MyScene(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.5).move_to(target))
        self.play(Restore(self.camera.frame))

# Zoomed scene
class MyScene(ZoomedScene):
    def construct(self):
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        # Use zoomed camera functionality

# Vector scene (linear algebra)
class MyScene(VectorScene):
    def construct(self):
        vector = self.add_vector([2, 3])
        matrix = [[1, 2], [3, 4]]
        self.apply_matrix(matrix)
```

### Advanced Graphing

```python
# Parametric functions
curve = ParametricFunction(
    lambda t: np.array([np.cos(t), np.sin(t), 0]),
    t_range=[0, TAU]
)

# Implicit functions
implicit_curve = ImplicitFunction(
    lambda x, y: x**2 + y**2 - 1
)

# Surface plots (3D)
surface = Surface(
    lambda u, v: np.array([u, v, u**2 + v**2]),
    u_range=[-2, 2],
    v_range=[-2, 2]
)

# Area under curve
area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.3)
riemann_rectangles = axes.get_riemann_rectangles(
    graph, x_range=[0, 2], dx=0.1
)
```

### Homotopy and Phase Flow

```python
# Complex homotopy
def complex_func(z, t):
    return z * np.exp(complex(0, t * TAU))

self.play(ComplexHomotopy(complex_func, mobject))

# Homotopy (general)
def homotopy_func(x, y, z, t):
    return [x * (1-t), y * (1-t), z]

self.play(Homotopy(homotopy_func, mobject))

# Phase flow
def flow_func(point):
    x, y, z = point
    return np.array([y, -x, 0])

self.play(PhaseFlow(flow_func, mobject))
```

### Override Animations

```python
# Override default animations for custom classes
class MySquare(Square):
    @override_animation(Create)
    def _create_override(self, **kwargs):
        return AnimationGroup(
            Create(self),
            FadeIn(self),
            **kwargs
        )
```

### Advanced Configuration

```python
# Configure scene settings
config.frame_width = 14.0
config.frame_height = 8.0
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60
config.background_color = WHITE

# In script
class MyScene(Scene):
    def __init__(self, **kwargs):
        config.background_color = BLACK
        super().__init__(**kwargs)
```

---

## QUICK REFERENCE: Common Patterns

### Basic Animation Flow

```python
class MyScene(Scene):
    def construct(self):
        # 1. Create objects
        circle = Circle()

        # 2. Style them
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(WHITE, width=3)

        # 3. Position them
        circle.shift(UP * 2)

        # 4. Animate
        self.play(Create(circle))
        self.wait()

        # 5. Transform
        square = Square()
        square.move_to(circle)
        self.play(Transform(circle, square))
        self.wait()
```

### Multiple Objects Pattern

```python
class MultipleObjects(Scene):
    def construct(self):
        # Create multiple objects
        shapes = VGroup(
            Circle(),
            Square(),
            Triangle()
        )

        # Arrange them
        shapes.arrange(RIGHT, buff=1)

        # Animate them
        self.play(
            LaggedStart(*[Create(s) for s in shapes], lag_ratio=0.3)
        )
        self.wait()
```

### Graph Plotting Pattern

```python
class GraphScene(Scene):
    def construct(self):
        # Setup axes
        axes = Axes(x_range=[-5, 5], y_range=[-3, 3])

        # Plot function
        graph = axes.plot(lambda x: x**2, color=BLUE)

        # Add labels
        labels = axes.get_axis_labels()

        # Animate
        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.wait()
```

### Math Formula Pattern

```python
class FormulaScene(Scene):
    def construct(self):
        # Create formula parts
        formula = MathTex(
            r"\int_0^1", r"x^2", r"dx", "=", r"\frac{1}{3}"
        )

        # Animate parts
        self.play(Write(formula[0:3]))  # Integral
        self.wait()
        self.play(Write(formula[3:]))   # Result
        self.wait()

        # Highlight specific part
        self.play(Indicate(formula[1]))  # Highlight x^2
```

---

## Common Gotchas and Tips

### Transform vs ReplacementTransform

- **`Transform(A, B)`**: Morphs A into B, but A remains on screen (B is just a target)
- **`ReplacementTransform(A, B)`**: Removes A and replaces it with B

```python
# After Transform, 'circle' is still the object reference
self.play(Transform(circle, square))  # circle morphs to look like square
self.play(FadeOut(circle))  # Remove the morphed object

# After ReplacementTransform, 'square' is now on screen
self.play(ReplacementTransform(circle, square))
self.play(FadeOut(square))  # Remove square
```

### Using Multi-part Math

```python
# Break formulas into parts for selective animation
eq = MathTex("E", "=", "m", "c^2")
# Can now animate: eq[0], eq[1], eq[2], eq[3] separately

# Color specific parts
eq[0].set_color(RED)   # Color E
eq[3].set_color(BLUE)  # Color c^2
```

### LaTeX Syntax in MathTex

```python
# Use raw strings (r"...") for LaTeX
MathTex(r"\frac{1}{2}")        # Good
MathTex("\\frac{1}{2}")         # Also works but messy

# Escape special characters
MathTex(r"\text{f(x) = x^2}")  # Good for text in math
```

### Coordinate Systems

- Screen coordinates: `[-7, 7]` horizontally, `[-4, 4]` vertically (default)
- Use `config.frame_width` and `config.frame_height` to check
- `axes.c2p(x, y)` converts coordinate to pixel position
- `axes.p2c(point)` converts pixel position to coordinate

---

## Resources

- **Official Docs**: https://docs.manim.community/en/stable/
- **Example Gallery**: https://docs.manim.community/en/stable/examples.html
- **Discord Community**: https://discord.gg/mMRrZQW
- **Online Editor**: https://try.manim.community/
- **GitHub**: https://github.com/ManimCommunity/manim

---

## Version Info

This reference is based on **Manim Community Edition v0.19.0**. Always check the official documentation for the latest updates and changes.
