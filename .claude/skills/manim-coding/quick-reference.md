# Manim Quick Reference Cheat Sheet

## Minimal Working Example

```python
from manim import *

class BasicScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()
```

## Command Line

```bash
# Preview in low quality (fastest)
manim -pql script.py SceneName

# High quality render
manim -pqh script.py SceneName

# Save last frame only
manim -s script.py SceneName
```

## Most Used Animations

| Animation | Usage |
|-----------|-------|
| `Create(obj)` | Draw object progressively |
| `FadeIn(obj)` | Fade in |
| `FadeOut(obj)` | Fade out |
| `Write(text)` | Handwriting effect |
| `Transform(a, b)` | Morph a into b |
| `ReplacementTransform(a, b)` | Replace a with b |

## Most Used Shapes

```python
Circle()
Square()
Triangle()
Rectangle(width=w, height=h)
Line(start, end)
Arrow(start, end)
Dot()
Text("string")
MathTex(r"\LaTeX")
```

## Scene Methods

```python
self.play(animation)      # Run animation
self.wait()               # Pause 1 second
self.add(obj)            # Add instantly
self.remove(obj)         # Remove instantly
```

## The .animate Syntax

```python
# Animate any method call
self.play(obj.animate.shift(UP))
self.play(obj.animate.rotate(PI/4))
self.play(obj.animate.set_color(RED))
self.play(obj.animate.scale(2))
```

## Positioning

```python
obj.shift(UP)                    # Relative move
obj.move_to(ORIGIN)              # Absolute position
obj.next_to(other, RIGHT)        # Position relative to another
obj.to_edge(UP)                  # Move to edge
obj.to_corner(UL)                # Move to corner
```

## Directions

```python
UP, DOWN, LEFT, RIGHT
UL, UR, DL, DR    # Corners
ORIGIN            # (0, 0, 0)
```

## Styling

```python
obj.set_color(BLUE)
obj.set_fill(RED, opacity=0.5)
obj.set_stroke(WHITE, width=3)
obj.set_opacity(0.5)
obj.scale(2)
obj.rotate(PI/4)
```

## Common Colors

```python
RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE
PINK, WHITE, BLACK, GRAY
LIGHT_BLUE, DARK_BLUE
```

## VGroup (Grouping)

```python
group = VGroup(obj1, obj2, obj3)
group.arrange(RIGHT)              # Arrange horizontally
group.arrange_in_grid(2, 2)       # Grid layout
self.play(FadeIn(group))          # Animate all together
```

## Axes and Graphing

```python
axes = Axes(
    x_range=[-10, 10, 1],
    y_range=[-5, 5, 1]
)
graph = axes.plot(lambda x: x**2)
self.play(Create(axes), Create(graph))
```

## Animation Timing

```python
self.play(Create(circle), run_time=3)    # 3 seconds
self.wait(2)                              # Wait 2 seconds
```

## Multiple Animations

```python
# Simultaneous
self.play(Create(circle), FadeIn(square))

# Sequential with lag
self.play(
    LaggedStart(
        Create(circle),
        Create(square),
        lag_ratio=0.5
    )
)
```

## Constants

```python
PI          # 3.14159...
TAU         # 2*PI = 6.28318...
DEGREES     # For angle conversions
```

## Common Mistakes

1. **Forgot `from manim import *`**
2. **Forgot `self` in Scene methods**
3. **Using `Transform` when you meant `ReplacementTransform`**
4. **Forgetting `r` prefix for LaTeX strings**: `MathTex(r"\frac{1}{2}")`
5. **Not using `.animate` for method animations**
