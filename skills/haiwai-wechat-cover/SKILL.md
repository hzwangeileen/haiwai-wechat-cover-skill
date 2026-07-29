---
name: haiwai-wechat-cover
description: Create premium 海外独角兽-branded WeChat cover packages from a user-selected image or image elements plus either a centered keyword or company logo. Use when Codex must design source-specific 2.35:1 and 1:1 covers, intelligently crop or recompose elements without changing their visual style, preserve editable Figma layers, export standard and 2× high-resolution PNGs, and return direct Figma links.
---

# 海外独角兽微信封面

Create every cover in the designated editable Figma workspace, then export standard and 2× PNGs for:

- 900 × 383 landscape cover
- 900 × 900 square cover
- 1307 × 383 side-by-side preview

Use the bundled white 海外独角兽 logo. Keep the selected background, central keyword or company logo, and brand logo as separate editable Figma layers.

## Required inputs

Require:

1. One selected background image.
2. Exactly one central-content mode:
   - keyword text; or
   - company logo image.

Accept optional:

- highlighted keyword ranges and explicit colors, such as `AI=#B51F2A`;
- focal-point or subject-preservation instructions;
- an editable Figma Design file URL override;
- an output directory.

Ask only for missing required inputs. Apply the defaults below without repeatedly reconfirming them.

## Load runtime guidance

Before editing the Figma workspace:

1. Read [references/design-principles.md](references/design-principles.md).
2. Read [references/figma-runtime.md](references/figma-runtime.md).
3. Load the `figma-use` skill before every Figma `use_figma` call.
4. Discover deferred Figma tools when needed: `use_figma`, `upload_assets`, and `download_assets`.

Require a connected Figma MCP with edit access to the active file. If it is unavailable, disconnected, or read-only, ask the user for an editable Figma Design URL or corrected access and stop before producing a partial package.

Resolve the directory containing this `SKILL.md` as the skill directory. Use:

- brand asset: `assets/haiwai-unicorn-logo-white.png`
- image utility: `scripts/prepare_image.py`

Never assume the current working directory is the skill directory.

## Fixed output constraints

Follow [references/layout-spec.md](references/layout-spec.md) exactly.

Core rules:

- Center the keyword or company logo.
- Use format-specific master central-content footprints so both outputs remain readable at their actual display sizes:
  - landscape: at most 360 × 150 px;
  - square: at most 500 × 230 px.
- Keep sizing consistent across runs within each format. The square content is intentionally larger because it is reduced more aggressively in share cards and the combined preview.
- Preserve logo aspect ratios. Never stretch, crop, or distort a company logo.
- Prefer a single keyword line. Allow at most two lines; shrink long text instead of exceeding the footprint.
- Place the 海外独角兽 logo at the upper right, 81 px wide, with 3% top and right margins.
- Add a subtle dark shadow to the white brand logo only when the local background is light.
- Treat all other composition positions, scales, crops, and element relationships as source-specific design decisions, not a template.

## Design from first principles

Do not mechanically fit the whole source into a corner.

Before editing:

1. Inventory the meaningful subjects, embedded text, logos, shadows, empty space, palette, and visual style.
2. Decide which elements must stay intact and which can be separated or cropped.
3. Identify the intended hierarchy: central keyword or company logo first, source subject second, brand logo third.
4. Choose the least destructive strategy that produces a balanced premium composition:
   - native crop;
   - source-backed crop that keeps a suitable original background;
   - proportional repositioning on an extended canvas;
   - extraction and recomposition of separable source elements;
   - restrained cleanup or tonal balancing that preserves the original style.
5. Reject layouts with weak balance, accidental collisions, excessive dead space, or a subject merely squeezed into a corner.

Do not treat background removal as the default. If the source background is white, red, or any other color that already supports the composition, preserve it as part of the image. Prefer a native crop or source-backed crop over a transparent cutout.

Use `scripts/prepare_image.py crop-region` to keep a rectangular region with its original background. It may cover unrelated source fragments with the sampled edge color only when the background is simple and continuous.

Use `scripts/prepare_image.py extract-polygon` only when a composite source truly requires independent transparent elements and the mask can pass 100% inspection. Preserve their original pixels, typography, materials, lighting, and shadows.

The example layout for one source must never become the default template for another source.

## Prepare the images

Inspect the source image before deciding how to fit it.

Create exact-size background rasters with `scripts/prepare_image.py`:

- Use `cover` with a visually chosen focal point when cropping preserves the subject.
- Use `contain-solid` when cropping would remove important subject matter and the source has a simple or nearly uniform edge background.
- Use `contain-blur` only for photographic or textured backgrounds where a source-derived soft extension preserves continuity.

Adapt the aspect ratio without changing the original visual style. Cropping, repositioning, proportional scaling, and source-derived canvas extension are allowed. Preserve the source's palette, lighting, materials, typography, object geometry, and photographic or illustrative treatment.

Do not redraw, restyle, replace, or generatively reinterpret the subject. Do not use generative expansion unless the user explicitly requests it; even then, preserve the original style and never alter logos, charts, screenshots, products, text, or other detail-sensitive content.

When a contained source overlaps the centered keyword or logo, reduce its scale proportionally and align the intact source toward an edge of the extended canvas. Keep the active format's central footprint visually clear whenever possible.

When this creates an unbalanced or corner-heavy result, first try a larger native crop or source-backed crop. Extract and recompose only when those less destructive options cannot produce the required balance.

The utility requires Pillow. If the active Python cannot import `PIL`, use the Codex workspace dependency loader to locate the bundled Python runtime. Do not install packages or change the user's Python environment without approval.

For a company logo, run the same script in `trim-alpha` mode before upload. The script removes transparent padding and adds a small clean margin. If the logo has an opaque background, preserve it and do not guess at background removal.

## Resolve the Figma workspace

Use this Figma Design file by default:

- file key: `EipE7fkEv9xLOzqX7yqSAP`
- URL: `https://www.figma.com/design/EipE7fkEv9xLOzqX7yqSAP/Untitled`

When the user provides another editable Figma Design URL, use that file for the run instead. This makes the Skill portable for collaborators who do not have access to the default workspace.

Do not create a new Figma file automatically. Do not overwrite prior outputs.

Create a new top-level Section named:

`海外独角兽封面｜<keyword-or-company>｜<YYYY-MM-DD>`

Place the new Section in clear canvas space to the right of existing content. Keep all three output frames for the run inside this Section.

## Build editable Figma layers

Follow the incremental sequence in `references/figma-runtime.md`.

Create these top-level frames:

1. `01 Landscape 900x383`
2. `02 Square 900x900`
3. `03 Combined Preview 1307x383`

Within each main cover, create named layers:

- `Background`
- `Center Content`
- `Haiwai Unicorn Logo`

For keyword mode:

1. Call `listAvailableFontsAsync()`.
2. Prefer `Albertus Nova` and its heaviest suitable upright style.
3. If unavailable, use exactly `Alegreya ExtraBold`.
4. Default to black or white based on contrast at the center of the image.
5. Apply user-specified highlight colors only to the specified ranges.
6. Report the actual font used and whether fallback occurred.

For company-logo mode:

- Upload the trimmed transparent image.
- Fit it inside the active format's master footprint: 360 × 150 px for landscape or 500 × 230 px for square.
- Preserve aspect ratio and transparency.

Construct the combined preview after the two main covers pass visual QA. Clone the completed covers: keep the landscape at 900 × 383, scale the square clone to 383 × 383, and separate them with a 24 px white gap.

## Validate and export

Visually inspect both main covers and the combined preview in Figma.

Check:

- exact frame dimensions;
- important subject matter remains visible;
- the adapted image preserves the original style, palette, lighting, materials, typography, and object geometry;
- center content is geometrically centered;
- each format uses its specified master content scale;
- the square title or company logo remains clearly readable after the square is reduced to 383 × 383 in the combined preview;
- no keyword overflow or unintended wrapping;
- no logo distortion or transparent-padding shrinkage;
- brand logo position, contrast, and safe margins;
- combined preview order and spacing.
- deliberate visual hierarchy, balance, rhythm, and premium finish;
- no element appears mechanically squeezed into a corner;
- source elements remain crisp at their displayed size.
- subject and center-content scale feels confident rather than surrounded by uncontrolled empty space;
- no large neutral region dominates the frame without a deliberate compositional purpose;
- no cutout halo, foreign fragment, polygon edge, or background mismatch is visible at 100%.

Fix issues before exporting.

Export PNGs with these names:

- `<slug>-wechat-landscape-900x383.png`
- `<slug>-wechat-square-900x900.png`
- `<slug>-wechat-combined-1307x383.png`

Also export 2× high-resolution masters:

- `<slug>-wechat-landscape-1800x766@2x.png`
- `<slug>-wechat-square-1800x1800@2x.png`
- `<slug>-wechat-combined-2614x766@2x.png`

Return:

1. links or paths to all standard and 2× PNGs;
2. the active Figma workspace URL;
3. direct `node-id` links to all three output frames;
4. the font actually used;
5. a brief note if fallback font, blurred extension, or any other adaptive treatment was used.

Do not claim an export or Figma link exists until the corresponding tool call succeeds.
