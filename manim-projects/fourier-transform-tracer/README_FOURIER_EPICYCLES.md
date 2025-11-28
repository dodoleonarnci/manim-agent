# Fourier Transform Epicycles - SVG Tracing Animation

A beautiful Manim animation demonstrating how Fourier Transform can decompose any closed curve into rotating circles (epicycles). This project creates a mesmerizing visualization showing how complex shapes emerge from simple circular motions.

## Features

✨ **Four Educational Scenes:**
1. **Fourier Transform Basics** (~8s) - Explains frequency decomposition
2. **Rotation to Waves** (~5s) - Shows how rotating vectors create sinusoidal waves
3. **Epicycle Mechanics** (~10s) - Demonstrates rotating circles connected head-to-tail
4. **SVG Tracing** (~60s) - Full epicycle animation drawing custom shapes

🎨 **Customizable:**
- Upload your own SVG files
- Adjust number of epicycles
- Built-in shapes: heart, star, square, circle
- **NEW:** Sample points visualization showing curve discretization

🔬 **Mathematically Rigorous:**
- Proper Discrete Fourier Transform (DFT) implementation
- Accurate complex number representation
- Frequency sorting for optimal visualization
- Visual demonstration of sampling process

## Installation

### Prerequisites

```bash
# Install Manim Community Edition
pip install manim

# Or via conda
conda install -c conda-forge manim
```

### Required Python Packages

- `manim` (Community Edition v0.19.0+)
- `numpy`
- `cmath` (built-in)

## Quick Start

### Option 1: Run Individual Scenes

```bash
# Scene 1: Fourier basics
manim -pql animation.py Scene1_FourierBasics

# Scene 1.5: Rotation to waves connection
manim -pql animation.py Scene1_5_RotationToWaves

# Scene 2: Epicycle mechanics
manim -pql animation.py Scene2_EpicycleMechanics

# Scene 3: SVG tracing (default heart shape)
manim -pql animation.py Scene3_SVGTracing
```

### Option 2: Run Full Combined Animation

```bash
# Low quality (for preview)
manim -pql animation.py FourierEpicyclesFull

# Medium quality (720p)
manim -pqm animation.py FourierEpicyclesFull

# High quality (1080p) - recommended for final output
manim -pqh animation.py FourierEpicyclesFull

# 4K quality
manim -pqk animation.py FourierEpicyclesFull
```

### Option 3: Pre-built Shape Variations

```bash
# Heart shape (default)
manim -pqh animation.py FourierEpicyclesHeart

# Custom SVG (see customization section below)
manim -pqh animation.py FourierEpicyclesCustom
```

## Customization

### Using Your Own SVG File

1. **Create or find an SVG file** with a simple closed path
   - Works best with single-path SVGs
   - Avoid extremely complex shapes (use simplified versions)

2. **Place your SVG** in the project directory

3. **Method A: Modify FourierEpicyclesCustom class**

   Edit `fourier_epicycles.py`:

   ```python
   class FourierEpicyclesCustom(FourierEpicyclesFull):
       def __init__(self, **kwargs):
           # Change this to your SVG file path
           custom_svg_path = "my_shape.svg"
           super().__init__(svg_path=custom_svg_path, num_epicycles=80, **kwargs)
   ```

   Then run:
   ```bash
   manim -pqh fourier_epicycles.py FourierEpicyclesCustom
   ```

4. **Method B: Create a new scene class**

   Add to `fourier_epicycles.py`:

   ```python
   class MyCustomShape(FourierEpicyclesFull):
       def __init__(self, **kwargs):
           super().__init__(
               svg_path="path/to/your.svg",
               num_epicycles=100,  # More = more accurate but slower
               **kwargs
           )
   ```

### Parameters

- **`svg_path`** (str): Path to SVG file, or `None` for default heart shape
- **`num_epicycles`** (int): Number of rotating circles to use
  - Default: 50-60
  - Recommended range: 30-150
  - More epicycles = more accurate but slower rendering
- **`num_samples`** (int): Number of points sampled from curve
  - Default: 200
  - Range: 100-500
  - Should be ≥ 2 × num_epicycles
  - **NEW:** These points are visualized as yellow dots before epicycles appear!

### Sample Points Visualization (New Feature!)

Scene 3 now shows the sample points extracted from the curve:

```python
# In params.py
SCENE3_SHOW_SAMPLE_POINTS = True  # Enable/disable visualization
SCENE3_SAMPLE_POINT_RADIUS = 0.04  # Size of dots
SCENE3_SAMPLE_POINT_COLOR = "YELLOW"  # Color of dots
```

This helps demonstrate:
- How the continuous curve is discretized
- The relationship between sampling rate and accuracy
- What data the DFT algorithm receives

See `SAMPLE_POINTS_QUICKSTART.md` for detailed usage!

### Built-in Shape Functions

You can also use programmatic shapes without SVG files:

```python
# In Scene3_SVGTracing, replace SVG loading with:
complex_points = create_simple_shape_points("heart", num_samples=200, radius=2)

# Available shapes:
# - "circle"
# - "square"
# - "heart"
# - "star"
```

## Output

The animation will be saved to:
```
media/videos/fourier_epicycles/[quality]/[SceneName].mp4
```

For example:
- Low quality (480p): `media/videos/fourier_epicycles/480p15/FourierEpicyclesFull.mp4`
- High quality (1080p): `media/videos/fourier_epicycles/1080p60/FourierEpicyclesFull.mp4`

## How It Works

### Mathematical Foundation

1. **Complex Number Representation**: Any 2D curve is represented as `z(t) = x(t) + i·y(t)`

2. **Fourier Series Decomposition**: The curve is decomposed into rotating circles:
   ```
   z(t) = Σ C_k · e^(i·k·t)
   ```

3. **Discrete Fourier Transform (DFT)**: Computes the coefficients:
   ```
   C_k = (1/N) · Σ z_n · e^(-2πikn/N)
   ```

4. **Epicycle Interpretation**:
   - Magnitude `|C_k|` = radius of k-th circle
   - Phase `arg(C_k)` = initial angle
   - Frequency `k` = rotations per period

### Algorithm Steps

1. **Load SVG** → Extract path points
2. **Sample Points** → Convert to complex numbers
3. **Compute DFT** → Get Fourier coefficients
4. **Sort by Magnitude** → Largest frequencies first
5. **Animate Epicycles** → Rotate circles at their frequencies
6. **Trace Path** → Draw curve from final circle's tip

## Troubleshooting

### LaTeX Errors

If you encounter LaTeX errors, the code already uses `Text()` instead of `MathTex()` for compatibility. If issues persist:

```bash
# Install LaTeX (optional, for advanced math rendering)
# macOS:
brew install --cask mactex-no-gui

# Ubuntu/Debian:
sudo apt-get install texlive texlive-latex-extra

# Windows: Install MiKTeX from miktex.org
```

### SVG Not Loading

- Ensure SVG has a valid closed path
- Try simplifying the SVG (remove multiple paths, gradients, etc.)
- Use online tools like [svgomg.net](https://svgomg.net/) to optimize
- Verify the SVG file path is correct

### Slow Rendering

- Reduce `num_epicycles` (try 30-50 instead of 100+)
- Use lower quality for testing: `-pql`
- Reduce `num_samples` (try 150 instead of 200)
- Scene 3 takes ~25-30 seconds of animation, be patient!

### Epicycles Don't Trace Shape Accurately

- Increase `num_epicycles` (60, 80, or 100+)
- Ensure SVG path is closed
- Check that curve is continuous (no gaps)
- Try increasing `num_samples` for smoother sampling

## Advanced Usage

### Extracting Just the Epicycle System

```python
# Create a custom scene with only epicycles (no full animation)
class JustEpicycles(Scene):
    def construct(self):
        # Create your shape
        points = create_simple_shape_points("star", num_samples=200)

        # Compute DFT
        coeffs = compute_dft_fast(points)

        # Create epicycle visualization
        # ... (see Scene3 code for details)
```

### Adjusting Animation Timing

Edit the `scene3_animation()` method:

```python
# Line ~360: Change rotation duration
self.wait(25)  # Change this number (currently ~3 rotations in 25s)
```

### Custom Color Schemes

Edit the `freq_to_color()` method in `create_epicycle_system()`:

```python
# Change from blue-to-red gradient to custom colors
color = interpolate_color(GREEN, PURPLE, freq_ratio)
```

## Examples

### Heart Shape (Default)
```bash
manim -pqh fourier_epicycles.py FourierEpicyclesHeart
```
Creates a beautiful heart tracing with 60 epicycles.

### Star from Custom SVG
```bash
# Using the included custom_shape.svg
manim -pqh fourier_epicycles.py FourierEpicyclesCustom
```
Traces the 5-pointed star with 80 epicycles.

### High-Detail Custom Shape
```python
class DetailedShape(FourierEpicyclesFull):
    def __init__(self, **kwargs):
        super().__init__(
            svg_path="detailed_logo.svg",
            num_epicycles=120,  # High detail
            **kwargs
        )
```

## Project Structure

```
.
├── fourier_epicycles.py      # Main animation code
├── custom_shape.svg           # Example SVG file (star)
├── README_FOURIER_EPICYCLES.md  # This file
└── research-reports/
    └── research-fourier-epicycles-svg-2025-11-27.md  # Research documentation
```

## Code Architecture

### Main Components

1. **Utility Functions**
   - `compute_dft()` / `compute_dft_fast()`: DFT computation
   - `extract_svg_points()`: SVG parsing
   - `create_simple_shape_points()`: Programmatic shapes

2. **Scene Classes**
   - `Scene1_FourierBasics`: Educational intro
   - `Scene2_EpicycleMechanics`: Epicycle demo
   - `Scene3_SVGTracing`: Full animation
   - `FourierEpicyclesFull`: Combined scene

3. **Helper Classes**
   - `FourierEpicyclesHeart`: Convenience wrapper
   - `FourierEpicyclesCustom`: Custom SVG template

## Performance Notes

- **Scene 1**: ~8 seconds animation, renders in ~5 seconds
- **Scene 2**: ~10 seconds animation, renders in ~8 seconds
- **Scene 3**: ~30 seconds animation, renders in ~20-40 seconds (depends on epicycle count)
- **Full Combined**: ~50 seconds animation, renders in ~35-60 seconds

High quality (1080p, 60fps) rendering takes longer. Use low quality (`-pql`) for testing.

## Tips for Best Results

1. **Start Simple**: Test with built-in shapes before using custom SVGs
2. **Optimize SVGs**: Simplify paths, remove unnecessary elements
3. **Tune Parameters**: Start with 50 epicycles, increase if needed
4. **Quality Settings**: Use `-pql` for testing, `-pqh` for final render
5. **Patience**: Scene 3 takes time to render due to complex animations

## Mathematical Deep Dive

For detailed mathematical explanations, see the research report:
`research-reports/research-fourier-epicycles-svg-2025-11-27.md`

Topics covered:
- Fourier Transform theory
- DFT computation algorithm
- Complex number representation of curves
- Epicycle mathematics
- Implementation details

## Contributing

To modify or extend this project:

1. **Add new shapes**: Edit `create_simple_shape_points()`
2. **Change animation style**: Modify scene classes
3. **Adjust colors**: Edit `freq_to_color()` and color constants
4. **Add effects**: Use Manim animations in scene methods

## Credits

Created using:
- [Manim Community Edition](https://www.manim.community/)
- Inspired by 3Blue1Brown's visualizations
- Mathematical concepts from various Fourier analysis sources

## References

- Fourier Transform: https://en.wikipedia.org/wiki/Fourier_transform
- Discrete Fourier Transform: https://en.wikipedia.org/wiki/Discrete_Fourier_transform
- Epicycles and Fourier: https://www.dynamicmath.xyz/fourier-epicycles/
- Complex Fourier Series: https://observablehq.com/@maddhattpatt/drawing-with-epicycles

## License

This code is provided for educational purposes. Feel free to modify and extend!

---

**Enjoy creating beautiful mathematical animations!**

For questions or issues, refer to:
- Manim Documentation: https://docs.manim.community/
- Manim Discord: https://discord.gg/mMRrZQW
