# Manim Coding Skill

This skill provides comprehensive reference material for **Manim Community Edition**, a Python library for creating programmatic mathematical animations.

## 📁 Files in This Skill

### `SKILL.md` (Main Reference)
The complete skill definition with comprehensive Manim reference organized into three sections:
- **Section 1: Essential Basics** - Most commonly used commands that appear in virtually every Manim project
- **Section 2: Intermediate Features** - Commonly used features for more complex animations
- **Section 3: Advanced Features** - Specialized features for advanced use cases

This is the primary reference file that Claude will use when helping with Manim code.

### `quick-reference.md`
A compact cheat sheet with the most essential commands in table format. Perfect for quick lookups:
- Minimal working example
- Command line usage
- Most used animations and shapes
- Common patterns

### `syntax-by-category.md`
Complete syntax reference organized by category (shapes, animations, positioning, etc.). Great for:
- Finding all options in a category
- Comparing similar commands
- Learning parameter options

### `examples.py`
Runnable Python examples demonstrating common patterns:
- Basic shapes and styling
- The `.animate` syntax
- Transform vs ReplacementTransform
- Text and math formulas
- Graphing functions
- Groups and layouts
- Updaters and ValueTracker
- 3D scenes
- Tables

**Run examples with:**
```bash
manim -pql examples.py SceneName
```

## 🎯 When This Skill Activates

Claude will automatically use this skill when you:
- Write Manim animation code
- Ask about Manim syntax or commands
- Debug Manim scripts
- Request help with mathematical visualizations
- Work with Python animation projects using Manim

## 🚀 Quick Start

**Minimal Manim Script:**
```python
from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))
        self.wait()
```

**Render it:**
```bash
manim -pql script.py MyScene
```

## 📚 Reference Organization

The skill organizes Manim commands by **frequency of use**:

### Very Common (Section 1)
- Basic scene structure
- Core animations: `Create`, `FadeIn`, `FadeOut`, `Write`, `Transform`
- Essential shapes: `Circle`, `Square`, `Triangle`, `Text`, `MathTex`
- The `.animate` syntax
- Basic positioning and styling
- Command line usage

### Common (Section 2)
- Advanced text animations
- Grouping with `VGroup`
- Coordinate systems and graphing
- Movement animations
- Animation timing and easing
- Tables and matrices
- 3D scenes
- Updaters

### Advanced (Section 3)
- Custom animations
- Specialized shapes
- Matrix transformations
- Indication animations
- Complex transforms
- Custom colors and palettes
- Scene variants
- Homotopy and phase flow

## 🔗 External Resources

- **Official Docs**: https://docs.manim.community/en/stable/
- **Example Gallery**: https://docs.manim.community/en/stable/examples.html
- **Online Editor**: https://try.manim.community/
- **Discord Community**: https://discord.gg/mMRrZQW
- **GitHub**: https://github.com/ManimCommunity/manim

## 📝 Notes

- This skill references **Manim Community Edition v0.19.0**
- Manim Community is distinct from the original 3b1b/manim
- Always use raw strings (`r"..."`) for LaTeX in `MathTex` and `Tex`
- The `.animate` syntax is the modern way to animate transformations
- Use `Transform` when you want to morph one object into another
- Use `ReplacementTransform` when you want to replace one object with another

## 💡 Tips for Best Results

1. **Start with Section 1** for basic tasks
2. **Check examples.py** for working code patterns
3. **Use quick-reference.md** for fast lookups
4. **Use syntax-by-category.md** to explore all options in a category
5. **Refer to SKILL.md** for complete documentation

## 🎓 Learning Path

1. **Beginner**: Focus on Section 1 (Essential Basics)
   - Learn basic scene structure
   - Master common shapes and animations
   - Practice the `.animate` syntax

2. **Intermediate**: Explore Section 2
   - Work with coordinate systems and graphs
   - Learn grouping and layouts
   - Experiment with timing and easing

3. **Advanced**: Dive into Section 3
   - Create custom animations
   - Use specialized transforms
   - Master 3D scenes and camera control

---

**Last Updated**: Based on Manim Community Edition v0.19.0 documentation
