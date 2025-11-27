# Manim Agent Skills

This directory contains specialized skills for the Manim Agent plugin, enabling comprehensive mathematical animation creation from research to implementation.

## 📦 Available Skills

### 1. 🎨 manim-coding
**Purpose**: Expert knowledge of Manim Community Edition syntax and implementation

**What it does**:
- Provides comprehensive Manim syntax reference
- Offers code examples and patterns
- Supplies implementation guidance
- Helps with debugging and troubleshooting

**When activated**: When writing Manim code, asking about Manim syntax, or working with mathematical visualizations

**Key files**:
- `SKILL.md` - Complete reference organized by frequency of use
- `quick-reference.md` - Compact cheat sheet
- `syntax-by-category.md` - Full syntax by category
- `examples.py` - 15+ runnable code examples

[📖 Full Documentation](manim-coding/README.md)

---

### 2. 🔬 math-research
**Purpose**: Research mathematical concepts and plan Manim animations

**What it does**:
- Looks up math content from Wikipedia, Brilliant.org, ProofWiki
- Synthesizes information from multiple sources
- Identifies visual elements for animation
- Creates detailed scene-by-scene animation plans
- Writes comprehensive markdown reports

**When activated**: When researching mathematical topics, planning visualizations, or exploring math concepts

**Key files**:
- `SKILL.md` - Complete research methodology and report template
- `report-template.md` - Blank template for reports
- `example-pythagorean-theorem.md` - Complete example report
- `research-process.md` - Quick reference guide

[📖 Full Documentation](math-research/README.md)

---

## 🔄 How Skills Work Together

These skills are designed to work as a complete workflow:

### End-to-End Workflow

```
1. RESEARCH (math-research skill)
   ↓
   User: "Research the Fourier transform and plan an animation"
   ↓
   Claude:
   - Fetches content from Wikipedia, Brilliant.org
   - Synthesizes mathematical concepts
   - Identifies visual elements
   - Plans 5 detailed scenes
   - Writes comprehensive report
   - Saves: research-reports/research-fourier-transform-2025-11-26.md

2. IMPLEMENTATION (manim-coding skill)
   ↓
   User: "Implement Scene 1 from the Fourier transform plan"
   ↓
   Claude:
   - Reads the animation plan from report
   - Uses manim-coding syntax reference
   - Writes Manim code implementing Scene 1
   - Provides proper syntax and patterns

3. ITERATION
   ↓
   User: "This scene is too complex, simplify it"
   ↓
   Claude:
   - Uses both skills together
   - Revises plan (math-research)
   - Updates code (manim-coding)
   - Iterates until perfect
```

### Skill Interaction Example

```python
# User asks a question
"Explain derivatives and create an animation"

# Claude activates BOTH skills:

# 1. math-research skill:
#    - Researches derivatives from sources
#    - Plans animation showing limit definition
#    - Creates detailed report

# 2. manim-coding skill:
#    - Provides syntax for implementation
#    - Shows how to animate limits
#    - Gives code examples

# Result: Complete solution from concept to code
```

---

## 🎯 When to Use Each Skill

### Use `math-research` when you want to:
- 📚 Understand a mathematical concept before animating
- 🔍 Look up definitions, theorems, or proofs
- 🎨 Plan how to visualize abstract math
- 📝 Create comprehensive animation plans
- 💡 Identify "aha!" moments for teaching
- 📊 Research examples and applications

**Trigger words**: "research", "look up", "plan animation", "what is", "explain concept"

### Use `manim-coding` when you want to:
- 💻 Write Manim code
- 🔧 Look up syntax for specific animations
- 🐛 Debug Manim scripts
- 📖 Find code examples
- ⚙️ Understand Manim features
- 🎬 Implement animations

**Trigger words**: "write code", "implement", "how to animate", "manim syntax", "create scene"

### Use BOTH when you want to:
- 🚀 Complete projects from research to implementation
- 🎓 Create educational mathematical content
- 📹 Produce high-quality math animations
- 🔄 Iterate between planning and coding

---

## 📂 Directory Structure

```
skills/
├── README.md                          # This file
│
├── manim-coding/                      # Coding skill
│   ├── README.md                      # Skill overview
│   ├── SKILL.md                       # Main reference (3 sections by frequency)
│   ├── quick-reference.md             # Cheat sheet
│   ├── syntax-by-category.md          # Complete syntax reference
│   └── examples.py                    # Runnable code examples
│
└── math-research/                     # Research skill
    ├── README.md                      # Skill overview
    ├── SKILL.md                       # Research methodology & template
    ├── report-template.md             # Blank template
    ├── example-pythagorean-theorem.md # Example report
    └── research-process.md            # Quick reference guide
```

---

## 🚀 Quick Start Guide

### For Beginners

**Step 1**: Start with a simple topic
```
"Research the Pythagorean theorem and plan an animation"
```
→ Claude uses `math-research` skill to create comprehensive plan

**Step 2**: Implement one scene at a time
```
"Implement Scene 1 from the plan"
```
→ Claude uses `manim-coding` skill to write code

**Step 3**: Test and iterate
```
"Make the animation slower"
"Add more colors"
"Explain this part more clearly"
```
→ Claude uses both skills to refine

### For Advanced Users

**Direct approach**: Combine research and implementation
```
"Research Taylor series and implement the first two scenes showing polynomial approximation"
```
→ Claude uses `math-research` to plan, then `manim-coding` to implement

**Iterative approach**: Deep dive on complex topics
```
1. "Research epsilon-delta definition of limits"
2. "Plan a 7-scene animation with progressive difficulty"
3. "Implement Scene 1 (introduction)"
4. "Implement Scene 2 (epsilon band visualization)"
... continue scene by scene
```

---

## 📊 Skill Capabilities

### math-research Capabilities

✅ **Can Do**:
- Research mathematical concepts from authoritative sources
- Create detailed animation plans
- Identify visual elements
- Write comprehensive reports
- Plan scene-by-scene narratives
- Estimate implementation difficulty
- Suggest Manim approaches
- Note common misconceptions
- Provide concrete examples

❌ **Cannot Do**:
- Write actual Manim code
- Implement animations
- Debug code
- Test or render videos

### manim-coding Capabilities

✅ **Can Do**:
- Provide Manim syntax and examples
- Write complete Manim scenes
- Explain how animations work
- Debug Manim code
- Suggest best practices
- Show multiple implementation approaches
- Optimize code
- Provide runnable examples

❌ **Cannot Do**:
- Research mathematical concepts (use math-research for this)
- Create animation plans (use math-research for this)
- Look up theorem proofs (use math-research for this)

---

## 💡 Example Use Cases

### Educational Content Creation

**Scenario**: Create a series on calculus fundamentals

```
1. "Research limits and plan 5 animations"
2. "Research derivatives and plan animations"
3. "Research integrals and plan animations"
4. "Implement all scenes for the limits series"
5. "Implement all scenes for derivatives"
6. "Implement all scenes for integrals"
```

### Thesis/Presentation Visualization

**Scenario**: Visualize research findings

```
1. "Research [specific theorem] and plan a rigorous proof animation"
2. "Create a visual explanation suitable for non-experts"
3. "Implement both versions"
4. "Refine based on feedback"
```

### Self-Learning

**Scenario**: Understand difficult math concept

```
1. "I don't understand [concept], research it and create a simple animation plan"
2. "Implement the simplest scene to help me understand"
3. "Now show me a more complex example"
```

---

## 🎓 Learning Path

### Phase 1: Foundations (Week 1-2)
**Goal**: Learn basic workflow

1. Use `math-research` on basic topics (Pythagorean theorem, area formulas)
2. Use `manim-coding` to implement simple shapes and animations
3. Practice the research → plan → implement workflow

**Topics to try**:
- Pythagorean theorem
- Quadratic formula
- Circle properties
- Basic trigonometry

### Phase 2: Intermediate (Week 3-4)
**Goal**: Handle more complex visualizations

1. Research intermediate calculus topics
2. Implement animations with graphs and transformations
3. Use updaters and advanced features

**Topics to try**:
- Derivatives (limit definition)
- Integration (area under curve)
- Fourier series
- Matrix transformations

### Phase 3: Advanced (Week 5+)
**Goal**: Master complex mathematical animations

1. Research advanced topics with formal proofs
2. Create multi-scene narrative animations
3. Implement custom animations and complex visuals

**Topics to try**:
- Epsilon-delta proofs
- Abstract algebra concepts
- 3D calculus visualizations
- Complex analysis

---

## 🔧 Tips and Best Practices

### General Tips
1. **Start simple**: Research basic topics first to understand the workflow
2. **One scene at a time**: Don't try to implement everything at once
3. **Iterate**: Refine plans based on implementation challenges
4. **Use both skills**: Research plans what to do, coding shows how to do it
5. **Save reports**: Build a library of animation plans for future reference

### Research Tips
1. Check multiple sources for accuracy
2. Look for visual diagrams in source materials
3. Include concrete examples in plans
4. Estimate difficulty realistically
5. Note common misconceptions

### Coding Tips
1. Test each scene before moving to the next
2. Use the quick-reference for common patterns
3. Start with low quality renders (`manim -pql`) for speed
4. Refer to examples.py for code patterns
5. Use proper LaTeX notation in MathTex

---

## 📚 Additional Resources

### Manim Resources
- **Official Docs**: https://docs.manim.community/en/stable/
- **Example Gallery**: https://docs.manim.community/en/stable/examples.html
- **Discord**: https://discord.gg/mMRrZQW
- **Online Editor**: https://try.manim.community/

### Math Resources
- **Wikipedia Math Portal**: https://en.wikipedia.org/wiki/Portal:Mathematics
- **Brilliant.org**: https://brilliant.org/
- **ProofWiki**: https://proofwiki.org/
- **Khan Academy**: https://www.khanacademy.org/

### Inspiration
- **3Blue1Brown**: https://www.youtube.com/c/3blue1brown (Original Manim creator)
- **Manim Community Showcase**: Amazing animations from the community

---

## 🆘 Troubleshooting

### "Claude isn't using the skill I want"

**Solution**: Be explicit in your request
- For research: Use "research", "look up", "plan animation"
- For coding: Use "implement", "write code", "create scene"

### "The animation plan is too complex"

**Solution**: Ask for simplification
```
"Simplify the plan to 3 scenes"
"Make it suitable for beginners"
"Focus on the core concept only"
```

### "The code isn't working"

**Solution**: Provide error details
```
"This code gives error: [paste error]"
"How do I fix this positioning issue?"
"The animation is too fast, how to slow it down?"
```

### "I don't understand the math"

**Solution**: Ask for clarification
```
"Explain [concept] in simpler terms"
"What are the prerequisites for understanding this?"
"Show me a concrete example"
```

---

## 📈 Version Info

**Skills Version**: 1.0.0
**Manim Version**: Community Edition v0.19.0+
**Last Updated**: 2025-11-26

---

## 🤝 Skill Interaction Matrix

| Task | math-research | manim-coding | Both |
|------|--------------|--------------|------|
| Look up theorem | ✅ | ❌ | |
| Plan animation | ✅ | ❌ | |
| Write code | ❌ | ✅ | |
| Debug code | ❌ | ✅ | |
| Find examples | ✅ | ✅ | ✅ |
| Full project | | | ✅ |
| Understand concept | ✅ | | |
| Implement scene | | ✅ | |
| Iterate design | | | ✅ |

---

**Ready to create amazing mathematical animations!** 🎬✨

Start with: `"Research [your favorite math topic] and plan an animation"`
