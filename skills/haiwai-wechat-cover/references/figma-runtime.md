# Figma runtime

Use this reference for every run. Load `design-principles.md` only for ambiguous or complex compositions as directed by `SKILL.md`.

Treat speed as removal of non-value work, not removal of quality. For ordinary sources, make one layout decision, one source upload, one atomic Figma mutation, one combined-preview judgment, and one parallel export batch. Add work only when a visible defect blocks subject completeness, title readability, or compositional balance.

## 1. Open the fixed workspace

Use:

- file key: `EipE7fkEv9xLOzqX7yqSAP`
- file URL: `https://www.figma.com/design/EipE7fkEv9xLOzqX7yqSAP/Untitled`

Do not call `create_new_file`.

For an ordinary run, do not start with a separate read-only `use_figma` call. In the first atomic mutation:

- verify the file is accessible and editable;
- find and validate the reusable top-level Section `海外独角兽封面｜MASTER`;
- scan top-level bounds and compute a target x-coordinate with at least 200 px clearance;
- duplicate the master directly into that clear position;
- perform the complete content update described below.

Because `use_figma` is atomic, let the call fail cleanly if the file or master is unavailable, read-only, missing, or invalid. Only then use a separate inspection call to diagnose or repair the workspace.

## 2. Font handling

The fixed master has already established `Alegreya ExtraBold`. In normal runs, inherit or load that exact font directly and skip `listAvailableFontsAsync()`.

Run font discovery only when repairing/creating the master, when the inherited font is missing, or when the user requests another family.

Choose the heaviest upright Albertus Nova style using this preference order when present:

`Black`, `ExtraBold`, `Extra Bold`, `Bold`, `SemiBold`, `Semi Bold`, `Regular`.

If the family is absent, verify and use:

```js
{ family: "Alegreya", style: "ExtraBold" }
```

Never guess style names. Load the selected font with `await figma.loadFontAsync(fontName)` before creating or editing text.

## 3. Prepare local rasters

Create a temporary working directory.

Generate:

- `background-landscape.png`
- `background-square.png`
- `company-logo-trimmed.png`, only for company-logo mode
- rectangular source-backed crops when the original background is already suitable
- independent transparent element PNGs when recomposition is the strongest strategy

Example:

```bash
python3 scripts/prepare_image.py fit-background \
  --input SOURCE \
  --output background-landscape.png \
  --width 900 --height 383 \
  --mode cover --focus-x 0.5 --focus-y 0.5
```

Use `contain-solid` when cropping would lose the subject and the source has a simple edge background. Use `contain-blur` only for photographic or textured backgrounds. Every adaptation must preserve the source style.

Use `--contain-scale`, `--align-x`, and `--align-y` to recompose the intact source on the extended canvas when the default centered placement conflicts with the central-content footprint.

Prefer `crop-region` when the original white, red, or other simple background can remain visible. Use `--cover-polygon` only to remove an unrelated fragment from a continuous flat background.

Use `extract-polygon` to separate source elements without generative redrawing only when a transparent layer is necessary. When subjects overlap inside a broad selection, repeat `--exclude-polygon` to subtract unrelated regions before upload. Inspect every cutout at 100%; refine masks until no fragment of another subject remains. Upload extracted elements as independent Figma layers and compose them according to the source-specific hierarchy.

## 4. Duplicate and update the master

Duplicate the validated `海外独角兽封面｜MASTER` Section into clear canvas space, rename it for the current run, and update its existing layers. Do not rebuild frames, brand-logo layers, safe margins, or combined-preview spacing from scratch.

The master must contain:

- landscape, square, and combined frames at the exact required dimensions;
- full-frame background/image placeholders;
- centered keyword/company-logo containers;
- fixed brand-logo image layers;
- hidden optional `Title Support` layers;
- the 24 px combined-preview gap and correctly scaled square preview.
- one hidden `Source Upload Cache` rectangle for a single ordinary-source upload.

Perform master validation, clear-position calculation, duplication, keyword replacement, font sizing, title positioning, optional-support configuration, combined-preview rebuilding, export-setting updates, and the combined QA screenshot in one `use_figma` call for an ordinary run. Return every mutated node ID. Do not edit text until the selected font has been loaded.

Place the Section at the discovered clear page position. Use the non-overlapping child positions declared in `layout-spec.md`. Resize the Section from actual child bounds after its contents are complete.

Set export settings on the three top-level outputs to PNG at scale 1.

## 5. Upload the image assets

For the normal direct-crop route:

- upload the original image once to the master’s hidden `Source Upload Cache`;
- capture the HTTP response’s `imageHash`;
- assign that same hash to landscape and square `Background` fills in `use_figma`;
- use separate `scaleMode: "CROP"` paints and `imageTransform` values to preserve proportions while independently moving/scaling each format's focal crop.

Ordinary sources should upload once and reuse the same `imageHash` across both formats. If a proposed ordinary-source solution requires more than two uploaded source assets or more than two Figma layout rounds, pause and simplify the adaptation before proceeding.

For routes that genuinely produce different rasters or separated elements, upload only those required assets:

- upload each prepared extended background to its matching `Background` node;
- in company-logo mode, upload the trimmed company logo to each `Center Content` image node using `FIT`.

Do not upload the same ordinary source separately to landscape and square.

The master already contains the fixed brand logo. Do not request new upload URLs or upload the bundled logo during a normal run. Upload it only while creating or repairing the master.

The canonical brand source is `assets/haiwai-unicorn-logo-white.png`: 928 × 801 RGBA pixels, SHA-256 `aac7770a785256cc83ed88987959f570866da224ac41aa9e74b97654f7c02b36`. Keep the master logo fill linked to this original asset with `FIT`. Never populate brand-logo layers from screenshots, chat previews, exported cover PNGs, thumbnails, or recompressed derivatives.

Do not send credentials, tokens, or unrelated files to upload URLs.

## 6. Add or refine center content

For keyword mode:

- load the chosen font;
- create the text in both covers;
- fit it into 360 × 150 px in landscape or 500 × 230 px in square;
- start short two-line titles near 64 px / 72 px line height in landscape and 88 px / 100 px line height in square, then adjust optically;
- use neutral tracking by default; add negative tracking only when the letterforms remain visibly open;
- preserve comfortable space between the two lines and at least roughly half a cap-height of optical padding inside any title-support layer;
- use explicit range styling for highlighted terms;
- center geometrically after final sizing;
- return all created or mutated node IDs.

For company-logo mode, inspect the uploaded logo in both covers and verify it is not visually undersized because of residual padding.

Prefer a clean transparent company-logo asset when edge-background removal is safe. Inspect it at 100% before upload. Preserve the original opaque version when transparency introduces halos, missing internal whites, broken counters, or damaged thin strokes.

Before upload, preview the cutout on checkerboard, light neutral, and dark/saturated backgrounds. Fail it for any residual matte rectangle, original edge color, white/gray fringe, halo, or dirty antialiasing. If it fails, use an official transparent/vector asset or the original opaque logo with the smallest intentional source-coordinated support; never upload a dirty pseudo-transparent cutout.

Prefer an official matching SVG/vector logo before raster upload. For a raster asset, compare native dimensions with every target footprint and fail any placement that enlarges the source or produces soft edges at 100%. Require at least 1.5× source pixels per displayed pixel and prefer 2× for fine wordmarks. Keep the supplied logo generation/version unless the user approves a redesign.

## 7. Title support and brand-logo contrast

First evaluate keyword/company-logo legibility with `Title Support` hidden.

- Leave it hidden when natural negative space and contrast are sufficient.
- Reject title placement over rapidly alternating colors, dense edges, embedded text, or multiple high-saturation regions. Recompose the artwork to create a stable reading zone before adding support.
- Never add a pure-white card or white gradient.
- If support is necessary, use a compact non-white translucent tint, restrained source- or brand-colored gradient, local weakening, or tonal veil.
- Adapt support shape, size, color, opacity, and radius to the current source.
- Prefer the smallest intervention that stabilizes readability and improves the overall composition. Keep the treatment mature and editorial; avoid cute rounding, candy-like gradients, thick outlines, glow, or excessive shadow.
- Never default to a fixed white rounded rectangle.

Apply the specified shadow only where the white logo lacks contrast. Reassign the full effects array; do not mutate it in place.

During QA, inspect the brand logo at 100% in the final export. If it appears soft or pixelated, fail the export and repair the master from the canonical 928 × 801 asset. Do not compensate with sharpening, larger display size, or another raster export/re-upload cycle.

During QA, fail the cover if individual letterforms lose clarity as they cross several colors, high-frequency edges, or source typography—even when the title is technically large enough.

For two-line titles, evaluate each line independently in both covers and in the reduced combined preview. The second line must not become less prominent because it crosses a busy object or similar-value region. Correct the reading zone or whole-title treatment before export.

If partial letterforms remain difficult to read after reasonable repositioning, reveal and adapt `Title Support`; do not keep it hidden merely to obtain a background-free appearance. Use one compact source-coordinated translucent panel or veil behind the complete title. For light illustrations, prefer warm ivory, pale gray, or a source tint rather than opaque pure white.

## 8. Batched layout and combined preview

For the normal route, use one atomic `use_figma` mutation after the source upload:

1. Validate the fixed master, compute the rightmost occupied bound, and choose the clear target position.
2. Duplicate and rename the fixed master Section.
3. Apply the shared `imageHash` with independent crop transforms.
4. Update keyword, font size, line height, tracking, and alignment.
5. Decide and configure title support for each format.
6. Configure the brand-logo shadow from local contrast.
7. Rebuild the combined preview: landscape at 900 × 383, square rescaled by `383 / 900` at x = 924, with a 24 px white gap.
8. Capture and return one inline screenshot of the final combined preview.

Return IDs for the combined frame and both clones.

## 9. Visual validation

Default to the inline combined-preview screenshot returned by the main mutation. Do not request a separate screenshot or metadata pass when it is sufficient. Request individual landscape or square screenshots only if the combined preview indicates a crop, obstruction, low-contrast, masking, or fine-detail risk. Allow at most one targeted correction call for an ordinary source; if another seems necessary, simplify and reassess the adaptation first. Fix:

- cropping that hides the subject;
- adaptation that changes the source style, colors, lighting, materials, text, or object geometry;
- adaptation that splits a continuous source illustration, sequence, diagram, directional flow, or object group into disconnected fragments and changes its intended reading;
- low contrast;
- off-center content;
- text overflow;
- logo distortion;
- soft, pixelated, recompressed, or repeatedly rasterized 海外独角兽 branding;
- company-logo residual matte, edge-color haze, white/gray fringe, or halo on light, dark, or saturated backgrounds;
- raster company-logo upscaling, soft edges at 100%, or failure to use an available matching official vector;
- content scale that is inconsistent with the format-specific master footprint;
- a square title that becomes too small or cramped after the square is reduced to 383 × 383;
- a two-line title whose second line is materially less legible or prominent than the first;
- wrong combined spacing.
- passive empty space that makes the source subjects feel timid;
- any mask halo, polygon edge, foreign fragment, or background mismatch.
- unnecessary, oversized, or source-incompatible title support.
- pure-white cards, habitual white gradients, or generic title plates that feel pasted onto the image.
- childish, toy-like, gaudy, overly cute, or excessively effect-heavy styling.

Do not proceed to export on a failed validation.

## 10. Export and deep links

Request the three `download_assets` calls in parallel for the standard deliverables, then download their URLs in parallel:

- `defaultScale: 1` for the standard PNG;

Use `defaultScale: 2` only when the user requests high-resolution/final delivery, the output has a known larger downstream use, or the standard export exposes a real raster-quality concern.

Save each exported PNG with the names specified in `SKILL.md`.

Do not validate the Skill package, sync the desktop copy, or touch GitHub during a normal image run. Those are maintenance actions for actual Skill-file changes only.

Construct deep links from the fixed file URL by adding `node-id=<normalized-id>`, replacing `:` with `-` in the query value. Preserve any required Figma URL structure.

Return:

- fixed workspace URL;
- landscape deep link;
- square deep link;
- combined deep link;
- three local PNG paths or hosted download links.
