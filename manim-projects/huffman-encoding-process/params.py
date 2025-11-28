"""
Huffman Encoding Process - Visual Parameters

All visual styling, timing, text, and layout parameters for the animation.
Modify these values to customize the appearance without changing the code.

Message: "AABBBCCCC"
Tree Structure:
        (9)
       /   \
      /     \
    (4)     C[4]
   /   \
  A[2] B[3]

Codes: A=00, B=01, C=1
"""

import numpy as np
from manim import *

# =============================================================================
# COLORS
# =============================================================================

COLORS = {
    # Tree elements
    "internal_node": BLUE,
    "internal_node_fill": BLUE,
    "leaf_node": GREEN,
    "leaf_node_fill": GREEN,
    "edge_inactive": GRAY,
    "edge_active": GOLD,
    "edge_label": WHITE,

    # Path highlighting
    "path_highlight": YELLOW,
    "path_glow": GOLD,

    # Text and labels
    "title_text": WHITE,
    "node_text": WHITE,
    "code_text": ORANGE,
    "message_text": WHITE,
    "message_active": YELLOW,

    # Bits and encoding
    "bit_0": BLUE,
    "bit_1": RED,
    "bit_block_0": BLUE,
    "bit_block_1": RED,
    "bit_stream": ORANGE,

    # UI elements
    "legend_box": DARK_GRAY,
    "legend_text": WHITE,
    "table_header": BLUE_C,
    "table_cell": WHITE,
    "progress_bar": GREEN,

    # Comparison elements
    "ascii_label": BLUE,
    "huffman_label": GREEN,
    "comparison_arrow": YELLOW,

    # Statistics
    "stats_good": GREEN,
    "stats_neutral": YELLOW,
    "stats_bad": RED,
}

# =============================================================================
# DIMENSIONS
# =============================================================================

DIMENSIONS = {
    # Node sizes
    "internal_node_radius": 0.4,
    "leaf_node_width": 1.2,
    "leaf_node_height": 0.7,

    # Edge properties
    "edge_width": 3,
    "edge_active_width": 5,

    # Bit visualization
    "bit_block_size": 0.3,
    "bit_block_spacing": 0.05,

    # Spacing and layout
    "tree_horizontal_spacing": 2.5,
    "tree_vertical_spacing": 1.8,
    "node_label_buffer": 0.1,

    # UI elements
    "legend_box_width": 3,
    "legend_box_height": 2,
    "table_cell_width": 1.5,
    "table_cell_height": 0.6,

    # Progress bar
    "progress_bar_width": 6,
    "progress_bar_height": 0.3,
}

# =============================================================================
# POSITIONS
# =============================================================================

POSITIONS = {
    # Tree layout
    "tree_center": ORIGIN,
    "root_position": UP * 2,

    # UI element positions
    "message_position": UP * 3.5,
    "legend_position": LEFT * 5 + UP * 2,
    "code_builder_position": RIGHT * 4 + UP * 2,
    "encoding_table_position": RIGHT * 4.5,
    "bit_stream_position": DOWN * 2.5,
    "progress_bar_position": UP * 3,

    # Comparison scene positions
    "ascii_side_position": LEFT * 3,
    "huffman_side_position": RIGHT * 3,
    "comparison_title_position": UP * 3.5,

    # Statistics positions
    "formula_position": ORIGIN,
    "summary_position": DOWN * 2,
    "gauge_position": UP * 1,
}

# =============================================================================
# TEXT CONTENT
# =============================================================================

TEXT = {
    # Scene titles
    "scene1_title": "Huffman Encoding Process",
    "scene4_title": "Original vs Compressed",
    "scene5_title": "Compression Statistics",

    # Message
    "message": "AABBBCCCC",

    # Legend
    "legend_title": "Encoding Rules",
    "legend_left": "Left → 0",
    "legend_right": "Right → 1",
    "legend_path": "Path = Code",

    # Node labels
    "root_label": "9",
    "left_internal_label": "4",
    "leaf_A_label": "A: 2",
    "leaf_B_label": "B: 3",
    "leaf_C_label": "C: 4",

    # Encoding table
    "table_title": "Huffman Codes",
    "table_header_char": "Char",
    "table_header_code": "Code",

    # Codes
    "code_A": "00",
    "code_B": "01",
    "code_C": "1",

    # Bit comparison
    "ascii_label": "Original (ASCII 8-bit)",
    "huffman_label": "Huffman Encoded",
    "bits_label": "bits",

    # Statistics
    "original_size_label": "Original Size",
    "compressed_size_label": "Compressed Size",
    "bits_saved_label": "Bits Saved",
    "compression_ratio_label": "Compression Ratio",

    # Annotations
    "encoding_annotation": "Traversing tree for character:",
    "path_annotation": "Path:",
    "code_annotation": "Code:",
}

# =============================================================================
# TIMING
# =============================================================================

TIMING = {
    # Scene 1: Tree presentation
    "tree_create": 1.5,
    "legend_fadein": 0.8,
    "node_indicate": 0.5,
    "message_write": 1.0,
    "pause_short": 0.5,
    "pause_medium": 1.0,
    "pause_long": 1.5,

    # Scene 2: Single character encoding
    "char_highlight": 0.8,
    "node_pulse": 0.5,
    "edge_highlight": 1.0,
    "bit_appear": 0.6,
    "code_flash": 0.8,

    # Scene 3: Full message encoding
    "char_encode_fast": 0.8,
    "path_flash_fast": 0.6,
    "bit_append": 0.4,
    "progress_update": 0.3,

    # Scene 4: Bit comparison
    "split_screen": 1.0,
    "ascii_build_per_char": 0.8,
    "huffman_build": 2.0,
    "comparison_arrow": 1.0,
    "size_emphasis": 1.5,

    # Scene 5: Compression stats
    "formula_write_per_line": 2.0,
    "result_indicate": 0.8,
    "gauge_fill": 2.0,
    "summary_slidein": 1.5,
    "final_flash": 1.0,
}

# =============================================================================
# SIZES
# =============================================================================

SIZES = {
    # Font sizes
    "title_font": 48,
    "message_font": 40,
    "node_label_font": 28,
    "legend_font": 24,
    "table_font": 28,
    "code_font": 32,
    "annotation_font": 24,
    "stats_font": 30,

    # Scale factors
    "indicate_scale": 1.3,
    "flash_scale": 1.5,
    "char_highlight_scale": 1.4,

    # Bit display
    "bit_font": 24,
}

# =============================================================================
# OPACITY
# =============================================================================

OPACITY = {
    # Node opacity
    "node_fill": 0.7,
    "node_stroke": 1.0,

    # Edge opacity
    "edge_inactive": 0.5,
    "edge_active": 1.0,

    # UI elements
    "legend_box": 0.3,
    "table_background": 0.2,
    "bit_block": 0.8,

    # Highlights
    "highlight": 0.9,
    "dim": 0.3,
}

# =============================================================================
# HUFFMAN TREE DATA
# =============================================================================

HUFFMAN_DATA = {
    "message": "AABBBCCCC",
    "frequencies": {"A": 2, "B": 3, "C": 4},
    "codes": {"A": "00", "B": "01", "C": "1"},
    "tree_structure": {
        "root": {
            "freq": 9,
            "left": {
                "freq": 4,
                "left": {"char": "A", "freq": 2},
                "right": {"char": "B", "freq": 3}
            },
            "right": {"char": "C", "freq": 4}
        }
    },
    # Encoded message: AA BB BBB C C C C
    "encoded_bits": "000001010111111",
    "encoded_segments": ["00", "00", "01", "01", "01", "1", "1", "1", "1"],
}

# =============================================================================
# COMPRESSION STATISTICS
# =============================================================================

COMPRESSION_STATS = {
    "message_length": 9,
    "ascii_bits_per_char": 8,
    "ascii_total_bits": 72,
    "huffman_total_bits": 14,
    "bits_saved": 58,
    "compression_ratio": 80.6,  # (72-14)/72 * 100%
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_tree_positions():
    """
    Calculate positions for all nodes in the Huffman tree.

    Returns:
        dict: Dictionary mapping node names to positions
    """
    h_spacing = DIMENSIONS["tree_horizontal_spacing"]
    v_spacing = DIMENSIONS["tree_vertical_spacing"]

    root_pos = POSITIONS["root_position"]

    positions = {
        "root": root_pos,
        "left_internal": root_pos + DOWN * v_spacing + LEFT * h_spacing / 2,
        "right_leaf_C": root_pos + DOWN * v_spacing + RIGHT * h_spacing / 2,
        "leaf_A": root_pos + DOWN * v_spacing * 2 + LEFT * h_spacing,
        "leaf_B": root_pos + DOWN * v_spacing * 2,
    }

    return positions

def get_char_code(char):
    """Get the Huffman code for a character"""
    return HUFFMAN_DATA["codes"].get(char, "")

def get_path_for_char(char):
    """
    Get the tree path for a character.

    Args:
        char: Character to encode

    Returns:
        list: List of directions ("left" or "right")
    """
    paths = {
        "A": ["left", "left"],
        "B": ["left", "right"],
        "C": ["right"]
    }
    return paths.get(char, [])

def char_to_ascii_binary(char):
    """
    Convert a character to 8-bit ASCII binary string.

    Args:
        char: Single character

    Returns:
        str: 8-bit binary string (e.g., "01000001" for 'A')
    """
    return format(ord(char), '08b')

def get_encoding_table_data():
    """
    Get the data for the encoding table.

    Returns:
        list: 2D list for Table mobject
    """
    return [
        ["A", "00"],
        ["B", "01"],
        ["C", "1"]
    ]
