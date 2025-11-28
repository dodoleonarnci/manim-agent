"""
Parameters for Fourier Transform Epicycles Animation

This file contains all configurable parameters for the animation.
Modify these values to customize the behavior of the visualization.
"""

# ============================================================================
# SCENE 1: FOURIER TRANSFORM BASICS
# ============================================================================

# Scene 1 timing
SCENE1_TITLE_WRITE_TIME = 1.5
SCENE1_TITLE_SCALE_TIME = 0.5
SCENE1_AXES_CREATE_TIME = 1.0
SCENE1_WAVE_CREATE_TIME = 1.5
SCENE1_DECOMPOSE_TIME = 2.0
SCENE1_WAIT_TIME = 0.5
SCENE1_FADEOUT_TIME = 0.5

# Wave parameters
WAVE_FREQUENCIES = [1, 3, 5]  # Frequencies of component waves
WAVE_AMPLITUDES = [1.0, 0.5, 0.3]  # Amplitudes of component waves
WAVE_COLORS = ["BLUE", "GREEN", "RED"]  # Colors for each component
COMBINED_WAVE_STROKE_WIDTH = 3  # Stroke width for the combined wave plot

# Axes configuration
AXES_X_RANGE = [0, 2, 0.5]  # [min, max, step] (in terms of PI)
AXES_Y_RANGE = [-2.5, 2.5, 1]
AXES_X_LENGTH = 10
AXES_Y_LENGTH = 4
SCENE1_AXES_SHIFT_DOWN = 0.5  # How far down to shift the axes
SCENE1_WAVE_SEPARATION_SHIFT = 2.5  # Vertical shift for component waves
SCENE1_FADED_OPACITY = 0.3  # Opacity for faded combined wave and axes during decomposition


# ============================================================================
# SCENE 1.5: ROTATION TO WAVES CONNECTION
# ============================================================================

# Scene 1.5 timing
SCENE1_5_TITLE_WRITE_TIME = 0.8
SCENE1_5_TITLE_SCALE_TIME = 0.3
SCENE1_5_CIRCLE_CREATE_TIME = 0.8
SCENE1_5_AXES_CREATE_TIME = 0.5
SCENE1_5_ROTATION_DURATION = 3.0  # One full rotation
SCENE1_5_WAIT_TIME = 0.3
SCENE1_5_FADEOUT_TIME = 0.5

# Rotation to waves parameters
SCENE1_5_ARROW_RADIUS = 1.5
SCENE1_5_ARROW_COLOR = "BLUE"
SCENE1_5_CIRCLE_COLOR = "BLUE"  # Color of the rotating circle
SCENE1_5_CIRCLE_STROKE_WIDTH = 2
SCENE1_5_ARROW_STROKE_WIDTH = 4
SCENE1_5_ARROW_TIP_RATIO = 0.2
SCENE1_5_TIP_DOT_RADIUS = 0.08
SCENE1_5_TIP_DOT_COLOR = "YELLOW"
SCENE1_5_WAVE_TRACE_COLOR = "BLUE"
SCENE1_5_WAVE_TRACE_WIDTH = 3
SCENE1_5_WAVE_STROKE_WIDTH = 3  # Stroke width for traced wave
SCENE1_5_PROJECTION_LINE_COLOR = "GRAY"
SCENE1_5_PROJECTION_STROKE_WIDTH = 2  # Stroke width for projection line
SCENE1_5_PROJECTION_DASH_LENGTH = 0.1

# Position offsets
SCENE1_5_CIRCLE_SHIFT = 3.0  # How far left to shift the circle
SCENE1_5_AXES_SHIFT_X = 2.0  # How far right to shift the axes
SCENE1_5_AXES_SHIFT_Y = 0.5  # How far down to shift the axes
SCENE1_5_AXES_SHIFT_RIGHT = 2.0  # How far right to shift the axes (deprecated, use SHIFT_X)
SCENE1_5_AXES_SHIFT_DOWN = 0.5   # How far down to shift the axes (deprecated, use SHIFT_Y)

# Axes dimensions
SCENE1_5_AXES_X_LENGTH = 5
SCENE1_5_AXES_Y_LENGTH = 3
SCENE1_5_AXES_Y_RANGE = [-2, 2, 1]


# ============================================================================
# SCENE 2: EPICYCLE MECHANICS
# ============================================================================

# Scene 2 timing
SCENE2_TITLE_WRITE_TIME = 1.0
SCENE2_TITLE_SCALE_TIME = 0.5
SCENE2_FIRST_EPICYCLE_TIME = 1.5
SCENE2_FIRST_EPICYCLE_CREATE_TIME = 1.5  # Time to create first epicycle
SCENE2_ADDITIONAL_EPICYCLE_TIME = 0.8
SCENE2_REMAINING_EPICYCLE_CREATE_TIME = 0.8  # Time to create each remaining epicycle
SCENE2_NUM_ROTATIONS = 2  # Number of full rotations (2 = twice around)
SCENE2_ROTATION_DURATION = 6.5  # How long epicycles rotate
SCENE2_FADEOUT_TIME = 0.5

# Epicycle parameters for Scene 2
SCENE2_RADII = [1.5, 0.8, 0.4, 0.2]  # Radius of each circle
SCENE2_FREQUENCIES = [1, -2, 3, -4]  # Rotation frequency (positive = CCW, negative = CW)
SCENE2_COLORS = ["BLUE", "GREEN", "YELLOW", "RED"]  # Color of each epicycle

# Visual styling for Scene 2
SCENE2_CIRCLE_STROKE_WIDTH = 2
SCENE2_ARROW_STROKE_WIDTH = 3
SCENE2_ARROW_TIP_RATIO = 0.15
SCENE2_TRACE_STROKE_WIDTH = 3
SCENE2_TRACE_COLOR = "WHITE"


# ============================================================================
# SCENE 3: SVG TRACING WITH FULL EPICYCLES
# ============================================================================

# Scene 3 timing
SCENE3_TITLE_WRITE_TIME = 1.0
SCENE3_TITLE_SCALE_TIME = 0.5
SCENE3_SVG_SHOW_TIME = 2.0
SCENE3_SVG_WAIT_TIME = 0.5
SCENE3_EPICYCLES_APPEAR_TIME = 2.0
SCENE3_EPICYCLE_CREATE_TIME = 2.0  # Time to create all epicycles
SCENE3_NUM_ROTATIONS = 1  # Number of times to trace the shape (1 = once, 2 = twice, etc.)
SCENE3_ROTATION_DURATION = 30.0  # Duration of rotation animation (user-customizable)
SCENE3_FINALE_TIME = 2.0
SCENE3_FINAL_WAIT_TIME = 1.0
SCENE3_FINALE_WAIT_TIME = 1.0  # Wait time after finale

# Reference shape display
SCENE3_REFERENCE_CREATE_TIME = 2.0  # Time to create reference shape
SCENE3_REFERENCE_WAIT_TIME = 0.5  # Wait time after showing reference

# Sample points visualization
SCENE3_SHOW_SAMPLE_POINTS = True  # Whether to display sample points
SCENE3_SAMPLE_POINT_RADIUS = 0.04  # Size of each sample point dot
SCENE3_SAMPLE_POINT_COLOR = "YELLOW"  # Color of sample points
SCENE3_SAMPLE_POINTS_CREATE_TIME = 1.5  # Time to create sample points
SCENE3_SAMPLE_POINTS_WAIT_TIME = 1.0  # Wait time after showing sample points
SCENE3_SAMPLE_POINTS_FADEOUT_TIME = 0.8  # Time to fade out sample points

# SVG and curve parameters
DEFAULT_SVG_PATH = "woman_flower.svg"  # None = use built-in heart shape
DEFAULT_SHAPE_TYPE = "heart"  # "heart", "star", "circle", or "square"
SCENE3_DEFAULT_SHAPE_RADIUS = 2.0  # Radius for default shape
NUM_SAMPLES = 1000  # Number of points to sample from the curve
NUM_EPICYCLES = 1000  # Number of epicycles to use (more = more accurate, slower)

# DFT computation method
USE_FAST_FFT = True  # True = use NumPy FFT, False = use manual DFT

# Visual styling for Scene 3
SCENE3_SVG_COLOR = "GRAY"
SCENE3_SVG_OPACITY = 0.5
SCENE3_SVG_SCALE = 2.5
SCENE3_REFERENCE_COLOR = "GRAY"  # Color for reference shape
SCENE3_REFERENCE_OPACITY = 0.5  # Opacity for reference shape

# Epicycle visual properties
SCENE3_EPICYCLE_CIRCLE_STROKE_WIDTH = 2
SCENE3_EPICYCLE_CIRCLE_OPACITY = 0.8
SCENE3_EPICYCLE_ARROW_STROKE_WIDTH = 3
SCENE3_EPICYCLE_ARROW_TIP_RATIO = 0.1
SCENE3_EPICYCLE_LAG_RATIO = 0.01  # Lag ratio for epicycle appearance
SCENE3_MIN_EPICYCLE_RADIUS = 0.001  # Minimum radius to display epicycle

# Traced path properties
SCENE3_TRACE_STROKE_WIDTH = 4
SCENE3_TRACE_COLOR = "YELLOW"
SCENE3_TRACED_PATH_COLOR = "YELLOW"  # Color of traced path
SCENE3_TRACED_PATH_STROKE_WIDTH = 4  # Stroke width of traced path
SCENE3_FINAL_TRACE_WIDTH = 6
SCENE3_FINAL_TRACE_COLOR = "WHITE"
SCENE3_FINALE_PATH_COLOR = "WHITE"  # Finale path color
SCENE3_FINALE_PATH_STROKE_WIDTH = 6  # Finale path stroke width

# Color gradient for epicycles
EPICYCLE_LOW_FREQ_COLOR = "BLUE"  # Color for low frequencies
EPICYCLE_HIGH_FREQ_COLOR = "RED"  # Color for high frequencies
SCENE3_LOW_FREQ_COLOR = "BLUE"  # Low frequency color for Scene 3
SCENE3_HIGH_FREQ_COLOR = "RED"  # High frequency color for Scene 3
EPICYCLE_FREQ_NORMALIZE = 20  # Normalize frequency ratio
SCENE3_FREQ_NORMALIZE_DIVISOR = 20  # Divisor for normalizing frequency

# ============================================================================
# GENERAL SETTINGS
# ============================================================================

# Font sizes
TITLE_FONT_SIZE = 36
SMALL_TITLE_SCALE = 0.6  # Scene 3
MEDIUM_TITLE_SCALE = 0.7  # Scenes 1 & 2
LABEL_FONT_SIZE = 24

# Animation quality presets
# These can be overridden by command-line flags (-ql, -qm, -qh, -qk)
DEFAULT_QUALITY = "low"  # "low", "medium", "high", "4k"

# Scene transitions
SCENE_TRANSITION_WAIT = 0.5

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

# Performance tuning
LAGGED_START_LAG_RATIO = 0.01  # Lag between epicycle appearances

# Trace path settings
TRACE_DISSIPATING_TIME = None  # None = permanent trace, float = fading trace

# Complex number representation
USE_COMPLEX_EXPONENTIAL = True  # Use e^(iθ) form vs separate sin/cos
