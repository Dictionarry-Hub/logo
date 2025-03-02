# Dictionarry Logos

This repository contains the official logo assets for Dictionarry.

## Contents

- `*/` - Generated PNG/SVG files at various resolutions for each program / app / whatever
- `convert.py` - Conversion script to generate PNG files from SVGs

## Conversion Script

The repository includes a Python script that converts SVG logos to PNG files at multiple resolutions.

### Requirements

```
pip install cairosvg
```

### Basic Usage

Convert an SVG to standard web sizes:

```
python convert.py svg/logo.svg
```

This generates PNGs at common sizes (16×16 through 1024×1024) in the `images/` directory.

### Custom Sizes

Specify custom sizes:

```
python svg_to_png.py svg/logo.svg -s 48 96 192
```

### Custom Output Directory

Change the output location:

```
python svg_to_png.py svg/logo.svg -o assets/icons
```

### All Options

```
python svg_to_png.py --help

Usage: svg_to_png.py [-h] [-o OUTPUT] [-s SIZES [SIZES ...]] svg_file

Convert SVG to multiple PNG sizes.

Positional arguments:
  svg_file              Path to SVG file

Optional arguments:
  -h, --help            Show this help message
  -o OUTPUT, --output OUTPUT
                        Output directory (default: images)
  -s SIZES [SIZES ...], --sizes SIZES [SIZES ...]
                        Sizes to generate (default: 16 32 48 64 128 192 256 512 1024)

Example: python svg_to_png.py logo.svg -s 32 64 128 256
```
