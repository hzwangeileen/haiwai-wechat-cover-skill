# Figma runtime

Use this reference for every run.

Read `design-principles.md` before choosing the layout.

## 1. Open the supplied workspace

Require a user-provided editable Figma Design URL. Extract the active file key from that URL and use it consistently for every Figma call and deep link in the run.

Do not call `create_new_file`.

Start with a read-only `use_figma` call:

- verify the file is accessible;
- inspect top-level page nodes;
- find and validate the reusable top-level Section `海外独角兽封面｜MASTER`;
- find the rightmost occupied x-coordinate;
- return the target x-coordinate for the new run Section with at least 200 px clearance.

Stop if the file is unavailable or read-only.

## 2. Font handling

When a validated master exists, inherit its established font and skip `listAvailableFontsAsync()` during normal runs.

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

When practical, perform master duplication, keyword replacement, font sizing, title positioning, optional-support configuration, and export-setting updates in one `use_figma` call. Return every mutated node ID. Do not edit text until the selected font has been loaded.

Place the Section at the discovered clear page position. Use the non-overlapping child positions declared in `layout-spec.md`. Resize the Section from actual child bounds after its contents are complete.

Set export settings on the three top-level outputs to PNG at scale 1.

## 5. Upload the image assets

For the normal direct-crop route:

- upload the original image once to the master’s hidden `Source Upload Cache`;
- capture the HTTP response’s `imageHash`;
- assign that same hash to landscape and square `Background` fills in `use_figma`;
- use separate `scaleMode: "CROP"` paints and `imageTransform` values to preserve proportions while independently moving/scaling each format’s focal crop.

For routes that genuinely produce different rasters or separated elements, upload only those required assets:

- upload each prepared extended background to its matching `Background` node;
- in company-logo mode, upload the trimmed company logo to each `Center Content` image node using `FIT`.

Do not upload the same ordinary source separately to landscape and square.

The master already contains the fixed brand logo. Do not request new upload URLs or upload the bundled logo during a normal run. Upload it only while creating or repairing the master.

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

## 7. Title support and brand-logo contrast

First evaluate keyword/company-logo legibility with `Title Support` hidden.

- Leave it hidden when natural negative space and contrast are sufficient.
- Reject title placement over rapidly alternating colors, dense edges, embedded text, or multiple high-saturation regions. Recompose the artwork to create a stable reading zone before adding support.
- If support is necessary, adapt its shape, size, color, opacity, blur/gradient treatment, and radius to the current source.
- Prefer the smallest intervention that stabilizes readability and improves the overall composition.
- Never default to a fixed white rounded rectangle.

Apply the specified shadow only where the white logo lacks contrast. Reassign the full effects array; do not mutate it in place.

During QA, fail the cover if individual letterforms lose clarity as they cross several colors, high-frequency edges, or source typography—even when the title is technically large enough.

## 8. Batched layout and combined preview

For the normal route, prefer one `use_figma` mutation after the source upload:

1. Duplicate and rename the master Section.
2. Apply the shared `imageHash` with independent crop transforms.
3. Update keyword, font size, line height, tracking, and alignment.
4. Decide and configure title support for each format.
5. Configure the brand-logo shadow from local contrast.
6. Rebuild the combined preview: landscape at 900 × 383, square rescaled by `383 / 900` at x = 924, with a 24 px white gap.

Return IDs for the combined frame and both clones.

## 9. Visual validation

Default to one inline screenshot or one screenshot of the final combined preview. Request individual landscape or square screenshots only if the combined preview indicates a crop, obstruction, low-contrast, masking, or fine-detail risk. Fix:

- cropping that hides the subject;
- adaptation that changes the source style, colors, lighting, materials, text, or object geometry;
- low contrast;
- off-center content;
- text overflow;
- logo distortion;
- content scale that is inconsistent with the format-specific master footprint;
- a square title that becomes too small or cramped after the square is reduced to 383 × 383;
- wrong combined spacing.
- passive empty space that makes the source subjects feel timid;
- any mask halo, polygon edge, foreign fragment, or background mismatch.
- unnecessary, oversized, or source-incompatible title support.

Do not proceed to export on a failed validation.

## 10. Export and deep links

Request the three `download_assets` calls in parallel for the standard deliverables, then download their URLs in parallel:

- `defaultScale: 1` for the standard PNG;

Use `defaultScale: 2` only when the user requests high-resolution/final delivery, the output has a known larger downstream use, or the standard export exposes a real raster-quality concern.

Save each exported PNG with the names specified in `SKILL.md`.

Do not validate the Skill package, sync a desktop copy, or touch GitHub during a normal image run. Those are maintenance actions for actual Skill-file changes only.

Construct deep links from the active file URL by adding `node-id=<normalized-id>`, replacing `:` with `-` in the query value. Preserve any required Figma URL structure.

Return:

- active workspace URL;
- landscape deep link;
- square deep link;
- combined deep link;
- three local PNG paths or hosted download links.
