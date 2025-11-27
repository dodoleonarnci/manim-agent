# Manim Agent - Animation Workflow Orchestrator

This directory contains the **manim-animator** agent, a specialized AI assistant that orchestrates complete Manim animation workflows from mathematical research to final implementation.

## 🤖 What is the Manim Animator Agent?

The **manim-animator** agent is an intelligent orchestrator that:
- Uses the **math-research** skill to research and plan animations
- Uses the **manim-coding** skill to implement Manim code
- Combines both skills to deliver complete animation workflows
- Handles complex multi-scene compositions
- Makes intelligent decisions about workflow execution

Think of it as a **project manager** that knows when to research, when to code, and how to deliver polished mathematical animations.

---

## 🎯 Four Core Workflows

The agent specializes in four distinct workflows:

### 1️⃣ Holistic Scene Generation
**What**: Create complete animations from scratch based on mathematical concepts
**When to use**: Starting a new animation project
**Example**: "Create an animation explaining derivatives"

**What the agent does**:
- Researches the concept from Wikipedia, Brilliant, ProofWiki
- Plans 5-7 scenes with detailed visualizations
- Implements each scene with proper Manim code
- Tests and refines the animation
- Delivers complete, render-ready code

### 2️⃣ Stylistic Refinement
**What**: Make visual and stylistic changes to existing animations
**When to use**: You have code but want to improve the look/feel
**Example**: "Make the colors more vibrant and slow down the transformations"

**What the agent does**:
- Analyzes existing code
- Plans specific visual modifications
- Implements style changes using proper Manim methods
- Tests changes for visual quality
- Maintains mathematical accuracy throughout

### 3️⃣ Multi-Scene Composition
**What**: Combine multiple scenes into longer, cohesive animations
**When to use**: Creating series, courses, or narrative animations
**Example**: "Combine my derivative and integral animations into one video"

**What the agent does**:
- Inventories existing scenes
- Plans narrative flow and transitions
- Creates missing pieces as needed
- Implements smooth transitions
- Delivers unified animation with consistent styling

### 4️⃣ Mathematical Interpretation
**What**: Analyze and improve existing animation code
**When to use**: Code review, optimization, or understanding existing work
**Example**: "Is this animation mathematically accurate? How can I improve it?"

**What the agent does**:
- Reads and analyzes the code
- Researches the mathematical concept
- Verifies accuracy and completeness
- Suggests improvements (mathematical, visual, pedagogical)
- Optionally implements improvements

---

## 📋 How to Use the Agent

### Activating the Agent

```bash
# In Claude Code CLI
/agents

# Or directly invoke
/agent manim-animator
```

Once activated, the agent automatically determines which workflow to use based on your request.

### Request Examples

#### Holistic Scene Generation
```
"Create an animation explaining the Pythagorean theorem"
"Visualize Fourier transforms with examples"
"Make a video about Taylor series convergence"
```

#### Stylistic Refinement
```
"Make this animation use a blue-to-purple gradient"
"Slow down the transformation by 50%"
"Use larger text and brighter colors"
"Add more emphasis on the key formula"
```

#### Multi-Scene Composition
```
"Combine scenes 1, 2, and 3 into one animation"
"Create a 5-part calculus series"
"Link my derivative and integral animations with transitions"
```

#### Mathematical Interpretation
```
"Is this derivative animation mathematically correct?"
"What does this scene demonstrate?"
"How can I improve this explanation of limits?"
"Review this code and suggest improvements"
```

---

## 🔄 Workflow Execution Examples

### Example 1: Complete Animation from Scratch

```
USER: "Create an animation explaining derivatives"

AGENT:
[AUTO-DETECTS: Holistic Scene Generation workflow]

Phase 1: Research (math-research skill)
✓ Fetching Wikipedia article on derivatives
✓ Fetching Brilliant.org explanations
✓ Synthesizing mathematical concepts
✓ Planning 5-scene animation structure
✓ Creating detailed report
✓ Saved: research-reports/research-derivatives-2025-11-26.md

Phase 2: Implementation (manim-coding skill)
✓ Creating derivatives.py
✓ Implementing Scene 1: Introduction
✓ Implementing Scene 2: Secant to Tangent
✓ Implementing Scene 3: Limit Definition
✓ Implementing Scene 4: Formula Derivation
✓ Implementing Scene 5: Examples
✓ Testing complete animation

Phase 3: Delivery
✓ Animation ready! 5 scenes, ~90 seconds total
✓ All files saved in current directory
✓ To render: manim -pqh derivatives.py

Would you like any adjustments?
```

### Example 2: Style Improvement

```
USER: "Make the derivative animation more colorful and add emphasis on the limit formula"

AGENT:
[AUTO-DETECTS: Stylistic Refinement workflow]

Phase 1: Analysis
✓ Reading derivatives.py
✓ Identifying visual elements
✓ Locating limit formula in Scene 3

Phase 2: Planning Changes (manim-coding skill)
Proposed changes:
- Function curve: BLUE → gradient(BLUE to PURPLE)
- Secant line: RED → ORANGE (more vibrant)
- Tangent line: GREEN → TEAL (better contrast)
- Limit formula: Add Circumscribe() animation for emphasis
- Background: Subtle dark grid for depth

Phase 3: Implementation
✓ Updated color scheme throughout
✓ Added emphasis animation to formula
✓ Tested Scene 3 render

Complete! The animation now uses vibrant gradients and highlights the limit formula with a circling animation.
```

### Example 3: Multi-Scene Composition

```
USER: "Combine my derivative, integral, and FTC animations into one complete video"

AGENT:
[AUTO-DETECTS: Multi-Scene Composition workflow]

Phase 1: Inventory
✓ Found: derivatives.py (5 scenes)
✓ Found: integrals.py (4 scenes)
✓ Missing: fundamental_theorem.py

Phase 2: Planning
Structure:
- Introduction (new)
- Part 1: Derivatives (5 scenes)
- Transition (new)
- Part 2: Integrals (4 scenes)
- Transition (new)
- Part 3: Fundamental Theorem (need to create)
- Conclusion (new)

Phase 3: Create Missing Content (math-research + manim-coding)
✓ Researching Fundamental Theorem of Calculus
✓ Planning 4-scene FTC section
✓ Implementing FTC scenes

Phase 4: Composition
✓ Creating calculus_complete.py
✓ Integrating all scenes
✓ Adding title cards
✓ Implementing smooth transitions
✓ Ensuring style consistency

Complete! Full calculus introduction ready (~8 minutes total).
To render: manim -pqh calculus_complete.py
```

### Example 4: Code Review and Improvement

```
USER: "Review this limit animation and tell me if it's good"
[provides code]

AGENT:
[AUTO-DETECTS: Mathematical Interpretation workflow]

Phase 1: Code Analysis
✓ Reading provided code
✓ Mathematical concept: Limit as x approaches a value
✓ Current implementation: Shows function and point

Phase 2: Research & Verification (math-research skill)
✓ Concept: Limit definition (epsilon-delta)
✓ Mathematical accuracy: ✓ Correct
✓ Completeness: Needs improvement

Phase 3: Analysis Report
STRENGTHS:
✓ Mathematically accurate
✓ Clean code structure
✓ Good visual presentation

WEAKNESSES:
✗ Doesn't show epsilon-delta bands
✗ Only one approach point (should show from both sides)
✗ Missing formal definition display
✗ No demonstration of "arbitrarily close"

Phase 4: Improvement Suggestions
MATHEMATICAL:
- Add epsilon-delta band visualization
- Show limit from left and right
- Display formal definition

VISUAL:
- Use color gradient for approaching values
- Highlight epsilon and delta regions
- Add animation of "squeeze"

PEDAGOGICAL:
- Build intuition before formalism
- Show multiple examples
- Address "does the limit always exist?" question

Would you like me to implement these improvements?
```

---

## 🎨 Agent Capabilities

### What the Agent CAN Do

✅ **Research mathematical concepts** from authoritative sources
✅ **Plan comprehensive animations** with scene-by-scene detail
✅ **Implement complete Manim code** from scratch
✅ **Make stylistic changes** to colors, timing, emphasis
✅ **Combine multiple animations** into cohesive videos
✅ **Analyze existing code** for accuracy and quality
✅ **Suggest improvements** (mathematical, visual, pedagogical)
✅ **Create research reports** documenting the planning process
✅ **Test and iterate** on animations
✅ **Maintain mathematical rigor** while optimizing visuals

### What the Agent CANNOT Do

❌ Render videos (you must run `manim` command yourself)
❌ Edit rendered video files
❌ Create audio or voiceovers
❌ Access external APIs beyond Wikipedia, Brilliant, ProofWiki
❌ Make value judgments about what math to teach
❌ Guarantee that animations will be pedagogically perfect without iteration

---

## 🛠️ Technical Details

### Agent Configuration

**Name**: `manim-animator`
**Model**: `claude-sonnet-4-5` (high capability for complex reasoning)
**Tools**: `[read, write, execute, grep, glob]`

### Skills Used

1. **math-research** - Accessed automatically for:
   - Mathematical concept research
   - Animation planning
   - Report generation
   - Accuracy verification

2. **manim-coding** - Accessed automatically for:
   - Syntax reference
   - Code implementation
   - Debugging
   - Style changes

### File Organization

The agent creates and uses these files/directories:

```
project/
├── research-reports/              # Research reports
│   ├── research-derivatives-2025-11-26.md
│   ├── research-integrals-2025-11-26.md
│   └── ...
│
├── [topic]_animation.py          # Individual animations
├── [topic]_complete.py           # Composed animations
└── media/                        # Rendered outputs (created by Manim)
```

---

## 📊 Workflow Decision Tree

The agent uses this logic to determine which workflow to execute:

```
User Request
│
├─ Contains "create", "make", "animate [concept]"
│  AND no existing code?
│  └─> WORKFLOW 1: Holistic Scene Generation
│
├─ Contains "change", "modify", "adjust", "make [style change]"
│  AND existing code?
│  └─> WORKFLOW 2: Stylistic Refinement
│
├─ Contains "combine", "merge", "series", "multiple scenes"?
│  └─> WORKFLOW 3: Multi-Scene Composition
│
└─ Contains "review", "analyze", "explain", "is this correct"
   AND existing code?
   └─> WORKFLOW 4: Mathematical Interpretation
```

---

## 💡 Best Practices

### Getting the Best Results

1. **Be Specific**: "Create an animation showing derivatives as slopes" is better than "make a calculus video"

2. **Specify Audience**: "For high school students" vs "For graduate math students" will change the approach

3. **Indicate Preferences**: "I prefer rigorous proofs" vs "I want intuitive explanations"

4. **Iterate**: Start simple, then request refinements

5. **Provide Context**: If combining scenes, explain the narrative you want

### Common Patterns

**Pattern 1: Research First, Implement Later**
```
Request 1: "Research Taylor series and create a detailed plan"
[Review plan]
Request 2: "Now implement Scene 1 and 2 from the plan"
```

**Pattern 2: Quick Prototype, Then Refine**
```
Request 1: "Create a basic derivative animation"
[Review output]
Request 2: "Add epsilon-delta visualization"
Request 3: "Make it more colorful and slower"
```

**Pattern 3: Build a Series**
```
Request 1: "Create Scene 1 of a calculus series: What is a derivative?"
Request 2: "Create Scene 2: The limit definition"
Request 3: "Create Scene 3: Common derivatives"
Request 4: "Combine all three with transitions"
```

---

## 🐛 Troubleshooting

### Agent Not Using Expected Workflow

**Issue**: Agent is researching when you wanted code changes
**Solution**: Be explicit: "Don't research, just modify the existing code to use blue colors"

### Mathematical Errors in Output

**Issue**: Animation shows incorrect math
**Solution**: Request review: "Review the mathematical accuracy of this animation"

### Animation Too Complex/Simple

**Issue**: Not matching desired level
**Solution**: Specify: "Make this suitable for high school students" or "Add rigorous epsilon-delta proof"

### Transitions Not Smooth

**Issue**: Scenes don't flow well together
**Solution**: Request: "Add smooth transitions between scenes 2 and 3" or use Workflow 3

---

## 📚 Example Projects

### Project 1: Complete Calculus Course

**Goal**: 10-video series covering calculus fundamentals

**Approach**:
1. Plan the curriculum (10 topics)
2. For each topic:
   - Use Workflow 1 to create animation
   - Use Workflow 2 to refine styling
3. Use Workflow 3 to create:
   - Series intro
   - Topic-to-topic transitions
   - Series conclusion

**Result**: Consistent, comprehensive calculus course

### Project 2: Single Deep-Dive Video

**Goal**: 10-minute video on Fourier transforms

**Approach**:
1. Use Workflow 1 to generate initial animation
2. Use Workflow 4 to review and identify gaps
3. Use Workflow 1 to fill gaps
4. Use Workflow 2 to perfect styling
5. Use Workflow 3 to combine all parts

**Result**: Polished, in-depth explanation

### Project 3: Style-Consistent Multi-Topic Animation

**Goal**: 5 different topics with unified visual style

**Approach**:
1. Define style guide (colors, fonts, pacing)
2. Use Workflow 1 for first topic
3. Use Workflow 2 to establish style
4. For remaining topics:
   - Use Workflow 1 for content
   - Use Workflow 2 to match established style
5. Use Workflow 3 to combine

**Result**: Professional-looking series with brand consistency

---

## 🎓 Learning the Agent

### Beginner Path

**Week 1**: Simple single-scene animations
```
"Create an animation showing the Pythagorean theorem"
"Create an animation explaining what derivatives are"
```

**Week 2**: Refinements and improvements
```
"Make the Pythagorean animation use bright colors"
"Add more examples to the derivative animation"
```

**Week 3**: Multi-scene projects
```
"Create a 3-scene animation: intro, derivation, examples"
```

**Week 4**: Complete workflows
```
"Create a complete explanation of integrals with 5 scenes, then refine the styling"
```

### Advanced Usage

- **Custom workflows**: Chain multiple workflow types
- **Style templates**: Create reusable style guides
- **Series production**: Plan and execute multi-video projects
- **Code reviews**: Use Workflow 4 to improve existing work

---

## 🔗 Integration with Skills

The agent seamlessly integrates both skills:

| Workflow | Primary Skill | Secondary Skill | Integration Point |
|----------|--------------|-----------------|-------------------|
| Holistic Generation | math-research | manim-coding | Research → Plan → Implement |
| Stylistic Refinement | manim-coding | - | Syntax reference → Implementation |
| Multi-Scene Composition | Both equally | - | Research gaps → Implement → Compose |
| Mathematical Interpretation | math-research | manim-coding | Analyze → Research → Suggest → Implement |

---

## ✅ Quality Checklist

When the agent completes work, verify:

- [ ] Mathematical accuracy (formulas, concepts correct)
- [ ] Visual clarity (easy to understand)
- [ ] Code quality (readable, well-commented)
- [ ] Proper pacing (not too fast or slow)
- [ ] Consistent styling (colors, fonts match)
- [ ] Smooth transitions (between scenes)
- [ ] Educational value (teaches effectively)
- [ ] Technical correctness (code runs without errors)

---

## 📞 Getting Help

### Agent-Specific Issues
Ask the agent directly:
- "Explain your workflow selection"
- "Why did you choose this approach?"
- "What other options do I have?"

### Skill-Specific Issues
Consult the skill documentation:
- `skills/math-research/README.md`
- `skills/manim-coding/README.md`

### General Manim Help
- Official docs: https://docs.manim.community/
- Discord: https://discord.gg/mMRrZQW

---

**Ready to create beautiful mathematical animations!** 🎬✨

To get started: `/agent manim-animator` then describe what you want to create!
