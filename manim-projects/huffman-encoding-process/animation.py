"""
Huffman Encoding Process Animation

Visualizes how Huffman encoding compresses data using a binary tree.
Focuses on the encoding process: tree traversal, bit generation, and compression.

Scenes:
1. PreBuiltTreeScene: Show the Huffman tree structure
2. EncodeSingleCharScene: Detailed walkthrough of encoding one character
3. EncodeFullMessageScene: Encode entire message character by character
4. BitComparisonScene: Compare original ASCII vs Huffman encoded bits
5. CompressionStatsScene: Calculate and display compression ratio

Message: "AABBBCCCC"
Tree: Root(9) -> Left(4) [A(2), B(3)], Right C(4)
Codes: A=00, B=01, C=1
Compression: 72 bits → 14 bits (80.6%)
"""

from manim import *
import numpy as np

# Import all parameters
from params import (
    COLORS, DIMENSIONS, POSITIONS, TEXT, TIMING, SIZES, OPACITY,
    HUFFMAN_DATA, COMPRESSION_STATS,
    get_tree_positions, get_char_code, get_path_for_char,
    char_to_ascii_binary, get_encoding_table_data
)

# =============================================================================
# HELPER FUNCTIONS AND CLASSES
# =============================================================================

class HuffmanTreeBuilder:
    """Helper class to build and manage the Huffman tree visualization"""

    @staticmethod
    def create_tree():
        """
        Create the complete Huffman tree structure.

        Returns:
            VGroup: The complete tree with nodes, edges, and labels
        """
        positions = get_tree_positions()

        # Create nodes
        root = Circle(
            radius=DIMENSIONS["internal_node_radius"],
            color=COLORS["internal_node"],
            fill_color=COLORS["internal_node_fill"],
            fill_opacity=OPACITY["node_fill"],
            stroke_width=DIMENSIONS["edge_width"]
        ).move_to(positions["root"])

        left_internal = Circle(
            radius=DIMENSIONS["internal_node_radius"],
            color=COLORS["internal_node"],
            fill_color=COLORS["internal_node_fill"],
            fill_opacity=OPACITY["node_fill"],
            stroke_width=DIMENSIONS["edge_width"]
        ).move_to(positions["left_internal"])

        leaf_A = Rectangle(
            width=DIMENSIONS["leaf_node_width"],
            height=DIMENSIONS["leaf_node_height"],
            color=COLORS["leaf_node"],
            fill_color=COLORS["leaf_node_fill"],
            fill_opacity=OPACITY["node_fill"],
            stroke_width=DIMENSIONS["edge_width"]
        ).move_to(positions["leaf_A"])

        leaf_B = Rectangle(
            width=DIMENSIONS["leaf_node_width"],
            height=DIMENSIONS["leaf_node_height"],
            color=COLORS["leaf_node"],
            fill_color=COLORS["leaf_node_fill"],
            fill_opacity=OPACITY["node_fill"],
            stroke_width=DIMENSIONS["edge_width"]
        ).move_to(positions["leaf_B"])

        leaf_C = Rectangle(
            width=DIMENSIONS["leaf_node_width"],
            height=DIMENSIONS["leaf_node_height"],
            color=COLORS["leaf_node"],
            fill_color=COLORS["leaf_node_fill"],
            fill_opacity=OPACITY["node_fill"],
            stroke_width=DIMENSIONS["edge_width"]
        ).move_to(positions["right_leaf_C"])

        # Create node labels
        root_label = Text(TEXT["root_label"], font_size=SIZES["node_label_font"], color=COLORS["node_text"])
        root_label.move_to(root.get_center())

        left_label = Text(TEXT["left_internal_label"], font_size=SIZES["node_label_font"], color=COLORS["node_text"])
        left_label.move_to(left_internal.get_center())

        leaf_A_label = Text(TEXT["leaf_A_label"], font_size=SIZES["node_label_font"], color=COLORS["node_text"])
        leaf_A_label.move_to(leaf_A.get_center())

        leaf_B_label = Text(TEXT["leaf_B_label"], font_size=SIZES["node_label_font"], color=COLORS["node_text"])
        leaf_B_label.move_to(leaf_B.get_center())

        leaf_C_label = Text(TEXT["leaf_C_label"], font_size=SIZES["node_label_font"], color=COLORS["node_text"])
        leaf_C_label.move_to(leaf_C.get_center())

        # Create edges
        edge_root_left = Line(
            root.get_bottom() + LEFT * 0.2,
            left_internal.get_top(),
            color=COLORS["edge_inactive"],
            stroke_width=DIMENSIONS["edge_width"],
            stroke_opacity=OPACITY["edge_inactive"]
        )

        edge_root_right = Line(
            root.get_bottom() + RIGHT * 0.2,
            leaf_C.get_top(),
            color=COLORS["edge_inactive"],
            stroke_width=DIMENSIONS["edge_width"],
            stroke_opacity=OPACITY["edge_inactive"]
        )

        edge_left_A = Line(
            left_internal.get_bottom() + LEFT * 0.15,
            leaf_A.get_top(),
            color=COLORS["edge_inactive"],
            stroke_width=DIMENSIONS["edge_width"],
            stroke_opacity=OPACITY["edge_inactive"]
        )

        edge_left_B = Line(
            left_internal.get_bottom() + RIGHT * 0.15,
            leaf_B.get_top(),
            color=COLORS["edge_inactive"],
            stroke_width=DIMENSIONS["edge_width"],
            stroke_opacity=OPACITY["edge_inactive"]
        )

        # Create edge labels (0 and 1)
        label_0_root = Text("0", font_size=SIZES["legend_font"], color=COLORS["edge_label"])
        label_0_root.next_to(edge_root_left, LEFT, buff=0.1)

        label_1_root = Text("1", font_size=SIZES["legend_font"], color=COLORS["edge_label"])
        label_1_root.next_to(edge_root_right, RIGHT, buff=0.1)

        label_0_left = Text("0", font_size=SIZES["legend_font"], color=COLORS["edge_label"])
        label_0_left.next_to(edge_left_A, LEFT, buff=0.1)

        label_1_left = Text("1", font_size=SIZES["legend_font"], color=COLORS["edge_label"])
        label_1_left.next_to(edge_left_B, RIGHT, buff=0.1)

        # Group everything
        tree = VGroup(
            # Edges first (drawn behind nodes)
            edge_root_left, edge_root_right, edge_left_A, edge_left_B,
            label_0_root, label_1_root, label_0_left, label_1_left,
            # Nodes
            root, left_internal, leaf_A, leaf_B, leaf_C,
            # Labels
            root_label, left_label, leaf_A_label, leaf_B_label, leaf_C_label
        )

        # Store references for later use
        tree.nodes = {
            "root": root,
            "left_internal": left_internal,
            "leaf_A": leaf_A,
            "leaf_B": leaf_B,
            "leaf_C": leaf_C
        }

        tree.edges = {
            "root_left": edge_root_left,
            "root_right": edge_root_right,
            "left_A": edge_left_A,
            "left_B": edge_left_B
        }

        tree.edge_labels = {
            "0_root": label_0_root,
            "1_root": label_1_root,
            "0_left": label_0_left,
            "1_left": label_1_left
        }

        return tree

    @staticmethod
    def get_edges_for_path(tree, char):
        """
        Get the edges that form the path for a character.

        Args:
            tree: The tree VGroup
            char: Character to encode ('A', 'B', or 'C')

        Returns:
            list: List of edge objects
        """
        paths = {
            "A": [tree.edges["root_left"], tree.edges["left_A"]],
            "B": [tree.edges["root_left"], tree.edges["left_B"]],
            "C": [tree.edges["root_right"]]
        }
        return paths.get(char, [])

    @staticmethod
    def get_nodes_for_path(tree, char):
        """
        Get the nodes in the path for a character.

        Args:
            tree: The tree VGroup
            char: Character to encode

        Returns:
            list: List of node objects
        """
        paths = {
            "A": [tree.nodes["root"], tree.nodes["left_internal"], tree.nodes["leaf_A"]],
            "B": [tree.nodes["root"], tree.nodes["left_internal"], tree.nodes["leaf_B"]],
            "C": [tree.nodes["root"], tree.nodes["leaf_C"]]
        }
        return paths.get(char, [])


def create_legend():
    """Create the legend box explaining encoding rules"""
    legend_box = Rectangle(
        width=DIMENSIONS["legend_box_width"],
        height=DIMENSIONS["legend_box_height"],
        color=COLORS["legend_box"],
        fill_color=COLORS["legend_box"],
        fill_opacity=OPACITY["legend_box"]
    )

    title = Text(TEXT["legend_title"], font_size=SIZES["legend_font"], color=COLORS["legend_text"])
    left_rule = Text(TEXT["legend_left"], font_size=SIZES["legend_font"] - 4, color=COLORS["legend_text"])
    right_rule = Text(TEXT["legend_right"], font_size=SIZES["legend_font"] - 4, color=COLORS["legend_text"])
    path_rule = Text(TEXT["legend_path"], font_size=SIZES["legend_font"] - 4, color=COLORS["legend_text"])

    rules = VGroup(title, left_rule, right_rule, path_rule).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
    rules.move_to(legend_box.get_center())

    legend = VGroup(legend_box, rules)
    legend.move_to(POSITIONS["legend_position"])

    return legend


def create_code_builder():
    """Create the code builder box that shows bits being built"""
    code_box = Rectangle(
        width=2.5,
        height=1.0,
        color=COLORS["code_text"],
        stroke_width=2
    )

    code_text = Text("Code: ", font_size=SIZES["code_font"], color=WHITE)
    code_bits = Text("", font_size=SIZES["code_font"], color=COLORS["code_text"])

    code_display = VGroup(code_text, code_bits).arrange(RIGHT, buff=0.2)
    code_display.move_to(code_box.get_center())

    code_builder = VGroup(code_box, code_display)
    code_builder.move_to(POSITIONS["code_builder_position"])

    code_builder.bits = code_bits  # Store reference for updating

    return code_builder


# =============================================================================
# SCENE 1: PRE-BUILT HUFFMAN TREE PRESENTATION
# =============================================================================

class PreBuiltTreeScene(Scene):
    """
    Scene 1: Present the pre-built Huffman tree structure.

    Shows:
    - Complete tree with internal nodes and leaf nodes
    - Edge labels (0 for left, 1 for right)
    - Legend explaining the encoding rules
    - Message to be encoded
    """

    def construct(self):
        self.prebuilt_tree_animation()

    def prebuilt_tree_animation(self):
        """Animation for pre-built tree scene - can be called from any scene"""
        # Create tree
        tree = HuffmanTreeBuilder.create_tree()

        # Create legend
        legend = create_legend()

        # Create message display
        message_label = Text("Message:", font_size=SIZES["message_font"] - 8, color=WHITE)
        message_text = Text(TEXT["message"], font_size=SIZES["message_font"], color=COLORS["message_text"])
        message_display = VGroup(message_label, message_text).arrange(RIGHT, buff=0.5)
        message_display.move_to(POSITIONS["message_position"])

        # Animation sequence
        self.play(Create(tree), run_time=TIMING["tree_create"])
        self.wait(TIMING["pause_short"])

        self.play(FadeIn(legend), run_time=TIMING["legend_fadein"])
        self.wait(TIMING["pause_medium"])

        # Highlight each leaf node briefly
        for leaf_key in ["leaf_A", "leaf_B", "leaf_C"]:
            leaf = tree.nodes[leaf_key]
            self.play(Indicate(leaf, scale_factor=SIZES["indicate_scale"]), run_time=TIMING["node_indicate"])

        self.wait(TIMING["pause_short"])

        self.play(Write(message_display), run_time=TIMING["message_write"])
        self.wait(TIMING["pause_long"])


# =============================================================================
# SCENE 2: ENCODE SINGLE CHARACTER (DETAILED WALKTHROUGH)
# =============================================================================

class EncodeSingleCharScene(Scene):
    """
    Scene 2: Detailed walkthrough of encoding the character 'A'.

    Shows:
    - Starting at root node
    - Traversing left (adding '0')
    - Traversing left again (adding '0')
    - Arriving at leaf node 'A'
    - Final code: "00"
    """

    def construct(self):
        self.encode_single_char_animation()

    def encode_single_char_animation(self):
        # Create tree
        tree = HuffmanTreeBuilder.create_tree()
        self.add(tree)

        # Create character spotlight
        char_box = Rectangle(
            width=1.5,
            height=1.5,
            color=COLORS["message_active"],
            stroke_width=4
        )
        char_letter = Text("A", font_size=SIZES["message_font"] * 1.5, color=COLORS["message_active"])
        char_display = VGroup(char_box, char_letter)
        char_display.move_to(UP * 3 + LEFT * 4)

        # Create code builder
        code_builder = create_code_builder()

        # Show character and code builder
        self.play(FadeIn(char_display), FadeIn(code_builder), run_time=0.8)
        self.wait(TIMING["pause_short"])

        # Highlight character
        self.play(Indicate(char_display, scale_factor=SIZES["char_highlight_scale"]), run_time=TIMING["char_highlight"])
        self.wait(TIMING["pause_short"])

        # Start at root
        root_node = tree.nodes["root"]
        self.play(Indicate(root_node, color=COLORS["path_glow"], scale_factor=1.2), run_time=TIMING["node_pulse"])
        self.wait(TIMING["pause_short"])

        # First edge: root -> left (add '0')
        edge1 = tree.edges["root_left"]
        self.play(
            edge1.animate.set_color(COLORS["edge_active"]).set_stroke(width=DIMENSIONS["edge_active_width"], opacity=OPACITY["edge_active"]),
            run_time=TIMING["edge_highlight"]
        )

        # Add '0' to code
        bit_0_first = Text("0", font_size=SIZES["code_font"], color=COLORS["code_text"])
        bit_0_first.next_to(code_builder.bits, RIGHT, buff=0.1)
        self.play(FadeIn(bit_0_first, shift=DOWN * 0.3), run_time=TIMING["bit_appear"])
        code_builder.bits = VGroup(code_builder.bits, bit_0_first)
        self.wait(TIMING["pause_short"])

        # Move to left internal node
        left_node = tree.nodes["left_internal"]
        self.play(Indicate(left_node, color=COLORS["path_glow"], scale_factor=1.2), run_time=TIMING["node_pulse"])
        self.wait(TIMING["pause_short"])

        # Second edge: left_internal -> left (add '0')
        edge2 = tree.edges["left_A"]
        self.play(
            edge2.animate.set_color(COLORS["edge_active"]).set_stroke(width=DIMENSIONS["edge_active_width"], opacity=OPACITY["edge_active"]),
            run_time=TIMING["edge_highlight"]
        )

        # Add second '0' to code
        bit_0_second = Text("0", font_size=SIZES["code_font"], color=COLORS["code_text"])
        bit_0_second.next_to(code_builder.bits, RIGHT, buff=0.1)
        self.play(FadeIn(bit_0_second, shift=DOWN * 0.3), run_time=TIMING["bit_appear"])
        code_builder.bits = VGroup(code_builder.bits, bit_0_second)
        self.wait(TIMING["pause_short"])

        # Arrive at leaf A
        leaf_A = tree.nodes["leaf_A"]
        self.play(Flash(leaf_A, color=COLORS["path_highlight"], flash_radius=0.8), run_time=TIMING["code_flash"])
        self.wait(TIMING["pause_medium"])

        # Final result emphasis
        final_code = Text("Code for A = 00", font_size=SIZES["code_font"] + 4, color=COLORS["code_text"])
        final_code.move_to(DOWN * 2.5)
        self.play(Write(final_code), run_time=1.0)
        self.wait(TIMING["pause_long"])


# =============================================================================
# SCENE 3: ENCODE FULL MESSAGE CHARACTER BY CHARACTER
# =============================================================================

class EncodeFullMessageScene(Scene):
    """
    Scene 3: Encode the entire message "AABBBCCCC" character by character.

    Shows:
    - Original message with current character highlighted
    - Tree with path flashing for each character
    - Growing bit stream
    - Encoding table reference
    - Progress indicator
    """

    def construct(self):
        self.encode_full_message_animation()

    def encode_full_message_animation(self):
        # Create tree
        tree = HuffmanTreeBuilder.create_tree()
        tree.scale(0.7).to_edge(LEFT, buff=1.0)
        self.add(tree)

        # Create encoding table
        table_data = get_encoding_table_data()
        table = Table(
            table_data,
            col_labels=[Text(TEXT["table_header_char"], font_size=SIZES["table_font"]),
                       Text(TEXT["table_header_code"], font_size=SIZES["table_font"])],
            include_outer_lines=True
        ).scale(0.6)
        table.move_to(POSITIONS["encoding_table_position"])

        self.play(table.create(), run_time=1.0)
        self.wait(TIMING["pause_short"])

        # Create message display
        message = TEXT["message"]
        message_chars = VGroup(*[Text(c, font_size=SIZES["message_font"], color=WHITE) for c in message])
        message_chars.arrange(RIGHT, buff=0.3)
        message_chars.move_to(UP * 3)

        self.play(Write(message_chars), run_time=1.0)
        self.wait(TIMING["pause_short"])

        # Create bit stream display
        bit_stream_label = Text("Encoded:", font_size=SIZES["annotation_font"], color=WHITE)
        bit_stream_label.move_to(POSITIONS["bit_stream_position"] + LEFT * 4)
        self.play(Write(bit_stream_label))

        bit_stream = VGroup()
        bit_stream.next_to(bit_stream_label, RIGHT, buff=0.3)

        # Encode each character
        for i, char in enumerate(message):
            # Highlight current character
            self.play(
                message_chars[i].animate.set_color(COLORS["message_active"]).scale(SIZES["char_highlight_scale"]),
                run_time=TIMING["char_encode_fast"] * 0.3
            )

            # Get path and flash it
            edges = HuffmanTreeBuilder.get_edges_for_path(tree, char)
            leaf_node = HuffmanTreeBuilder.get_nodes_for_path(tree, char)[-1]

            # Flash path
            path_animations = [
                edge.animate.set_color(COLORS["path_highlight"]).set_stroke(width=DIMENSIONS["edge_active_width"])
                for edge in edges
            ]
            self.play(*path_animations, run_time=TIMING["path_flash_fast"])

            # Add code to bit stream
            code = get_char_code(char)
            code_text = Text(code, font_size=SIZES["bit_font"], color=COLORS["bit_stream"])
            if len(bit_stream) > 0:
                code_text.next_to(bit_stream, RIGHT, buff=0.15)
            else:
                code_text.move_to(bit_stream_label.get_right() + RIGHT * 0.5)

            self.play(FadeIn(code_text, shift=UP * 0.2), run_time=TIMING["bit_append"])
            bit_stream.add(code_text)

            # Reset path color
            reset_animations = [
                edge.animate.set_color(COLORS["edge_inactive"]).set_stroke(width=DIMENSIONS["edge_width"])
                for edge in edges
            ]
            self.play(*reset_animations, run_time=0.2)

            # Reset character color
            self.play(
                message_chars[i].animate.set_color(WHITE).scale(1 / SIZES["char_highlight_scale"]),
                run_time=0.2
            )

        # Final emphasis on complete bit stream
        self.play(
            bit_stream.animate.set_color(COLORS["code_text"]).scale(1.2),
            run_time=TIMING["pause_medium"]
        )
        self.wait(TIMING["pause_long"])


# =============================================================================
# SCENE 4: ORIGINAL VS COMPRESSED BIT COMPARISON
# =============================================================================

class BitComparisonScene(Scene):
    """
    Scene 4: Visual comparison of original ASCII bits vs Huffman encoded bits.

    Shows:
    - Left side: Original message in 8-bit ASCII (72 bits total)
    - Right side: Huffman encoded bits (14 bits total)
    - Visual bit blocks with color coding
    - Size labels and comparison
    """

    def construct(self):
        self.bit_comparison_animation()

    def bit_comparison_animation(self):
        # Title
        title = Text(TEXT["scene4_title"], font_size=SIZES["title_font"], color=COLORS["title_text"])
        title.to_edge(UP)
        self.play(Write(title), run_time=1.0)
        self.wait(TIMING["pause_short"])

        # Create split screen labels
        ascii_label = Text(TEXT["ascii_label"], font_size=SIZES["stats_font"], color=COLORS["ascii_label"])
        ascii_label.move_to(UP * 2.5 + LEFT * 3)

        huffman_label = Text(TEXT["huffman_label"], font_size=SIZES["stats_font"], color=COLORS["huffman_label"])
        huffman_label.move_to(UP * 2.5 + RIGHT * 3)

        self.play(
            FadeIn(ascii_label, shift=RIGHT),
            FadeIn(huffman_label, shift=LEFT),
            run_time=TIMING["split_screen"]
        )
        self.wait(TIMING["pause_short"])

        # Build ASCII side (9 characters × 8 bits = 72 bits)
        message = TEXT["message"]
        ascii_bits_group = VGroup()

        for i, char in enumerate(message):
            binary = char_to_ascii_binary(char)
            char_label = Text(char, font_size=SIZES["annotation_font"] - 4, color=WHITE)

            # Create 8 bit blocks
            bit_blocks = VGroup()
            for bit in binary:
                block = Square(
                    side_length=DIMENSIONS["bit_block_size"],
                    fill_color=COLORS["bit_block_0"] if bit == '0' else COLORS["bit_block_1"],
                    fill_opacity=OPACITY["bit_block"],
                    stroke_width=1,
                    stroke_color=WHITE
                )
                bit_blocks.add(block)

            bit_blocks.arrange(RIGHT, buff=DIMENSIONS["bit_block_spacing"])

            char_group = VGroup(char_label, bit_blocks).arrange(DOWN, buff=0.2)
            ascii_bits_group.add(char_group)

        ascii_bits_group.arrange(DOWN, buff=0.15).scale(0.5)
        ascii_bits_group.next_to(ascii_label, DOWN, buff=0.5)

        # Animate ASCII bits appearing
        for char_group in ascii_bits_group:
            self.play(FadeIn(char_group), run_time=TIMING["ascii_build_per_char"] * 0.5)

        # Add total label
        ascii_total = Text("72 bits", font_size=SIZES["stats_font"] - 4, color=COLORS["ascii_label"])
        ascii_total.next_to(ascii_bits_group, DOWN, buff=0.3)
        self.play(Write(ascii_total))

        self.wait(TIMING["pause_short"])

        # Build Huffman side (14 bits total)
        huffman_bits = HUFFMAN_DATA["encoded_bits"]
        huffman_blocks = VGroup()

        for bit in huffman_bits:
            block = Square(
                side_length=DIMENSIONS["bit_block_size"] * 1.5,
                fill_color=COLORS["bit_block_0"] if bit == '0' else COLORS["bit_block_1"],
                fill_opacity=OPACITY["bit_block"],
                stroke_width=2,
                stroke_color=WHITE
            )
            huffman_blocks.add(block)

        huffman_blocks.arrange(RIGHT, buff=DIMENSIONS["bit_block_spacing"] * 2)
        huffman_blocks.scale(0.8)
        huffman_blocks.next_to(huffman_label, DOWN, buff=0.5)

        self.play(Create(huffman_blocks), run_time=TIMING["huffman_build"])

        # Add total label
        huffman_total = Text("14 bits", font_size=SIZES["stats_font"] - 4, color=COLORS["huffman_label"])
        huffman_total.next_to(huffman_blocks, DOWN, buff=0.3)
        self.play(Write(huffman_total))

        self.wait(TIMING["pause_medium"])

        # Comparison arrow
        arrow = Arrow(
            ascii_total.get_right(),
            huffman_total.get_left(),
            color=COLORS["comparison_arrow"],
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        savings_text = Text("58 bits saved!", font_size=SIZES["stats_font"] - 4, color=COLORS["stats_good"])
        savings_text.next_to(arrow, UP, buff=0.2)

        self.play(Create(arrow), Write(savings_text), run_time=TIMING["comparison_arrow"])
        self.wait(TIMING["pause_long"])


# =============================================================================
# SCENE 5: COMPRESSION RATIO CALCULATION
# =============================================================================

class CompressionStatsScene(Scene):
    """
    Scene 5: Calculate and display compression statistics.

    Shows:
    - Step-by-step compression ratio calculation
    - Formula display with results
    - Visual gauge showing 80.6% compression
    - Summary box with key statistics
    """

    def construct(self):
        self.compression_stats_animation()

    def compression_stats_animation(self):
        # Title
        title = Text(TEXT["scene5_title"], font_size=SIZES["title_font"], color=COLORS["title_text"])
        title.to_edge(UP)
        self.play(Write(title), run_time=1.0)
        self.wait(TIMING["pause_short"])

        # Create calculation formulas using Text (no LaTeX required)
        stats = COMPRESSION_STATS

        line1_text = Text("Original Size = 9 chars × 8 bits = ", font_size=SIZES["stats_font"] - 2, color=WHITE)
        line1_result = Text("72 bits", font_size=SIZES["stats_font"] - 2, color=COLORS["stats_neutral"])
        line1 = VGroup(line1_text, line1_result).arrange(RIGHT, buff=0.2)

        line2_text = Text("Compressed Size = ", font_size=SIZES["stats_font"] - 2, color=WHITE)
        line2_result = Text("14 bits", font_size=SIZES["stats_font"] - 2, color=COLORS["stats_good"])
        line2 = VGroup(line2_text, line2_result).arrange(RIGHT, buff=0.2)

        line3_text = Text("Bits Saved = 72 - 14 = ", font_size=SIZES["stats_font"] - 2, color=WHITE)
        line3_result = Text("58 bits", font_size=SIZES["stats_font"] - 2, color=COLORS["stats_good"])
        line3 = VGroup(line3_text, line3_result).arrange(RIGHT, buff=0.2)

        line4_text = Text("Compression Ratio = 58/72 × 100% = ", font_size=SIZES["stats_font"] - 2, color=WHITE)
        line4_result = Text("80.6%", font_size=SIZES["stats_font"], color=COLORS["stats_good"])
        line4 = VGroup(line4_text, line4_result).arrange(RIGHT, buff=0.2)

        formula_lines = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        formula_lines.move_to(ORIGIN + UP * 0.5)

        # Animate each formula line
        for i, line in enumerate(formula_lines):
            self.play(Write(line), run_time=TIMING["formula_write_per_line"])
            self.play(Indicate(line[1], scale_factor=1.3), run_time=TIMING["result_indicate"])  # Highlight result
            self.wait(TIMING["pause_short"])

        self.wait(TIMING["pause_medium"])

        # Create visual gauge/progress bar
        gauge_background = Rectangle(
            width=DIMENSIONS["progress_bar_width"],
            height=DIMENSIONS["progress_bar_height"] * 2,
            color=GRAY,
            fill_color=GRAY,
            fill_opacity=0.2,
            stroke_width=2
        )

        gauge_fill = Rectangle(
            width=DIMENSIONS["progress_bar_width"] * 0.806,  # 80.6%
            height=DIMENSIONS["progress_bar_height"] * 2,
            color=COLORS["stats_good"],
            fill_color=COLORS["stats_good"],
            fill_opacity=0.8,
            stroke_width=0
        )
        gauge_fill.align_to(gauge_background, LEFT)

        gauge = VGroup(gauge_background, gauge_fill)
        gauge.move_to(DOWN * 2)

        gauge_label = Text("80.6% Compression", font_size=SIZES["stats_font"], color=COLORS["stats_good"])
        gauge_label.next_to(gauge, DOWN, buff=0.3)

        # Animate gauge
        # Create empty fill to start
        gauge_fill_start = Rectangle(
            width=0.01,
            height=DIMENSIONS["progress_bar_height"] * 2,
            color=COLORS["stats_good"],
            fill_color=COLORS["stats_good"],
            fill_opacity=0.8,
            stroke_width=0
        )
        gauge_fill_start.align_to(gauge_background, LEFT)

        self.play(FadeIn(gauge_background))
        self.add(gauge_fill_start)
        self.play(
            Transform(gauge_fill_start, gauge_fill),
            Write(gauge_label),
            run_time=TIMING["gauge_fill"]
        )
        self.wait(TIMING["pause_medium"])

        # Final celebration
        self.play(
            Flash(gauge_label, color=COLORS["stats_good"], flash_radius=1.5),
            run_time=TIMING["final_flash"]
        )
        self.wait(TIMING["pause_long"])


# =============================================================================
# COMBINED SCENES - All scenes in sequence
# =============================================================================

class CombinedScenes(Scene):
    """Combines all scenes in the correct order for a single video."""

    def construct(self):
        # Scene 1: Pre-built tree
        PreBuiltTreeScene.prebuilt_tree_animation(self)
        self.clear()

        # Scene 2: Encode single character
        EncodeSingleCharScene.encode_single_char_animation(self)
        self.clear()

        # Scene 3: Encode full message
        EncodeFullMessageScene.encode_full_message_animation(self)
        self.clear()

        # Scene 4: Bit comparison
        BitComparisonScene.bit_comparison_animation(self)
        self.clear()

        # Scene 5: Compression stats
        CompressionStatsScene.compression_stats_animation(self)
