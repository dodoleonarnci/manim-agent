# SVG Troubleshooting Guide

## Common SVG Issues and Solutions

### Issue 1: Sample Points Clustered in One Spot

**Symptom:**
- Sample points (yellow dots) appear only at the center
- Not distributed across the entire shape
- Happens with complex SVGs but not simple ones

**Cause:**
Complex SVG files often contain multiple paths (submobjects). The animation was only sampling from the first path, which might be a small decorative element.

**Solution:**
✅ **FIXED** - The animation now automatically selects the largest submobject (main shape).

**What You'll See:**
```
SVG has 3 submobjects
Using submobject with 9048 points (largest)
```

This debug message confirms the correct path is being used.

**If Still Not Working:**
1. Check your SVG file structure:
   ```python
   from manim import SVGMobject
   svg = SVGMobject("your_file.svg")
   print(f"Submobjects: {len(svg.submobjects)}")
   for i, sub in enumerate(svg.submobjects):
       print(f"  {i}: {len(sub.points)} points")
   ```

2. Simplify your SVG:
   - Use online tools like [svgomg.net](https://svgomg.net/)
   - Remove unnecessary layers/groups
   - Merge multiple paths into one

---

### Issue 2: No Epicycles Displayed

**Symptom:**
```
⚠️ Warning: No epicycles to display (all filtered out due to small radius)
   Try decreasing SCENE3_MIN_EPICYCLE_RADIUS in params.py
```

**Cause:**
All epicycles have radii smaller than `SCENE3_MIN_EPICYCLE_RADIUS`.

**Solution:**
```python
# In params.py
SCENE3_MIN_EPICYCLE_RADIUS = 0.001  # Decrease from 0.01
# Or
NUM_EPICYCLES = 80  # Increase number of epicycles
```

---

### Issue 3: SVG Not Found

**Symptom:**
```
Error loading SVG: FileNotFoundError
```

**Solution:**
1. Ensure SVG file is in the project directory
2. Use correct filename (case-sensitive)
3. Check file path in `params.py`:
   ```python
   DEFAULT_SVG_PATH = "your_file.svg"  # Or None for default heart
   ```

---

### Issue 4: SVG Appears Too Small/Large

**Symptom:**
- Shape is tiny or extends beyond frame
- Sample points are barely visible or off-screen

**Solution:**
Adjust scaling in `params.py`:
```python
SCENE3_SVG_SCALE = 2.5  # Increase to make larger
SCENE3_SVG_SCALE = 1.0  # Decrease to make smaller
```

**Auto-calculate optimal scale:**
```python
# In Scene 3, after loading SVG
svg_mob.scale_to_fit_height(5)  # Fit to height of 5 units
# or
svg_mob.scale_to_fit_width(6)   # Fit to width of 6 units
```

---

### Issue 5: Wrong Part of SVG Traced

**Symptom:**
- Epicycles trace a detail, not the main shape
- Even after multi-path fix

**Diagnosis:**
Run this to see which submobject is being used:
```python
from manim import SVGMobject
svg = SVGMobject("your_file.svg")

for i, sub in enumerate(svg.submobjects):
    print(f"Submobject {i}: {len(sub.points)} points")
    # Plot or inspect this submobject to see what it is
```

**Solution:**
If the largest submobject isn't the main shape (rare), you have two options:

**Option A: Modify your SVG** (recommended)
- Remove unwanted paths in Illustrator/Inkscape
- Keep only the main outline you want to trace

**Option B: Manual override** (advanced)
Modify `extract_svg_points()` to use a specific submobject:
```python
# In animation.py, line ~75
# Replace:
largest_submobject = max(svg_mobject.submobjects, key=lambda s: len(s.points))

# With:
largest_submobject = svg_mobject.submobjects[2]  # Force use submobject 2
```

---

### Issue 6: Epicycles Don't Match Shape Well

**Symptom:**
- Tracing is rough or inaccurate
- Doesn't capture shape details

**Solution:**
Increase sampling and epicycles:
```python
# In params.py
NUM_SAMPLES = 400      # More sample points (from 200)
NUM_EPICYCLES = 100    # More epicycles (from 50)
```

**Trade-offs:**
- More samples = better accuracy, slower rendering
- More epicycles = better accuracy, much slower rendering
- Recommended: `NUM_SAMPLES ≥ 2 × NUM_EPICYCLES`

---

### Issue 7: Animation Takes Too Long

**Symptom:**
- Rendering is very slow
- Each frame takes many seconds

**Solution:**
Reduce complexity:
```python
# In params.py
NUM_SAMPLES = 100       # Reduce from 200+
NUM_EPICYCLES = 30      # Reduce from 50+
SCENE3_ROTATION_DURATION = 30.0  # Reduce from 60.0
```

For testing, use low quality:
```bash
manim -pql animation.py Scene3_SVGTracing  # Low quality, fast
```

---

### Issue 8: SVG Colors/Styling Lost

**Symptom:**
- SVG appears as solid gray
- Original colors not shown

**Explanation:**
This is expected behavior. The animation:
1. Shows SVG as gray reference shape
2. Samples points from the outline
3. Traces with epicycles (colored by frequency)

**If You Want Original Colors:**
Manim's `SVGMobject` does preserve colors, but for this animation we intentionally use:
```python
svg_mob.set_color(GRAY).set_opacity(0.5)
```

To keep original colors:
```python
# In animation.py, comment out the color override
# svg_mob.set_color(reference_color).set_opacity(params.SCENE3_REFERENCE_OPACITY)
```

---

## Debug Mode

Add this to see detailed information:

```python
# In params.py (add new parameter)
DEBUG_SVG_INFO = True

# In animation.py, scene3_animation()
if hasattr(params, 'DEBUG_SVG_INFO') and params.DEBUG_SVG_INFO:
    print(f"Complex points: {len(complex_points)}")
    print(f"Point spread: X=[{min(p.real for p in complex_points):.2f}, {max(p.real for p in complex_points):.2f}]")
    print(f"Point spread: Y=[{min(p.imag for p in complex_points):.2f}, {max(p.imag for p in complex_points):.2f}]")
    print(f"Coefficients: {len(coefficients)}")
    print(f"Epicycles: {len(top_coeffs)}")
```

---

## SVG Preparation Tips

### Optimal SVG Characteristics:
✅ Single continuous closed path
✅ Simplified (< 1000 points ideal)
✅ No text elements
✅ No embedded images
✅ Centered at origin
✅ Reasonable size (not too large/small)

### Tools for SVG Optimization:
- [svgomg.net](https://svgomg.net/) - Online SVG optimizer
- Adobe Illustrator - "Simplify" paths, "Object > Path > Clean Up"
- Inkscape - "Path > Simplify"

### SVG Export Settings:
- **Illustrator**: File > Export > SVG
  - Styling: Presentation Attributes
  - Decimal Places: 2
  - Minify: Yes
  - Responsive: No

- **Inkscape**: File > Save As > Optimized SVG
  - Enable "Simplify colors"
  - Enable "Shorten color values"
  - Number of significant digits: 3

---

## Getting Help

If issues persist:

1. **Check documentation:**
   - `README_FOURIER_EPICYCLES.md` - Main guide
   - `SVG_MULTIPATH_FIX.md` - Multi-path details
   - `SAMPLE_POINTS_FEATURE.md` - Sample points info

2. **Test with built-in shapes:**
   ```python
   # In params.py
   DEFAULT_SVG_PATH = None  # Use built-in heart shape
   ```

   If built-in shapes work but your SVG doesn't, the issue is with your SVG file.

3. **Inspect your SVG:**
   - Open in text editor
   - Look for multiple `<path>` elements
   - Check for complexity (very long `d=` attributes)

4. **Try the simple test SVG:**
   ```python
   DEFAULT_SVG_PATH = "custom_shape.svg"  # Simple star shape
   ```

---

## Quick Reference

| Problem | Solution |
|---------|----------|
| Points clustered | ✅ Auto-fixed (selects largest submobject) |
| No epicycles | Decrease `SCENE3_MIN_EPICYCLE_RADIUS` |
| SVG not found | Check filename and path |
| Too small/large | Adjust `SCENE3_SVG_SCALE` |
| Poor accuracy | Increase `NUM_SAMPLES` and `NUM_EPICYCLES` |
| Too slow | Decrease `NUM_SAMPLES` and `NUM_EPICYCLES` |
| Wrong shape traced | Simplify SVG or manual override |

---

**Last Updated:** 2025-11-28
