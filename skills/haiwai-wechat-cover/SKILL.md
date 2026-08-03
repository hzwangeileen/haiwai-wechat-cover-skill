---
name: haiwai-wechat-cover
description: Create premium 海外独角兽-branded WeChat cover packages from a user-selected image or image elements plus either a centered keyword or company logo. Use when Codex must design source-specific 2.35:1 and 1:1 covers, intelligently crop or recompose elements without changing their visual style, preserve editable Figma layers, export production-ready PNGs, and return direct Figma links.
---

# 海外独角兽微信封面

Create every cover in the designated editable Figma workspace, then export production-ready PNGs for:

- 900 × 383 landscape cover
- 900 × 900 square cover
- 1307 × 383 side-by-side preview

Use the bundled white 海外独角兽 logo. Keep the selected background, central keyword or company logo, and brand logo as separate editable Figma layers.

Use one default high-quality workflow. Do not expose or invent separate “fast”, “standard”, or “refined” modes. Aim to complete ordinary sources in roughly 2–3 minutes by reusing the fixed Figma master, uploading assets only when necessary, batching safe Figma mutations, and limiting QA/export work. Let complex sources take longer; never trade deformation, crude cropping, weak hierarchy, or a generic look for speed.

Optimize for useful visual quality per minute. Spend time only on changes that materially improve:

1. subject completeness;
2. title readability;
3. compositional balance and visual integration.

Choose the cheapest reversible treatment that clears all three gates. Stop designing once the combined preview is attractive, clear, balanced, and free of visible defects. Do not add layers, effects, masks, gradients, alternate versions, or extra inspection passes merely to make the process appear more refined.

Judge the final cover from first principles, not by whether it follows a familiar template. Require a premium, mature, editorial finish with controlled contrast, confident spacing, clean edges, and restrained effects. Reject results that feel childish, toy-like, crude, excessively cute, visually noisy, or generically “AI designed,” even when every required element is technically present.

## Required inputs

Require:

1. One selected background image.
2. Exactly one central-content mode:
   - keyword text; or
   - company logo image.

Accept optional:

- highlighted keyword ranges and explicit colors, such as `AI=#B51F2A`;
- focal-point or subject-preservation instructions;
- a Figma team override;
- an output directory.

Ask only for missing required inputs. Apply the defaults below without repeatedly reconfirming them.

## Load runtime guidance

For an ordinary single-image source with an obvious lightweight adaptation route:

1. Read [references/figma-runtime.md](references/figma-runtime.md) and [references/layout-spec.md](references/layout-spec.md).
2. Apply the core design rules in this `SKILL.md` without loading extra references.
3. Load the `figma-use` skill before every Figma `use_figma` call.
4. Discover deferred Figma tools only when needed: `use_figma`, `upload_assets`, and `download_assets`.

Read [references/design-principles.md](references/design-principles.md) only when crop versus extension is genuinely ambiguous, multiple subjects conflict, light adaptation cannot create a stable title zone, or the first combined-preview QA fails for a compositional reason.

Require a connected Figma MCP with edit access to the designated file. If it is unavailable, disconnected, or read-only, ask the user to fix access and stop before producing a partial package.

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
- Give two-line titles visible breathing room. Do not use line height smaller than the font size or negative tracking by default. Reduce type size before tightening line spacing, tracking, or support-layer padding.
- Treat the supplied Agent Identity reference as the canonical title appearance: Kadwa Regular, upright, centered, neutral tracking, and a calm two-line stack. Use 35 px font size with 46 px line height in the 900 × 383 landscape frame. In the 900 × 900 square frame, use 82 px with 108 px line height so its reduction to 383 × 383 reproduces the same approximately 35 px / 46 px visual scale.
- Place the 海外独角兽 logo at the upper right, 81 px wide, with 3% top and right margins.
- Add a subtle dark shadow to the white brand logo only when the local background is light.
- Treat the bundled `assets/haiwai-unicorn-logo-white.png` as the canonical high-resolution brand master. Its expected source is 928 × 801 RGBA pixels with SHA-256 `aac7770a785256cc83ed88987959f570866da224ac41aa9e74b97654f7c02b36`. Never substitute a screenshot, chat thumbnail, preview export, recompressed copy, or previously exported cover crop.
- Preserve the brand logo with Figma `FIT` behavior and proportional geometry. Never stretch, squash, crop, rasterize, sharpen, or repeatedly export and re-upload it. At 81 px display width, always render from the canonical master already embedded in the fixed Figma template.
- Treat any title or company-logo background, plate, gradient, blur, or local weakening as optional. First test the content directly on the composition. If it is clearly readable, use no support at all.
- Never use a pure-white support plate or default white gradient. If support is genuinely necessary, derive a compact translucent tint, restrained source-colored gradient, or local tonal veil from the image and logo palette. Keep it subtle, mature, and no larger than required.
- Do not over-prioritize a background-free title. If any word, line, or material part of the letterforms becomes hard to read over multicolor objects, source typography, or changing light/dark regions, add a compact coordinated translucent support after reasonable placement adjustments. A light illustration may use a warm ivory, pale gray, or source-tinted translucent panel; keep it visibly integrated and distinct from a default opaque white card.
- Treat all other composition positions, scales, crops, and element relationships as source-specific design decisions, not a template.

## Design from first principles

Do not mechanically fit the whole source into a corner or park the entire visual group on one side of a landscape cover.

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

Make this decision once for an ordinary source. Prefer, in order: independent proportional crops with focal adjustment; proportional containment on an extended source-color canvas; movement or weakening of one local conflict; multi-element separation only when the first three cannot satisfy the quality gates. Do not generate speculative alternatives unless the first combined preview fails.

For landscape covers, never confine all meaningful source content to only the left or right outer third while the opposite side remains visually empty. Asymmetry is allowed, but the visual mass must cross the center axis, distribute through upper/lower zones, or gain a genuine counterweight from another source element. The centered title and empty space alone do not count as sufficient counterweight. Prefer a centered proportional crop or a source-wide distribution before moving the entire image group to one side.

For title legibility, judge the final composition in this order:

1. Use natural negative space with no backing when the title or company logo is already clear.
2. Reposition or reframe source elements when that creates a better title zone without harming the subject.
3. Only when necessary, add the least intrusive coordinated support: a compact non-white translucent tint, a restrained source-colored gradient, local weakening, or a tonal veil.
4. Size and shape that support for the current source. Do not reuse a fixed white rounded rectangle, opacity, radius, or footprint across unrelated images.

The absence of a title backing is not a goal by itself, and the presence of one is not a quality signal. The test is whether the whole cover feels intentional, premium, immediately readable, and visually integrated with the source rather than carrying a generic pasted-on label.

Require a stable low-interference reading zone for every title. Do not solve a noisy title area merely by increasing font size or weight. If letterforms cross rapidly alternating light/dark regions, saturated color changes, dense edges, or embedded source text, reframe or recompose the artwork first; add restrained local support only when the composition still needs it.

Do not treat background removal as the default. If the source background is white, red, or any other color that already supports the composition, preserve it as part of the image. Prefer a native crop or source-backed crop over a transparent cutout.

Use `scripts/prepare_image.py crop-region` to keep a rectangular region with its original background. It may cover unrelated source fragments with the sampled edge color only when the background is simple and continuous.

Use `scripts/prepare_image.py extract-polygon` only when a composite source truly requires independent transparent elements and the mask can pass 100% inspection. Preserve their original pixels, typography, materials, lighting, and shadows.

The example layout for one source must never become the default template for another source.

Default to minimum necessary recomposition. Preserve the source's overall relationships whenever possible. Prefer, in order: proportional scaling, position adjustment, small crops, extension of the native background, or moving one or two key elements to open a clear title zone. If moving solves the problem, do not split the image. If the overall composition can survive, do not rebuild it. Use multi-element separation and rearrangement only when lighter adjustments still cannot preserve the subject, title readability, and compositional balance together. Never redesign a source merely to demonstrate recomposition.

Treat continuity as semantic, not merely visual. Never split one continuous illustration, process, sequence, diagram, object group, or directional composition into disconnected left/right or top/bottom fragments just to open a title gap. Do not duplicate, mirror, reorder, or spatially separate source regions when that changes how the original is read. Preserve the intact source as one proportional unit whenever its internal relationships carry meaning; create the title zone with native-background extension, whole-image scaling/repositioning, or minimal local weakening instead.

## Prepare the images

Inspect the source image before deciding how to fit it.

Never require the uploaded source to match either WeChat output ratio. Treat mismatched dimensions as normal. Adapt each format independently with visually chosen cropping, proportional scaling, downsampling, and ordinary image compression as needed. Reframe the source to improve composition while preserving important subjects and useful detail.

“Compression” means proportional resizing and sensible file-size optimization. Never stretch width and height independently, squash objects, alter proportions, or lower image quality enough to create visible artifacts.

Classify the source before choosing tools. Follow the routing matrix in [references/design-principles.md](references/design-principles.md):

1. If proportional cropping preserves the subject, upload the original once and reuse its Figma `imageHash` for both formats with independent crop transforms and focal positions.
2. If cropping loses the subject and the background is white, solid, or a simple gradient, extend that background and proportionally scale/reposition the subject.
3. If only the title zone is blocked, move or locally weaken one or two elements; do not split the whole image.
4. Only when multiple subjects genuinely cannot be retained together, separate the minimum number of elements and proportionally recompose them.
5. If a photograph, complex texture, or spatial scene genuinely needs unseen content, perform a style-preserving image edit or generative extension before Figma layout.

Ordinary sources must default to this lightweight adaptation path. Never escalate an aspect-ratio mismatch by itself into element separation or complex recomposition. If the proposed approach requires more than two source-asset uploads or more than two Figma layout rounds, stop and reassess whether proportional scaling, focal-point adjustment, native-background extension, or local weakening can solve it.

Interpret “turn this vertical image into a horizontal image” as extending or reconstructing the composition, never as horizontally stretching the whole image. Allow limited non-uniform widening only for pure, deformation-safe texture or gradient backgrounds. Never deform people, products, text, logos, charts, screenshots, illustrations, or geometric objects.

Reject direct cropping when it retains less than roughly 60% of the meaningful composition, or when important elements occupy both the top and bottom of the source and cannot survive together. Route such sources to source-derived canvas extension or element recomposition even when a crop would be faster.

Create exact-size background rasters with `scripts/prepare_image.py`:

- Use `cover` with a visually chosen focal point when cropping preserves the subject.
- Use `contain-solid` when cropping would remove important subject matter and the source has a simple or nearly uniform edge background.
- Use `contain-blur` only for photographic or textured backgrounds where a source-derived soft extension preserves continuity.

Adapt the aspect ratio without changing the original visual style. Cropping, repositioning, proportional scaling, and source-derived canvas extension are allowed. Preserve the source's palette, lighting, materials, typography, object geometry, and photographic or illustrative treatment.

Do not redraw, restyle, replace, or generatively reinterpret the subject. Use generative extension only when the routing matrix identifies missing photographic, textured, or spatial content that cannot be solved with a crop or source-derived extension. Preserve the original style and protect logos, charts, screenshots, products, text, faces, and other detail-sensitive content.

When a contained source overlaps the centered keyword or logo, reduce its scale proportionally and align the intact source toward an edge of the extended canvas. Keep the active format's central footprint visually clear whenever possible.

When this creates an unbalanced or corner-heavy result, first try a larger native crop or source-backed crop. Extract and recompose only when those less destructive options cannot produce the required balance.

The utility requires Pillow. If the active Python cannot import `PIL`, use the Codex workspace dependency loader to locate the bundled Python runtime. Do not install packages or change the user's Python environment without approval.

For a company logo:

1. Prefer the company's official SVG/vector asset when it is available and matches the logo version supplied by the user. Do not replace an older supplied identity with a newer redesign without confirmation.
2. Before placing a raster logo, compare its native pixel dimensions with the largest displayed footprint. Require at least 1.5× pixel coverage for a normal 1× export and prefer 2× coverage when the logo contains fine curves, small type, or may be reused at higher resolution. Never enlarge a raster beyond its native dimensions and ship visibly soft edges.
3. If the raster is undersized, search the official company site, official documentation CDN, or official repository for the matching SVG/vector version. If no matching vector or higher-resolution asset is available, reduce the displayed size to a crisp level or ask for a better source; do not invent detail with sharpening or AI upscaling.
4. If it already has transparency, run `trim-alpha` before upload.
5. If it has a uniform or nearly uniform edge background, prefer `remove-edge-background --trim` to create a transparent cutout.
6. Inspect the transparent result at 100% on a checkerboard plus both a light and a dark/high-saturation test background. Reject it if any rectangular matte, edge-color residue, white/gray fringe, halo, dirty antialiasing, missing internal white region, broken counter, damaged thin stroke, shadow, or altered brand color remains. A transparent canvas alone is not evidence of a clean cutout.
7. Test the clean transparent logo directly on the composition first. If it is readable, add no support.
8. If it is not readable, add a compact source- or brand-coordinated tinted gradient or translucent non-white support. Never place the logo on a default pure-white card.
9. When clean removal cannot pass the three-background test, prefer an official transparent/vector logo. Otherwise preserve the original opaque logo inside the smallest intentional, source-coordinated support treatment; never ship a visibly dirty pseudo-transparent cutout.

## Use the fixed Figma workspace

Use this Figma Design file and its reusable master for every run:

- file key: `EipE7fkEv9xLOzqX7yqSAP`
- URL: `https://www.figma.com/design/EipE7fkEv9xLOzqX7yqSAP/Untitled`

Do not create a new Figma file. Do not overwrite prior outputs.

Find the top-level Section named `海外独角兽封面｜MASTER`. Duplicate its landscape, square, and combined frames into a new run-specific Section. The master owns:

- exact canvas sizes and combined-preview spacing;
- fixed 海外独角兽 logo layers, safe margins, and logo shadow defaults;
- reusable centered keyword/company-logo containers;
- an optional title-support layer that is hidden by default.
- a hidden `Source Upload Cache` image node used to upload an ordinary source once and capture its reusable `imageHash`.

Do not upload the fixed brand logo again when the master is available. Replace only source-specific image/company-logo fills and text. If the master is missing or structurally invalid, repair it once from the bundled assets, then continue from the repaired master.

Treat a soft or pixelated 海外独角兽 logo as a broken master, not an acceptable export. Verify that every cloned brand-logo layer still uses the canonical high-resolution image fill with `FIT`. If a layer points to a thumbnail, screenshot, derived PNG, or degraded re-upload, replace it from the bundled canonical asset before export.

Create a new top-level Section named:

`海外独角兽封面｜<keyword-or-company>｜<YYYY-MM-DD>`

Place the new Section in clear canvas space to the right of existing content. Keep all three output frames for the run inside this Section.

## Build editable Figma layers

Follow the batched sequence in `references/figma-runtime.md`.

Duplicate these top-level master frames:

1. `01 Landscape 900x383`
2. `02 Square 900x900`
3. `03 Combined Preview 1307x383`

Within each main cover, create named layers:

- `Background`
- `Center Content`
- `Haiwai Unicorn Logo`
- `Title Support` (optional and hidden by default)

For keyword mode:

1. Use exactly `{ family: "Kadwa", style: "Regular" }` for the default title. Do not inherit the old Alegreya/Albertus setting from earlier master versions.
2. Load Kadwa Regular directly and skip font discovery when it succeeds. If the exact family/style is unavailable, stop and report the missing font; do not silently substitute another family or weight.
3. Use 35 px font size and 46 px line height in the 900 × 383 landscape frame.
4. Use 82 px font size and 108 px line height in the 900 × 900 square frame; this becomes approximately 35 px / 46 px after the square is scaled to 383 × 383.
5. Use upright text, neutral tracking, centered paragraph alignment, and centered vertical/horizontal placement. Prefer a balanced two-line stack for a two-part title, as in `Agent\nIdentity`; use no more than two lines.
6. Default to black or white based on the stable title-zone contrast. Apply user-specified highlight colors only to explicitly specified ranges.
7. Keep these sizes fixed by default. Reduce only when the supplied title would overflow its footprint; never enlarge merely to fill empty space. Report any size reduction.

For a two-line keyword, validate each line independently at final display size and again inside the 383 × 383 combined preview. Both lines must have comparable prominence and fully readable letterforms. Do not accept a title because the first line is strong while the second line crosses a busy object, similar-value color, source typography, or high-frequency edge. Fix the weaker line by moving the intact title/source, adjusting the title zone, changing the whole title color, or adding the smallest integrated local veil; do not solve it by crowding, outlining, or styling the two lines as unrelated elements.

When direct placement still causes partial letter loss, title support becomes required rather than optional. Apply one unified support treatment behind the whole title so both lines retain equal hierarchy. Do not leave a title technically visible but effortful to read merely to preserve a “no background” look.

For company-logo mode:

- Prefer a clean trimmed transparent image when the source permits safe edge-background removal.
- Fit it inside the active format's master footprint: 360 × 150 px for landscape or 500 × 230 px for square.
- Preserve aspect ratio and transparency.
- If the transparent logo lacks contrast, add only the smallest mature source- or brand-colored gradient/tint needed for legibility. If it reads directly, keep `Title Support` hidden.

Construct the combined preview after the two main covers pass visual QA. Clone the completed covers: keep the landscape at 900 × 383, scale the square clone to 383 × 383, and separate them with a 24 px white gap.

On the ordinary single-image route, capture the upload response’s `imageHash`, then use one atomic `use_figma` call to validate the master, compute the next clear canvas position, duplicate the master, assign independently cropped background fills to both formats, update text/size/line height, configure adaptive title support, set logo shadows, rebuild the combined preview, capture its QA screenshot, and return all affected node IDs. Do not make a separate read-only Figma preflight or split actions into multiple calls unless this atomic call fails because the master is missing, invalid, or inaccessible.

## Validate and export

By default, visually inspect the final combined preview using the screenshot returned by the main mutation call. Do not make a separate screenshot or metadata call when that preview is sufficient. Inspect an individual landscape or square frame only when the combined preview reveals or suggests cropping, masking, contrast, readability, logo, or safe-margin risk that cannot be judged reliably at the reduced size.

Check:

- exact frame dimensions;
- important subject matter remains visible;
- the adapted image preserves the original style, palette, lighting, materials, typography, and object geometry;
- center content is geometrically centered;
- each format uses its specified master content scale;
- the square title or company logo remains clearly readable after the square is reduced to 383 × 383 in the combined preview;
- no keyword overflow or unintended wrapping;
- no logo distortion or transparent-padding shrinkage;
- no company-logo matte, residual edge color, rectangular haze, white/gray fringe, or halo on light, dark, and saturated local backgrounds;
- company logos remain crisp at 100% and are not raster-upscaled beyond their native dimensions; official matching vectors are used when available;
- brand logo position, contrast, and safe margins;
- the 海外独角兽 logo remains crisp at 100% in 1× output and at 100% in any requested 2× output; no thumbnail source, repeated rasterization, interpolation softness, or compression artifact is present;
- combined preview order and spacing.
- deliberate visual hierarchy, balance, rhythm, and premium finish;
- no element appears mechanically squeezed into a corner;
- landscape visual mass is not parked entirely on one side; meaningful artwork crosses the center axis or has a genuine source-derived counterweight.
- source elements remain crisp at their displayed size.
- subject and center-content scale feels confident rather than surrounded by uncontrolled empty space;
- no large neutral region dominates the frame without a deliberate compositional purpose;
- no cutout halo, foreign fragment, polygon edge, or background mismatch is visible at 100%.
- any title support is demonstrably necessary, source-coordinated, and no larger or heavier than needed;
- no pure-white support card or habitual white gradient appears;
- text or a company logo that reads directly has no backing;
- any required backing uses a restrained source- or brand-coordinated tint/gradient and feels integrated rather than pasted on;
- no unnecessary title support obscures useful artwork or makes the cover feel templated.
- the final tone is mature, premium, and editorial rather than childish, toy-like, cute, gaudy, or over-effected.
- two-line titles do not feel vertically compressed, tightly tracked, or crowded against their support boundary.
- every line of a two-line title remains individually prominent and readable at both native size and 383 px preview size; the second line may not be materially weaker than the first.
- title letterforms do not cross rapidly changing light/dark regions, multiple saturated colors, dense edges, or embedded source text.
- adaptation preserves the source's semantic continuity; no continuous illustration, sequence, diagram, directional flow, or object group has been split into disconnected fragments merely to create a title gap.

Fix issues before exporting.

For an ordinary source, allow at most one targeted Figma correction call after the combined-preview QA. If a second correction appears necessary, reassess whether proportional scaling, crop focus, source-color extension, or simpler title support can solve the problem before adding more layers or calls.

Export PNGs with these names:

- `<slug>-wechat-landscape-900x383.png`
- `<slug>-wechat-square-900x900.png`
- `<slug>-wechat-combined-1307x383.png`

Request and download the three 1× exports in parallel.

Export 2× high-resolution masters only when the user requests high-resolution/final delivery, the asset will be repurposed beyond normal WeChat display, or 1× inspection reveals a genuine raster-quality risk:

- `<slug>-wechat-landscape-1800x766@2x.png`
- `<slug>-wechat-square-1800x1800@2x.png`
- `<slug>-wechat-combined-2614x766@2x.png`

Return:

1. links or paths to all exported PNGs;
2. the fixed Figma workspace URL;
3. direct `node-id` links to all three output frames;
4. the font actually used;
5. a brief note if fallback font, blurred extension, or any other adaptive treatment was used.

Do not claim an export or Figma link exists until the corresponding tool call succeeds.

Do not run Skill validation, sync the desktop copy, commit, or push GitHub during ordinary cover production. Perform those maintenance actions only when the Skill files themselves changed.
