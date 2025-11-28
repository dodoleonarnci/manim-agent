# Epicycle Rotation Fix - Technical Details

## The Problem

The epicycles (circles and arrows) were not visibly rotating. They appeared stationary even though the traced path was being drawn.

## Root Cause

The issue was with **how updaters were attached** to Manim mobjects:

### ❌ Original (Broken) Code

```python
epicycle_group = VGroup(*circles, *arrows)
epicycle_group.add_updater(update_epicycles)
```

**Why this failed:**
- Adding an updater to a `VGroup` doesn't automatically propagate updates to child mobjects
- The updater function receives the VGroup as `mob`, but modifies individual arrows/circles inside
- Manim's animation system doesn't trigger VGroup updaters reliably during `.play()` animations

### ✅ Fixed Code

```python
# Add updater to EACH arrow and circle individually
for arrow in arrows:
    arrow.add_updater(update_epicycles)
for circle in circles:
    circle.add_updater(update_epicycles)
```

**Why this works:**
- Each mobject has its own updater reference
- When `self.play(time_tracker.animate...)` runs, ALL updaters are called on every frame
- The updater function loops through all epicycles and updates them together
- This ensures synchronized, visible rotation

## Key Technical Details

### 1. Updater Function Signature

```python
def update_epicycles(mob):
    """mob = the individual arrow or circle that triggered this call"""
    time = time_tracker.get_value()

    # Update ALL epicycles based on current time
    # (even though mob is just one object, we update the whole system)
    for i, (arrow, circle, coeff, freq) in enumerate(...):
        # Calculate new positions for all epicycles
        ...
```

**Important:** Even though `mob` is just one object, the function updates the entire epicycle system. This is fine because:
- All updaters run the same function
- The function is idempotent (running it multiple times per frame doesn't break anything)
- It ensures all epicycles stay synchronized

### 2. ValueTracker for Explicit Control

```python
time_tracker = ValueTracker(0)

self.play(
    time_tracker.animate.set_value(3 * TAU),  # 3 full rotations
    run_time=60,  # 60 seconds
    rate_func=linear  # Constant speed
)
```

**Benefits:**
- **Precise timing:** Exactly 3 rotations in exactly 60 seconds
- **Linear motion:** `rate_func=linear` ensures constant angular velocity
- **Deterministic:** Same result every time, no dependence on `self.renderer.time`
- **Controllable:** Easy to adjust speed, duration, or number of rotations

### 3. TracedPath Lambda Function

```python
traced_path = TracedPath(
    lambda: arrows[-1].get_end(),  # Lambda ensures it's called every frame
    stroke_width=4,
    stroke_color=YELLOW,
    dissipating_time=None
)
```

**Why lambda:**
- `TracedPath` needs a **callable** that returns a point
- `lambda: arrows[-1].get_end()` creates a function that's called every frame
- This dynamically tracks the tip of the last arrow as it moves

## Testing Methodology

Created `test_rotation.py` with two test scenes:

### Test 1: Manual Updates
Manually updates positions in discrete steps to verify basic geometry works:
```python
for step in range(4):
    time_val = (step + 1) * PI / 4  # 45 degrees per step
    # Update all positions manually
    self.wait(0.5)  # Pause to see each step
```

**Purpose:** Confirms the math is correct and mobjects CAN move.

### Test 2: ValueTracker with Updaters
Uses the same pattern as the fixed code:
```python
time_tracker = ValueTracker(0)
for arrow in arrows:
    arrow.add_updater(update_function)

self.play(time_tracker.animate.set_value(2*TAU), run_time=8, rate_func=linear)
```

**Purpose:** Confirms updaters work correctly and rotation is smooth.

### Test 3: Ultra-Simple Single Arrow
Single rotating arrow to isolate any issues:
```python
def rotate_arrow(mob):
    angle = time_tracker.get_value()
    new_end = 2 * np.array([np.cos(angle), np.sin(angle), 0])
    arrow.put_start_and_end_on(ORIGIN, new_end)
```

**Purpose:** Minimal test case - if this doesn't rotate, something fundamental is wrong.

## Verification Steps

To confirm the fix works:

1. **Visual Inspection:**
   - Circles should visibly rotate around their centers
   - Arrows should spin at different rates (based on frequency)
   - Higher frequency arrows spin faster

2. **Path Tracing:**
   - The traced path should perfectly match the target shape
   - Path should be drawn continuously, not in jumps
   - After N rotations, path should repeat (closed curve)

3. **Frame-by-Frame:**
   - Pause the video at different times
   - Arrow tips should be at different positions
   - Circles should be centered at arrow bases

4. **Debug Text (Optional):**
   ```python
   time_text = always_redraw(
       lambda: Text(f"t = {time_tracker.get_value():.2f}").to_corner(UL)
   )
   self.add(time_text)
   ```
   - Time value should increase smoothly from 0 to 3×2π
   - If time is stuck, ValueTracker animation isn't running

## Common Pitfalls

### ❌ Using `self.renderer.time`
```python
time = self.renderer.time * time_scale  # BAD
```
- Not synchronized with animations
- Hard to control precisely
- May drift or skip frames

### ❌ Adding updater to VGroup
```python
group = VGroup(circle, arrow)
group.add_updater(update_func)  # Doesn't propagate
```
- Updater doesn't affect children
- Children remain stationary

### ❌ Forgetting `lambda` in TracedPath
```python
traced_path = TracedPath(arrows[-1].get_end())  # WRONG
```
- Passes a single point, not a function
- Path won't update as arrow moves

### ❌ Using `self.wait()` instead of `self.play()`
```python
time_tracker.set_value(TAU)  # Instant change
self.wait(5)  # No animation happens
```
- Must use `.animate` with `.play()` for smooth transitions

## Performance Considerations

With 50-100 epicycles:

- **Updater calls per frame:** 50-100 (one per mobject)
- **Total updates per frame:** Each updater updates ALL epicycles
- **Redundant computation:** Yes, but necessary for synchronization
- **Optimization:** Could cache intermediate positions, but complexity outweighs benefit

For better performance:
- Reduce `num_epicycles` (30-50 is usually sufficient)
- Use `-ql` (low quality) for testing
- Render final version with `-qh` (high quality)

## Summary

The fix was simple but critical:

**Before:** Updater on VGroup → No visible rotation
**After:** Updaters on each mobject → Smooth rotation ✅

This demonstrates a key Manim principle: **updaters must be attached to the specific mobjects you want to update**, not to container groups.

---

**Files Modified:**
- `animation.py` - Scene2 and Scene3 updater attachment
- `params.py` - Created (rotation parameters)
- `test_rotation.py` - Created (debugging tests)

**Result:** Epicycles now rotate beautifully! 🎉
