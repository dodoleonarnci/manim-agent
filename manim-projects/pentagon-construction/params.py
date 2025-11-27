"""
Pentagon Construction Animation Parameters

This module externalizes all visual and timing parameters for the compass and
straightedge construction of a regular pentagon. By separating parameters from
animation logic, we enable easy customization and experimentation without
modifying the core animation code.

Parameter Categories:
- COLORS: All color definitions for geometric objects
- TEXT: Scene titles, labels, and annotations
- DIMENSIONS: Sizes for circles, lines, points
- POSITIONS: Camera and object positioning
- TIMING: Animation duration for each step
- SIZES: Font sizes and scale factors
- OPACITY: Transparency values for construction elements
"""

from manim import *
import numpy as np

# =============================================================================
# COLORS
# =============================================================================

COLORS = {
    # Compass and straightedge tools
    "compass_arm": GRAY,
    "compass_arc": GREEN,
    "straightedge": WHITE,

    # Construction elements
    "circle": WHITE,
    "horizontal_diameter": BLUE,
    "vertical_diameter": RED,
    "construction_lines": GRAY,
    "construction_arcs": GREEN,

    # Pentagon and final elements
    "pentagon_outline": GOLD,
    "pentagon_fill": GOLD,

    # Points
    "center_point": YELLOW,          # O
    "diameter_points": BLUE,         # X, Y, Z, A
    "midpoint": GREEN,               # M
    "golden_point": ORANGE,          # R
    "pentagon_vertices": RED,        # A, B, C, D, E

    # Labels
    "label_text": WHITE,
    "title_text": GOLD,
    "annotation_text": BLUE_C,

    # Verification elements
    "angle_arc": YELLOW,
    "measurement_line": BLUE_C,
    "golden_ratio_highlight": GOLD,

    # Background
    "background": "#2b2b2b",  # Manim dark background
}

# =============================================================================
# TEXT
# =============================================================================

TEXT = {
    # Scene titles
    "intro_title": "Regular Pentagon Construction",
    "intro_subtitle": "Using Compass and Straightedge",

    # Step descriptions
    "step_perpendicular": "Step 1: Create Perpendicular Diameters",
    "step_midpoint": "Step 2: Find Midpoint of Radius",
    "step_golden_arc": "Step 3: Construct the Golden Arc",
    "step_mark_vertices": "Step 4: Mark Pentagon Vertices",
    "step_complete": "Step 5: Complete the Pentagon",

    # Point labels
    "label_O": "O",  # Center
    "label_A": "A",  # Top vertex
    "label_B": "B",  # Pentagon vertices
    "label_C": "C",
    "label_D": "D",
    "label_E": "E",
    "label_X": "X",  # Left diameter endpoint
    "label_Y": "Y",  # Right diameter endpoint
    "label_Z": "Z",  # Bottom diameter endpoint
    "label_M": "M",  # Midpoint
    "label_R": "R",  # Golden arc intersection

    # Annotations
    "annotation_midpoint": "M is the midpoint of OY",
    "annotation_golden_ratio": r"MA = \frac{r\sqrt{5}}{2}",
    "annotation_side_length": "AR = side length of pentagon",
    "annotation_angle": r"72° = \frac{360°}{5}",
    "annotation_interior_angle": r"108°",
    "annotation_phi": r"\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618",

    # Verification text
    "verification_equal_sides": "All sides equal",
    "verification_equal_angles": "All angles = 108°",
    "verification_golden_ratio": r"Diagonal/Side = \phi",
}

# =============================================================================
# DIMENSIONS
# =============================================================================

DIMENSIONS = {
    # Circle
    "circle_radius": 3.0,  # Main circle radius in Manim units
    "circle_stroke_width": 3,

    # Lines
    "diameter_stroke_width": 3,
    "construction_line_width": 2,
    "pentagon_stroke_width": 5,
    "arc_stroke_width": 3,

    # Points
    "point_radius": 0.08,
    "center_point_radius": 0.1,
    "vertex_point_radius": 0.1,

    # Compass visualization
    "compass_arm_length": 1.5,
    "compass_arm_width": 0.05,

    # Measurement arrows
    "measurement_arrow_buff": 0.1,
    "measurement_arrow_stroke_width": 2,
}

# =============================================================================
# POSITIONS
# =============================================================================

POSITIONS = {
    # Main circle center
    "circle_center": ORIGIN,

    # Label positioning offsets (relative to points)
    "label_offset_O": DOWN * 0.3 + LEFT * 0.3,
    "label_offset_A": UP * 0.4,
    "label_offset_B": RIGHT * 0.4 + UP * 0.3,
    "label_offset_C": RIGHT * 0.4 + DOWN * 0.2,
    "label_offset_D": LEFT * 0.4 + DOWN * 0.2,
    "label_offset_E": LEFT * 0.4 + UP * 0.3,
    "label_offset_X": LEFT * 0.4,
    "label_offset_Y": RIGHT * 0.4,
    "label_offset_Z": DOWN * 0.4,
    "label_offset_M": DOWN * 0.35,
    "label_offset_R": DOWN * 0.35,

    # Title positions
    "title_position": UP * 3.5,
    "subtitle_position": UP * 3.0,
    "step_description_position": DOWN * 3.5,

    # Annotation positions
    "annotation_position": RIGHT * 4 + UP * 2,
}

# =============================================================================
# TIMING
# =============================================================================

TIMING = {
    # Scene durations (total time for each scene)
    "intro_scene": 4.0,
    "perpendicular_scene": 6.0,
    "midpoint_scene": 5.0,
    "golden_arc_scene": 7.0,
    "mark_vertices_scene": 8.0,
    "complete_pentagon_scene": 5.0,
    "verification_scene": 6.0,

    # Individual animation durations
    "fade_in": 0.8,
    "fade_out": 0.6,
    "draw_line": 1.5,
    "draw_circle": 2.0,
    "draw_arc": 2.0,
    "create_point": 0.5,
    "write_text": 1.0,
    "move_compass": 1.0,
    "transform": 1.5,
    "indicate": 1.0,

    # Pauses between steps
    "pause_short": 0.5,
    "pause_medium": 1.0,
    "pause_long": 1.5,

    # Compass animation timing
    "compass_open": 1.0,
    "compass_close": 0.8,
    "compass_move": 1.0,
    "compass_draw_arc": 2.5,
}

# =============================================================================
# SIZES
# =============================================================================

SIZES = {
    # Font sizes
    "title_font_size": 56,
    "subtitle_font_size": 40,
    "step_font_size": 36,
    "label_font_size": 32,
    "annotation_font_size": 28,

    # Scale factors
    "title_scale": 1.0,
    "label_scale": 0.8,
    "annotation_scale": 0.7,
    "compass_scale": 1.0,

    # Indication effects
    "indicate_scale_factor": 1.3,
    "flash_scale_factor": 1.5,
}

# =============================================================================
# OPACITY
# =============================================================================

OPACITY = {
    # Construction elements (can be faded)
    "construction_line_active": 1.0,
    "construction_line_faded": 0.3,
    "construction_arc_active": 1.0,
    "construction_arc_faded": 0.25,

    # Main elements (usually visible)
    "circle_active": 1.0,
    "circle_faded": 0.5,
    "pentagon_outline": 1.0,
    "pentagon_fill": 0.2,

    # Points and labels
    "point_opacity": 1.0,
    "label_opacity": 1.0,
    "label_faded": 0.4,

    # Compass
    "compass_opacity": 0.8,

    # Annotations
    "annotation_opacity": 0.9,
}

# =============================================================================
# GEOMETRIC CALCULATIONS
# =============================================================================

# These are computed values based on the construction
GEOMETRY = {
    # Golden ratio
    "phi": (1 + np.sqrt(5)) / 2,

    # Calculated dimensions (based on DIMENSIONS["circle_radius"])
    "radius": DIMENSIONS["circle_radius"],
}

# Pentagon side length for a circle of given radius
GEOMETRY["pentagon_side_length"] = 2 * GEOMETRY["radius"] * np.sin(np.pi / 5)

# Arc radius from M to A (the golden arc)
GEOMETRY["golden_arc_radius"] = GEOMETRY["radius"] * np.sqrt(5) / 2

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_pentagon_vertices(radius=None, start_angle=np.pi/2):
    """
    Calculate the five vertices of a regular pentagon inscribed in a circle.

    Args:
        radius: Circle radius (defaults to DIMENSIONS["circle_radius"])
        start_angle: Starting angle in radians (defaults to π/2, top of circle)

    Returns:
        List of 5 numpy arrays representing vertex positions
    """
    if radius is None:
        radius = DIMENSIONS["circle_radius"]

    angles = [start_angle + i * 2 * np.pi / 5 for i in range(5)]
    vertices = [
        np.array([radius * np.cos(angle), radius * np.sin(angle), 0])
        for angle in angles
    ]
    return vertices

def get_circle_point(angle, radius=None, center=None):
    """
    Get a point on the circle at a given angle.

    Args:
        angle: Angle in radians (0 = right, π/2 = up)
        radius: Circle radius (defaults to DIMENSIONS["circle_radius"])
        center: Circle center (defaults to POSITIONS["circle_center"])

    Returns:
        numpy array representing the point position
    """
    if radius is None:
        radius = DIMENSIONS["circle_radius"]
    if center is None:
        center = POSITIONS["circle_center"]

    return center + np.array([
        radius * np.cos(angle),
        radius * np.sin(angle),
        0
    ])

def get_label_position(point, offset_key):
    """
    Get the position for a label relative to a point.

    Args:
        point: numpy array of point position
        offset_key: Key in POSITIONS dict (e.g., "label_offset_A")

    Returns:
        numpy array representing the label position
    """
    return point + POSITIONS[offset_key]
