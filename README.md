# Manim Animation Agent

A comprehensive system for creating beautiful mathematical animations using Claude Code and Manim Community Edition. Combines intelligent research, expert coding, and streamlined project management into a complete animation workflow.

## Claude Code prompt only vs. Agent workflow
<img src="https://github.com/user-attachments/assets/6b6632f7-e239-44a9-a9ea-1f8af2754781" width="400"/> <img src="https://github.com/user-attachments/assets/bca3a255-a4cd-428b-9838-e2396ae4e9d0" width="400"/> 
## Longer video demos (done in one shot)
![Fourier Transform Drawing](https://github.com/user-attachments/assets/cc745e72-d532-4737-9840-ea8ea5f78ddc)
![Huffman Encoding](https://github.com/user-attachments/assets/ef063faf-cc34-4234-bc51-9a1a6c55150c)


## 🎯 What This Does

**Create professional mathematical animations from natural language requests:**
```
"Animate the Huffman encoding process for the message AABBBCCCC"
↓
Complete animation with 5 scenes, 80.6% compression visualization, and customizable parameters
[View the result: CombinedScenes.mp4]
```

**Two-part system:**
1. **Claude Code Plugin** - Intelligent agent that researches, plans, and implements animations
2. **Project Manager** - Interactive interface for organizing projects and rendering videos

## 🚀 Quick Start

### Prerequisites

```bash
# Install Manim Community Edition
pip install manim

# Install ffmpeg (for video combination)
brew install ffmpeg  # macOS
# OR
sudo apt install ffmpeg  # Linux
```

### Create Your First Animation

**Step 1: Use Claude Code to create animation**
```bash
# In Claude Code
/animate Explain the Pythagorean theorem with a 3-4-5 triangle
```

The agent will:
- Research the mathematical concept
- Create a detailed animation plan
- Implement complete Manim scenes
- Extract customizable visual parameters
- Generate project documentation

**Step 2: Render using the project manager**
```bash
# Run the interactive interface
python main.py

# Select project → file → scene → quality
# Or render combined video of all scenes
```

## 📁 Project Structure

```
manim-agent/
│
├── main.py                      # Interactive project manager and renderer
├── README.md                    # This file
│
├── manim-projects/              # All animation projects
│   ├── huffman-encoding/
│   │   ├── animation.py         # Main animation code (8 scenes)
│   │   ├── params.py            # Visual parameters (colors, timing, etc.)
│   │   ├── research.md          # Research report and planning
│   │   ├── README.md            # Customization guide
│   │   └── media/               # Rendered videos (created by Manim)
│   │
│   ├── golden-ratio-spiral/
│   ├── lorenz-attractor-1.0/
│   ├── lorenz-attractor-2.0/
│   └── pentagon-construction/
│
├── agents/                      # Agent definitions
│   └── manim-animator.md        # Main orchestrator agent
│
└── skills/                      # Specialized skills
    ├── math-research/           # Research mathematical concepts
    └── manim-coding/            # Manim syntax expertise
```

## 🎬 Complete Workflow

### 1. Create Animation with Claude Code

```bash
# Activate the animation workflow
/animate Create a visualization of the golden ratio spiral

# Or use the agent directly
/agent manim-animator
"Create an animation showing Huffman encoding"
```

**What happens:**
1. **Research Phase** - Gathers information from Wikipedia, academic sources
2. **Planning Phase** - Creates detailed scene-by-scene plan
3. **Implementation Phase** - Writes complete Manim code
4. **Parameter Extraction** - Separates visual parameters into params.py
5. **Documentation** - Generates README with customization guide

**Output:**
```
manim-projects/huffman-encoding/
├── animation.py       # 8 scenes, 746 lines
├── params.py          # All colors, text, dimensions, timing
├── research.md        # Comprehensive research (39 KB)
├── README.md          # Customization guide
└── huffman_data.json  # Computed data for the animation
```

### 2. Customize (Optional)

Edit `params.py` to change visual appearance **without touching code**:

```python
# Change color scheme
COLORS = {
    "primary_blue": "#FF6B6B",     # From blue to coral red
    "leaf_node_fill": "#4ECDC4",   # From green to teal
}

# Adjust pacing
TIMING = {
    "wait_long": 3.0,              # Slower pace
    "tree_create_duration": 5.0,   # More time for tree
}

# Resize elements
SIZES = {
    "title_large": 56,             # Larger title
    "node_char": 24,               # Bigger labels
}
```

### 3. Render with Project Manager

```bash
python main.py
```

**Interactive menu:**
```
Select Project:
  1. huffman-encoding
  2. golden-ratio-spiral
  3. pentagon-construction

Select Scene:
  -1. Combined video (all scenes in one file)
   0. All scenes (separate files)
   1. IntroScene
   2. FrequencyScene
   ...
```

**Rendering options:**
- `-1` → Single video with all scenes concatenated (no popups)
- `0` → Render all scenes as separate files
- `1+` → Render individual scene

## 💻 Project Manager Commands

### `/render` - High Quality Render (1080p60)
Renders selected scenes in high quality with preview.

### `/preview` - Quick Preview (480p15)
Fast low-quality render for testing.

### `/load` - Load Project
Interactive selection from existing projects.

### `/list` - List All Projects
Shows all projects with creation dates and file counts.

### `/info` - Project Information
Shows details about the currently loaded project.

### `/files` - Show Project Files
Lists all Python files, research reports, and rendered videos.

### `/help` - Show Help
Displays all available commands.

### `/exit` or `/quit` - Exit
Exits the project manager.

## Lorenz Attractor 1.0 vs 2.0

A side-by-side comparison demonstrating the power of the new **agents & skills architecture**.

| Version | Method | Develop Time | Demo Video |
|---------|--------|----------|------------|
| **1.0** | Detailed manual prompt to Claude Code | ~2mins | [`manim-projects/lorenz-attractor-1.0/media/videos/LorenzAttractorTracing.mp4`](manim-projects/lorenz-attractor-1.0/media/videos/LorenzAttractorTracing.mp4) |
| **2.0** | `/animate` command with automated agents & skills | ~5mins | [`manim-projects/lorenz-attractor-2.0/media/videos/animation/1080p60/LorenzAttractor.mp4`](manim-projects/lorenz-attractor-2.0/media/videos/animation/1080p60/LorenzAttractor.mp4) |

**Key Difference:**
- **v1.0:** Manual step-by-step instructions → single-shot code generation
- **v2.0:** `/animate` → automated research (math-research skill) → structured planning → implementation (manim-coding skill)

## 🛠️ Plugin Components

### Manim Animator Agent
**Location:** `agents/manim-animator.md`

Orchestrates the complete workflow from concept to implementation.

**Core workflows:**
1. **Holistic Scene Generation** - Research → Plan → Implement
2. **Stylistic Refinement** - Colors, timing, positioning
3. **Multi-Scene Composition** - Combine animations
4. **Mathematical Interpretation** - Review and improve
5. **Parameter Extraction** - Separate visuals from logic

### Math Research Skill
**Location:** `skills/math-research/`

Researches mathematical concepts and creates animation plans.

**Features:**
- MediaWiki API for Wikipedia access
- Websearch other relevant sites such as Brilliant.org, GeeksforGeeks, ProofWiki, and WolframAlpha
- Research checklist before starting
- Early exit for comprehensive sources
- Scene-by-scene planning with visual specifications
- Implementation pseudocode

### Manim Coding Skill
**Location:** `skills/manim-coding/`

Expert knowledge of Manim Community Edition syntax.

**Features:**
- Complete syntax reference
- 15+ runnable examples
- Quick reference cheat sheets
- Common patterns and best practices

## 🎯 Advanced Features

### Combined Video Rendering

Create a single video from all scenes:

```bash
# Using main.py
/render → Select project → Select file → Choose -1

# Direct command
cd manim-projects/huffman-encoding
manim -qh animation.py
```

The system automatically:
1. Renders all scenes in sequence
2. Finds the output directory (any quality)
3. Concatenates videos using ffmpeg
4. Creates `CombinedScenes.mp4`
5. Shows file size and location

### Parameter Customization

Every animation includes `params.py` with organized sections:

```python
COLORS = {...}       # All color definitions
TEXT = {...}         # All text strings
DIMENSIONS = {...}   # Sizes, widths, spacing
POSITIONS = {...}    # Y-coordinates, layout
TIMING = {...}       # Animation durations
SIZES = {...}        # Font sizes, scales
OPACITY = {...}      # Fill and stroke opacities
SPECIAL = {...}      # Algorithm-specific params
```

### Quality Settings

```bash
# Low quality (480p, 15fps) - Fast preview
manim -pql animation.py SceneName

# Medium quality (720p, 30fps)
manim -pqm animation.py SceneName

# High quality (1080p, 60fps) - Default
manim -pqh animation.py SceneName

# 4K quality (2160p, 60fps)
manim -pqk animation.py SceneName
```


## 📊 Agent Workflows

### Workflow 1: Holistic Scene Generation
**When:** Creating new animations

**Process:**
1. Research mathematical concept from multiple sources
2. Plan scene-by-scene structure
3. Implement Manim code
4. Extract visual parameters
5. Generate documentation

**Example:**
```
"Create animation explaining derivatives"
→ Research report
→ 5 scenes implemented
→ Parameters externalized
→ README with customization guide
```

### Workflow 2: Stylistic Refinement
**When:** Adjusting colors, timing, positions

**Process:**
1. Identify target elements
2. Update parameters or code
3. Test changes

**Example:**
```
"Make the colors more vibrant and slow down transitions"
→ Updated COLORS in params.py
→ Adjusted TIMING values
→ Changes complete
```

### Workflow 3: Multi-Scene Composition
**When:** Combining multiple animations

**Process:**
1. Inventory existing scenes
2. Plan narrative flow
3. Create transitions
4. Render combined video

### Workflow 4: Mathematical Interpretation
**When:** Reviewing or improving code

**Process:**
1. Analyze mathematical accuracy
2. Check pedagogical clarity
3. Suggest improvements

### Workflow 5: Parameter Extraction
**When:** After creating any animation

**Process:**
1. Identify customizable parameters (colors, text, dimensions, positions, timing, sizes, opacities)
2. Create params.py with organized sections
3. Update animation.py to import parameters
4. Generate README with customization guide

## 📖 Documentations

### Quick References
- [Manim Coding Quick Reference](skills/manim-coding/quick-reference.md)
- [Math Research Process](skills/math-research/research-process.md)
- [Agent Workflows](agents/workflow-quick-reference.md)

### Detailed Guides
- [Agent Overview](agents/README.md)
- [Math Research Skill](skills/math-research/README.md)
- [Manim Coding Skill](skills/manim-coding/README.md)

### Examples
- [Pentagon Construction](manim-projects/pentagon-construction/README.md) - ⭐ **Featured showcase project** ([Video](manim-projects/pentagon-construction/media/videos/animation/1080p60/CombinedScenes.mp4))
- [Huffman Encoding Process](manim-projects/huffman-encoding-process/README.md) - ⭐ **Featured showcase project** ([Video](manim-projects/huffman-encoding-process/media/videos/animation/1080p60/CombinedScenes.mp4))
- [Golden Ratio Spiral](manim-projects/golden-ratio-spiral/README.md)

## 🎓 Best Practices

### 1. Be Specific in Requests - describe scene-by-scene
```
✅ "Animate the construction of a regular pentagon using compass and straightedge"
❌ "Make a geometry animation"
```

### 2. Specify Audience / Concept Complexity
```
✅ "Explain derivatives for high school students"
✅ "Rigorous epsilon-delta proof for graduate students"
```

### 3. Use Parameter Files
- Edit `params.py` for visual changes
- Keep code changes for logic/math only
- Version control both separately

## 🤝 Contributing

### Adding Example Projects
1. Create animation using `/animate`
2. Ensure params.py is well-organized
3. Write comprehensive README.md
4. Test all scenes render correctly

### Improving Agent Workflows
1. Edit `agents/manim-animator.md`
2. Add new workflows or refine existing
3. Test with diverse requests
4. Document changes

### Expanding Skills
1. Add new skill in `skills/`
2. Create SKILL.md with definition
3. Update agent to use new skill
4. Add examples and documentation

## 🎉 Acknowledgments

- **Grant Sanderson (3Blue1Brown)** - Creator of original Manim
- **Manim Community** - Maintaining Manim Community Edition
- **Wikipedia, GeeksforGeeks, Brilliant, ProofWiki** - Authoritative mathematical content

---

## 🚀 Get Started Now

```bash
# 1. View the featured examples
open manim-projects/huffman-encoding-process/media/videos/animation/1080p60/CombinedScenes.mp4

# 2. Create your first animation
/animate Explain the Pythagorean theorem

# 3. Render it
python main.py
→ Select project
→ Select animation.py
→ Choose scene or combined video

# 4. Watch mathematics come to life! 🎬✨
```
