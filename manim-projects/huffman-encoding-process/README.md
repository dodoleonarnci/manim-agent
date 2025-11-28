# Huffman Encoding Process Animation

A focused visualization demonstrating how Huffman encoding compresses data using binary tree traversal. This animation skips introductory material and jumps straight into the encoding demonstration.

## Overview

This project visualizes the Huffman encoding process using the simple example **"AABBBCCCC"** (9 characters, 3 unique symbols). The animation clearly demonstrates:

1. The pre-built Huffman tree structure
2. How characters are encoded by traversing the tree (left=0, right=1)
3. Encoding a complete message character by character
4. Comparison of original ASCII vs compressed bit representation
5. Compression ratio calculation showing 80.6% compression

## Project Structure

```
huffman-encoding-process/
├── animation.py                  # Main animation with 5 scenes
├── params.py                     # Visual parameters (externalized)
├── README.md                     # This file
└── media/                        # Rendered videos (created by Manim)
```

## The Huffman Tree

For the message "AABBBCCCC", the Huffman tree structure is:

```
        (9)
       /   \
      /     \
    (4)     C[4]
   /   \
  A[2] B[3]
```

**Encoding Rules:**
- **Left edge** → Add `0` to code
- **Right edge** → Add `1` to code
- **Path from root to leaf** = character's binary code

**Resulting Codes:**
- `A` → `00` (left → left)
- `B` → `01` (left → right)
- `C` → `1` (right)

## The 5 Scenes

### Scene 1: PreBuiltTreeScene (~10 seconds)
Shows the complete Huffman tree with:
- Internal nodes (blue circles with frequencies)
- Leaf nodes (green rectangles with characters)
- Edge labels (0 for left, 1 for right)
- Legend explaining the encoding rules
- The message "AABBBCCCC" to be encoded

**Render:** `manim -pql animation.py PreBuiltTreeScene`

### Scene 2: EncodeSingleCharScene (~15 seconds)
Detailed walkthrough of encoding the character 'A':
- Start at root node
- Traverse left (add '0' to code)
- Traverse left again (add '0' to code)
- Arrive at leaf 'A'
- Final code displayed: "00"

**Render:** `manim -pql animation.py EncodeSingleCharScene`

### Scene 3: EncodeFullMessageScene (~25 seconds)
Encodes all 9 characters of "AABBBCCCC":
- Tree displayed on left
- Encoding table reference on right
- Each character highlighted in sequence
- Path flashes in tree for each encoding
- Growing bit stream shows accumulated codes
- Final encoded message: "000001010111111" (14 bits)

**Render:** `manim -pql animation.py EncodeFullMessageScene`

### Scene 4: BitComparisonScene (~20 seconds)
Visual comparison of original vs compressed:
- **Left side:** ASCII representation (9 chars × 8 bits = 72 bits)
  - Each character shown as 8 colored bit blocks
- **Right side:** Huffman encoding (14 bits total)
  - Compact bit sequence
- **Comparison:** Arrow showing 58 bits saved

**Render:** `manim -pql animation.py BitComparisonScene`

### Scene 5: CompressionStatsScene (~20 seconds)
Calculates compression ratio step by step:
```
Original Size = 9 chars × 8 bits = 72 bits
Compressed Size = 14 bits
Bits Saved = 72 - 14 = 58 bits
Compression Ratio = 58/72 × 100% = 80.6%
```
- Formula displayed line by line
- Visual gauge showing 80.6% compression
- Results highlighted with color coding

**Render:** `manim -pql animation.py CompressionStatsScene`

## Rendering Instructions

### Individual Scenes

**Low quality (fast preview):**
```bash
manim -pql animation.py PreBuiltTreeScene
manim -pql animation.py EncodeSingleCharScene
manim -pql animation.py EncodeFullMessageScene
manim -pql animation.py BitComparisonScene
manim -pql animation.py CompressionStatsScene
```

**High quality (1080p60):**
```bash
manim -pqh animation.py PreBuiltTreeScene
manim -pqh animation.py EncodeSingleCharScene
manim -pqh animation.py EncodeFullMessageScene
manim -pqh animation.py BitComparisonScene
manim -pqh animation.py CompressionStatsScene
```

### All Scenes (Batch Render)

```bash
# Low quality preview
for scene in PreBuiltTreeScene EncodeSingleCharScene EncodeFullMessageScene BitComparisonScene CompressionStatsScene; do
    manim -pql animation.py $scene
done

# High quality
for scene in PreBuiltTreeScene EncodeSingleCharScene EncodeFullMessageScene BitComparisonScene CompressionStatsScene; do
    manim -pqh animation.py $scene
done
```

### Quality Options

- `-ql`: Low quality (480p15, fast preview)
- `-qm`: Medium quality (720p30)
- `-qh`: High quality (1080p60)
- `-qk`: 4K quality (2160p60)

Add `-p` flag to automatically preview: `manim -pqh animation.py SceneName`

## Customization

All visual parameters are externalized to `params.py` for easy customization without touching the animation code.

### Colors
Edit the `COLORS` dictionary:
```python
COLORS = {
    "internal_node": BLUE,          # Internal node color
    "leaf_node": GREEN,             # Leaf node color
    "edge_active": GOLD,            # Active path highlighting
    "bit_0": BLUE,                  # Color for '0' bits
    "bit_1": RED,                   # Color for '1' bits
    # ... and many more
}
```

### Timing
Adjust animation speeds in the `TIMING` dictionary:
```python
TIMING = {
    "tree_create": 1.5,             # Tree creation duration
    "char_highlight": 0.8,          # Character highlighting
    "edge_highlight": 1.0,          # Edge traversal speed
    "pause_medium": 1.0,            # Pause between steps
    # ... and more
}
```

### Dimensions
Change sizes and spacing in the `DIMENSIONS` dictionary:
```python
DIMENSIONS = {
    "internal_node_radius": 0.4,    # Size of internal nodes
    "leaf_node_width": 1.2,         # Width of leaf rectangles
    "tree_horizontal_spacing": 2.5, # Space between nodes
    "bit_block_size": 0.3,          # Size of bit visualization
    # ... and more
}
```

### Text Content
Modify labels and messages in the `TEXT` dictionary:
```python
TEXT = {
    "message": "AABBBCCCC",         # The message to encode
    "legend_left": "Left → 0",      # Legend text
    "legend_right": "Right → 1",    # Legend text
    # ... and more
}
```

## Mathematical Foundation

### Huffman Encoding Formula
The average code length is:
```
L_avg = Σ(f_i × |c_i|)

where:
- f_i = frequency of character i
- |c_i| = length of code for character i
```

For "AABBBCCCC":
```
L_avg = (2×2) + (3×2) + (4×1) = 4 + 6 + 4 = 14 bits
```

### Compression Ratio
```
Compression Ratio = (Original - Compressed) / Original × 100%
                  = (72 - 14) / 72 × 100%
                  = 80.6%
```

## Key Features

✓ **No LaTeX Required:** Uses `Text` instead of `MathTex` for better compatibility
✓ **Modular Design:** Each scene is independent and can be rendered separately
✓ **Fully Externalized Parameters:** Change visuals without touching code
✓ **Clear Visual Hierarchy:** Color-coded nodes, edges, and bits
✓ **Step-by-Step Progression:** From single character to full message
✓ **Pedagogical Focus:** Designed to teach the encoding process clearly

## Dependencies

- **Python** 3.8+
- **Manim Community Edition** v0.19.0+
- **NumPy** (included with Manim)

### Install Manim

```bash
pip install manim
```

For detailed installation instructions, see: https://docs.manim.community/en/stable/installation.html

## Educational Use

This animation is ideal for:
- Computer science courses covering data compression
- Information theory lessons
- Algorithm visualization demonstrations
- Self-study of Huffman encoding

The animation focuses exclusively on the **encoding process**, demonstrating:
1. How binary tree structure determines codes
2. Why frequent characters get shorter codes
3. How traversal generates binary sequences
4. The compression benefits of variable-length encoding

## Technical Notes

### Tree Structure Generation
The tree is built using:
- `Circle()` for internal nodes
- `Rectangle()` for leaf nodes
- `Line()` for edges with `0`/`1` labels
- Positions calculated using helper function `get_tree_positions()`

### Path Highlighting
Character encoding uses:
- `Indicate()` for node emphasis
- Color animation for edge highlighting
- Sequential bit appending to code builder
- `Flash()` for arrival at leaf nodes

### Bit Visualization
Bits are displayed as:
- Colored squares (`Square()` mobjects)
- Blue for '0', Red for '1'
- Arranged horizontally with spacing

## Compression Results

For the example message "AABBBCCCC":

| Metric | Value |
|--------|-------|
| Original (ASCII) | 72 bits (9 bytes) |
| Huffman Encoded | 14 bits (1.75 bytes) |
| Bits Saved | 58 bits |
| **Compression Ratio** | **80.6%** |

This demonstrates the power of Huffman encoding: nearly 6× reduction in size!

## Future Extensions

Possible additions to this project:
- **Tree Construction Scene:** Show how the tree is built from character frequencies
- **Decoding Scene:** Reverse the process to decode the bit stream
- **Different Messages:** Compare compression for different character distributions
- **Real-World Examples:** Apply to actual text files or data

## Author

Created using the Manim Animation Agent
Date: 2025-11-27

## License

This animation is provided for educational purposes.

---

## Quick Start

```bash
# 1. Clone or download this project

# 2. Install Manim
pip install manim

# 3. Test with low quality preview
manim -pql animation.py PreBuiltTreeScene

# 4. Render all scenes in high quality
for scene in PreBuiltTreeScene EncodeSingleCharScene EncodeFullMessageScene BitComparisonScene CompressionStatsScene; do
    manim -pqh animation.py $scene
done

# 5. Find rendered videos in media/videos/animation/1080p60/
```

**Enjoy learning about Huffman encoding through visualization!** 🎬✨
