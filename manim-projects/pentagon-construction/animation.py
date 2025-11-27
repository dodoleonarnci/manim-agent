"""
Regular Pentagon Construction Animation

This module implements a step-by-step animation of constructing a regular pentagon
using only compass and straightedge. The construction is based on the classical
method that leverages the golden ratio.

All visual parameters are externalized to params.py for easy customization.

Scenes:
1. IntroScene: Title and initial circle setup
2. PerpendicularDiameters: Draw horizontal and vertical diameters
3. FindMidpoint: Find midpoint M of radius OA
4. GoldenArc: The key arc from M through B to find point R
5. MarkVertices: Use AR as compass radius to mark all 5 vertices
6. CompletePentagon: Connect vertices to form the pentagon
7. Verification: Show angles and side lengths are equal

Mathematical Foundation:
The construction works by embedding the golden ratio φ = (1+√5)/2 into the
geometry. The key step is constructing an arc of radius MA = r√5/2, which
leads to a point R such that AR equals the pentagon's side length.

Author: Manim Coding Skill Agent
Date: 2025-11-27
"""

from manim import *
import numpy as np

# Import all parameters from params module
from params import (
    COLORS, TEXT, DIMENSIONS, POSITIONS, TIMING, SIZES, OPACITY, GEOMETRY,
    get_pentagon_vertices, get_circle_point, get_label_position
)


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_label(text_key, position):
    """
    Create a text label at the given position.
    Uses Text instead of MathTex for better compatibility.

    Args:
        text_key: Key in TEXT dict
        position: Position for the label

    Returns:
        Text mobject
    """
    return Text(
        TEXT[text_key],
        font_size=SIZES["label_font_size"],
        color=COLORS["label_text"]
    ).move_to(position)


class IntroScene(Scene):
    """
    Scene 1: Introduction and Setup

    Displays the title and creates the base circle with center point O.
    This establishes the foundation for all subsequent construction steps.
    """

    def construct(self):
        # Create title and subtitle
        title = Text(
            TEXT["intro_title"],
            font_size=SIZES["title_font_size"],
            color=COLORS["title_text"]
        ).move_to(POSITIONS["title_position"])

        subtitle = Text(
            TEXT["intro_subtitle"],
            font_size=SIZES["subtitle_font_size"],
            color=COLORS["label_text"]
        ).move_to(POSITIONS["subtitle_position"])

        # Animate title appearance
        self.play(
            Write(title, run_time=TIMING["write_text"]),
        )
        self.play(
            FadeIn(subtitle, run_time=TIMING["fade_in"]),
        )
        self.wait(TIMING["pause_medium"])

        # Fade out title and subtitle
        self.play(
            FadeOut(title, run_time=TIMING["fade_out"]),
            FadeOut(subtitle, run_time=TIMING["fade_out"]),
        )

        # Create the main circle
        circle = Circle(
            radius=DIMENSIONS["circle_radius"],
            color=COLORS["circle"],
            stroke_width=DIMENSIONS["circle_stroke_width"]
        ).move_to(POSITIONS["circle_center"])

        # Create center point O
        center_dot = Dot(
            POSITIONS["circle_center"],
            radius=DIMENSIONS["center_point_radius"],
            color=COLORS["center_point"]
        )

        # Create label for center
        label_O = create_label("label_O", get_label_position(POSITIONS["circle_center"], "label_offset_O"))

        # Animate circle and center point
        self.play(
            Create(circle, run_time=TIMING["draw_circle"]),
        )
        self.play(
            FadeIn(center_dot, run_time=TIMING["create_point"]),
            Write(label_O, run_time=TIMING["write_text"]),
        )

        self.wait(TIMING["pause_long"])


class PerpendicularDiameters(Scene):
    """
    Scene 2: Creating Perpendicular Diameters

    Constructs horizontal diameter (X to Y) and vertical diameter (Z to A).
    These perpendicular diameters divide the circle into four equal quadrants
    and establish the reference frame for the construction.
    """

    def construct(self):
        # Recreate circle and center from previous scene
        circle = Circle(
            radius=DIMENSIONS["circle_radius"],
            color=COLORS["circle"],
            stroke_width=DIMENSIONS["circle_stroke_width"]
        ).move_to(POSITIONS["circle_center"])

        center_dot = Dot(
            POSITIONS["circle_center"],
            radius=DIMENSIONS["center_point_radius"],
            color=COLORS["center_point"]
        )

        label_O = create_label("label_O", get_label_position(POSITIONS["circle_center"], "label_offset_O"))

        # Add circle and center without animation (continuing from previous scene)
        self.add(circle, center_dot, label_O)

        # Calculate diameter endpoints
        r = DIMENSIONS["circle_radius"]
        center = POSITIONS["circle_center"]

        point_X = center + LEFT * r  # Left
        point_Y = center + RIGHT * r  # Right
        point_Z = center + DOWN * r  # Bottom
        point_A = center + UP * r    # Top

        # Create horizontal diameter (X to Y)
        horizontal_diameter = Line(
            point_X, point_Y,
            color=COLORS["horizontal_diameter"],
            stroke_width=DIMENSIONS["diameter_stroke_width"]
        )

        # Create vertical diameter (Z to A)
        vertical_diameter = Line(
            point_Z, point_A,
            color=COLORS["vertical_diameter"],
            stroke_width=DIMENSIONS["diameter_stroke_width"]
        )

        # Create endpoint dots
        dot_X = Dot(point_X, radius=DIMENSIONS["point_radius"], color=COLORS["diameter_points"])
        dot_Y = Dot(point_Y, radius=DIMENSIONS["point_radius"], color=COLORS["diameter_points"])
        dot_Z = Dot(point_Z, radius=DIMENSIONS["point_radius"], color=COLORS["diameter_points"])
        dot_A = Dot(point_A, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])

        # Create labels
        label_X = create_label("label_X", get_label_position(point_X, "label_offset_X"))
        label_Y = create_label("label_Y", get_label_position(point_Y, "label_offset_Y"))
        label_Z = create_label("label_Z", get_label_position(point_Z, "label_offset_Z"))
        label_A = create_label("label_A", get_label_position(point_A, "label_offset_A"))

        # Show step description
        step_text = Text(
            TEXT["step_perpendicular"],
            font_size=SIZES["step_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["step_description_position"])

        self.play(FadeIn(step_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_short"])

        # Draw horizontal diameter
        self.play(
            Create(horizontal_diameter, run_time=TIMING["draw_line"]),
            FadeIn(dot_X, run_time=TIMING["create_point"]),
            FadeIn(dot_Y, run_time=TIMING["create_point"]),
        )
        self.play(
            Write(label_X, run_time=TIMING["write_text"]),
            Write(label_Y, run_time=TIMING["write_text"]),
        )

        self.wait(TIMING["pause_short"])

        # Draw vertical diameter
        self.play(
            Create(vertical_diameter, run_time=TIMING["draw_line"]),
            FadeIn(dot_Z, run_time=TIMING["create_point"]),
            FadeIn(dot_A, run_time=TIMING["create_point"]),
        )
        self.play(
            Write(label_Z, run_time=TIMING["write_text"]),
            Write(label_A, run_time=TIMING["write_text"]),
        )

        self.wait(TIMING["pause_medium"])
        self.play(FadeOut(step_text, run_time=TIMING["fade_out"]))
        self.wait(TIMING["pause_short"])


class FindMidpoint(Scene):
    """
    Scene 3: Finding the Midpoint

    Finds the midpoint M of radius OY using compass construction.
    This midpoint is crucial for the next step where we construct
    the golden ratio arc.
    """

    def construct(self):
        # Recreate elements from previous scenes
        r = DIMENSIONS["circle_radius"]
        center = POSITIONS["circle_center"]

        circle = Circle(
            radius=r,
            color=COLORS["circle"],
            stroke_width=DIMENSIONS["circle_stroke_width"]
        ).move_to(center)

        center_dot = Dot(center, radius=DIMENSIONS["center_point_radius"], color=COLORS["center_point"])
        label_O = create_label("label_O", get_label_position(center, "label_offset_O"))

        point_Y = center + RIGHT * r
        horizontal_diameter = Line(center + LEFT * r, point_Y, color=COLORS["horizontal_diameter"], stroke_width=DIMENSIONS["diameter_stroke_width"])
        vertical_diameter = Line(center + DOWN * r, center + UP * r, color=COLORS["vertical_diameter"], stroke_width=DIMENSIONS["diameter_stroke_width"])

        dot_Y = Dot(point_Y, radius=DIMENSIONS["point_radius"], color=COLORS["diameter_points"])
        label_Y = create_label("label_Y", get_label_position(point_Y, "label_offset_Y"))

        point_A = center + UP * r
        dot_A = Dot(point_A, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_A = create_label("label_A", get_label_position(point_A, "label_offset_A"))

        # Add existing elements
        self.add(circle, center_dot, label_O, horizontal_diameter, vertical_diameter, dot_Y, label_Y, dot_A, label_A)

        # Show step description
        step_text = Text(
            TEXT["step_midpoint"],
            font_size=SIZES["step_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["step_description_position"])

        self.play(FadeIn(step_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_short"])

        # Highlight the radius OY
        radius_OY = Line(
            center, point_Y,
            color=COLORS["construction_lines"],
            stroke_width=DIMENSIONS["construction_line_width"] + 2
        )
        self.play(Create(radius_OY, run_time=TIMING["draw_line"]))
        self.play(Indicate(radius_OY, color=COLORS["golden_ratio_highlight"], run_time=TIMING["indicate"]))

        # Calculate midpoint M
        point_M = center + RIGHT * (r / 2)

        # Show compass construction of midpoint (simplified: show arcs from O and Y)
        # Arc from O
        arc_from_O = Arc(
            radius=r / 2 + 0.5,
            start_angle=-PI / 6,
            angle=PI / 3,
            arc_center=center,
            color=COLORS["construction_arcs"],
            stroke_width=DIMENSIONS["arc_stroke_width"]
        ).set_opacity(OPACITY["construction_arc_active"])

        # Arc from Y
        arc_from_Y = Arc(
            radius=r / 2 + 0.5,
            start_angle=PI - PI / 6,
            angle=PI / 3,
            arc_center=point_Y,
            color=COLORS["construction_arcs"],
            stroke_width=DIMENSIONS["arc_stroke_width"]
        ).set_opacity(OPACITY["construction_arc_active"])

        self.play(
            Create(arc_from_O, run_time=TIMING["draw_arc"] * 0.6),
            Create(arc_from_Y, run_time=TIMING["draw_arc"] * 0.6),
        )

        # Create midpoint M
        dot_M = Dot(point_M, radius=DIMENSIONS["point_radius"], color=COLORS["midpoint"])
        label_M = create_label("label_M", get_label_position(point_M, "label_offset_M"))

        self.play(
            FadeIn(dot_M, scale=SIZES["indicate_scale_factor"], run_time=TIMING["create_point"]),
        )
        self.play(Write(label_M, run_time=TIMING["write_text"]))

        # Show annotation
        annotation = Text(
            TEXT["annotation_midpoint"],
            font_size=SIZES["annotation_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["annotation_position"])

        self.play(FadeIn(annotation, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_medium"])

        # Fade out construction arcs and annotation
        self.play(
            FadeOut(arc_from_O, run_time=TIMING["fade_out"]),
            FadeOut(arc_from_Y, run_time=TIMING["fade_out"]),
            FadeOut(annotation, run_time=TIMING["fade_out"]),
            FadeOut(step_text, run_time=TIMING["fade_out"]),
            radius_OY.animate.set_opacity(OPACITY["construction_line_faded"])
        )

        self.wait(TIMING["pause_short"])


class GoldenArc(Scene):
    """
    Scene 4: The Golden Ratio Arc

    This is the key step in the construction. We draw an arc from M with
    radius MA, which equals r√5/2. This arc intersects the horizontal
    diameter at point R, where AR equals the side length of the pentagon.
    This step embeds the golden ratio into the construction.
    """

    def construct(self):
        # Recreate elements from previous scenes
        r = DIMENSIONS["circle_radius"]
        center = POSITIONS["circle_center"]

        circle = Circle(radius=r, color=COLORS["circle"], stroke_width=DIMENSIONS["circle_stroke_width"]).move_to(center)
        center_dot = Dot(center, radius=DIMENSIONS["center_point_radius"], color=COLORS["center_point"])
        label_O = create_label("label_O", get_label_position(center, "label_offset_O"))

        horizontal_diameter = Line(center + LEFT * r, center + RIGHT * r, color=COLORS["horizontal_diameter"], stroke_width=DIMENSIONS["diameter_stroke_width"])
        vertical_diameter = Line(center + DOWN * r, center + UP * r, color=COLORS["vertical_diameter"], stroke_width=DIMENSIONS["diameter_stroke_width"])

        point_A = center + UP * r
        dot_A = Dot(point_A, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_A = create_label("label_A", get_label_position(point_A, "label_offset_A"))

        point_M = center + RIGHT * (r / 2)
        dot_M = Dot(point_M, radius=DIMENSIONS["point_radius"], color=COLORS["midpoint"])
        label_M = create_label("label_M", get_label_position(point_M, "label_offset_M"))

        # Add existing elements
        self.add(circle, center_dot, label_O, horizontal_diameter, vertical_diameter, dot_A, label_A, dot_M, label_M)

        # Show step description
        step_text = Text(
            TEXT["step_golden_arc"],
            font_size=SIZES["step_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["step_description_position"])

        self.play(FadeIn(step_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_short"])

        # Highlight M and A
        self.play(
            Indicate(dot_M, color=COLORS["midpoint"], scale_factor=SIZES["indicate_scale_factor"], run_time=TIMING["indicate"]),
            Indicate(dot_A, color=COLORS["pentagon_vertices"], scale_factor=SIZES["indicate_scale_factor"], run_time=TIMING["indicate"]),
        )

        # Draw construction line from M to A (showing compass radius)
        line_MA = DashedLine(
            point_M, point_A,
            color=COLORS["construction_lines"],
            stroke_width=DIMENSIONS["construction_line_width"]
        )
        self.play(Create(line_MA, run_time=TIMING["draw_line"]))

        # Calculate arc radius: MA = sqrt(r^2 + (r/2)^2) = r*sqrt(5)/2
        arc_radius = np.linalg.norm(point_A - point_M)

        # Calculate where arc intersects horizontal diameter
        # The arc from M with radius MA intersects the line OX at point R
        # R is to the left of O, at distance OR = (sqrt(5) - 1) * r / 2
        point_R = center + LEFT * ((np.sqrt(5) - 1) * r / 2)

        # Draw the golden arc from M
        # Arc goes from A down to intersect the horizontal diameter
        # Calculate angles for the arc
        angle_to_A = np.arctan2((point_A - point_M)[1], (point_A - point_M)[0])
        angle_to_R = np.arctan2((point_R - point_M)[1], (point_R - point_M)[0])

        # Ensure we go clockwise from A to R
        if angle_to_R > angle_to_A:
            angle_to_R -= 2 * PI

        golden_arc = Arc(
            radius=arc_radius,
            start_angle=angle_to_A,
            angle=angle_to_R - angle_to_A,
            arc_center=point_M,
            color=COLORS["golden_ratio_highlight"],
            stroke_width=DIMENSIONS["arc_stroke_width"] + 2
        )

        self.play(Create(golden_arc, run_time=TIMING["compass_draw_arc"]))

        # Create point R
        dot_R = Dot(point_R, radius=DIMENSIONS["point_radius"], color=COLORS["golden_point"])
        label_R = create_label("label_R", get_label_position(point_R, "label_offset_R"))

        self.play(
            FadeIn(dot_R, scale=SIZES["flash_scale_factor"], run_time=TIMING["create_point"]),
        )
        self.play(Write(label_R, run_time=TIMING["write_text"]))

        # Draw line AR (the pentagon side length)
        line_AR = Line(
            point_A, point_R,
            color=COLORS["pentagon_outline"],
            stroke_width=DIMENSIONS["pentagon_stroke_width"]
        )

        self.play(Create(line_AR, run_time=TIMING["draw_line"]))

        # Show annotation about the golden ratio
        annotation = Text(
            TEXT["annotation_side_length"],
            font_size=SIZES["annotation_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["annotation_position"])

        self.play(FadeIn(annotation, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_long"])

        # Fade out construction elements but keep AR and points
        self.play(
            FadeOut(line_MA, run_time=TIMING["fade_out"]),
            golden_arc.animate.set_opacity(OPACITY["construction_arc_faded"]),
            FadeOut(annotation, run_time=TIMING["fade_out"]),
            FadeOut(step_text, run_time=TIMING["fade_out"]),
        )

        self.wait(TIMING["pause_short"])


class MarkVertices(Scene):
    """
    Scene 5: Mark Pentagon Vertices

    Using AR as the compass radius, we mark all five vertices of the pentagon
    around the circle. Starting from A, we mark B, then from B we mark C,
    and so on until all five vertices are established.
    """

    def construct(self):
        # Recreate elements from previous scenes
        r = DIMENSIONS["circle_radius"]
        center = POSITIONS["circle_center"]

        circle = Circle(radius=r, color=COLORS["circle"], stroke_width=DIMENSIONS["circle_stroke_width"]).move_to(center)
        center_dot = Dot(center, radius=DIMENSIONS["center_point_radius"], color=COLORS["center_point"])
        label_O = create_label("label_O", get_label_position(center, "label_offset_O"))

        # Fade horizontal and vertical diameters
        horizontal_diameter = Line(center + LEFT * r, center + RIGHT * r, color=COLORS["horizontal_diameter"], stroke_width=DIMENSIONS["diameter_stroke_width"]).set_opacity(OPACITY["construction_line_faded"])
        vertical_diameter = Line(center + DOWN * r, center + UP * r, color=COLORS["vertical_diameter"], stroke_width=DIMENSIONS["diameter_stroke_width"]).set_opacity(OPACITY["construction_line_faded"])

        # Calculate pentagon vertices
        vertices = get_pentagon_vertices(r, start_angle=PI / 2)
        point_A, point_B, point_C, point_D, point_E = vertices

        # A is already marked
        dot_A = Dot(point_A, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_A = create_label("label_A", get_label_position(point_A, "label_offset_A"))

        # Add existing elements
        self.add(circle, center_dot, label_O, horizontal_diameter, vertical_diameter, dot_A, label_A)

        # Show step description
        step_text = Text(
            TEXT["step_mark_vertices"],
            font_size=SIZES["step_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["step_description_position"])

        self.play(FadeIn(step_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_short"])

        # Pentagon side length (distance AR, which equals distance between adjacent vertices)
        side_length = np.linalg.norm(point_B - point_A)

        # Mark vertex B from A
        arc_A_to_B = Arc(
            radius=side_length,
            start_angle=0,  # Start from right
            angle=2 * PI / 5,  # 72 degrees
            arc_center=point_A,
            color=COLORS["construction_arcs"],
            stroke_width=DIMENSIONS["arc_stroke_width"]
        )

        self.play(Create(arc_A_to_B, run_time=TIMING["draw_arc"]))

        dot_B = Dot(point_B, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_B = create_label("label_B", get_label_position(point_B, "label_offset_B"))

        self.play(
            FadeIn(dot_B, scale=SIZES["indicate_scale_factor"], run_time=TIMING["create_point"]),
            Write(label_B, run_time=TIMING["write_text"]),
        )

        # Fade the arc
        self.play(arc_A_to_B.animate.set_opacity(OPACITY["construction_arc_faded"]))

        # Mark vertex C from B
        arc_B_to_C = Arc(
            radius=side_length,
            start_angle=PI / 2 + 2 * PI / 5,
            angle=2 * PI / 5,
            arc_center=point_B,
            color=COLORS["construction_arcs"],
            stroke_width=DIMENSIONS["arc_stroke_width"]
        )

        self.play(Create(arc_B_to_C, run_time=TIMING["draw_arc"]))

        dot_C = Dot(point_C, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_C = create_label("label_C", get_label_position(point_C, "label_offset_C"))

        self.play(
            FadeIn(dot_C, scale=SIZES["indicate_scale_factor"], run_time=TIMING["create_point"]),
            Write(label_C, run_time=TIMING["write_text"]),
        )

        self.play(arc_B_to_C.animate.set_opacity(OPACITY["construction_arc_faded"]))

        # Mark vertex D from C
        arc_C_to_D = Arc(
            radius=side_length,
            start_angle=PI / 2 + 4 * PI / 5,
            angle=2 * PI / 5,
            arc_center=point_C,
            color=COLORS["construction_arcs"],
            stroke_width=DIMENSIONS["arc_stroke_width"]
        )

        self.play(Create(arc_C_to_D, run_time=TIMING["draw_arc"]))

        dot_D = Dot(point_D, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_D = create_label("label_D", get_label_position(point_D, "label_offset_D"))

        self.play(
            FadeIn(dot_D, scale=SIZES["indicate_scale_factor"], run_time=TIMING["create_point"]),
            Write(label_D, run_time=TIMING["write_text"]),
        )

        self.play(arc_C_to_D.animate.set_opacity(OPACITY["construction_arc_faded"]))

        # Mark vertex E from D
        arc_D_to_E = Arc(
            radius=side_length,
            start_angle=PI / 2 + 6 * PI / 5,
            angle=2 * PI / 5,
            arc_center=point_D,
            color=COLORS["construction_arcs"],
            stroke_width=DIMENSIONS["arc_stroke_width"]
        )

        self.play(Create(arc_D_to_E, run_time=TIMING["draw_arc"]))

        dot_E = Dot(point_E, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        label_E = create_label("label_E", get_label_position(point_E, "label_offset_E"))

        self.play(
            FadeIn(dot_E, scale=SIZES["indicate_scale_factor"], run_time=TIMING["create_point"]),
            Write(label_E, run_time=TIMING["write_text"]),
        )

        self.play(arc_D_to_E.animate.set_opacity(OPACITY["construction_arc_faded"]))

        # Verification: show arc from E back to A
        arc_E_to_A = Arc(
            radius=side_length,
            start_angle=PI / 2 + 8 * PI / 5,
            angle=2 * PI / 5,
            arc_center=point_E,
            color=COLORS["golden_ratio_highlight"],
            stroke_width=DIMENSIONS["arc_stroke_width"] + 1
        )

        self.play(Create(arc_E_to_A, run_time=TIMING["draw_arc"]))
        self.play(Indicate(dot_A, color=COLORS["golden_ratio_highlight"], scale_factor=SIZES["indicate_scale_factor"], run_time=TIMING["indicate"]))

        self.wait(TIMING["pause_medium"])

        # Fade out construction arcs
        self.play(
            FadeOut(arc_A_to_B, run_time=TIMING["fade_out"]),
            FadeOut(arc_B_to_C, run_time=TIMING["fade_out"]),
            FadeOut(arc_C_to_D, run_time=TIMING["fade_out"]),
            FadeOut(arc_D_to_E, run_time=TIMING["fade_out"]),
            FadeOut(arc_E_to_A, run_time=TIMING["fade_out"]),
            FadeOut(step_text, run_time=TIMING["fade_out"]),
        )

        self.wait(TIMING["pause_short"])


class CompletePentagon(Scene):
    """
    Scene 6: Complete the Pentagon

    Connect the five vertices with straight lines to form the regular pentagon.
    This is the satisfying conclusion of the construction.
    """

    def construct(self):
        # Recreate elements from previous scenes
        r = DIMENSIONS["circle_radius"]
        center = POSITIONS["circle_center"]

        circle = Circle(radius=r, color=COLORS["circle"], stroke_width=DIMENSIONS["circle_stroke_width"]).move_to(center).set_opacity(OPACITY["circle_faded"])
        center_dot = Dot(center, radius=DIMENSIONS["center_point_radius"], color=COLORS["center_point"]).set_opacity(OPACITY["construction_line_faded"])
        label_O = create_label("label_O", get_label_position(center, "label_offset_O")).set_opacity(OPACITY["label_faded"])

        # Get pentagon vertices
        vertices = get_pentagon_vertices(r, start_angle=PI / 2)
        point_A, point_B, point_C, point_D, point_E = vertices

        # Create vertex dots and labels
        dot_A = Dot(point_A, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_B = Dot(point_B, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_C = Dot(point_C, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_D = Dot(point_D, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_E = Dot(point_E, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])

        label_A = create_label("label_A", get_label_position(point_A, "label_offset_A"))
        label_B = create_label("label_B", get_label_position(point_B, "label_offset_B"))
        label_C = create_label("label_C", get_label_position(point_C, "label_offset_C"))
        label_D = create_label("label_D", get_label_position(point_D, "label_offset_D"))
        label_E = create_label("label_E", get_label_position(point_E, "label_offset_E"))

        # Add existing elements
        self.add(circle, center_dot, label_O)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_E)
        self.add(label_A, label_B, label_C, label_D, label_E)

        # Show step description
        step_text = Text(
            TEXT["step_complete"],
            font_size=SIZES["step_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["step_description_position"])

        self.play(FadeIn(step_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_short"])

        # Create pentagon sides
        side_AB = Line(point_A, point_B, color=COLORS["pentagon_outline"], stroke_width=DIMENSIONS["pentagon_stroke_width"])
        side_BC = Line(point_B, point_C, color=COLORS["pentagon_outline"], stroke_width=DIMENSIONS["pentagon_stroke_width"])
        side_CD = Line(point_C, point_D, color=COLORS["pentagon_outline"], stroke_width=DIMENSIONS["pentagon_stroke_width"])
        side_DE = Line(point_D, point_E, color=COLORS["pentagon_outline"], stroke_width=DIMENSIONS["pentagon_stroke_width"])
        side_EA = Line(point_E, point_A, color=COLORS["pentagon_outline"], stroke_width=DIMENSIONS["pentagon_stroke_width"])

        # Draw sides one by one
        self.play(Create(side_AB, run_time=TIMING["draw_line"]))
        self.play(Create(side_BC, run_time=TIMING["draw_line"]))
        self.play(Create(side_CD, run_time=TIMING["draw_line"]))
        self.play(Create(side_DE, run_time=TIMING["draw_line"]))
        self.play(Create(side_EA, run_time=TIMING["draw_line"]))

        self.wait(TIMING["pause_medium"])

        # Create filled pentagon and transform
        pentagon = Polygon(
            *vertices,
            color=COLORS["pentagon_outline"],
            fill_color=COLORS["pentagon_fill"],
            fill_opacity=OPACITY["pentagon_fill"],
            stroke_width=DIMENSIONS["pentagon_stroke_width"]
        )

        # Group all sides
        sides_group = VGroup(side_AB, side_BC, side_CD, side_DE, side_EA)

        self.play(
            Transform(sides_group, pentagon, run_time=TIMING["transform"]),
        )

        # Highlight the completed pentagon
        self.play(
            Indicate(pentagon, color=COLORS["golden_ratio_highlight"], scale_factor=1.1, run_time=TIMING["indicate"] * 1.5),
        )

        self.wait(TIMING["pause_long"])
        self.play(FadeOut(step_text, run_time=TIMING["fade_out"]))
        self.wait(TIMING["pause_short"])


class Verification(Scene):
    """
    Scene 7: Verification (Optional)

    Verify that the pentagon is regular by showing:
    1. All interior angles are 108 degrees
    2. All sides are equal length
    3. Connection to the golden ratio
    """

    def construct(self):
        # Recreate elements from previous scenes
        r = DIMENSIONS["circle_radius"]
        center = POSITIONS["circle_center"]

        # Get pentagon vertices
        vertices = get_pentagon_vertices(r, start_angle=PI / 2)
        point_A, point_B, point_C, point_D, point_E = vertices

        # Create pentagon
        pentagon = Polygon(
            *vertices,
            color=COLORS["pentagon_outline"],
            fill_color=COLORS["pentagon_fill"],
            fill_opacity=OPACITY["pentagon_fill"],
            stroke_width=DIMENSIONS["pentagon_stroke_width"]
        )

        # Create vertex dots and labels
        dot_A = Dot(point_A, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_B = Dot(point_B, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_C = Dot(point_C, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_D = Dot(point_D, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])
        dot_E = Dot(point_E, radius=DIMENSIONS["vertex_point_radius"], color=COLORS["pentagon_vertices"])

        label_A = create_label("label_A", get_label_position(point_A, "label_offset_A"))
        label_B = create_label("label_B", get_label_position(point_B, "label_offset_B"))
        label_C = create_label("label_C", get_label_position(point_C, "label_offset_C"))
        label_D = create_label("label_D", get_label_position(point_D, "label_offset_D"))
        label_E = create_label("label_E", get_label_position(point_E, "label_offset_E"))

        # Add elements
        self.add(pentagon)
        self.add(dot_A, dot_B, dot_C, dot_D, dot_E)
        self.add(label_A, label_B, label_C, label_D, label_E)

        # Show verification title
        verification_title = Text(
            "Verification: Regular Pentagon",
            font_size=SIZES["step_font_size"],
            color=COLORS["title_text"]
        ).move_to(POSITIONS["step_description_position"])

        self.play(FadeIn(verification_title, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_short"])

        # 1. Show angle at vertex A (108 degrees)
        angle_arc = Arc(
            radius=0.5,
            start_angle=2 * PI / 5,
            angle=3 * PI / 5,
            arc_center=point_A,
            color=COLORS["angle_arc"],
            stroke_width=3
        )

        angle_label = Text(
            "108°",  # Simplified from TEXT["annotation_interior_angle"]
            font_size=SIZES["annotation_font_size"],
            color=COLORS["angle_arc"]
        ).next_to(point_A, DOWN, buff=0.8)

        self.play(Create(angle_arc, run_time=TIMING["draw_arc"]))
        self.play(Write(angle_label, run_time=TIMING["write_text"]))
        self.wait(TIMING["pause_medium"])

        # 2. Show all angles are equal
        all_angles_text = Text(
            TEXT["verification_equal_angles"],
            font_size=SIZES["annotation_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["annotation_position"])

        self.play(FadeIn(all_angles_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_medium"])

        self.play(
            FadeOut(angle_arc, run_time=TIMING["fade_out"]),
            FadeOut(angle_label, run_time=TIMING["fade_out"]),
            FadeOut(all_angles_text, run_time=TIMING["fade_out"]),
        )

        # 3. Show side length equality with tick marks
        # Add tick marks to all sides
        tick_marks = VGroup()
        for i in range(5):
            v1 = vertices[i]
            v2 = vertices[(i + 1) % 5]
            midpoint = (v1 + v2) / 2

            # Perpendicular direction
            direction = v2 - v1
            perp = np.array([-direction[1], direction[0], 0])
            perp = perp / np.linalg.norm(perp) * 0.15

            tick = Line(
                midpoint - perp, midpoint + perp,
                color=COLORS["measurement_line"],
                stroke_width=4
            )
            tick_marks.add(tick)

        self.play(Create(tick_marks, run_time=TIMING["draw_line"] * 1.5))

        equal_sides_text = Text(
            TEXT["verification_equal_sides"],
            font_size=SIZES["annotation_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["annotation_position"])

        self.play(FadeIn(equal_sides_text, run_time=TIMING["fade_in"]))
        self.wait(TIMING["pause_medium"])

        self.play(
            FadeOut(tick_marks, run_time=TIMING["fade_out"]),
            FadeOut(equal_sides_text, run_time=TIMING["fade_out"]),
        )

        # 4. Show golden ratio (draw one diagonal)
        diagonal_AC = Line(
            point_A, point_C,
            color=COLORS["golden_ratio_highlight"],
            stroke_width=DIMENSIONS["pentagon_stroke_width"] - 1
        )

        self.play(Create(diagonal_AC, run_time=TIMING["draw_line"]))

        # Golden ratio annotation
        phi_text = Text(
            "φ = (1 + √5)/2 ≈ 1.618",  # Simplified from TEXT["annotation_phi"]
            font_size=SIZES["annotation_font_size"],
            color=COLORS["golden_ratio_highlight"]
        ).move_to(POSITIONS["annotation_position"] + UP * 0.5)

        golden_ratio_text = Text(
            TEXT["verification_golden_ratio"],
            font_size=SIZES["annotation_font_size"],
            color=COLORS["annotation_text"]
        ).move_to(POSITIONS["annotation_position"] + DOWN * 0.5)

        self.play(
            Write(phi_text, run_time=TIMING["write_text"]),
            FadeIn(golden_ratio_text, run_time=TIMING["fade_in"]),
        )

        self.wait(TIMING["pause_long"])

        # Final rotation to show symmetry
        self.play(
            Rotate(
                VGroup(pentagon, dot_A, dot_B, dot_C, dot_D, dot_E, label_A, label_B, label_C, label_D, label_E, diagonal_AC),
                angle=2 * PI / 5,
                run_time=TIMING["transform"] * 2,
                rate_func=smooth
            )
        )

        self.wait(TIMING["pause_long"])


# =============================================================================
# MAIN SCENE - Combines all scenes in sequence
# =============================================================================

class PentagonConstruction(Scene):
    """
    Main scene that combines all construction steps into one continuous animation.
    This can be rendered as a single video showing the complete construction process.
    """

    def construct(self):
        # Run all scenes in sequence
        intro = IntroScene()
        intro.construct()

        perpendicular = PerpendicularDiameters()
        perpendicular.construct()

        midpoint = FindMidpoint()
        midpoint.construct()

        golden = GoldenArc()
        golden.construct()

        vertices = MarkVertices()
        vertices.construct()

        complete = CompletePentagon()
        complete.construct()

        verify = Verification()
        verify.construct()
