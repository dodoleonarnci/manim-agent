# Directory Guidelines for Manim Projects

## Overview

All Manim animation projects should be organized in dedicated subdirectories under `/manim-projects/`.

## Directory Structure

```
/manim-projects/
├── project-name-1/
│   ├── animation.py
│   ├── research-reports/
│   │   └── research-topic-YYYY-MM-DD.md
│   ├── assets/
│   │   └── custom-shapes.svg
│   └── media/
│       └── videos/
│           └── ...
├── project-name-2/
│   ├── ...
└── project-name-3/
    └── ...
```

## Workflow

### 1. Start New Project

```bash
# Create project directory
mkdir -p /manim-projects/your-project-name

# Navigate to it
cd /manim-projects/your-project-name
```

### 2. Research Phase (math-research skill)

```bash
# Create research directory
mkdir -p research-reports

# Research reports saved to:
# /manim-projects/your-project-name/research-reports/research-topic-YYYY-MM-DD.md
```

### 3. Implementation Phase (manim-coding skill)

```bash
# Create animation file
# /manim-projects/your-project-name/animation.py

# Create assets directory if needed
mkdir -p assets

# Run animations from project directory
manim -pql animation.py SceneName
```

## File Paths

All file operations should use absolute paths:

- ✅ **Correct**: `/manim-projects/fourier-epicycles/animation.py`
- ❌ **Wrong**: `~/Desktop/animation.py`
- ❌ **Wrong**: `animation.py` (relative path without context)

## Benefits

1. **Organization**: Each project is self-contained
2. **Portability**: Easy to share/move entire projects
3. **Clean outputs**: Media files stay with their source
4. **Research tracking**: Research reports linked to implementations
5. **Version control**: Each project can be its own git repo

## Skills Implementation

Both `math-research` and `manim-coding` skills have been updated to:
- Create project directories in `/manim-projects/`
- Work exclusively within project subdirectories
- Use absolute paths for all file operations
- Verify working directory before operations

## Updated: 2025-11-27
