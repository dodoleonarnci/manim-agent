# Setup Guide for Manim

This guide will help you install Manim to render the Lorenz attractor animation.

## Installation Options

### Option 1: Install via pip (Recommended)

```bash
pip install manim
```

Or with conda:
```bash
conda install -c conda-forge manim
```

### Option 2: Install with all dependencies

Manim requires some system dependencies. On macOS:

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install py3cairo ffmpeg

# Install Manim
pip install manim
```

On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
pip install manim
```

## Verify Installation

Check that Manim is installed correctly:

```bash
manim --version
```

Or:
```bash
python3 -m manim --version
```

## Rendering the Animation

Once Manim is installed, navigate to the project directory:

```bash
cd manim-projects/lorenz-attractor
```

### Quick Preview (Low Quality)
Fastest render for testing:
```bash
manim -pql lorenz_attractor_animation.py LorenzAttractor
```

### High Quality
Production quality (1080p):
```bash
manim -pqh lorenz_attractor_animation.py LorenzAttractor
```

### 4K Quality
Highest quality (2160p):
```bash
manim -pqk lorenz_attractor_animation.py LorenzAttractor
```

### Save without Opening
Remove `-p` flag to render without auto-playing:
```bash
manim -ql lorenz_attractor_animation.py LorenzAttractor
```

## Output Location

Rendered videos are saved to:
```
media/videos/lorenz_attractor_animation/[quality]/LorenzAttractor.mp4
```

Where `[quality]` is one of:
- `480p15` (low quality)
- `1080p60` (high quality)
- `2160p60` (4K quality)

## Troubleshooting

### Issue: "command not found: manim"

Try using the Python module directly:
```bash
python3 -m manim -pql lorenz_attractor_animation.py LorenzAttractor
```

### Issue: "No module named manim"

Manim is not installed. Run:
```bash
pip install manim
```

### Issue: Cairo or FFmpeg errors

You need to install system dependencies. See Option 2 above.

### Issue: Animation is too slow

- Use `-ql` (low quality) for faster preview
- Reduce the number of points in the trajectory (edit `t = np.linspace(0, 40, 4000)`)
- Use a faster computer or render overnight for high quality

## Performance Tips

- **Preview first**: Always test with `-ql` before rendering high quality
- **Partial rendering**: Comment out sections of `construct()` to test specific parts
- **Reduce complexity**: Lower `num_segments` or trajectory points for faster renders

## Alternative: Use the Tracing Scene

The `LorenzAttractorTracing` scene is simpler and renders faster:

```bash
manim -pqh lorenz_attractor_animation.py LorenzAttractorTracing
```

## Getting Help

- Manim Documentation: https://docs.manim.community/
- Manim Discord: https://manim.community/discord/
- GitHub Issues: https://github.com/ManimCommunity/manim/issues

## Using main.py Helper

You can also use the project's main.py interface:

```bash
cd ../..  # Go to manim-agent directory
python main.py --project lorenz-attractor
```

Then use commands:
- `/render` - Render high quality
- `/preview` - Render low quality preview
- `/files` - See generated files
