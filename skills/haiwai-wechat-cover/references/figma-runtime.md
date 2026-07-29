# Figma runtime

Use this reference for every run.

Read `design-principles.md` before choosing the layout.

## 1. Resolve and open the workspace

Use the user-provided editable Figma Design URL when present. Otherwise use the default:

- file key: `EipE7fkEv9xLOzqX7yqSAP`
- file URL: `https://www.figma.com/design/EipE7fkEv9xLOzqX7yqSAP/Untitled`

Extract the active file key from the resolved URL and use it consistently for every Figma call and deep link in the run.

Do not call `create_new_file`.

Start with a read-only `use_figma` call:

- verify the file is accessible;
- inspect top-level page nodes;
- find the rightmost occupied x-coordinate;
- return the target x-coordinate for the new run Section with at least 200 px clearance.

Stop if the file is unavailable or read-only.

## 2. Font discovery

Load `figma-use`. Run a read-only discovery call before creating keyword text:

```js
const fonts = await figma.listAvailableFontsAsync()
const albertus = fonts
  .map(f => f.fontName)
  .filter(f => f.family.toLowerCase() === 'albertus nova')
return { albertus }
```

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

## 4. Build the skeleton

Use one incremental `use_figma` call to create a run-specific top-level Section, then create the three output frames inside it. Keep each call under 10 logical operations where practical.

Create the main cover frames first. Add:

- a full-frame background rectangle;
- source-specific image layers or extracted element layers;
- a centered content layer;
- a brand-logo rectangle;
- meaningful names for every node.

Return every created node ID. Do not create text until the selected font has been loaded.

Place the Section at the discovered clear page position. Use the non-overlapping child positions declared in `layout-spec.md`. Resize the Section from actual child bounds after its contents are complete.

Set export settings on the three top-level outputs to PNG at scale 1.

## 5. Upload the image assets

Use Figma `upload_assets` with the target node ID:

- upload each prepared background to its matching `Background` node using `FILL`;
- upload the bundled brand logo to each `Haiwai Unicorn Logo` node using `FIT`;
- in company-logo mode, upload the trimmed company logo to each `Center Content` image node using `FIT`.

Upload the same source separately for each target node when required by the tool's single-use upload URL contract.

Do not send credentials, tokens, or unrelated files to upload URLs.

## 6. Add or refine center content

For keyword mode:

- load the chosen font;
- create the text in both covers;
- fit it into 360 × 150 px in landscape or 500 × 230 px in square;
- start short two-line titles near 70 px / 66 px line height in landscape and 100 px / 92 px line height in square, then adjust optically;
- use explicit range styling for highlighted terms;
- center geometrically after final sizing;
- return all created or mutated node IDs.

For company-logo mode, inspect the uploaded logo in both covers and verify it is not visually undersized because of residual padding.

## 7. Brand logo contrast

Inspect screenshots of both main covers.

Apply the specified shadow only where the white logo lacks contrast. Reassign the full effects array; do not mutate it in place.

## 8. Combined preview

After the two main covers are correct:

1. Clone the landscape frame into the combined frame at its original size.
2. Clone the square frame.
3. Rescale the square clone by `383 / 900`.
4. Position it at x = 924, y = 0.
5. Keep the combined frame white and 1307 × 383.

Return IDs for the combined frame and both clones.

## 9. Visual validation

Use inline screenshots or `get_screenshot` after each major stage. Fix:

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

Do not proceed to export on a failed validation.

## 10. Export and deep links

Use `download_assets` twice per top-level output frame:

- `defaultScale: 1` for the standard PNG;
- `defaultScale: 2` for the high-resolution master.

Save each exported PNG with the names specified in `SKILL.md`.

Construct deep links from the active file URL by adding `node-id=<normalized-id>`, replacing `:` with `-` in the query value. Preserve any required Figma URL structure.

Return:

- active workspace URL;
- landscape deep link;
- square deep link;
- combined deep link;
- three local PNG paths or hosted download links.
