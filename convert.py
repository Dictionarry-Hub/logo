#!/usr/bin/env python3
"""
SVG to PNG Converter

This script converts an SVG file to multiple PNG files of different sizes.
It requires cairosvg to be installed.

Installation:
    pip install cairosvg

Usage:
    python svg_to_png.py logo.svg
    python svg_to_png.py logo.svg -o output_folder
    python svg_to_png.py logo.svg -s 32 64 128 256
"""

import os
import sys
import argparse
from pathlib import Path


def convert_svg_to_pngs(svg_path, sizes, output_dir="images"):
    """Convert SVG to PNG files at various sizes."""
    try:
        import cairosvg
    except ImportError:
        print("Error: cairosvg library not installed.")
        print("Please install it with: pip install cairosvg")
        sys.exit(1)

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)

    # Get the base name without extension
    base_name = os.path.splitext(os.path.basename(svg_path))[0]

    # Read the SVG file
    try:
        with open(svg_path, 'rb') as svg_file:
            svg_data = svg_file.read()
    except Exception as e:
        print(f"Error reading SVG file: {str(e)}")
        sys.exit(1)

    # Convert and save the PNG files at each size
    for size in sizes:
        output_path = os.path.join(output_dir,
                                   f"{base_name}-{size}x{size}.png")
        print(f"Converting to {output_path}...")

        try:
            cairosvg.svg2png(bytestring=svg_data,
                             write_to=output_path,
                             output_width=size,
                             output_height=size)
        except Exception as e:
            print(f"Error converting to {size}x{size}: {str(e)}")
            continue

    print(f"\nConversions completed. Files saved in '{output_dir}' directory:")
    for size in sizes:
        file_path = os.path.join(output_dir, f"{base_name}-{size}x{size}.png")
        if os.path.exists(file_path):
            print(f"  - {file_path}")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Convert SVG to multiple PNG sizes.",
        epilog="Example: python svg_to_png.py logo.svg -s 32 64 128 256")
    parser.add_argument("svg_file", help="Path to SVG file")
    parser.add_argument("-o",
                        "--output",
                        default="images",
                        help="Output directory (default: images)")
    parser.add_argument(
        "-s",
        "--sizes",
        type=int,
        nargs="+",
        default=[16, 32, 48, 64, 128, 192, 256, 512, 1024],
        help="Sizes to generate (default: 16 32 48 64 128 192 256 512 1024)")

    args = parser.parse_args()

    # Check if the SVG file exists
    if not os.path.isfile(args.svg_file):
        print(f"Error: SVG file '{args.svg_file}' not found.")
        sys.exit(1)

    # Convert the SVG to PNGs
    convert_svg_to_pngs(args.svg_file, args.sizes, args.output)


if __name__ == "__main__":
    main()
