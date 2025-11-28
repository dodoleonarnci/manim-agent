---
name: math-research
description: Research mathematical concepts from Wikipedia, Brilliant.org, and ProofWiki to create comprehensive reports and Manim animation plans. Use when exploring mathematical topics, looking up definitions, theorems, or planning mathematical visualizations.
allowed-tools: Read, Write, Grep, Glob, Bash
---

# Mathematical Content Research Skill

This skill specializes in researching mathematical concepts from authoritative sources and creating comprehensive reports with Manim animation plans.

## Purpose

**This skill ONLY does research and planning. It does NOT implement code.**

When activated, this skill will:
1. Look up mathematical content from online sources
2. Synthesize information into clear explanations
3. Create detailed plans for Manim animations
4. Write comprehensive markdown reports

## Project Directory Setup

**IMPORTANT**: Research reports should be saved in the active Manim project directory.

### Directory Structure

When working on a Manim animation project:
- Project directory: `/manim-projects/your-project-name/`
- Research reports: `/manim-projects/your-project-name/research-reports/`

### Setup Before Research

```bash
# Ensure you're in the correct project directory
cd /manim-projects/your-project-name

# Create research-reports subdirectory
mkdir -p research-reports
```

**All research reports MUST be saved in**: `/manim-projects/your-project-name/research-reports/`

## When to Use This Skill

Use this skill when you need to:
- Research a mathematical concept before animating it
- Look up definitions, theorems, or proofs
- Understand the visual structure of mathematical ideas
- Plan how to animate mathematical concepts effectively
- Create educational content about mathematics
- Find authoritative sources for mathematical topics

**Trigger phrases**:
- "Look up [math topic]"
- "Research [mathematical concept]"
- "What is [math term]"
- "How would you visualize [math concept]"
- "Create an animation plan for [theorem]"
- "Explain [mathematical idea] and plan an animation"

---

## Research Sources

### 1. Wikipedia (Primary Source - Always Use First)

**When to use**: For all mathematical topics, from basic to advanced

**IMPORTANT - MediaWiki API Usage**:
⚠️ **DO NOT use direct URL fetching from Wikipedia** - this results in 403 errors.
✅ **USE the MediaWiki API instead**:

```
API Endpoint: https://en.wikipedia.org/w/api.php
Parameters:
  - action=query
  - titles=[Topic_Name]
  - prop=extracts|revisions
  - format=json
  - formatversion=2
  - explaintext=1 (for plain text)
  - rvprop=content (for wikitext if needed)
```

**Example API calls**:
```
https://en.wikipedia.org/w/api.php?action=parse&page=Pythagorean_theorem&format=json
```

**How to fetch**:
Use the Bash tool with curl since WebFetch may return 403 errors with Wikipedia:
```bash
curl -s "https://en.wikipedia.org/w/api.php?action=parse&page=Pythagorean_theorem&format=json&prop=text&formatversion=2"
```

**What to look for**:
- Clear definitions and explanations
- Historical context
- Visual diagrams and illustrations (descriptions)
- Related concepts and applications
- Mathematical notation and formulas
- Examples and special cases
- Construction methods (for geometry)
- Step-by-step procedures

**Early Exit Criteria**:
If the Wikipedia API response is comprehensive (>1000 words, covers key concepts, includes examples), you may **skip additional sources** and proceed directly to planning. This saves time for well-documented topics.

### 2. Brilliant.org (Secondary Source - Use for Intuition)

**When to use**: For intuitive explanations and visual understanding

**What to look for**:
- Intuitive explanations
- Step-by-step breakdowns
- Visual approaches
- Problem-solving strategies
- Interactive concepts

**URLs**:
- `https://brilliant.org/wiki/[topic-name]/`
- Use hyphens, lowercase
- Examples:
  - `https://brilliant.org/wiki/pythagorean-theorem/`
  - `https://brilliant.org/wiki/derivatives/`
  - `https://brilliant.org/wiki/integration-techniques/`

**Note**: Brilliant may not have all topics. If a page doesn't exist, note this in the report and rely more on Wikipedia.

### 3. ProofWiki (Tertiary Source - Advanced Topics Only)

**When to use**: ONLY for advanced mathematical topics that require rigorous proofs

**What to look for**:
- Formal proofs and derivations
- Rigorous mathematical definitions
- Lemmas and corollaries
- Proof structure and logic flow

**URLs**:
- `https://proofwiki.org/wiki/[Topic_Name]`
- Use underscores for spaces
- Examples:
  - `https://proofwiki.org/wiki/Fundamental_Theorem_of_Calculus`
  - `https://proofwiki.org/wiki/Cauchy-Schwarz_Inequality`

**When NOT to use ProofWiki**:
- Basic arithmetic or algebra
- High school level mathematics
- Introductory calculus concepts
- Simple geometric concepts

**When TO use ProofWiki**:
- Real analysis and complex analysis
- Abstract algebra (groups, rings, fields)
- Topology
- Advanced number theory
- Graduate-level mathematics
- When formal proofs are specifically requested

---

## Determining Topic Complexity

Before choosing sources, assess the mathematical level:

### Basic/Introductory Topics (Wikipedia + Brilliant)
- Arithmetic operations
- Basic algebra
- Geometry (shapes, areas, volumes)
- Introductory trigonometry
- Basic calculus (derivatives, integrals)
- Linear equations and inequalities
- Simple probability and statistics
- Basic matrix operations

### Intermediate Topics (Wikipedia + Brilliant)
- Differential equations
- Multivariable calculus
- Linear algebra (eigenvalues, transformations)
- Intermediate probability theory
- Fourier series
- Optimization problems
- Graph theory basics

### Advanced Topics (Wikipedia + Brilliant + ProofWiki)
- Real and complex analysis
- Abstract algebra (group theory, ring theory)
- Topology
- Measure theory
- Functional analysis
- Differential geometry
- Advanced number theory
- Category theory

---

## Research Process

Follow this systematic approach:

### Step 0: Create Research Checklist

**FIRST STEP**: Before any research, create a checklist based on the animation request.

Analyze the user's request and create a task list covering:
- **Core Concept**: What mathematical concept needs to be explained?
- **Visual Elements**: What objects/shapes/graphs are needed?
- **Key Information**: What definitions, formulas, or theorems are essential?
- **Construction Steps** (if applicable): What step-by-step process should be shown?
- **Animation Scenes**: How many scenes are needed? What's the narrative flow?
- **Special Requirements**: Any specific requests (historical context, proofs, examples)?

**Example Checklist** (for "Construct a regular pentagon"):
```
☐ Research pentagon definition and properties
☐ Find compass-and-straightedge construction method
☐ Document each construction step with diagrams
☐ Identify mathematical principles (golden ratio connection)
☐ Plan 5-7 animation scenes showing step-by-step construction
☐ Note visual elements (compass arcs, lines, points, labels)
☐ Determine timing and pacing for each step
```

**Output the checklist** at the start of your research to show the user what you'll be investigating.

### Step 1: Assess Topic Complexity and Research Depth

**IMPORTANT**: Before diving into research, assess how complex the animation request is.

**Minimal Research Required** (5-10 minutes):
- **Simple, well-known concepts** that don't require deep investigation
- Topics you're already familiar with (basic geometry, simple algebra)
- Concepts that can be visualized straightforwardly
- Examples:
  - Basic shapes (circle, square, triangle properties)
  - Simple number patterns
  - Elementary animations (moving objects, fading, scaling)
  - Basic arithmetic visualizations
- **Action**: Skip detailed web research. Use your knowledge to create a brief plan directly. Document key parameters and visual approach only.

**Standard Research Required** (15-30 minutes):
- **Moderate complexity** topics that benefit from authoritative sources
- Topics with multiple visualization approaches
- Concepts that need mathematical accuracy verification
- Examples:
  - Golden ratio, Fibonacci sequence
  - Pythagorean theorem with multiple proofs
  - Derivatives and integrals
  - Trigonometric identities
- **Action**: Research from Wikipedia + Brilliant.org, create structured plan

**Comprehensive Research Required** (30-60 minutes):
- **Advanced or specialized** topics requiring deep investigation
- Topics with rigorous proofs
- Complex multi-part mathematical structures
- Examples:
  - Fourier transforms
  - Group theory visualizations
  - Complex analysis
  - Differential geometry
- **Action**: Full research from all sources including ProofWiki, detailed comprehensive report

### Step 2: Gather Information (Based on Complexity)

**IMPORTANT**: Always use MediaWiki API for Wikipedia, not direct URL fetching!

**For Minimal Research**:
- Use your existing knowledge
- Quick Wikipedia API check if needed (1-2 minutes)
- Focus on visual approach only

**For Standard Research**:
1. **Start with Wikipedia via MediaWiki API** - Get overview, definitions, formulas
   - Use API endpoint: `https://en.wikipedia.org/w/api.php?action=query&titles=[Topic]&prop=extracts&format=json&formatversion=2&explaintext=1`
   - **Early Exit**: If Wikipedia response is comprehensive (>1000 words, covers all checklist items, includes step-by-step methods), **SKIP** Brilliant.org and proceed to Step 3
   - Estimated time: 5-15 min
2. **Check Brilliant.org** (ONLY if Wikipedia was insufficient) - Get intuitive explanations and visual approaches (10-15 min)

**For Comprehensive Research**:
1. **Start with Wikipedia via MediaWiki API** - Get overview, definitions, formulas
   - Same API endpoint as above
   - **Early Exit**: If Wikipedia is comprehensive, you may skip Brilliant.org but still check ProofWiki for formal proofs
   - Estimated time: 10-20 min
2. **Check Brilliant.org** (if needed) - Get intuitive explanations and visual approaches (10-15 min)
3. **Check ProofWiki** - Get rigorous proofs and formal definitions (15-20 min)

**Time-Saving Tip**: Many well-documented topics (geometric constructions, classical theorems, standard algorithms) have excellent Wikipedia coverage. Don't spend extra time on additional sources if Wikipedia provides everything needed.

### Step 3: Synthesize Information
- Extract key concepts and definitions
- Identify visual elements (graphs, diagrams, transformations)
- Note mathematical notation and formulas
- Find concrete examples and special cases
- Identify prerequisite knowledge

### Step 4: Plan Manim Animations
Think about how to visualize the concept:
- What objects need to be shown?
- What transformations demonstrate the concept?
- What is the narrative flow?
- What are the key "aha!" moments?
- How can abstract concepts be made concrete?

### Step 5: Write Comprehensive Report
Create a markdown file with:
- Topic overview and definitions
- Key mathematical concepts
- Visual elements identified
- Detailed Manim animation plan
- Sources and references

---

## Report Template

Use this structure for all research reports:

```markdown
# Mathematical Research Report: [Topic Name]

**Date**: [YYYY-MM-DD]
**Complexity Level**: [Basic / Intermediate / Advanced]
**Research Duration**: [X minutes]

---

## 1. Overview

[Brief 2-3 sentence summary of the mathematical concept]

---

## 2. Mathematical Definition

### Formal Definition
[Precise mathematical definition with proper notation]

### Intuitive Explanation
[Explain in simple terms what the concept means]

### Prerequisites
- [List required background knowledge]
- [Concepts students should know first]

---

## 3. Key Concepts and Properties

### Core Concepts
1. **[Concept 1]**: [Explanation]
2. **[Concept 2]**: [Explanation]
3. **[Concept 3]**: [Explanation]

### Important Properties
- **[Property 1]**: [Description and significance]
- **[Property 2]**: [Description and significance]

### Special Cases
- [Special case 1 and its significance]
- [Special case 2 and its significance]

---

## 4. Mathematical Notation and Formulas

### Primary Formula(s)
```
[Main formula in LaTeX notation]
```

### Related Formulas
```
[Supporting formulas]
```

### Notation Guide
- `[symbol]`: [meaning]
- `[symbol]`: [meaning]

---

## 5. Visual Elements Identified

### Geometric Representations
- [Describe any geometric shapes, regions, or objects]
- [How they relate to the mathematical concept]

### Graphs and Plots
- [Functions to be graphed]
- [Important features of the graphs]
- [Transformations or changes over time]

### Diagrams and Illustrations
- [Conceptual diagrams needed]
- [Flow diagrams or process illustrations]

### Color Coding Strategy
- [What different colors should represent]
- [How to use color to clarify concepts]

---

## 6. Concrete Examples

### Example 1: [Simple Case]
**Setup**: [Describe the example]
**Calculation**: [Show the math]
**Result**: [What it demonstrates]
**Visualization**: [How to show this in Manim]

### Example 2: [Intermediate Case]
[Same structure as Example 1]

### Example 3: [Edge Case or Interesting Case]
[Same structure as Example 1]

---

## 7. Manim Animation Plan

### Animation Structure Overview
[High-level narrative flow of the animation]

### Scene 1: [Introduction/Setup]
**Duration**: ~[X] seconds
**Objective**: [What this scene establishes]

**Visual Elements**:
- [Object 1]: [Description and styling]
- [Object 2]: [Description and styling]

**Animations**:
1. [Animation step 1]
2. [Animation step 2]
3. [Animation step 3]

**Code Approach**:
```
[Pseudocode or high-level description]
- Create objects: Circle(), Axes(), etc.
- Position elements: next_to(), shift()
- Animate: Create(), Transform(), etc.
```

### Scene 2: [Core Concept Demonstration]
[Same structure as Scene 1]

### Scene 3: [Examples/Applications]
[Same structure as Scene 1]

### Scene 4: [Conclusion]
[Same structure as Scene 1]

### Technical Considerations
- **Coordinate System**: [Which axes or plane to use]
- **Camera Positioning**: [Any special camera work needed]
- **Mathematical Functions**: [Key functions to plot]
- **Text/LaTeX**: [Important formulas to display]
- **Timing**: [Pacing considerations]
- **Transitions**: [How scenes connect]

---

## 8. Key "Aha!" Moments

[Identify the moments where understanding clicks]

1. **[Moment 1]**: [What realization] - [How to visualize it]
2. **[Moment 2]**: [What realization] - [How to visualize it]
3. **[Moment 3]**: [What realization] - [How to visualize it]

---

## 9. Common Misconceptions

[What students often get wrong about this topic]

1. **Misconception**: [The wrong belief]
   **Reality**: [The correct understanding]
   **How to address in animation**: [Visualization strategy]

2. [Additional misconceptions...]

---

## 10. Extensions and Related Topics

### Related Concepts
- [Related topic 1] - [How it connects]
- [Related topic 2] - [How it connects]

### Advanced Extensions
- [Advanced topic that builds on this]
- [Applications in other fields]

### Suggested Follow-up Animations
1. [Topic to explore next]
2. [Related visualization idea]

---

## 11. Sources and References

### Primary Sources
- **Wikipedia**: [Full URL]
  - [Key sections referenced]

- **Brilliant.org**: [Full URL]
  - [Key insights gained]

- **ProofWiki**: [Full URL] (if applicable)
  - [Proofs or theorems referenced]

### Additional Resources
- [Any other sources consulted]

---

## 12. Implementation Notes

### Estimated Complexity
**Manim Difficulty**: [Easy / Medium / Hard / Very Hard]
**Estimated Implementation Time**: [X hours]

### Required Manim Features
- [List specific Manim classes/animations needed]
- [Any custom animations that might be required]
- [Special considerations (3D, complex math, etc.)]

### Recommended Development Order
1. [First step to implement]
2. [Second step to implement]
3. [Continue in logical order...]

---

## 13. Summary

[Final paragraph summarizing the research and animation approach]

---

**Report Status**: Complete
**Ready for Implementation**: [Yes/No - explain if no]
```

---

## Best Practices

### Research Quality
1. **Always verify information across sources** - Don't rely on a single source
2. **Prioritize authoritative sources** - Wikipedia and academic sources over random blogs
3. **Check publication dates** - Prefer recent content for evolving topics
4. **Look for visual diagrams** - They inform animation planning
5. **Note mathematical rigor** - Understand both formal and intuitive explanations

### Animation Planning
1. **Think pedagogically** - How would a teacher explain this?
2. **Build incrementally** - Start simple, add complexity gradually
3. **Use concrete before abstract** - Show examples before generalizations
4. **Highlight transformations** - Math is about change and relationships
5. **Plan for "aha!" moments** - Structure animations around key insights
6. **Consider timing** - Not too fast, not too slow
7. **Use color meaningfully** - Color should clarify, not confuse

### Report Writing
1. **Be comprehensive** - Include all relevant details
2. **Use proper LaTeX notation** - Mathematical formulas should be precise
3. **Include code hints** - Mention specific Manim classes to use
4. **Think about narrative** - Animations tell stories
5. **Identify challenges** - Note difficult aspects to implement
6. **Suggest examples** - Concrete cases make concepts clearer

---

## Example Research Queries

### Good Queries (Specific and Clear)
- "Research the Pythagorean theorem and create an animation plan"
- "Look up the Fourier transform and plan a visualization"
- "What is Taylor series expansion? Plan an animation showing convergence"
- "Research the epsilon-delta definition of limits and plan a visual explanation"

### Queries Requiring Clarification
- "Tell me about math" - Too vague, need specific topic
- "Make an animation" - Need to know what mathematical concept
- "Explain everything about calculus" - Too broad, need specific subtopic

---

## Output Format

### File Naming Convention
Save reports as: `research-[topic-name]-[YYYY-MM-DD].md`

Examples:
- `research-pythagorean-theorem-2025-11-26.md`
- `research-fourier-transform-2025-11-26.md`
- `research-taylor-series-2025-11-26.md`

### File Location

**CRITICAL**: Save reports in the project's research directory:

**Full path**: `/manim-projects/your-project-name/research-reports/`

Before saving:
```bash
# Verify you're in the correct location
pwd  # Should show /manim-projects/your-project-name

# Create directory if needed
mkdir -p research-reports
```

**Example full paths**:
- `/manim-projects/fourier-epicycles/research-reports/research-fourier-transform-2025-11-26.md`
- `/manim-projects/calculus-viz/research-reports/research-derivatives-2025-11-26.md`

---

## Common Mathematical Topics Reference

### Algebra
- Polynomials, factoring, quadratic formula
- Systems of equations
- Exponents and logarithms
- Complex numbers

### Geometry
- Triangles, circles, polygons
- Area and volume formulas
- Transformations (rotation, reflection, translation)
- Coordinate geometry

### Trigonometry
- Sin, cos, tan functions
- Unit circle
- Trigonometric identities
- Inverse trig functions

### Calculus
- Limits and continuity
- Derivatives and differentiation rules
- Integrals and integration techniques
- Fundamental theorem of calculus
- Multivariable calculus
- Differential equations

### Linear Algebra
- Vectors and matrices
- Matrix operations
- Determinants and eigenvalues
- Linear transformations
- Vector spaces

### Advanced Topics
- Real analysis (sequences, series, convergence)
- Complex analysis
- Abstract algebra (groups, rings, fields)
- Topology
- Number theory

---

## Reminders

1. **This skill does NOT write code** - It only researches and plans
2. **Always cite sources** - Include full URLs in reports
3. **Be thorough** - Better too much detail than too little
4. **Think visually** - Every concept should have visual elements identified
5. **Plan for education** - Animations should teach, not just demonstrate
6. **Use proper mathematical notation** - LaTeX for all formulas
7. **Consider the audience** - Explain prerequisite knowledge needed

---

## Skills This Works With

This skill complements the **manim-coding** skill:
1. **math-research** creates the plan
2. **manim-coding** provides the syntax for implementation
3. Together they enable mathematical animation creation from concept to code

---

## Version Info

This skill is designed to work with:
- **Wikipedia**: Current version (continuously updated)
- **Brilliant.org**: Current version
- **ProofWiki**: Current version
- **Manim Community Edition**: v0.19.0+

Always check sources for the most up-to-date information.
