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
- Assume the uploaded source will usually have a different aspect ratio. Crop and proportionally resize it independently for the landscape and square outputs.
- Allow sensible raster compression/downsampling when it does not create visible softness, banding, halos, or block artifacts.
- Preserve the selected image's principal subject.
- Reject a direct crop that retains less than roughly 60% of the meaningful composition, or cannot preserve important elements spanning both the top and bottom.
- Prefer a focal-point cover crop when safe.
- Use a source-derived solid extension for simple or nearly uniform backgrounds when a cover crop would cut important content.
- Use a source-derived blurred extension only for photographic or textured backgrounds.
- Never stretch the source image.
- Treat a vertical-to-horizontal conversion as crop, canvas extension, or recomposition—not horizontal stretching.
- Permit limited non-uniform widening only for pure texture or gradient background regions containing no subject, object, text, logo, or geometry that can visibly deform.
- Preserve the original style, palette, lighting, material appearance, typography, and object geometry.
- Never redraw or generatively restyle the subject merely to fit the target ratio.
- Default to minimum necessary recomposition: preserve overall source relationships and try proportional scaling, repositioning, small cropping, native-background extension, or moving one or two key elements before any multi-element separation.
- Do not split or rebuild a composition when movement or canvas extension solves the title-zone problem.
- In landscape covers, do not park the entire meaningful image group in the left or right outer third. Require the source visual mass to cross the center axis, distribute through upper/lower zones, or retain a genuine source-derived counterweight.
- Do not treat the centered title or an empty opposite side as sufficient visual counterweight.

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
- Use confident type size without making the title feel packed. As a starting point with Alegreya ExtraBold, use about 64 px with 72 px line height in landscape and 88 px with 100 px line height in square, then adjust optically.
- Keep two-line line height at least equal to the font size; generally prefer about 1.08–1.16×.
- Use neutral tracking by default. Do not apply negative tracking merely to make the title larger.
- When a support layer is present, preserve generous optical padding on all sides; reduce the title before squeezing its padding.
- Shrink long text to fit; never exceed the active format's footprint.
- Default color: black or white, whichever has stronger local contrast.
- Apply explicit highlight colors only when requested.
- Start with no background behind the keyword.
- Add a plate, gradient, blur, veil, or local weakening only when direct placement fails the combined tests of contrast, hierarchy, and overall beauty.
- Adapt support to the source; do not use a pure-white card or white gradient, or reuse a fixed radius, opacity, or size.
- Prefer a restrained non-white tint or source-colored gradient only when support is necessary. Keep the result mature and editorial.
- Require a stable low-interference reading zone. Reframe or recompose before relying on heavier type, and never let title letterforms cross rapidly alternating colors, dense edges, or embedded source text.
- For two-line titles, require both lines to remain independently prominent at native size and in the 383 × 383 preview. The second line must not be materially weaker than the first.
- When any word or substantial letterform remains effortful to read after reasonable placement, require one compact support behind the whole title. On light artwork, use a warm ivory, pale gray, or source-tinted translucent panel instead of an opaque pure-white card.

### Company logo

- Prefer an official matching SVG/vector asset.
- Preserve the logo generation/version supplied by the user; do not silently substitute a newer redesign.
- For raster assets, require at least 1.5× native pixel coverage relative to the largest displayed footprint and prefer 2× for fine wordmarks. Never enlarge a raster beyond native size for final delivery.
- Trim transparent padding before placement.
- When the source has a safely removable uniform edge background, create and inspect a clean transparent cutout first.
- Preserve the original opaque logo if removal damages internal white shapes, counters, antialiasing, strokes, shadows, or brand colors.
- Validate a transparent cutout at 100% on checkerboard, light neutral, and dark/saturated backgrounds. Reject any residual matte rectangle, edge-color haze, white/gray fringe, halo, or dirty antialiasing.
- Prefer an official transparent/vector mark after a failed cutout. Otherwise retain the opaque logo with the smallest intentional source-coordinated support instead of shipping a dirty pseudo-transparent asset.
- Use FIT/contain behavior.
- Preserve aspect ratio and alpha.
- Test the logo directly on the image first; when it is clear, add no background.
- When contrast is insufficient, use the smallest source- or brand-coordinated non-white translucent tint or restrained gradient needed for clarity.
- Never add a default pure-white card. Do not add an outline or recolor unless requested.

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

Export each frame at 1× by default:

- 1× compatibility output at the frame's native dimensions;

Export a 2× high-resolution master only for explicit high-resolution/final delivery, known larger reuse, or a demonstrated raster-quality need.

Do not resize the Figma frames for the 2× export; use the export scale so vector text and logos remain crisp.
