# Manim Agent Plugin - Complete Overview

A visual guide to understanding how all components work together.

## 🎯 The Big Picture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MANIM AGENT PLUGIN                           │
│                                                                 │
│  Transform mathematical concepts into beautiful animations     │
└─────────────────────────────────────────────────────────────────┘
                                ▼
        ┌───────────────────────────────────────────┐
        │     🤖 MANIM ANIMATOR AGENT               │
        │  Intelligent Workflow Orchestrator        │
        │                                           │
        │  • Decides which skills to use            │
        │  • Manages workflow execution             │
        │  • Coordinates research → implementation  │
        └───────────────────────────────────────────┘
                        ▼           ▼
        ┌───────────────┴───┐   ┌─┴─────────────────┐
        │                   │   │                   │
┌───────▼────────┐  ┌──────▼─────────┐  ┌──────────▼────────┐
│ 🔬 MATH        │  │ 🤖 ORCHESTRATOR │  │ 🎨 MANIM          │
│ RESEARCH       │  │                 │  │ CODING            │
│ SKILL          │  │ Workflows:      │  │ SKILL             │
│                │  │ 1. Generate     │  │                   │
│ Researches &   │◄─┤ 2. Refine       │─►│ Implements &      │
│ Plans          │  │ 3. Compose      │  │ Codes             │
│                │  │ 4. Interpret    │  │                   │
└────────────────┘  └─────────────────┘  └───────────────────┘
        │                                          │
        ▼                                          ▼
┌────────────────┐                      ┌──────────────────┐
│ 📄 RESEARCH    │                      │ 💻 MANIM CODE    │
│ REPORTS        │                      │                  │
│                │                      │ Complete Python  │
│ Detailed plans │                      │ implementation   │
│ with scenes    │                      │ ready to render  │
└────────────────┘                      └──────────────────┘
                                                  │
                                                  ▼
                                        ┌──────────────────┐
                                        │ 🎬 RENDERED      │
                                        │ ANIMATION        │
                                        │                  │
                                        │ Beautiful math   │
                                        │ visualization    │
                                        └──────────────────┘
```

---

## 📦 Component Breakdown

### Component 1: Math Research Skill 🔬

**Location**: `skills/math-research/`

```
┌─────────────────────────────────────┐
│     MATH RESEARCH SKILL             │
├─────────────────────────────────────┤
│                                     │
│  Input: Mathematical topic          │
│         "Fourier transform"         │
│                                     │
│  ▼ Searches:                        │
│    • Wikipedia (always)             │
│    • Brilliant.org (intuition)      │
│    • ProofWiki (if advanced)        │
│                                     │
│  ▼ Analyzes:                        │
│    • Definitions                    │
│    • Visual elements                │
│    • Examples                       │
│    • Teaching moments               │
│                                     │
│  ▼ Plans:                           │
│    • Scene-by-scene breakdown       │
│    • Visual element specs           │
│    • Animation sequences            │
│    • Implementation pseudocode      │
│                                     │
│  Output: Comprehensive report       │
│          (13 sections)              │
└─────────────────────────────────────┘
```

**Files**:
- `SKILL.md` - Methodology & template
- `report-template.md` - Blank template
- `example-pythagorean-theorem.md` - Full example
- `research-process.md` - Quick guide

### Component 2: Manim Coding Skill 🎨

**Location**: `skills/manim-coding/`

```
┌─────────────────────────────────────┐
│     MANIM CODING SKILL              │
├─────────────────────────────────────┤
│                                     │
│  Input: Implementation request      │
│         "Create Scene 1"            │
│                                     │
│  ▼ References:                      │
│    • Syntax guide (3 sections)      │
│      - Essential (most used)        │
│      - Intermediate (common)        │
│      - Advanced (specialized)       │
│                                     │
│  ▼ Provides:                        │
│    • Exact Manim syntax             │
│    • Code examples                  │
│    • Best practices                 │
│    • Common patterns                │
│                                     │
│  ▼ Implements:                      │
│    • Scene classes                  │
│    • Animations                     │
│    • Visual elements                │
│    • Proper styling                 │
│                                     │
│  Output: Working Manim code         │
│          (Python .py files)         │
└─────────────────────────────────────┘
```

**Files**:
- `SKILL.md` - Complete reference
- `quick-reference.md` - Cheat sheet
- `syntax-by-category.md` - Organized syntax
- `examples.py` - 15+ runnable examples

### Component 3: Manim Animator Agent 🤖

**Location**: `agents/manim-animator.md`

```
┌──────────────────────────────────────────────┐
│        MANIM ANIMATOR AGENT                  │
├──────────────────────────────────────────────┤
│                                              │
│  Input: User request                         │
│         "Create animation on derivatives"    │
│                                              │
│  ▼ Analyzes request:                         │
│    • Determines workflow needed              │
│    • Identifies complexity level             │
│    • Plans execution strategy                │
│                                              │
│  ▼ Executes one of 4 workflows:              │
│                                              │
│    1️⃣ HOLISTIC GENERATION                    │
│       Research → Plan → Implement            │
│       [Uses BOTH skills]                     │
│                                              │
│    2️⃣ STYLISTIC REFINEMENT                   │
│       Analyze → Modify → Test                │
│       [Uses coding skill]                    │
│                                              │
│    3️⃣ MULTI-SCENE COMPOSITION                │
│       Inventory → Plan → Combine             │
│       [Uses BOTH skills]                     │
│                                              │
│    4️⃣ MATHEMATICAL INTERPRETATION            │
│       Analyze → Research → Suggest           │
│       [Uses BOTH skills]                     │
│                                              │
│  Output: Complete solution                   │
│          (Reports + Code)                    │
└──────────────────────────────────────────────┘
```

**Files**:
- `manim-animator.md` - Agent definition
- `README.md` - Complete guide
- `workflow-quick-reference.md` - Quick reference

---

## 🔄 The Four Workflows in Detail

### Workflow 1: Holistic Scene Generation 🎨

```
USER REQUEST: "Create animation explaining [concept]"
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 1: RESEARCH (math-research skill)            │
├─────────────────────────────────────────────────────┤
│ • Fetch from Wikipedia, Brilliant, ProofWiki       │
│ • Understand concept deeply                        │
│ • Identify visual elements                         │
│ • Plan 5-7 scenes                                  │
│ • Create comprehensive report                      │
│                                                     │
│ OUTPUT: research-reports/research-[topic]-date.md  │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 2: IMPLEMENTATION (manim-coding skill)       │
├─────────────────────────────────────────────────────┤
│ • Read the research report                         │
│ • Implement Scene 1 (Introduction)                 │
│ • Implement Scene 2 (Core concept)                 │
│ • Implement Scene 3 (Examples)                     │
│ • ... continue for all planned scenes              │
│ • Test with manim -pql                             │
│                                                     │
│ OUTPUT: [topic]_animation.py                       │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 3: REFINEMENT                                │
├─────────────────────────────────────────────────────┤
│ • Review with user                                 │
│ • Make requested adjustments                       │
│ • Final polish                                     │
│                                                     │
│ OUTPUT: Polished, render-ready animation           │
└─────────────────────────────────────────────────────┘
```

### Workflow 2: Stylistic Refinement ✨

```
USER REQUEST: "Make this more colorful and slower"
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 1: ANALYSIS                                  │
├─────────────────────────────────────────────────────┤
│ • Read existing code                               │
│ • Identify visual elements to modify               │
│ • Understand current styling                       │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 2: PLANNING (manim-coding skill)             │
├─────────────────────────────────────────────────────┤
│ • Reference syntax for color methods               │
│ • Plan timing adjustments (run_time)               │
│ • Consider visual impact                           │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 3: IMPLEMENTATION                            │
├─────────────────────────────────────────────────────┤
│ • Edit code with new colors                        │
│ • Adjust run_time parameters                       │
│ • Test changes                                     │
│                                                     │
│ OUTPUT: Modified code with new styling             │
└─────────────────────────────────────────────────────┘
```

### Workflow 3: Multi-Scene Composition 🎬

```
USER REQUEST: "Combine animations A, B, C into one video"
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 1: INVENTORY                                 │
├─────────────────────────────────────────────────────┤
│ • Identify existing scenes                         │
│ • Check for missing pieces                         │
│ • Plan narrative flow                              │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 2: CREATE MISSING PIECES (if needed)         │
├─────────────────────────────────────────────────────┤
│ • Research missing topics (math-research)          │
│ • Implement missing scenes (manim-coding)          │
│ • Create transition scenes                         │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 3: COMPOSITION                               │
├─────────────────────────────────────────────────────┤
│ • Combine all scenes in one file                   │
│ • Add title cards and transitions                  │
│ • Ensure style consistency                         │
│ • Test complete sequence                           │
│                                                     │
│ OUTPUT: [topic]_complete.py (unified animation)    │
└─────────────────────────────────────────────────────┘
```

### Workflow 4: Mathematical Interpretation 🔍

```
USER REQUEST: "Is this animation correct? How to improve?"
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 1: CODE ANALYSIS                             │
├─────────────────────────────────────────────────────┤
│ • Read the code thoroughly                         │
│ • Identify mathematical concepts shown             │
│ • Trace animation flow                             │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 2: RESEARCH & VERIFY (math-research skill)   │
├─────────────────────────────────────────────────────┤
│ • Look up the mathematical concept                 │
│ • Verify accuracy of implementation                │
│ • Check for completeness                           │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 3: ANALYSIS REPORT                           │
├─────────────────────────────────────────────────────┤
│ • Explain what code demonstrates                   │
│ • Identify strengths                               │
│ • Identify weaknesses                              │
│ • Suggest improvements:                            │
│   - Mathematical (accuracy, completeness)          │
│   - Visual (clarity, colors)                       │
│   - Pedagogical (teaching effectiveness)           │
└─────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ PHASE 4: OPTIONAL IMPLEMENTATION                   │
├─────────────────────────────────────────────────────┤
│ • If user requests, implement improvements         │
│ • Show before/after comparison                     │
│                                                     │
│ OUTPUT: Analysis report + Improved code (optional) │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Decision Flow: Which Workflow?

```
                    USER MAKES REQUEST
                           │
                           ▼
              ┌────────────────────────┐
              │ Does existing code     │
              │ exist for this task?   │
              └────────────────────────┘
                    │            │
                   NO           YES
                    │            │
                    ▼            ▼
          ┌─────────────┐   ┌──────────────────────┐
          │ NEW TOPIC?  │   │ What type of change? │
          └─────────────┘   └──────────────────────┘
                 │                │        │        │
                YES         STYLE  REVIEW  COMBINE
                 │           │      │        │
                 ▼           ▼      ▼        ▼
         ┌──────────┐  ┌────────┐ ┌────┐ ┌───────┐
         │WORKFLOW 1│  │WORKFLOW│ │WF 4│ │WF 3   │
         │GENERATE  │  │2 REFINE│ │    │ │COMPOSE│
         └──────────┘  └────────┘ └────┘ └───────┘
```

---

## 📁 File Organization

### Input → Processing → Output Flow

```
┌─────────────────────────────────────────────────────────┐
│                    INPUT PHASE                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  User Request: "Create animation on [topic]"           │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────┐
│                 PROCESSING PHASE                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Plugin Components:                                     │
│  ├─ skills/                                            │
│  │  ├─ math-research/    (Researches & Plans)         │
│  │  └─ manim-coding/     (Implements Code)            │
│  └─ agents/                                            │
│     └─ manim-animator    (Orchestrates Workflow)       │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   OUTPUT PHASE                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Generated Files:                                       │
│  ├─ research-reports/                                  │
│  │  └─ research-[topic]-[date].md                     │
│  ├─ [topic]_animation.py                               │
│  └─ media/                (created by Manim)           │
│     └─ videos/                                         │
│        └─ [output].mp4                                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🎓 Complete Example: From Start to Finish

### Example: Creating a Derivative Animation

```
STEP 1: USER ACTIVATION
───────────────────────
$ /agent manim-animator

STEP 2: USER REQUEST
────────────────────
"Create an animation explaining derivatives for high school students"

STEP 3: AGENT PROCESSING
─────────────────────────

┌─ Phase 1: Research (5 min)
│  ✓ Fetching Wikipedia: Derivative
│  ✓ Fetching Brilliant: Derivatives
│  ✓ Synthesizing information
│  ✓ Planning 5 scenes:
│    1. Introduction (what is a derivative?)
│    2. Secant line to tangent line
│    3. Limit definition visualization
│    4. Formula: f'(x) = lim[h→0] (f(x+h)-f(x))/h
│    5. Examples (x², sin(x), etc.)
│  ✓ Creating report
│  📄 Saved: research-reports/research-derivatives-2025-11-26.md
│
├─ Phase 2: Implementation (20 min)
│  ✓ Creating derivatives.py
│  ✓ Implementing Scene 1: Introduction
│     - Create axes
│     - Plot f(x) = x²
│     - Add title and labels
│  ✓ Implementing Scene 2: Secant to Tangent
│     - Show two points on curve
│     - Draw secant line
│     - Animate points approaching
│     - Show limit to tangent
│  ✓ Implementing Scene 3: Limit Definition
│     - Display formula
│     - Show h getting smaller
│     - Visualize the limit
│  ✓ Implementing Scene 4: Formula Application
│     - Derive f'(x) for f(x)=x²
│     - Show f'(x) = 2x
│  ✓ Implementing Scene 5: More Examples
│     - Quick examples with other functions
│  ✓ Testing: manim -pql derivatives.py
│  💻 Complete code ready!
│
└─ Phase 3: Delivery
   ✓ Animation complete!
   ✓ Total scenes: 5
   ✓ Estimated duration: ~90 seconds
   ✓ Files created:
     - research-reports/research-derivatives-2025-11-26.md
     - derivatives.py

STEP 4: USER REFINEMENT
────────────────────────
"Make it more colorful and emphasize the limit formula"

Agent processes (Workflow 2):
✓ Reading derivatives.py
✓ Updating color scheme:
  - Function: BLUE → gradient(BLUE, PURPLE)
  - Secant: RED → ORANGE
  - Points: WHITE → YELLOW
✓ Adding emphasis:
  - Circumscribe(formula) animation
  - Flash on key parts
✓ Changes complete!

STEP 5: USER RENDERS
─────────────────────
$ manim -pqh derivatives.py

Output: media/videos/derivatives/1080p60/[scenes].mp4

✅ COMPLETE! Beautiful animation ready to share!
```

---

## 🚀 Quick Command Reference

```bash
# Activate agent
/agent manim-animator

# Common requests
"Create animation on [topic]"
"Make this [style change]"
"Combine [animations]"
"Is this code correct?"

# Rendering
manim -pql file.py Scene    # Preview (fast)
manim -pqh file.py Scene    # High quality
manim -pqk file.py Scene    # 4K quality
manim -s file.py Scene      # Last frame only
```

---

## 📊 Plugin Statistics

### Components
- **2 Skills** (math-research, manim-coding)
- **1 Agent** (manim-animator)
- **4 Workflows** (generate, refine, compose, interpret)
- **15+ Files** (documentation + examples)

### Documentation
- **Main README**: Complete plugin overview
- **Skills README**: How skills work together
- **Agent README**: Detailed workflow guide
- **Quick Reference**: Fast lookup for workflows
- **15 Total Docs**: Comprehensive coverage

### Examples
- **1 Complete Research Report**: Pythagorean theorem
- **15+ Code Examples**: Runnable Manim patterns
- **4 Workflow Examples**: Each workflow demonstrated

---

## ✨ Key Features Summary

✅ **Intelligent**: Auto-selects appropriate workflow
✅ **Comprehensive**: Research → Plan → Implement → Refine
✅ **Educational**: Focuses on teaching effectiveness
✅ **Flexible**: Handles simple to complex topics
✅ **Well-Documented**: Extensive guides and examples
✅ **Battle-Tested**: Based on proven patterns

---

## 🎯 Success Metrics

### Quality Indicators
- ✅ Mathematical accuracy verified from multiple sources
- ✅ Code runs without errors
- ✅ Animations are visually clear
- ✅ Pacing is appropriate for audience
- ✅ Educational value is high

### Performance
- Fast iteration with low-quality renders
- Comprehensive planning reduces rework
- Modular scenes enable easy updates
- Reusable reports build knowledge base

---

## 🎬 Ready to Create!

**The complete Manim Agent plugin is ready to transform mathematical concepts into beautiful animations.**

Start with: `/agent manim-animator` and let the magic begin! ✨

---

**Questions?** Check the documentation index in the main README.md
