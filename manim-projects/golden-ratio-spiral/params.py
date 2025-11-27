# golden_ratio_spiral_params.py
# Visual parameters for Golden Ratio Spiral animation
# Edit these values to customize the animation appearance without touching the main code

# ============================================================
# COLORS
# ============================================================

COLORS = {
    # Primary colors
    "gold": "#FFD700",          # Main golden color for φ
    "background": "#000000",    # Background (default black)

    # Segment/part colors
    "segment_a": "#3498DB",     # Blue for segment 'a'
    "segment_b": "#E74C3C",     # Red for segment 'b'
    "whole": "#FFFFFF",         # White for whole segment

    # Property visualization colors
    "property_1": "#3498DB",    # Blue for first property
    "property_2": "#2ECC71",    # Green for second property
    "phi_rect": "#3498DB",      # Blue for φ rectangle
    "unit_square": "#E74C3C",   # Red for unit square/1

    # Fibonacci colors
    "fib_numbers": "#3498DB",   # Blue for Fibonacci numbers
    "fib_highlight": "#F1C40F", # Yellow for highlighting additions
    "ratio_close": "#F1C40F",   # Yellow for ratios close to φ
    "ratio_exact": "#FFD700",   # Gold for ratios very close to φ
    "convergence": "#2ECC71",   # Green for convergence statement
}

# ============================================================
# TEXT CONTENT
# ============================================================

TEXT = {
    # Scene 1: Introduction
    "intro_title": "The Golden Ratio",
    "phi_symbol": "φ",
    "phi_value": "≈ 1.618033988...",
    "segment_a_label": "a",
    "segment_b_label": "b",
    "segment_whole_label": "a + b",
    "golden_equation": "(a + b)/a = a/b = φ",
    "algebraic_equation": "x² - x - 1 = 0",
    "phi_solution": "φ = (1 + √5) / 2",

    # Scene 2: Properties
    "properties_title": "Unique Properties of φ",
    "prop1_title": "Squaring Property",
    "prop1_equation": "φ² = φ + 1",
    "prop1_numerical": "1.618² ≈ 2.618 = 1.618 + 1",
    "prop2_title": "Reciprocal Property",
    "prop2_equation": "1/φ = φ - 1",
    "prop2_numerical": "1/1.618 ≈ 0.618 = 1.618 - 1",

    # Scene 3: Fibonacci
    "fibonacci_title": "Fibonacci Connection",
    "fib_sequence_label": "Fibonacci Sequence:",
    "ratio_label": "Ratio of consecutive terms:",
    "phi_comparison": "φ = 1.618...",
    "convergence_statement": "As n → ∞, ratio → φ",

    # Scene 4-5: Placeholders
    "rectangles_title": "Golden Rectangles",
    "spiral_title": "The Golden Spiral",
}

# ============================================================
# DIMENSIONS
# ============================================================

DIMENSIONS = {
    # Line and stroke widths
    "line_stroke": 8,           # Width of main line segments
    "rect_stroke": 3,           # Width of rectangle strokes
    "dot_radius": 0.1,          # Radius of division point dot

    # Segment lengths
    "segment_total_length": 6,  # Total length of line segment in Scene 1

    # Rectangle sizes (Scene 2)
    "rect_width": 2.5,          # Width of rectangles in properties scene
}

# ============================================================
# POSITIONS
# ============================================================

POSITIONS = {
    # Title positions (Y coordinates, relative to top)
    "title_edge_buffer": 1.0,   # Distance from top edge

    # Scene 1 positions
    "phi_symbol_y": 0,          # Center position for φ symbol
    "equation_y": 3.5,          # Y position for equations at bottom

    # Scene 2 positions
    "prop_title_y": 2,          # Y position for property titles
    "rect_x": 3.5,              # X position for visual rectangles

    # Scene 3 positions
    "fib_text_y_offset": 0.8,   # Offset below title
    "fib_start_x": -5,          # Starting X position for sequence
    "convergence_shift_up": 1.5, # How much to shift sequence up
}

# ============================================================
# TIMING (in seconds)
# ============================================================

TIMING = {
    # Scene 1: Introduction
    "intro_title_fadein": 1.0,
    "phi_symbol_write": 1.5,
    "phi_value_wait": 0.5,
    "segment_wait": 0.5,
    "equation_wait": 2.0,
    "transform_wait": 1.0,
    "solution_wait": 2.0,
    "fadeout_wait": 0.5,

    # Scene 2: Properties
    "property_fadein": 1.0,
    "property_wait": 1.0,
    "numerical_wait": 2.0,
    "visual_wait": 1.0,
    "visual_decompose_wait": 2.0,

    # Scene 3: Fibonacci
    "fib_number_fadein": 0.5,
    "fib_addition_highlight": 0.3,
    "fib_comma": 0.2,
    "fib_sequence_shift": 0.8,
    "ratio_write": 0.6,
    "ratio_wait": 1.0,
    "convergence_wait": 2.0,

    # General
    "default_wait": 0.5,
}

# ============================================================
# SIZES
# ============================================================

SIZES = {
    # Font sizes
    "title_font": 60,           # Main scene titles
    "subtitle_font": 50,        # Subtitles
    "phi_symbol_font": 120,     # Large φ symbol
    "phi_value_font": 36,       # φ numerical value
    "equation_font": 40,        # Mathematical equations
    "label_font": 36,           # Segment labels
    "property_title_font": 36,  # Property titles
    "property_font": 40,        # Property equations
    "numerical_font": 32,       # Numerical verifications
    "rect_label_font": 32,      # Rectangle labels
    "fib_sequence_font": 32,    # Fibonacci numbers
    "fib_title_font": 32,       # Fibonacci section titles
    "ratio_font": 28,           # Ratio display
    "convergence_font": 28,     # Convergence statement

    # Scale factors
    "global_scale": 1.0,        # Global scale multiplier (1.0 = default)
}

# ============================================================
# OPACITY
# ============================================================

OPACITY = {
    "rect_fill": 0.3,           # Fill opacity for rectangles
    "rect_stroke": 1.0,         # Stroke opacity for rectangles
}

# ============================================================
# MATHEMATICAL CONSTANTS
# ============================================================
# (Computed values - generally don't need to change these)

import numpy as np

MATH_CONSTANTS = {
    "phi": (1 + np.sqrt(5)) / 2,  # The golden ratio
}

# ============================================================
# FIBONACCI SEQUENCE
# ============================================================

FIBONACCI = {
    "sequence": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],  # Fibonacci numbers to display
    "ratio_display_indices": [0, 1, 2, 3, 4, 6, 8],      # Which ratios to show
    "ratio_exact_threshold": 0.001,  # Difference threshold for "exact" color
    "ratio_close_threshold": 0.01,   # Difference threshold for "close" color
}

# ============================================================
# FRAME CONFIGURATION
# ============================================================
# Uncomment and modify these to change aspect ratio and resolution

# FRAME_CONFIG = {
#     "aspect_ratio": 16/9,       # Default 16:9 widescreen
#     "pixel_width": 1920,        # Default HD width
#     "pixel_height": 1080,       # Default HD height
#     "frame_width": 14.0,        # Default frame width
#     "frame_height": 8.0,        # Default frame height
# }
