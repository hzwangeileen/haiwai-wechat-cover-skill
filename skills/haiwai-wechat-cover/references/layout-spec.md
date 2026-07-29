# Layout specification

## Canvas sizes

| Output | Width | Height | Notes |
|---|---:|---:|---|
| Landscape | 900 | 383 | WeChat 2.35:1 message-list cover |
| Square | 900 | 900 | WeChat share card and account home |
| Combined | 1307 | 383 | Landscape left, 24 px gap, square right at 383 × 383 |

Use a white fill behind the combined preview and its 24 px gap.

These are output constraints, not a composition template. Choose subject placement from the source using `design-principles.md`.

Place the three frames inside a new run-specific Section:

- landscape section position: x = 80, y = 100;
- square section position: x = 80, y = 583;
- combined section position: x = 1080, y = 100.

Place the Section itself to the right of the rightmost existing top-level page node with at least 200 px clearance. These canvas positions do not affect exported frame contents.

## Background

- Fill the complete target canvas.
- Preserve the selected image's principal subject.
- Prefer a focal-point cover crop when safe.
- Use a source-derived solid extension for simple or nearly uniform backgrounds when a cover crop would cut important content.
- Use a source-derived blurred extension only for photographic or textured backgrounds.
- Never stretch the source image.
- Preserve the original style, palette, lighting, material appearance, typography, and object geometry.
- Never redraw or generatively restyle the subject merely to fit the target ratio.

## Central content

Use a format-specific master visual footprint:

| Format | Maximum width | Maximum height | Centered box |
| --- | ---: | ---: | --- |
| Landscape | 360 px | 150 px | x = 270, y = 116.5 |
| Square | 500 px | 230 px | x = 200, y = 335 |

Both boxes share the exact canvas center. Keep sizing consistent across runs within each format.

The square footprint is intentionally larger. The square is reduced to 383 × 383 in the combined preview and often appears as a small share-card thumbnail, so matching the landscape's native pixel size makes the square title look too small.

### Keyword

- Horizontal alignment: center.
- Vertical alignment: center.
- Font preference: Albertus Nova, then Alegreya ExtraBold.
- Upright style only; no italics.
- Single line preferred; two lines maximum.
- Use confident type size and comfortable line spacing for short two-line titles. As a starting point with Alegreya ExtraBold, use about 70 px with 66 px line height in landscape and 100 px with 92 px line height in square, then adjust optically.
- Shrink long text to fit; never exceed the active format's footprint.
- Default color: black or white, whichever has stronger local contrast.
- Apply explicit highlight colors only when requested.

### Company logo

- Trim transparent padding before placement.
- Use FIT/contain behavior.
- Preserve aspect ratio and alpha.
- Do not add a background, outline, or recolor unless requested.

## 海外独角兽 logo

Use `assets/haiwai-unicorn-logo-white.png`.

- display width: 81 px;
- preserve aspect ratio;
- landscape right margin: 27 px;
- landscape top margin: 11.5 px;
- square right margin: 27 px;
- square top margin: 27 px;
- align the displayed logo's top-right bounding box to the margins above.

On a light local background, apply a restrained dark drop shadow:

- color: black at 35% opacity;
- offset: 0 × 2 px;
- blur radius: 4 px;
- spread: 0.

Do not add a shadow on a sufficiently dark background.

## Combined preview

- frame: 1307 × 383;
- background: white;
- landscape clone: x = 0, y = 0, size 900 × 383;
- gap: x = 900–923, width 24 px;
- square clone: x = 924, y = 0, size 383 × 383;
- preserve all child layers in both clones.
- inspect the square title at the reduced 383 × 383 size; it must remain prominent and comfortable to read.

## Resolution

Export each frame twice:

- 1× compatibility output at the frame's native dimensions;
- 2× high-resolution master.

Do not resize the Figma frames for the 2× export; use the export scale so vector text and logos remain crisp.
