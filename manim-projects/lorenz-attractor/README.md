# Lorenz Attractor

3D visualization of the chaotic Lorenz attractor with rotating camera views.

Created: 2025-11-26

## Project Files

- Animation code: `lorenz_attractor_animation.py`
- Research reports: `research-reports/lorenz_attractor_overview.md`
- Session history: `session.json`

## Scenes

This project contains two animation scenes:

### 1. LorenzAttractor (Main Scene)
A complete visualization of the Lorenz attractor with:
- 3D axes and labels
- Color-gradient trajectory (blue → purple → red → orange → yellow)
- Rotating camera with multiple viewing angles
- ~30 second duration

### 2. LorenzAttractorTracing
An alternative version showing:
- Real-time tracing of the trajectory
- Moving particle following the path
- Slower camera rotation during tracing
- ~15 second duration

## Rendering

### Preview (low quality, fast)
```bash
manim -pql lorenz_attractor_animation.py LorenzAttractor
```

### High quality
```bash
manim -pqh lorenz_attractor_animation.py LorenzAttractor
```

### 4K quality
```bash
manim -pqk lorenz_attractor_animation.py LorenzAttractor
```

### Render the tracing scene
```bash
manim -pqh lorenz_attractor_animation.py LorenzAttractorTracing
```

## Parameters

The animation uses the classic Lorenz parameters:
- σ (sigma) = 10.0
- ρ (rho) = 28.0
- β (beta) = 8/3

Initial condition: (1.0, 1.0, 1.0)

## Mathematical Background

See `research-reports/lorenz_attractor_overview.md` for detailed mathematical explanation including:
- Differential equations
- Physical interpretation
- Chaotic behavior and sensitivity
- Numerical integration methods
- Historical significance

## Output

Rendered videos will be saved to:
```
media/videos/lorenz_attractor_animation/[quality]/[SceneName].mp4
```
