# Version Comparison Summary

This document provides a quick reference for the differences between Lorenz Attractor 1.0 and 2.0.

## Side-by-Side Comparison

| Feature | Version 1.0 | Version 2.0 |
|---------|-------------|-------------|
| **Created With** | Detailed manual prompt | `/animate` command |
| **Research Method** | Manual conversation | Automated (math-research skill) |
| **Code Generation** | Direct prompting | Structured (manim-coding skill) |
| **Development Time** | ~10-15 minutes | ~5-8 minutes |
| **Video Duration** | 20 seconds | 19.3 seconds |
| **File Size** | 804 KB | 2.4 MB (higher quality) |
| **Resolution** | Standard | 1080p60 |
| **Gradient Colors** | 5 colors | 3 colors (cleaner) |
| **LaTeX Required** | Possibly | No (uses Text) |
| **Documentation** | Basic README | Research report + detailed README |
| **Scenes** | 2 (main + tracing) | 1 (focused) |

## Demo Videos

### Version 1.0
- **Location:** `../lorenz-attractor-1.0/media/videos/LorenzAttractorTracing.mp4`
- **Approach:** Manual prompt-driven development
- **Features:** Particle tracing, multi-color gradient

### Version 2.0
- **Location:** `media/videos/animation/1080p60/LorenzAttractor.mp4`
- **Approach:** Automated agents & skills workflow
- **Features:** Clean gradient, optimized intro, better documentation

## Key Innovation: Agents & Skills

Version 2.0 uses a **multi-agent architecture**:

```
/animate command
    ↓
Manim Animator Agent
    ↓
┌─────────────────┬─────────────────┐
│ math-research   │ manim-coding    │
│ skill           │ skill           │
│                 │                 │
│ • Fetches from  │ • Syntax guide  │
│   Wikipedia     │ • Best practices│
│ • Creates       │ • Pattern       │
│   research      │   library       │
│   report        │                 │
└─────────────────┴─────────────────┘
    ↓
Final Animation
```

## Benefits of 2.0 Approach

1. **Faster Development:** Automated research saves time
2. **Better Quality:** Consistent best practices from skills
3. **Reproducible:** Same workflow for all math animations
4. **Maintainable:** Separated concerns (research vs code)
5. **Scalable:** Easy to add new skills for different domains

## Try It Yourself

**Version 1.0 Method:**
```bash
# Requires detailed manual prompt explaining:
# - Mathematical background
# - Equations and parameters
# - Desired visual style
# - Animation sequence
```

**Version 2.0 Method:**
```bash
/animate
# Then simply: "Animate a 3D tracing of the lorenz attractor..."
# Agent handles research, planning, and implementation automatically
```

---

See the main README.md for comprehensive comparison and full documentation.
