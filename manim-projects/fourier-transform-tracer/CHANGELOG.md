# Changelog - Fourier Transform Epicycles Animation

## [2025-11-28] - SVG Multi-Path Support Fixed

### Fixed
- **SVG multi-path handling**: Sample points now correctly distributed across entire shape
  - Complex SVGs like `woman_flower.svg` have multiple submobjects/paths
  - Previous code only sampled from first submobject (often a small detail)
  - Now automatically selects largest submobject (main shape)
  - Added debug output showing which submobject is selected

- **Impact**:
  - `woman_flower.svg`: Sample points now spread across entire flower (was: clustered at center)
  - `custom_shape.svg`: Still works correctly (backward compatible)
  - Built-in shapes: Still works correctly (backward compatible)

### Technical Details
- `extract_svg_points()` now uses: `max(submobjects, key=lambda s: len(s.points))`
- Automatically finds submobject with most points (typically the main shape)
- No user intervention required
- See `SVG_MULTIPATH_FIX.md` for full details

---

## [2025-11-28] - Sample Points Visualization Added

### Added
- **Sample points visualization** in Scene 3
  - Yellow dots show discrete points sampled from the SVG/curve
  - Appears after reference shape, before epicycles
  - Fully customizable via `params.py`

- **New Parameters** (`params.py`):
  ```python
  SCENE3_SHOW_SAMPLE_POINTS = True
  SCENE3_SAMPLE_POINT_RADIUS = 0.04
  SCENE3_SAMPLE_POINT_COLOR = "YELLOW"
  SCENE3_SAMPLE_POINTS_CREATE_TIME = 1.5
  SCENE3_SAMPLE_POINTS_WAIT_TIME = 1.0
  SCENE3_SAMPLE_POINTS_FADEOUT_TIME = 0.8
  ```

- **New Documentation**:
  - `SAMPLE_POINTS_FEATURE.md` - Complete feature documentation
  - `SAMPLE_POINTS_QUICKSTART.md` - Quick start guide
  - Updated `README_FOURIER_EPICYCLES.md` with new feature

### Changed
- Scene 3 duration increased by ~3.3 seconds when sample points are enabled
- Default `NUM_SAMPLES` remains 200 (good balance for visualization)
- Default `NUM_EPICYCLES` set to 50 (was inconsistent)

### Educational Impact
- Students can now **see** the discretization process
- Demonstrates the input to the DFT algorithm
- Shows relationship between sampling density and curve accuracy
- Helps explain Nyquist sampling concepts

---

## [2025-11-28] - Bug Fixes

### Fixed
- **LaggedStart Error**: Fixed crash when all epicycles filtered out
  - Added check for empty circles/arrows VGroups
  - Provides helpful error message
  - Gracefully exits instead of crashing
  - See `LAGGEDSTART_FIX.md` for details

### Changed
- `SCENE3_MIN_EPICYCLE_RADIUS` now defaults to 0.001 (was 0.01)
  - Allows more epicycles to be displayed
  - Reduces likelihood of "no epicycles" error

---

## [2025-11-28] - Parameter Refactoring

### Changed
- **Complete parameter extraction** to `params.py`
  - All 4 scenes fully parameterized
  - 125 total parameters defined
  - 88 parameters actively used
  - Zero hardcoded "magic numbers" remaining

- **New parameter organization**:
  - Scene 1: Fourier basics (15 parameters)
  - Scene 1.5: Rotation to waves (23 parameters)
  - Scene 2: Epicycle mechanics (11 parameters)
  - Scene 3: SVG tracing (47 parameters)
  - Global: Shared parameters (29 parameters)

### Added
- `PARAMETER_REFACTORING_WORKFLOW.md` - Workflow documentation
- Color parameters as strings with `globals()[]` conversion
- Position, timing, and visual property parameters

### Benefits
- Easy customization without touching code
- Clear organization by scene
- Better collaboration (non-programmers can adjust)
- Quick experimentation with different values
- Self-documenting configuration

---

## Previous Features

### Core Functionality
- Four educational scenes demonstrating Fourier Transform
- DFT implementation for decomposing curves
- Epicycle visualization with head-to-tail positioning
- SVG file support with custom shapes
- Built-in parametric shapes (heart, star, circle, square)

### Mathematical Accuracy
- Proper complex number representation
- Frequency sorting for optimal visualization
- ValueTracker for precise animation control
- Individual mobject updaters for smooth rotation

### Customization
- Adjustable number of epicycles
- Configurable sampling rate
- Custom SVG support
- Multiple quality presets

---

## File Structure

```
fourier-transform-tracer/
├── animation.py                          # Main animation code
├── params.py                             # All configuration parameters
├── README_FOURIER_EPICYCLES.md          # Main documentation
├── SAMPLE_POINTS_FEATURE.md             # Sample points docs
├── SAMPLE_POINTS_QUICKSTART.md          # Quick start guide
├── LAGGEDSTART_FIX.md                   # Bug fix documentation
├── PARAMETER_REFACTORING_WORKFLOW.md    # Workflow guide
├── CHANGELOG.md                          # This file
├── research-reports/                     # Research documentation
└── media/                                # Rendered videos
```

---

## Version History

### v1.3.0 (2025-11-28)
- Sample points visualization
- LaggedStart error fix
- Complete parameter refactoring
- Comprehensive documentation

### v1.2.0 (2025-11-27)
- Scene 1.5 addition (rotation to waves)
- Head-to-tail epicycle positioning fix
- Rotation animation fix with ValueTracker
- Individual mobject updaters

### v1.1.0 (2025-11-27)
- Multi-scene composition
- SVG file support
- Built-in parametric shapes
- DFT implementation

### v1.0.0 (2025-11-27)
- Initial release
- Basic epicycle animation
- Three educational scenes
- Fourier Transform visualization

---

## Coming Soon

Potential future enhancements:
- Interactive parameter adjustment during playback
- Multiple SVG shapes in one animation
- Comparison mode (show DFT vs ideal)
- Audio synchronization
- 3D epicycle visualization
- Real-time curve drawing input
