# Math Research Skill

This skill enables Claude to research mathematical concepts from authoritative online sources and create comprehensive reports with detailed Manim animation plans.

## 🎯 Purpose

**This skill is for RESEARCH and PLANNING only - it does NOT write code.**

The math-research skill:
1. 📚 Looks up mathematical concepts from Wikipedia, Brilliant.org, and ProofWiki
2. 🔍 Synthesizes information from multiple sources
3. 🎨 Identifies visual elements for animation
4. 📝 Creates detailed Manim animation plans
5. 💾 Writes comprehensive markdown reports

## 📁 Files in This Skill

### `SKILL.md` (Main Skill Definition)
The complete skill specification including:
- When and how to use each research source
- Guidelines for determining math complexity
- Systematic research process
- Comprehensive report template
- Best practices for research and planning

### `report-template.md`
A blank template ready to be filled out for any mathematical topic. Contains all sections with placeholder text and instructions.

### `example-pythagorean-theorem.md`
A complete example report showing exactly what a finished research document looks like. Demonstrates:
- How to research a topic (Pythagorean theorem)
- How to plan a multi-scene animation
- How to identify visual elements
- How to structure implementation notes

## 🌐 Research Sources

### 1. Wikipedia (Always Use First)
- **URL Pattern**: `https://en.wikipedia.org/wiki/[Topic_Name]`
- **Use For**: All topics (basic to advanced)
- **Provides**: Definitions, formulas, context, diagrams

### 2. Brilliant.org (Use for Intuition)
- **URL Pattern**: `https://brilliant.org/wiki/[topic-name]/`
- **Use For**: Intuitive explanations, visual understanding
- **Provides**: Step-by-step explanations, problem-solving approaches

### 3. ProofWiki (Advanced Topics Only)
- **URL Pattern**: `https://proofwiki.org/wiki/[Topic_Name]`
- **Use For**: Graduate-level math, formal proofs
- **Provides**: Rigorous proofs, formal definitions

## 🎓 Topic Complexity Guide

### Basic Topics (Wikipedia + Brilliant)
- Arithmetic, basic algebra, geometry
- Introductory trigonometry and calculus
- Simple probability and statistics
- Basic matrix operations

### Intermediate Topics (Wikipedia + Brilliant)
- Differential equations
- Multivariable calculus
- Linear algebra (eigenvalues, transformations)
- Fourier series

### Advanced Topics (Wikipedia + Brilliant + ProofWiki)
- Real/complex analysis
- Abstract algebra
- Topology
- Measure theory
- Functional analysis
- Category theory

## 🚀 How to Use This Skill

### Trigger Phrases

Claude will automatically activate this skill when you say:
- "Look up [mathematical topic]"
- "Research [concept] and plan an animation"
- "What is [math term]? Plan a visualization"
- "Create an animation plan for [theorem]"
- "Explain [topic] and how to animate it"

### Example Requests

**Good requests** (specific and clear):
```
"Research the Fourier transform and create an animation plan"
"Look up the epsilon-delta definition of limits and plan a visual explanation"
"What is the Taylor series? Plan an animation showing convergence"
"Research derivatives and plan a beginner-friendly visualization"
```

**Requests needing clarification**:
```
"Tell me about math" - Too vague
"Make an animation" - Need specific topic
"Explain calculus" - Too broad, need subtopic
```

## 📋 Report Structure

Every research report includes 13 sections:

1. **Overview** - Brief summary
2. **Mathematical Definition** - Formal and intuitive explanations
3. **Key Concepts and Properties** - Core ideas
4. **Notation and Formulas** - LaTeX formulas
5. **Visual Elements** - What to animate
6. **Concrete Examples** - Specific cases
7. **Manim Animation Plan** - Detailed scene-by-scene plan
8. **Key "Aha!" Moments** - Educational insights
9. **Common Misconceptions** - What students get wrong
10. **Extensions** - Related topics
11. **Sources** - Full citations
12. **Implementation Notes** - Difficulty, time estimates
13. **Summary** - Comprehensive wrap-up

## 🎬 Animation Planning Features

Each report includes detailed animation plans with:

### Scene-by-Scene Breakdown
- Duration estimates
- Objectives for each scene
- Visual elements needed
- Step-by-step animations
- Pseudocode/implementation hints

### Technical Specifications
- Required Manim classes
- Coordinate systems needed
- Color schemes
- Timing considerations
- Camera positioning

### Implementation Guidance
- Estimated difficulty level
- Time to implement
- Recommended development order
- Potential challenges and solutions
- Testing strategies

## 💡 Output Format

### File Naming
Reports are saved as: `research-[topic-name]-[YYYY-MM-DD].md`

Examples:
- `research-fourier-transform-2025-11-26.md`
- `research-taylor-series-2025-11-26.md`
- `research-matrix-multiplication-2025-11-26.md`

### File Location
Reports are saved in: `research-reports/` directory (created if needed)

## 🔄 Workflow Integration

This skill works seamlessly with the **manim-coding** skill:

1. **Step 1**: Use `math-research` to look up a topic and create a plan
   - Generates comprehensive report with animation plan

2. **Step 2**: Use `manim-coding` to implement the plan
   - Provides syntax and code examples for Manim

3. **Step 3**: Iterate and refine
   - Adjust plan based on implementation challenges
   - Update report with lessons learned

## 📊 Example Workflow

```
User: "Research the limit definition and plan an animation"

Claude (math-research skill):
1. Fetches from Wikipedia: formal epsilon-delta definition
2. Fetches from Brilliant: intuitive explanation
3. Synthesizes information
4. Identifies visual elements (graphs, epsilon/delta bands)
5. Plans 5-scene animation
6. Writes comprehensive report
7. Saves to: research-reports/research-limit-definition-2025-11-26.md

User: "Now implement Scene 1 from the plan"

Claude (manim-coding skill):
1. Reads the animation plan from report
2. Provides Manim code for Scene 1
3. Uses proper syntax from manim-coding skill
4. Implements the planned visualization
```

## ✅ Best Practices

### When Researching
1. ✅ Always check multiple sources
2. ✅ Verify mathematical accuracy
3. ✅ Look for visual diagrams in sources
4. ✅ Note both formal and intuitive explanations
5. ✅ Include concrete examples

### When Planning Animations
1. ✅ Think pedagogically (how would a teacher explain this?)
2. ✅ Build incrementally (simple → complex)
3. ✅ Use concrete examples before abstractions
4. ✅ Plan for "aha!" moments
5. ✅ Consider timing and pacing
6. ✅ Use color meaningfully
7. ✅ Test ideas mentally before writing

### When Writing Reports
1. ✅ Be comprehensive and detailed
2. ✅ Use proper LaTeX notation
3. ✅ Include specific Manim classes to use
4. ✅ Think about narrative flow
5. ✅ Identify implementation challenges
6. ✅ Provide multiple concrete examples
7. ✅ Cite all sources with full URLs

## ⚠️ Important Notes

### What This Skill Does
- ✅ Researches mathematical concepts
- ✅ Creates detailed animation plans
- ✅ Writes comprehensive reports
- ✅ Identifies visual elements
- ✅ Suggests Manim approaches

### What This Skill Does NOT Do
- ❌ Write actual Manim code
- ❌ Implement animations
- ❌ Test or debug code
- ❌ Render videos

For code implementation, use the **manim-coding** skill.

## 📚 Example Topics to Research

### Calculus
- Limits and continuity
- Derivatives (geometric interpretation)
- Integrals (area under curve)
- Fundamental theorem of calculus
- Taylor series
- L'Hôpital's rule

### Linear Algebra
- Matrix multiplication
- Determinants
- Eigenvalues and eigenvectors
- Linear transformations
- Vector spaces

### Geometry
- Pythagorean theorem
- Circle theorems
- Conic sections
- Geometric transformations
- Geometric proofs

### Advanced Topics
- Fourier transform
- Laplace transform
- Green's theorem
- Stokes' theorem
- Group theory basics

## 🎯 Quality Indicators

A good research report should:
- ✅ Have clear, accurate mathematical definitions
- ✅ Include 3+ concrete examples
- ✅ Identify specific visual elements
- ✅ Provide scene-by-scene animation plans
- ✅ Include pseudocode/implementation hints
- ✅ Cite all sources with full URLs
- ✅ Note potential challenges
- ✅ Estimate implementation difficulty and time
- ✅ Be ready for someone to implement without asking questions

## 🔗 Related Resources

- **Manim Documentation**: https://docs.manim.community/en/stable/
- **Wikipedia Math Portal**: https://en.wikipedia.org/wiki/Portal:Mathematics
- **Brilliant.org**: https://brilliant.org/
- **ProofWiki**: https://proofwiki.org/

## 💬 Getting Help

If the skill needs clarification on:
- Topic scope → Ask for more specific subtopic
- Complexity level → Ask if basic, intermediate, or advanced
- Animation style → Ask for preferences (rigorous vs. intuitive)
- Audience → Ask about target education level

## 📝 Version Info

This skill is designed to work with:
- **Manim Community Edition**: v0.19.0+
- **Wikipedia**: Current version (continuously updated)
- **Brilliant.org**: Current version
- **ProofWiki**: Current version

---

**Last Updated**: 2025-11-26
**Skill Version**: 1.0.0
**Complements**: manim-coding skill
