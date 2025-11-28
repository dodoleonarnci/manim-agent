# Parameter Refactoring Workflow

## Purpose

When creating Manim animations, it's critical to **extract all "magic numbers" into a `params.py` file** and replace hardcoded values in the animation code with parameter references. This makes animations easy to customize without touching the core logic. Make sure that all magic numbers named do exist in `params.py`.

## Critical Rule

**❌ WRONG: Hardcoded "magic numbers" in animation code**
```python
# animation.py
title = Text("My Animation", font_size=36)
self.play(Write(title), run_time=1.5)
circle = Circle(radius=2.0, color=BLUE, stroke_width=3)
```

**✅ CORRECT: Parameters imported from params.py**
```python
# animation.py
import params

title = Text("My Animation", font_size=params.TITLE_FONT_SIZE)
self.play(Write(title), run_time=params.TITLE_WRITE_TIME)
circle = Circle(
    radius=params.CIRCLE_RADIUS,
    color=globals()[params.CIRCLE_COLOR],  # Convert string to color constant
    stroke_width=params.CIRCLE_STROKE_WIDTH
)
```

---

## Step-by-Step Workflow

### Step 1: Create params.py File

Create a `params.py` file in the project directory with clear sections:

```python
"""
Parameters for [Animation Name]

Modify these values to customize the animation without touching animation.py
"""

# ============================================================================
# SCENE 1: [Scene Name]
# ============================================================================

# Timing parameters
SCENE1_TITLE_WRITE_TIME = 1.5
SCENE1_TITLE_SCALE_TIME = 0.5
SCENE1_MAIN_ANIMATION_TIME = 3.0
SCENE1_FADEOUT_TIME = 0.5

# Visual parameters
TITLE_FONT_SIZE = 36
TITLE_SCALE = 0.7
MAIN_OBJECT_RADIUS = 2.0
MAIN_OBJECT_COLOR = "BLUE"  # String name, will convert to constant
MAIN_OBJECT_STROKE_WIDTH = 3

# Position parameters
MAIN_OBJECT_SHIFT_X = 2.0
MAIN_OBJECT_SHIFT_Y = 1.0

# ============================================================================
# SCENE 2: [Another Scene]
# ============================================================================

# ... more parameters
```

### Step 2: Import params in animation.py

Add the import at the top of `animation.py`:

```python
from manim import *
import numpy as np
import params  # Import all configurable parameters
```

### Step 3: Replace ALL Magic Numbers

Go through animation.py **scene by scene** and replace every hardcoded number. Do this for EVERY SCENE.:

#### Timing Values

**Before:**
```python
self.play(Write(title), run_time=1.5)
self.wait(2.0)
```

**After:**
```python
self.play(Write(title), run_time=params.SCENE1_TITLE_WRITE_TIME)
self.wait(params.SCENE1_WAIT_TIME)
```

#### Visual Properties

**Before:**
```python
title = Text("My Title", font_size=36)
circle = Circle(radius=2.5, stroke_width=3)
```

**After:**
```python
title = Text("My Title", font_size=params.TITLE_FONT_SIZE)
circle = Circle(
    radius=params.CIRCLE_RADIUS,
    stroke_width=params.CIRCLE_STROKE_WIDTH
)
```

#### Colors (Special Handling)

Colors in Manim are constants (e.g., `BLUE`, `RED`). Store them as strings in params.py and convert:

**params.py:**
```python
CIRCLE_COLOR = "BLUE"
ARROW_COLOR = "RED"
```

**animation.py:**
```python
# Convert string to Manim color constant
circle_color = globals()[params.CIRCLE_COLOR]
circle = Circle(color=circle_color)

# Or inline:
arrow = Arrow(color=globals()[params.ARROW_COLOR])
```

#### Lists and Arrays

**Before:**
```python
radii = [1.5, 0.8, 0.4, 0.2]
frequencies = [1, 2, 3, 4]
colors = [BLUE, GREEN, YELLOW, RED]
```

**After (params.py):**
```python
EPICYCLE_RADII = [1.5, 0.8, 0.4, 0.2]
EPICYCLE_FREQUENCIES = [1, 2, 3, 4]
EPICYCLE_COLORS = ["BLUE", "GREEN", "YELLOW", "RED"]  # Strings
```

**After (animation.py):**
```python
radii = params.EPICYCLE_RADII
frequencies = params.EPICYCLE_FREQUENCIES
colors = [globals()[c] for c in params.EPICYCLE_COLORS]
```

#### Loops with Parameters

**Before:**
```python
for i in range(3):
    wave = axes.plot(lambda x: amplitudes[i] * np.sin(freqs[i] * x))
```

**After (params.py):**
```python
WAVE_AMPLITUDES = [1.0, 0.5, 0.3]
WAVE_FREQUENCIES = [1, 3, 5]
```

**After (animation.py):**
```python
for i in range(len(params.WAVE_FREQUENCIES)):
    wave = axes.plot(
        lambda x, i=i: params.WAVE_AMPLITUDES[i] * np.sin(params.WAVE_FREQUENCIES[i] * x)
    )
```

---

## Comprehensive Example

### params.py

```python
"""Animation Parameters"""

# ============================================================================
# GENERAL
# ============================================================================

TITLE_FONT_SIZE = 36
LABEL_FONT_SIZE = 24
TITLE_SCALE = 0.7

# ============================================================================
# SCENE 1
# ============================================================================

# Timing
SCENE1_INTRO_TIME = 1.5
SCENE1_MAIN_TIME = 3.0
SCENE1_OUTRO_TIME = 0.5

# Objects
CIRCLE_RADIUS = 2.0
CIRCLE_COLOR = "BLUE"
CIRCLE_STROKE_WIDTH = 3

# Positions
CIRCLE_POSITION_X = 2.0
CIRCLE_POSITION_Y = -1.0
```

### animation.py

```python
from manim import *
import params

class MyScene(Scene):
    def construct(self):
        # Title with parameterized font size and timing
        title = Text("My Animation", font_size=params.TITLE_FONT_SIZE)
        self.play(Write(title), run_time=params.SCENE1_INTRO_TIME)
        self.play(title.animate.scale(params.TITLE_SCALE).to_edge(UP))

        # Circle with all parameters
        circle = Circle(
            radius=params.CIRCLE_RADIUS,
            color=globals()[params.CIRCLE_COLOR],
            stroke_width=params.CIRCLE_STROKE_WIDTH
        )
        circle.shift(
            RIGHT * params.CIRCLE_POSITION_X +
            DOWN * params.CIRCLE_POSITION_Y
        )

        self.play(Create(circle), run_time=params.SCENE1_MAIN_TIME)
        self.play(FadeOut(circle), run_time=params.SCENE1_OUTRO_TIME)
```

---

## What Counts as a "Magic Number"?

### ✅ EXTRACT These

- **All numeric literals:**
  - Timing: `run_time=1.5` → `run_time=params.ANIMATION_TIME`
  - Sizes: `font_size=36` → `font_size=params.FONT_SIZE`
  - Dimensions: `radius=2.0` → `radius=params.RADIUS`
  - Positions: `shift(UP * 2)` → `shift(UP * params.SHIFT_AMOUNT)`
  - Stroke widths: `stroke_width=3` → `stroke_width=params.STROKE_WIDTH`
  - Opacities: `opacity=0.5` → `opacity=params.OPACITY`

- **String literals (colors):**
  - `color=BLUE` → `color=globals()[params.COLOR]` (store "BLUE" in params)

- **Lists of values:**
  - `radii = [1.5, 0.8, 0.4]` → `radii = params.RADII_LIST`

### ❌ DON'T Extract These

- **Mathematical constants:**
  - `PI`, `TAU`, `E` (Manim/NumPy constants)
  - `2*PI` (mathematical expressions using constants)

- **Manim constants:**
  - `UP`, `DOWN`, `LEFT`, `RIGHT`, `ORIGIN`
  - Exception: Multipliers like `UP * 2.5` → extract the `2.5`

- **Fixed mathematical relationships:**
  - `radius * np.cos(angle)` (formula, not a magic number)
  - `x_range=[0, 2*PI]` (the 2 is mathematical, but extract PI multiplier if configurable)

- **Iteration bounds from data:**
  - `range(len(points))` (determined by data, not a parameter)

- **Indices:**
  - `array[0]`, `waves[i]` (data access, not configuration)

---

## Organization in params.py

### Group by Scene

```python
# ============================================================================
# SCENE 1: INTRODUCTION
# ============================================================================

# ... Scene 1 parameters

# ============================================================================
# SCENE 2: MAIN CONTENT
# ============================================================================

# ... Scene 2 parameters
```

### Group by Type Within Scenes

```python
# ============================================================================
# SCENE 1
# ============================================================================

# Timing parameters
SCENE1_INTRO_TIME = 1.5
SCENE1_MAIN_TIME = 3.0

# Visual parameters
SCENE1_CIRCLE_RADIUS = 2.0
SCENE1_CIRCLE_COLOR = "BLUE"

# Position parameters
SCENE1_CIRCLE_X = 2.0
SCENE1_CIRCLE_Y = -1.0
```

### Use Descriptive Names

**❌ Bad:**
```python
R = 2.0
T = 1.5
C = "BLUE"
```

**✅ Good:**
```python
CIRCLE_RADIUS = 2.0
ANIMATION_TIME = 1.5
CIRCLE_COLOR = "BLUE"
```

---

## Testing After Refactoring

### Step 1: Test Each Scene Individually

```bash
# Test that each scene still works
manim -pql animation.py Scene1
manim -pql animation.py Scene2
manim -pql animation.py Scene3
```

### Step 2: Test Combined Scene

```bash
manim -pql animation.py CombinedScene
```

### Step 3: Verify Customization Works

Modify a few values in `params.py` and re-render to ensure parameters are actually being used:

```python
# Change in params.py
CIRCLE_RADIUS = 3.5  # Was 2.0
ANIMATION_TIME = 5.0  # Was 1.5
```

Re-render and verify the circle is bigger and animation is slower.

---

## Common Patterns

### Pattern 1: Nested Parameters

**params.py:**
```python
AXES_X_RANGE = [0, 2, 0.5]  # [min, max, step] in terms of PI
AXES_Y_RANGE = [-2.5, 2.5, 1]
```

**animation.py:**
```python
axes = Axes(
    x_range=[
        params.AXES_X_RANGE[0] * PI,
        params.AXES_X_RANGE[1] * PI,
        params.AXES_X_RANGE[2] * PI
    ],
    y_range=params.AXES_Y_RANGE
)
```

### Pattern 2: Calculated Values

Some values can be calculated from others:

**params.py:**
```python
CIRCLE_RADIUS = 2.0
ARROW_LENGTH = CIRCLE_RADIUS * 1.5  # 50% longer than radius
```

### Pattern 3: Color Lists

**params.py:**
```python
WAVE_COLORS = ["BLUE", "GREEN", "RED"]
```

**animation.py:**
```python
wave_colors = [globals()[c] for c in params.WAVE_COLORS]
for i, color in enumerate(wave_colors):
    wave = axes.plot(func, color=color)
```

---

## Checklist for Complete Refactoring

- [ ] Created `params.py` file
- [ ] Added `import params` to `animation.py`
- [ ] Replaced all timing values (`run_time`, `wait`)
- [ ] Replaced all font sizes
- [ ] Replaced all radii, widths, heights
- [ ] Replaced all stroke widths
- [ ] Replaced all opacities
- [ ] Replaced all position offsets (shifts)
- [ ] Replaced all colors (converted to string names)
- [ ] Replaced all list/array constants
- [ ] Added clear comments in `params.py`
- [ ] Organized params by scene
- [ ] Tested individual scenes
- [ ] Tested combined scene
- [ ] Verified parameters can be changed and take effect

---

## Example: Before and After

### BEFORE (animation.py with magic numbers) ❌

```python
class MyScene(Scene):
    def construct(self):
        title = Text("Epicycles", font_size=36)
        self.play(Write(title), run_time=1.5)
        self.play(title.animate.scale(0.7).to_edge(UP), run_time=0.5)

        radii = [1.5, 0.8, 0.4]
        frequencies = [1, -2, 3]
        colors = [BLUE, GREEN, RED]

        for r, f, c in zip(radii, frequencies, colors):
            circle = Circle(radius=r, color=c, stroke_width=2)
            arrow = Arrow(ORIGIN, r*RIGHT, color=c, buff=0, stroke_width=3)
            self.play(Create(circle), GrowArrow(arrow), run_time=0.8)
```

### AFTER (with params.py) ✅

**params.py:**
```python
# Scene timing
TITLE_WRITE_TIME = 1.5
TITLE_SCALE_TIME = 0.5
EPICYCLE_CREATE_TIME = 0.8

# Visual properties
TITLE_FONT_SIZE = 36
TITLE_SCALE = 0.7

# Epicycle parameters
EPICYCLE_RADII = [1.5, 0.8, 0.4]
EPICYCLE_FREQUENCIES = [1, -2, 3]
EPICYCLE_COLORS = ["BLUE", "GREEN", "RED"]
EPICYCLE_CIRCLE_STROKE = 2
EPICYCLE_ARROW_STROKE = 3
```

**animation.py:**
```python
import params

class MyScene(Scene):
    def construct(self):
        title = Text("Epicycles", font_size=params.TITLE_FONT_SIZE)
        self.play(Write(title), run_time=params.TITLE_WRITE_TIME)
        self.play(
            title.animate.scale(params.TITLE_SCALE).to_edge(UP),
            run_time=params.TITLE_SCALE_TIME
        )

        # Convert color strings to constants
        colors = [globals()[c] for c in params.EPICYCLE_COLORS]

        for r, f, c in zip(params.EPICYCLE_RADII, params.EPICYCLE_FREQUENCIES, colors):
            circle = Circle(
                radius=r,
                color=c,
                stroke_width=params.EPICYCLE_CIRCLE_STROKE
            )
            arrow = Arrow(
                ORIGIN,
                r * RIGHT,
                color=c,
                buff=0,
                stroke_width=params.EPICYCLE_ARROW_STROKE
            )
            self.play(
                Create(circle),
                GrowArrow(arrow),
                run_time=params.EPICYCLE_CREATE_TIME
            )
```

---

## Integration with Skills

This workflow should be followed when:

1. **manim-coding skill** creates a new animation
2. **After initial implementation** but before finalizing
3. **As part of the standard workflow**, not an afterthought

### Updated Workflow

1. ✅ Research (math-research skill)
2. ✅ Implement animation (manim-coding skill)
3. ✅ **Extract parameters to params.py** ← ADD THIS STEP
4. ✅ **Replace magic numbers in animation.py** ← ADD THIS STEP
5. ✅ Test and verify
6. ✅ Document

---

## Benefits

✅ **Easy customization** - Change timing, colors, sizes without touching code
✅ **Clear organization** - All configuration in one place
✅ **Better collaboration** - Non-programmers can adjust parameters
✅ **Experimentation** - Quickly try different values
✅ **Maintainability** - Logic separated from configuration
✅ **Documentation** - Parameters self-document what's configurable

---

## Summary

**The Golden Rule:**

> **If it's a number in your animation code, it should probably be a parameter.**

Every `run_time=`, `font_size=`, `radius=`, `stroke_width=`, `shift()` value should come from `params.py`, not be hardcoded in `animation.py`.

This makes animations **professional**, **customizable**, and **maintainable**.
