#!/usr/bin/env python3
"""Prepare background and logo rasters for the Haiwai WeChat cover skill."""

from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path
from statistics import median

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def save_image(image: Image.Image, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    suffix = output.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        image.convert("RGB").save(output, quality=95, optimize=True)
    else:
        image.save(output, format="PNG", optimize=True)


def cover_crop(
    image: Image.Image,
    width: int,
    height: int,
    focus_x: float,
    focus_y: float,
) -> Image.Image:
    source = image.convert("RGBA")
    scale = max(width / source.width, height / source.height)
    resized = source.resize(
        (round(source.width * scale), round(source.height * scale)),
        Image.Resampling.LANCZOS,
    )
    max_left = max(0, resized.width - width)
    max_top = max(0, resized.height - height)
    focus_px_x = focus_x * resized.width
    focus_px_y = focus_y * resized.height
    left = round(clamp(focus_px_x - width / 2, 0, max_left))
    top = round(clamp(focus_px_y - height / 2, 0, max_top))
    return resized.crop((left, top, left + width, top + height))


def contain_blur(
    image: Image.Image,
    width: int,
    height: int,
    blur: float,
    contain_scale: float,
    align_x: float,
    align_y: float,
) -> Image.Image:
    source = image.convert("RGBA")
    background = cover_crop(source, width, height, 0.5, 0.5)
    background = background.filter(ImageFilter.GaussianBlur(radius=blur))
    background = ImageEnhance.Brightness(background).enhance(0.72)

    scale = min(width / source.width, height / source.height) * contain_scale
    foreground = source.resize(
        (max(1, round(source.width * scale)), max(1, round(source.height * scale))),
        Image.Resampling.LANCZOS,
    )
    left = round((width - foreground.width) * align_x)
    top = round((height - foreground.height) * align_y)
    background.alpha_composite(foreground, (left, top))
    return background


def sample_edge_color(image: Image.Image) -> tuple[int, int, int, int]:
    source = image.convert("RGBA")
    sample = source.resize((64, 64), Image.Resampling.BILINEAR)
    pixels: list[tuple[int, int, int, int]] = []
    for x in range(64):
        pixels.extend((sample.getpixel((x, 0)), sample.getpixel((x, 63))))
    for y in range(1, 63):
        pixels.extend((sample.getpixel((0, y)), sample.getpixel((63, y))))
    visible = [pixel for pixel in pixels if pixel[3] > 8]
    if not visible:
        return (255, 255, 255, 255)
    return tuple(round(median(pixel[channel] for pixel in visible)) for channel in range(4))


def contain_solid(
    image: Image.Image,
    width: int,
    height: int,
    contain_scale: float,
    align_x: float,
    align_y: float,
) -> Image.Image:
    source = image.convert("RGBA")
    background = Image.new("RGBA", (width, height), sample_edge_color(source))
    scale = min(width / source.width, height / source.height) * contain_scale
    foreground = source.resize(
        (max(1, round(source.width * scale)), max(1, round(source.height * scale))),
        Image.Resampling.LANCZOS,
    )
    left = round((width - foreground.width) * align_x)
    top = round((height - foreground.height) * align_y)
    background.alpha_composite(foreground, (left, top))
    return background


def trim_alpha(
    image: Image.Image,
    threshold: int,
    padding_ratio: float,
) -> tuple[Image.Image, tuple[int, int, int, int] | None]:
    source = image.convert("RGBA")
    alpha = source.getchannel("A")
    mask = alpha.point(lambda value: 255 if value > threshold else 0)
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("The image contains no visible pixels above the alpha threshold.")

    cropped = source.crop(bbox)
    padding = round(max(cropped.width, cropped.height) * padding_ratio)
    result = Image.new(
        "RGBA",
        (cropped.width + padding * 2, cropped.height + padding * 2),
        (0, 0, 0, 0),
    )
    result.alpha_composite(cropped, (padding, padding))
    return result, bbox


def parse_polygon(value: str) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    for raw_point in value.split():
        try:
            raw_x, raw_y = raw_point.split(",", 1)
            points.append((int(raw_x), int(raw_y)))
        except ValueError as error:
            raise argparse.ArgumentTypeError(
                "polygon must be space-separated x,y points"
            ) from error
    if len(points) < 3:
        raise argparse.ArgumentTypeError("polygon requires at least three points")
    return points


def parse_box(value: str) -> tuple[int, int, int, int]:
    try:
        x, y, width, height = (int(part) for part in value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("box must be x,y,width,height") from error
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("box width and height must be positive")
    return (x, y, width, height)


def cmd_fit_background(args: argparse.Namespace) -> None:
    image = Image.open(args.input)
    if args.mode == "cover":
        result = cover_crop(
            image,
            args.width,
            args.height,
            clamp(args.focus_x, 0, 1),
            clamp(args.focus_y, 0, 1),
        )
    elif args.mode == "contain-solid":
        result = contain_solid(
            image,
            args.width,
            args.height,
            clamp(args.contain_scale, 0.05, 1),
            clamp(args.align_x, 0, 1),
            clamp(args.align_y, 0, 1),
        )
    else:
        result = contain_blur(
            image,
            args.width,
            args.height,
            args.blur,
            clamp(args.contain_scale, 0.05, 1),
            clamp(args.align_x, 0, 1),
            clamp(args.align_y, 0, 1),
        )
    save_image(result, args.output)
    print(
        json.dumps(
            {
                "command": "fit-background",
                "mode": args.mode,
                "source_size": list(image.size),
                "output_size": [args.width, args.height],
                "contain_scale": args.contain_scale,
                "align": [args.align_x, args.align_y],
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )


def cmd_trim_alpha(args: argparse.Namespace) -> None:
    image = Image.open(args.input)
    result, bbox = trim_alpha(image, args.threshold, args.padding_ratio)
    save_image(result, args.output)
    print(
        json.dumps(
            {
                "command": "trim-alpha",
                "source_size": list(image.size),
                "content_bbox": list(bbox) if bbox else None,
                "output_size": list(result.size),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )


def cmd_extract_polygon(args: argparse.Namespace) -> None:
    source = Image.open(args.input).convert("RGBA")
    mask = Image.new("L", source.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(args.polygon, fill=255)
    for exclusion in args.exclude_polygon:
        draw.polygon(exclusion, fill=0)
    if args.feather > 0:
        mask = mask.filter(ImageFilter.GaussianBlur(radius=args.feather))
    mask = ImageChops.multiply(source.getchannel("A"), mask)
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError("The polygon does not contain visible pixels.")
    padding = max(0, args.padding)
    padded_bbox = (
        max(0, bbox[0] - padding),
        max(0, bbox[1] - padding),
        min(source.width, bbox[2] + padding),
        min(source.height, bbox[3] + padding),
    )
    result = source.crop(padded_bbox)
    result.putalpha(mask.crop(padded_bbox))
    save_image(result, args.output)
    print(
        json.dumps(
            {
                "command": "extract-polygon",
                "source_size": list(source.size),
                "polygon": args.polygon,
                "exclude_polygons": args.exclude_polygon,
                "content_bbox": list(padded_bbox),
                "output_size": list(result.size),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )


def cmd_crop_region(args: argparse.Namespace) -> None:
    source = Image.open(args.input).convert("RGBA")
    cleaned = source.copy()
    background = Image.new("RGBA", source.size, sample_edge_color(source))
    for polygon in args.cover_polygon:
        mask = Image.new("L", source.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.polygon(polygon, fill=255)
        if args.feather > 0:
            mask = mask.filter(ImageFilter.GaussianBlur(radius=args.feather))
        cleaned = Image.composite(background, cleaned, mask)

    x, y, width, height = args.box
    if x < 0 or y < 0 or x + width > source.width or y + height > source.height:
        raise ValueError("The crop box must remain inside the source image.")
    result = cleaned.crop((x, y, x + width, y + height))
    save_image(result, args.output)
    print(
        json.dumps(
            {
                "command": "crop-region",
                "source_size": list(source.size),
                "box": list(args.box),
                "cover_polygons": args.cover_polygon,
                "output_size": list(result.size),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )


def cmd_remove_edge_background(args: argparse.Namespace) -> None:
    source = Image.open(args.input).convert("RGBA")
    rgb = source.convert("RGB")
    background_color = sample_edge_color(source)[:3]
    width, height = source.size
    pixels = rgb.load()
    visited = bytearray(width * height)
    queue: deque[tuple[int, int]] = deque()

    def is_background(x: int, y: int) -> bool:
        pixel = pixels[x, y]
        return max(
            abs(pixel[channel] - background_color[channel]) for channel in range(3)
        ) <= args.tolerance

    def enqueue(x: int, y: int) -> None:
        index = y * width + x
        if not visited[index] and is_background(x, y):
            visited[index] = 1
            queue.append((x, y))

    for x in range(width):
        enqueue(x, 0)
        enqueue(x, height - 1)
    for y in range(1, height - 1):
        enqueue(0, y)
        enqueue(width - 1, y)

    while queue:
        x, y = queue.popleft()
        if x > 0:
            enqueue(x - 1, y)
        if x + 1 < width:
            enqueue(x + 1, y)
        if y > 0:
            enqueue(x, y - 1)
        if y + 1 < height:
            enqueue(x, y + 1)

    mask = Image.new("L", source.size, 255)
    mask_data = mask.load()
    for y in range(height):
        row = y * width
        for x in range(width):
            if visited[row + x]:
                mask_data[x, y] = 0
    if args.feather > 0:
        mask = mask.filter(ImageFilter.GaussianBlur(radius=args.feather))
    mask = ImageChops.multiply(source.getchannel("A"), mask)
    result = source.copy()
    result.putalpha(mask)
    if args.trim:
        bbox = mask.getbbox()
        if bbox is None:
            raise ValueError("No foreground remains after background removal.")
        result = result.crop(bbox)
    save_image(result, args.output)
    print(
        json.dumps(
            {
                "command": "remove-edge-background",
                "source_size": list(source.size),
                "background_color": list(background_color),
                "tolerance": args.tolerance,
                "feather": args.feather,
                "output_size": list(result.size),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    fit = subparsers.add_parser("fit-background")
    fit.add_argument("--input", required=True, type=Path)
    fit.add_argument("--output", required=True, type=Path)
    fit.add_argument("--width", required=True, type=int)
    fit.add_argument("--height", required=True, type=int)
    fit.add_argument(
        "--mode",
        choices=("cover", "contain-solid", "contain-blur"),
        default="cover",
    )
    fit.add_argument("--focus-x", type=float, default=0.5)
    fit.add_argument("--focus-y", type=float, default=0.5)
    fit.add_argument("--contain-scale", type=float, default=1.0)
    fit.add_argument("--align-x", type=float, default=0.5)
    fit.add_argument("--align-y", type=float, default=0.5)
    fit.add_argument("--blur", type=float, default=28.0)
    fit.set_defaults(func=cmd_fit_background)

    trim = subparsers.add_parser("trim-alpha")
    trim.add_argument("--input", required=True, type=Path)
    trim.add_argument("--output", required=True, type=Path)
    trim.add_argument("--threshold", type=int, default=8)
    trim.add_argument("--padding-ratio", type=float, default=0.03)
    trim.set_defaults(func=cmd_trim_alpha)

    extract = subparsers.add_parser("extract-polygon")
    extract.add_argument("--input", required=True, type=Path)
    extract.add_argument("--output", required=True, type=Path)
    extract.add_argument("--polygon", required=True, type=parse_polygon)
    extract.add_argument(
        "--exclude-polygon",
        action="append",
        type=parse_polygon,
        default=[],
        help="source-coordinate polygon to subtract; may be repeated",
    )
    extract.add_argument("--feather", type=float, default=2.0)
    extract.add_argument("--padding", type=int, default=8)
    extract.set_defaults(func=cmd_extract_polygon)

    crop = subparsers.add_parser("crop-region")
    crop.add_argument("--input", required=True, type=Path)
    crop.add_argument("--output", required=True, type=Path)
    crop.add_argument("--box", required=True, type=parse_box)
    crop.add_argument(
        "--cover-polygon",
        action="append",
        type=parse_polygon,
        default=[],
        help="source-coordinate polygon to replace with the sampled edge color",
    )
    crop.add_argument("--feather", type=float, default=3.0)
    crop.set_defaults(func=cmd_crop_region)

    remove_background = subparsers.add_parser("remove-edge-background")
    remove_background.add_argument("--input", required=True, type=Path)
    remove_background.add_argument("--output", required=True, type=Path)
    remove_background.add_argument("--tolerance", type=int, default=8)
    remove_background.add_argument("--feather", type=float, default=1.0)
    remove_background.add_argument("--trim", action="store_true")
    remove_background.set_defaults(func=cmd_remove_edge_background)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if getattr(args, "width", 1) <= 0 or getattr(args, "height", 1) <= 0:
        parser.error("width and height must be positive")
    args.func(args)


if __name__ == "__main__":
    main()
