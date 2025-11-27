# Math Research Process - Quick Reference

A quick guide to researching mathematical topics and planning Manim animations.

---

## 5-Step Research Process

### 📍 Step 1: Assess Topic Complexity
**Question**: Is this basic, intermediate, or advanced math?

- **Basic**: High school level or below → Use Wikipedia + Brilliant
- **Intermediate**: Undergraduate level → Use Wikipedia + Brilliant
- **Advanced**: Graduate level, requires proofs → Use Wikipedia + Brilliant + ProofWiki

### 🔍 Step 2: Gather Information

**Always search in this order:**

1. **Wikipedia** (primary source)
   - Get formal definition
   - Understand historical context
   - Find formulas and notation
   - Look for diagrams/illustrations
   - Check related concepts

2. **Brilliant.org** (intuitive understanding)
   - Get step-by-step explanations
   - Find visual approaches
   - Understand problem-solving strategies
   - See interactive demonstrations

3. **ProofWiki** (only for advanced topics)
   - Get rigorous proofs
   - Find formal mathematical definitions
   - Understand proof structure

### 🧠 Step 3: Synthesize Information

**Extract and organize:**
- ✅ Key definitions (formal and intuitive)
- ✅ Important formulas and notation
- ✅ Visual elements (shapes, graphs, diagrams)
- ✅ Concrete examples
- ✅ Properties and special cases
- ✅ Common misconceptions
- ✅ Prerequisites

### 🎨 Step 4: Plan Manim Animations

**Think visually:**
- What objects need to be shown?
- What transformations demonstrate the concept?
- What's the narrative flow?
- Where are the "aha!" moments?
- How to make abstract ideas concrete?

**Plan scene by scene:**
- Scene objectives
- Visual elements needed
- Animation sequence
- Code approach (pseudocode)
- Timing estimates

### 📝 Step 5: Write Comprehensive Report

**Use the template structure:**
1. Overview
2. Mathematical definition
3. Key concepts
4. Notation and formulas
5. Visual elements
6. Concrete examples
7. **Manim animation plan** (detailed)
8. "Aha!" moments
9. Common misconceptions
10. Extensions
11. Sources
12. Implementation notes
13. Summary

---

## Research Checklist

Before finishing a report, verify you have:

### Content Quality
- [ ] Accurate mathematical definitions
- [ ] Both formal and intuitive explanations
- [ ] At least 3 concrete examples
- [ ] Proper LaTeX notation for all formulas
- [ ] Prerequisites clearly listed
- [ ] Common misconceptions addressed

### Visual Planning
- [ ] Geometric representations identified
- [ ] Graphs/plots specified
- [ ] Color scheme planned
- [ ] Diagrams described
- [ ] Visual "aha!" moments noted

### Animation Planning
- [ ] 3+ scenes planned in detail
- [ ] Each scene has clear objective
- [ ] Visual elements listed for each scene
- [ ] Animation steps specified
- [ ] Pseudocode/implementation hints provided
- [ ] Timing estimates given
- [ ] Technical considerations noted

### Implementation Readiness
- [ ] Difficulty level assessed
- [ ] Time estimate provided
- [ ] Required Manim features listed
- [ ] Potential challenges identified
- [ ] Recommended development order suggested
- [ ] Testing strategy outlined

### Documentation
- [ ] All sources cited with full URLs
- [ ] Date accessed noted for each source
- [ ] Related topics suggested
- [ ] Report properly formatted
- [ ] File named correctly: `research-[topic]-[date].md`

---

## Quick Decision Trees

### Which sources to use?

```
Is the topic advanced (graduate-level math)?
│
├─ YES → Use Wikipedia + Brilliant + ProofWiki
│
└─ NO → Is it intermediate (undergraduate)?
    │
    ├─ YES → Use Wikipedia + Brilliant
    │
    └─ NO → It's basic → Use Wikipedia + Brilliant
```

### How many scenes to plan?

```
Is the concept simple and visual?
│
├─ YES → 3-4 scenes (intro, demo, examples, conclusion)
│
└─ NO → Is it complex with multiple parts?
    │
    ├─ YES → 5-7 scenes (break into logical steps)
    │
    └─ UNSURE → Start with 4 scenes, expand if needed
```

### How detailed should examples be?

```
Always include:
├─ Simple/basic example (easy to understand)
├─ Intermediate example (shows typical use)
└─ Interesting example (edge case or application)

Optional:
└─ Real-world application example
```

---

## Animation Planning Tips

### Scene Structure
Each scene should have:
1. **Clear objective** - What should viewers learn?
2. **Visual elements** - What objects appear?
3. **Animation sequence** - What happens step by step?
4. **Code hints** - Which Manim classes to use?
5. **Duration** - How long should it take?

### Good Scene Objectives
✅ "Introduce the concept and define terms"
✅ "Demonstrate the formula with concrete numbers"
✅ "Show visual proof of why the theorem works"
✅ "Apply the concept to a real-world problem"

❌ "Show stuff"
❌ "Make it look cool"
❌ "Explain everything"

### Visual Element Descriptions
Be specific about:
- **Type**: Circle, Square, Axes, Graph, Text, etc.
- **Styling**: Color, opacity, stroke width
- **Position**: Where it appears (coordinates or relative)
- **Size**: Dimensions or scale
- **Labels**: What text/math appears

**Good example**:
"Blue circle with radius 1, filled with opacity 0.5, centered at origin, with label 'C' at top"

**Bad example**:
"A circle"

### Pseudocode Quality
Include:
- Specific Manim class names
- Positioning methods
- Animation types
- Parameter hints

**Good pseudocode**:
```
circle = Circle(radius=1).set_fill(BLUE, opacity=0.5)
circle.move_to(axes.c2p(0, 0))
self.play(Create(axes), FadeIn(circle))
```

**Bad pseudocode**:
```
Make a circle and show it
```

---

## Common Mistakes to Avoid

### Research Phase
❌ Using only one source
❌ Skipping visual diagrams in sources
❌ Not checking mathematical accuracy
❌ Ignoring intuitive explanations
❌ Forgetting to note prerequisites

### Planning Phase
❌ Planning animations that are too complex to implement
❌ Not considering timing/pacing
❌ Skipping concrete examples
❌ Using vague descriptions
❌ Not identifying "aha!" moments
❌ Forgetting about color coding
❌ Not estimating difficulty

### Report Writing
❌ Missing sections from template
❌ Using informal notation instead of LaTeX
❌ Not citing sources
❌ Being too vague about visual elements
❌ Not providing implementation hints
❌ Skipping the summary

---

## Time Estimates

### Research Duration
- **Basic topic**: 10-15 minutes
- **Intermediate topic**: 15-25 minutes
- **Advanced topic**: 25-40 minutes

### Report Writing Duration
- **First report**: 30-45 minutes (learning template)
- **Subsequent reports**: 20-30 minutes
- **Complex topics**: 40-60 minutes

### Total Time
- **Basic topic**: ~45-60 minutes total
- **Intermediate topic**: ~50-70 minutes total
- **Advanced topic**: ~70-100 minutes total

---

## Quality Checks

### Before Finishing
Ask yourself:

1. **Completeness**: Did I fill out every section?
2. **Accuracy**: Is the math correct?
3. **Clarity**: Can someone implement this without questions?
4. **Visual**: Are visual elements clearly described?
5. **Practical**: Are examples concrete and useful?
6. **Sources**: Are all sources cited?
7. **Ready**: Is this ready for implementation?

### Final Review
- Read through the entire report
- Verify all LaTeX is properly formatted
- Check that all URLs are complete
- Ensure scene plans are detailed enough
- Confirm difficulty and time estimates are realistic

---

## File Organization

```
research-reports/
├── research-pythagorean-theorem-2025-11-26.md
├── research-fourier-transform-2025-11-26.md
├── research-taylor-series-2025-11-26.md
└── research-matrix-multiplication-2025-11-26.md
```

**Naming convention**: `research-[topic-name]-[YYYY-MM-DD].md`
- Use lowercase
- Use hyphens for spaces
- Include date for versioning
- Be specific (not "calculus", use "derivatives" or "integrals")

---

## Example Topic Progression

### Start Simple (Build Confidence)
1. Pythagorean theorem
2. Quadratic formula
3. Circle area formula
4. Sine and cosine waves

### Move to Intermediate
5. Derivatives (limit definition)
6. Integration (area under curve)
7. Matrix multiplication
8. Fourier series basics

### Tackle Advanced (When Ready)
9. Epsilon-delta proof of limit
10. Taylor series convergence
11. Eigenvalue decomposition
12. Fundamental theorem of calculus (rigorous proof)

---

## Helpful Reminders

- 📚 This skill is for **research and planning**, not coding
- 🎨 Think like an educator: How would you teach this?
- 🔍 Multiple sources = better understanding
- 📊 Concrete examples make abstract ideas clear
- 🎬 Plan scenes like telling a story
- ⏱️ Estimate realistically (beginners need more time)
- ✅ Complete reports = smooth implementation
- 🔄 This skill pairs with **manim-coding** for full workflow

---

**Quick Start**: Pick a topic → Research 3 sources → Identify visuals → Plan scenes → Write report → Ready for coding!
