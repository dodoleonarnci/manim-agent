# Golden Ratio Spiral Animation

A mathematical animation exploring the golden ratio (φ ≈ 1.618) and its connection to the Fibonacci sequence.

## Project Structure

```
golden-ratio-spiral/
├── animation.py    # Main Manim animation code
├── params.py       # Visual parameters (colors, timing, positions)
└── README.md       # This file
```

## Scenes

1. **IntroScene** - Introduction to φ with line segment division
2. **PropertiesScene** - Unique properties (φ² = φ + 1, 1/φ = φ - 1)
3. **FibonacciConnection** - Fibonacci sequence converging to φ
4. **GoldenRectangles** - (Coming soon) Building golden rectangles
5. **SpiralBuilding** - (Coming soon) Drawing the golden spiral

## Quick Customization Guide

All visual parameters are in `params.py`. Edit that file to customize the animation without touching any code!

### Common Changes

**Change color scheme:**
```python
COLORS = {
    "gold": "#FF6B6B",  # Change from gold to coral red
    "segment_a": "#4ECDC4",  # Teal instead of blue
    # ... etc
}
```

**Adjust pacing:**
```python
TIMING = {
    "intro_title_fadein": 2.0,  # Increase for slower, decrease for faster
    "phi_symbol_write": 3.0,
    # ... etc
}
```

**Resize elements:**
```python
SIZES = {
    "title_font": 72,  # Larger title
    "global_scale": 1.2,  # Scale everything by 1.2x
    # ... etc
}
```

**Reposition elements:**
```python
POSITIONS = {
    "equation_y": 4.0,  # Move equations higher
    # Positive Y = up, Negative Y = down
    # Positive X = right, Negative X = left
    # Frame bounds: X ∈ [-7, 7], Y ∈ [-4, 4]
}
```

**Change text:**
```python
TEXT = {
    "intro_title": "El Número Dorado",  # Spanish translation
    "phi_symbol": "φ",
    # ... etc
}
```

## Rendering

**Quick preview (low quality, fast):**
```bash
cd manim-projects/golden-ratio-spiral
manim -pql animation.py IntroScene
```

**High quality:**
```bash
manim -pqh animation.py IntroScene
```

**Render all scenes:**
```bash
manim -pqh animation.py
```

**Quality options:**
- `-ql` → 480p, 15fps (low quality)
- `-qm` → 720p, 30fps (medium quality)
- `-qh` → 1080p, 60fps (high quality)
- `-qk` → 4K, 60fps (4K quality)

**Other flags:**
- `-p` → Preview after rendering
- `--save_last_frame` → Save final frame as image
- `-s` → Skip animation, show only last frame

## Parameters Reference

See `params.py` for complete list of customizable parameters organized by category:
- **COLORS** - 14 color definitions
- **TEXT** - 20+ text strings
- **DIMENSIONS** - Line widths, sizes
- **POSITIONS** - X/Y coordinates
- **TIMING** - Animation durations
- **SIZES** - Font sizes, scales
- **OPACITY** - Fill and stroke opacities
- **MATH_CONSTANTS** - φ value
- **FIBONACCI** - Sequence and thresholds

## Mathematical Content

For detailed mathematical background, see:
- `/research-reports/golden-ratio-spiral.md` (comprehensive research report)
- Wikipedia: [Golden Ratio](https://en.wikipedia.org/wiki/Golden_ratio)
- Wikipedia: [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number)
