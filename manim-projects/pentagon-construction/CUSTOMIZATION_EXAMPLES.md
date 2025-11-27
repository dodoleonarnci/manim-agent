# Customization Examples

This document shows examples of how to customize the pentagon construction animation by editing `params.py`.

## Example 1: Change Color Scheme to Blue Theme

Edit the `COLORS` dictionary in `params.py`:

```python
COLORS = {
    # Compass and straightedge tools
    "compass_arm": GRAY,
    "compass_arc": BLUE_C,  # Changed from GREEN
    "straightedge": WHITE,

    # Construction elements
    "circle": BLUE_A,  # Changed from WHITE
    "horizontal_diameter": BLUE_C,
    "vertical_diameter": TEAL_C,  # Changed from RED
    "construction_lines": BLUE_E,  # Changed from GRAY
    "construction_arcs": BLUE_C,  # Changed from GREEN

    # Pentagon and final elements
    "pentagon_outline": TEAL_A,  # Changed from GOLD
    "pentagon_fill": TEAL_A,  # Changed from GOLD

    # ... rest unchanged
}
```

## Example 2: Make Animation Faster

Edit the `TIMING` dictionary in `params.py`:

```python
TIMING = {
    # Scene durations (total time for each scene)
    "intro_scene": 2.0,  # Changed from 4.0
    "perpendicular_scene": 3.0,  # Changed from 6.0
    "midpoint_scene": 2.5,  # Changed from 5.0
    "golden_arc_scene": 4.0,  # Changed from 7.0
    "mark_vertices_scene": 5.0,  # Changed from 8.0
    "complete_pentagon_scene": 3.0,  # Changed from 5.0
    "verification_scene": 4.0,  # Changed from 6.0

    # Individual animation durations
    "fade_in": 0.4,  # Changed from 0.8
    "fade_out": 0.3,  # Changed from 0.6
    "draw_line": 0.8,  # Changed from 1.5
    "draw_circle": 1.0,  # Changed from 2.0
    "draw_arc": 1.0,  # Changed from 2.0
    # ... etc
}
```

## Example 3: Larger Pentagon

Edit the `DIMENSIONS` dictionary in `params.py`:

```python
DIMENSIONS = {
    # Circle
    "circle_radius": 4.0,  # Changed from 3.0
    "circle_stroke_width": 4,  # Changed from 3

    # Lines
    "diameter_stroke_width": 4,  # Changed from 3
    "construction_line_width": 3,  # Changed from 2
    "pentagon_stroke_width": 6,  # Changed from 5
    "arc_stroke_width": 4,  # Changed from 3

    # Points
    "point_radius": 0.10,  # Changed from 0.08
    "center_point_radius": 0.12,  # Changed from 0.1
    "vertex_point_radius": 0.12,  # Changed from 0.1

    # ... rest unchanged
}
```

## Example 4: Different Text and Labels

Edit the `TEXT` dictionary in `params.py`:

```python
TEXT = {
    # Scene titles
    "intro_title": "Constructing a Regular Pentagon",  # Changed
    "intro_subtitle": "Classical Geometry Method",  # Changed

    # Step descriptions
    "step_perpendicular": "Draw perpendicular diameters",  # Simplified
    "step_midpoint": "Find the midpoint",  # Simplified
    "step_golden_arc": "The golden ratio arc",  # Simplified
    "step_mark_vertices": "Mark the vertices",  # Simplified
    "step_complete": "Connect the vertices",  # Simplified

    # ... rest unchanged
}
```

## Example 5: Larger Fonts

Edit the `SIZES` dictionary in `params.py`:

```python
SIZES = {
    # Font sizes
    "title_font_size": 64,  # Changed from 56
    "subtitle_font_size": 48,  # Changed from 40
    "step_font_size": 40,  # Changed from 36
    "label_font_size": 36,  # Changed from 32
    "annotation_font_size": 32,  # Changed from 28

    # ... rest unchanged
}
```

## Example 6: More Transparent Construction Lines

Edit the `OPACITY` dictionary in `params.py`:

```python
OPACITY = {
    # Construction elements (can be faded)
    "construction_line_active": 0.8,  # Changed from 1.0
    "construction_line_faded": 0.15,  # Changed from 0.3
    "construction_arc_active": 0.8,  # Changed from 1.0
    "construction_arc_faded": 0.15,  # Changed from 0.25

    # Main elements (usually visible)
    "circle_active": 1.0,
    "circle_faded": 0.3,  # Changed from 0.5

    # ... rest unchanged
}
```

## Example 7: Different Label Positions

Edit the `POSITIONS` dictionary in `params.py`:

```python
POSITIONS = {
    # ... other positions unchanged ...

    # Label positioning offsets (relative to points)
    "label_offset_O": DOWN * 0.5 + LEFT * 0.5,  # Changed - further away
    "label_offset_A": UP * 0.6,  # Changed - higher
    "label_offset_B": RIGHT * 0.5 + UP * 0.4,  # Changed
    # ... etc
}
```

## Example 8: Change Background Color

The background color is set in `params.py` but needs to be applied in the Manim config. Add this to your command:

```bash
manim -ql --background_color "#f5f5dc" animation.py IntroScene
```

Or for a light blue background:

```bash
manim -ql --background_color "#e6f2ff" animation.py IntroScene
```

## Tips for Customization

1. **Test incrementally**: After making changes, test with one scene first:
   ```bash
   manim -ql animation.py IntroScene
   ```

2. **Save backups**: Before major changes, save a copy of `params.py`:
   ```bash
   cp params.py params_backup.py
   ```

3. **Use Manim colors**: Manim provides many predefined colors:
   - `BLUE_A`, `BLUE_B`, `BLUE_C`, `BLUE_D`, `BLUE_E`
   - `RED_A` through `RED_E`
   - `GREEN_A` through `GREEN_E`
   - `YELLOW_A` through `YELLOW_E`
   - `GOLD`, `TEAL`, `PURPLE`, `MAROON`, etc.

4. **Experiment with timing**: Different audiences may prefer different pacing:
   - **Fast**: Halve all timing values for quick overview
   - **Slow**: Double timing for educational/explanatory videos
   - **Variable**: Keep intro/conclusion fast, slow down key steps

5. **Color harmony**: Choose colors that work well together:
   - **Monochromatic**: Different shades of one color
   - **Complementary**: Opposite colors (blue/orange, red/green)
   - **Analogous**: Adjacent colors (blue, blue-green, green)

6. **Accessibility**: Consider color-blind friendly palettes:
   - Use high contrast
   - Avoid red-green combinations
   - Use patterns/line styles in addition to colors
