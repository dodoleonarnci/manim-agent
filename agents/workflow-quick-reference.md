# Manim Animator Workflow Quick Reference

A quick guide to using the manim-animator agent for different tasks.

---

## 🚀 Quick Start

```bash
# Activate the agent
/agent manim-animator

# Then make your request!
```

---

## 📋 Four Workflows at a Glance

| Workflow | When to Use | Example Request | What You Get |
|----------|-------------|----------------|--------------|
| **Holistic Scene Generation** | Starting fresh | "Create animation explaining derivatives" | Research report + Complete code |
| **Stylistic Refinement** | Improving visuals | "Make this more colorful and slower" | Modified code with new styling |
| **Multi-Scene Composition** | Combining work | "Combine scenes into one video" | Unified animation with transitions |
| **Mathematical Interpretation** | Code review | "Is this animation accurate?" | Analysis + Improvement suggestions |

---

## 🔄 Workflow 1: Holistic Scene Generation

### Use When:
- Starting a new animation project
- Need both research and implementation
- Want complete solution from concept to code

### Example Requests:
```
"Create an animation explaining the Pythagorean theorem"
"Visualize Fourier transforms"
"Make a video about Taylor series"
"Animate the concept of derivatives"
```

### What Happens:
1. ✅ Researches concept from Wikipedia, Brilliant, ProofWiki
2. ✅ Creates detailed animation plan (5-7 scenes)
3. ✅ Writes comprehensive research report
4. ✅ Implements each scene in Manim
5. ✅ Tests and delivers complete animation

### You Receive:
- Research report in `research-reports/`
- Complete Python file with all scenes
- Ready-to-render animation

### Typical Duration:
- Simple topic: 5-10 minutes
- Complex topic: 15-30 minutes

---

## 🎨 Workflow 2: Stylistic Refinement

### Use When:
- Have existing code
- Want to change colors, timing, emphasis
- Need visual improvements without changing content

### Example Requests:
```
"Make the colors more vibrant"
"Slow down the transformation by 50%"
"Use blue gradient instead of solid color"
"Add emphasis animation to the main formula"
"Make text larger and easier to read"
"Change background to dark mode"
```

### What Happens:
1. ✅ Reads and analyzes existing code
2. ✅ Plans specific visual modifications
3. ✅ Implements changes using Manim syntax
4. ✅ Tests to verify improvements
5. ✅ Maintains mathematical accuracy

### You Receive:
- Modified code with new styling
- Explanation of what was changed

### Typical Duration:
- Simple changes: 1-3 minutes
- Complex restyling: 5-10 minutes

---

## 🎬 Workflow 3: Multi-Scene Composition

### Use When:
- Combining multiple animations
- Creating series or courses
- Building narrative flow across scenes
- Need transitions between topics

### Example Requests:
```
"Combine my derivative and integral animations"
"Create a 5-part calculus series"
"Link scenes 1, 2, and 3 with smooth transitions"
"Make a complete video from these three topics"
```

### What Happens:
1. ✅ Inventories existing scenes
2. ✅ Plans narrative structure and flow
3. ✅ Researches and creates missing pieces
4. ✅ Implements transitions and title cards
5. ✅ Ensures style consistency across all parts
6. ✅ Delivers unified animation

### You Receive:
- New combined Python file
- All scenes integrated with transitions
- Consistent styling throughout
- Optional: New research reports for missing pieces

### Typical Duration:
- Simple combination: 5-10 minutes
- Complex series: 20-40 minutes

---

## 🔍 Workflow 4: Mathematical Interpretation

### Use When:
- Reviewing existing animation code
- Verifying mathematical accuracy
- Seeking improvement suggestions
- Understanding what code does

### Example Requests:
```
"Is this animation mathematically correct?"
"What does this scene demonstrate?"
"How can I improve this explanation?"
"Review this code and suggest changes"
"Does this clearly show the concept?"
```

### What Happens:
1. ✅ Reads and analyzes code
2. ✅ Researches the mathematical concept
3. ✅ Verifies accuracy and completeness
4. ✅ Identifies strengths and weaknesses
5. ✅ Suggests improvements (math, visual, pedagogical)
6. ✅ Optionally implements improvements

### You Receive:
- Detailed analysis report
- Mathematical verification
- Improvement suggestions
- Optional: Improved code

### Typical Duration:
- Analysis only: 3-5 minutes
- With improvements: 10-20 minutes

---

## 🎯 Request Patterns

### Pattern 1: Complete Project (Workflow 1)
```
Request: "Create an animation explaining [concept]"

Agent executes:
1. Research → 2. Plan → 3. Implement → 4. Deliver

You get: Research report + Complete code
```

### Pattern 2: Iterative Improvement (Workflows 1 → 2)
```
Request 1: "Create basic derivative animation"
Request 2: "Make it more colorful"
Request 3: "Add more examples"

Agent executes:
1. Workflow 1 (generate)
2. Workflow 2 (refine colors)
3. Workflow 2 (add content)

You get: Polished animation after iterations
```

### Pattern 3: Series Production (Workflows 1 → 3)
```
Request 1: "Create animation on derivatives"
Request 2: "Create animation on integrals"
Request 3: "Combine them into one video"

Agent executes:
1. Workflow 1 (derivatives)
2. Workflow 1 (integrals)
3. Workflow 3 (combine)

You get: Unified multi-topic animation
```

### Pattern 4: Review and Improve (Workflow 4 → 2)
```
Request 1: "Review this animation code"
Request 2: "Implement your suggested improvements"

Agent executes:
1. Workflow 4 (analyze and suggest)
2. Workflow 2 (implement changes)

You get: Improved, reviewed animation
```

---

## 💬 Phrasing Tips

### For Holistic Generation (Workflow 1):
✅ "Create animation showing..."
✅ "Visualize [concept]"
✅ "Make a video about..."
✅ "Animate [mathematical topic]"

❌ Don't say: "Change the code" (existing code = Workflow 2)

### For Stylistic Refinement (Workflow 2):
✅ "Make this [style change]"
✅ "Change colors to..."
✅ "Slow down the animation"
✅ "Add emphasis on..."

❌ Don't say: "Create animation" (new = Workflow 1)

### For Multi-Scene Composition (Workflow 3):
✅ "Combine [scenes/files]"
✅ "Create a series with..."
✅ "Link these animations"
✅ "Make one video from..."

❌ Don't say: "Create separate animations" (separate = Workflow 1)

### For Mathematical Interpretation (Workflow 4):
✅ "Is this correct?"
✅ "Review this code"
✅ "What does this show?"
✅ "How can I improve..."

❌ Don't say: "Make this from scratch" (new = Workflow 1)

---

## 🔧 Workflow Modifiers

Add these to your requests to modify behavior:

### Audience Level:
- "...for high school students"
- "...for undergraduate math majors"
- "...for graduate students"
- "...for general audience"

### Style Preferences:
- "...with rigorous proofs"
- "...with intuitive explanations"
- "...using bright colors"
- "...in dark mode"

### Pacing:
- "...keep it short (under 1 minute)"
- "...detailed and thorough"
- "...quick overview"

### Scope:
- "...just the basic concept"
- "...include advanced applications"
- "...show multiple examples"

---

## 📊 Workflow Selection Logic

```
Your Request
│
├─ Has existing code? ─── NO ──> WORKFLOW 1 (Generate)
│   │
│   └─── YES ─┬─> Want to analyze/review? ──> WORKFLOW 4 (Interpret)
│             │
│             └─> Want style changes? ──> WORKFLOW 2 (Refine)
│
└─ Want to combine multiple? ──> WORKFLOW 3 (Compose)
```

---

## ⚡ Speed Tips

### Fastest Workflow: Stylistic Refinement (1-3 min)
Request: "Make this blue instead of red"

### Quick Workflow: Holistic Generation for Simple Topics (5-10 min)
Request: "Create animation showing 3-4-5 triangle"

### Moderate Workflow: Interpretation + Improvement (10-20 min)
Request: "Review and improve this animation"

### Longer Workflow: Multi-Scene Composition (20-40 min)
Request: "Create complete calculus series with 5 topics"

---

## ✅ Checklist for Success

Before requesting, clarify:

- [ ] Do I have existing code? (Yes → Workflow 2 or 4, No → Workflow 1)
- [ ] Am I combining multiple things? (Yes → Workflow 3)
- [ ] What audience level? (High school, undergrad, etc.)
- [ ] What style preferences? (Rigorous, intuitive, etc.)
- [ ] What scope? (Basic, detailed, examples, etc.)

After receiving output, verify:

- [ ] Mathematics is accurate
- [ ] Visual clarity is good
- [ ] Pacing feels right
- [ ] Code runs without errors
- [ ] Meets my original goal

---

## 🎓 Example Conversations

### Beginner Request:
```
YOU: "Create an animation explaining what a derivative is"

AGENT: [Workflow 1 - Holistic Generation]
- Researches derivatives
- Plans 5 scenes
- Implements complete animation
- Delivers code + research report

YOU: "That's great! Now make it more colorful"

AGENT: [Workflow 2 - Stylistic Refinement]
- Updates color scheme
- Tests changes
- Delivers modified code
```

### Intermediate Request:
```
YOU: "I have this derivative code. Is it mathematically accurate?"

AGENT: [Workflow 4 - Mathematical Interpretation]
- Analyzes code
- Verifies mathematics
- Identifies improvements
- Suggests changes

YOU: "Implement your suggestions"

AGENT: [Workflow 2 - Stylistic Refinement]
- Applies improvements
- Tests enhanced version
- Delivers improved code
```

### Advanced Request:
```
YOU: "Create a 3-part calculus introduction: derivatives, integrals, and the fundamental theorem"

AGENT: [Workflow 1 repeated + Workflow 3]
- Creates derivatives animation
- Creates integrals animation
- Creates FTC animation
- Combines all three with transitions
- Delivers unified series

YOU: "Make the color scheme consistent and add chapter titles"

AGENT: [Workflow 2 - Stylistic Refinement]
- Standardizes colors across all scenes
- Adds title cards
- Tests complete video
- Delivers polished series
```

---

## 🔗 Quick Links

- **Agent Details**: See `agents/manim-animator.md`
- **Full Guide**: See `agents/README.md`
- **Math Research Skill**: See `skills/math-research/`
- **Manim Coding Skill**: See `skills/manim-coding/`

---

## 🆘 Common Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Agent is researching when I wanted quick changes | Request phrased like new project | Say "Don't research, just modify..." |
| Agent made one scene, I wanted multiple | Request wasn't specific | Say "Create 5 scenes showing..." |
| Style isn't consistent across scenes | Multiple separate requests | Use Workflow 3 to unify styling |
| Animation too advanced/simple | Didn't specify audience | Add "for [audience level]" to request |

---

**Remember**: The agent is intelligent - it will choose the right workflow based on your request. Trust it, but guide it with clear, specific requests!

**Start with**: `/agent manim-animator` then describe what you want! 🚀
