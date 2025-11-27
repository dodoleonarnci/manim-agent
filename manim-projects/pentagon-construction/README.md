# Regular Pentagon Construction Animation

⭐ **Featured showcase project** - This is the main example demonstrating the capabilities of the Manim Animation Agent.

This project implements a step-by-step compass and straightedge construction of a regular pentagon using Manim.

## 🎬 Watch the Animation

**Full Combined Video (All 7 Scenes):**
- Location: `media/videos/animation/1080p60/CombinedScenes.mp4`
- Quality: 1080p60 (Full HD at 60 fps)
- Size: 4.2 MB
- Duration: ~2 minutes

**Preview Images:**
- `pentagon-preview.png` - Frame from midpoint construction
- `pentagon-showcase.png` - Frame from completed pentagon

## Project Structure

```
pentagon-construction/
├── animation.py                  # Main animation code with all 7 scenes
├── params.py                     # All visual and timing parameters (externalized)
├── README.md                     # This file
├── pentagon-preview.png          # Preview frame 1
├── pentagon-showcase.png         # Preview frame 2
└── media/
    └── videos/
        └── animation/
            ├── 480p15/           # Low quality renders (individual scenes)
            ├── 720p30/           # Medium quality renders
            └── 1080p60/          # High quality renders
                └── CombinedScenes.mp4  # ⭐ Full animation
```

## Key Features

- **Fully Externalized Parameters**: All colors, dimensions, timing, text, and styling are defined in `params.py`
- **Modular Scene Design**: Each construction step is a separate scene
- **Educational Focus**: Clear step-by-step visualization of the classical geometric construction
- **Golden Ratio**: Demonstrates how the pentagon construction embeds the golden ratio φ

## Scenes

1. **IntroScene**: Title and initial circle setup
2. **PerpendicularDiameters**: Draw horizontal and vertical diameters
3. **FindMidpoint**: Find midpoint M of radius OY
4. **GoldenArc**: The key arc from M through A to find point R
5. **MarkVertices**: Use AR as compass radius to mark all 5 vertices
6. **CompletePentagon**: Connect vertices to form the pentagon
7. **Verification**: Show angles and side lengths are equal

## Rendering Individual Scenes

To render a specific scene at low quality (fast preview):

```bash
manim -ql animation.py IntroScene
manim -ql animation.py PerpendicularDiameters
manim -ql animation.py FindMidpoint
manim -ql animation.py GoldenArc
manim -ql animation.py MarkVertices
manim -ql animation.py CompletePentagon
manim -ql animation.py Verification
```

## Rendering Full Animation

### Option 1: Using the Combined Scene (Recommended)

The animation includes a `PentagonConstruction` scene that combines all 7 scenes into one continuous animation:

```bash
# Render all scenes in one combined video
manim -qh animation.py PentagonConstruction

# The output will be automatically combined into CombinedScenes.mp4
```

**Note:** The combined video is already available at `media/videos/animation/1080p60/CombinedScenes.mp4`

### Option 2: Render Individual Scenes

To render all individual scenes separately:

```bash
# Render each scene individually at high quality
for scene in IntroScene PerpendicularDiameters FindMidpoint GoldenArc MarkVertices CompletePentagon Verification; do
    manim -qh animation.py $scene
done

# Then combine using ffmpeg (done automatically by main.py)
```

## Quality Options

- `-ql`: Low quality (480p15, fast preview)
- `-qm`: Medium quality (720p30)
- `-qh`: High quality (1080p60)
- `-qk`: 4K quality (2160p60)

## Customization

All visual parameters can be easily customized by editing `params.py`:

### Colors
Edit the `COLORS` dictionary to change:
- Compass and straightedge colors
- Construction line colors
- Pentagon colors
- Point and label colors

### Timing
Edit the `TIMING` dictionary to adjust:
- Scene durations
- Animation speeds
- Pause lengths between steps

### Dimensions
Edit the `DIMENSIONS` dictionary to change:
- Circle radius
- Line widths
- Point sizes

### Text
Edit the `TEXT` dictionary to modify:
- Scene titles
- Point labels
- Annotations

## Mathematical Foundation

The construction is based on the classical method that leverages the golden ratio:

1. Start with a circle of radius r with center O
2. Create perpendicular diameters
3. Find midpoint M of radius OY
4. Draw arc from M with radius MA (equals r√5/2)
5. This arc intersects the horizontal diameter at R
6. The distance AR equals the pentagon's side length
7. Use AR to mark all 5 vertices around the circle

**Key Insight**: The construction embeds the golden ratio φ = (1+√5)/2 through the arc radius calculation.

## Dependencies

- Python 3.7+
- Manim Community Edition (v0.19.0 or later)
- NumPy

Install Manim:
```bash
pip install manim
```

## Notes

- The code uses `Text` instead of `MathTex` for better compatibility (no LaTeX required)
- Mathematical formulas are displayed as Unicode text
- All geometric calculations use exact trigonometry for accuracy
- Construction arcs fade after use to maintain visual clarity

## Research

This animation is based on the research report at:
`research-reports/pentagon-construction.md`

The report contains:
- Detailed mathematical foundation
- Multiple construction methods (Classical, Euclid's, Richmond's)
- Animation planning and scene breakdowns
- Visual design recommendations
- Historical context and references

## Author

Created by: Manim Coding Skill Agent
Date: 2025-11-27
