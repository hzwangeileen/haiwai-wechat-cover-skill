# Design principles

Use these principles to choose a composition from the source rather than forcing a preset template.

## 1. Read the source

Identify:

- primary and secondary subjects;
- whether subjects are separable;
- embedded text or logos that must remain exact;
- the original palette, lighting, materials, shadows, texture, and image-making style;
- natural empty space and directional movement;
- resolution limits.

Do not treat a composite source image as one indivisible rectangle when its elements can be recomposed cleanly. Do not treat every separable subject as a mandatory transparent cutout.

## 2. Establish hierarchy

The reading order is:

1. central keyword or company logo;
2. source subject or subjects;
3. 海外独角兽 brand logo.

Keep the center content easy to read without making the source decorative or insignificant.

Do not assume centered content needs a background. First use the image's natural negative space and local contrast. A backing plate, gradient, blur, veil, or local tonal weakening is an adaptive compositional tool, not a template requirement.

Treat a company logo as transparent by preference, not by force. Remove a uniform edge background only when the result preserves every internal white region, counter, stroke, shadow, and brand color. Test the transparent logo directly on the composition; add no backing when it reads clearly. When support is necessary, use a restrained non-white tint or source-/brand-colored gradient rather than a pure-white card.

## 3. Choose a strategy

Use the least destructive strategy that creates a balanced cover:

Apply a minimum-necessary-recomposition rule before the routing matrix: preserve the source's overall relationships first. Try proportional scaling, position adjustment, small cropping, native-background extension, or moving one or two key elements before separating multiple elements. If movement is sufficient, do not split. If the overall composition can be retained, do not rebuild it. Multi-element separation is a last resort, not a demonstration of capability.

Treat ordinary aspect-ratio adaptation as a lightweight path. A mismatched canvas is not evidence that the source needs separation. Estimate complexity before production: if a plan needs more than two source uploads or more than two Figma layout rounds, reassess crop, focal position, native-background extension, proportional contain, or local weakening first.

For landscape composition, reject single-side parking: do not place the entire meaningful image group only in the left or right outer third and leave the opposite side empty. A centered title does not by itself balance a one-sided subject block. Preserve balance by letting the overall source cross the center axis, distributing source content through upper and lower zones, or retaining a real source-derived counterweight. Use asymmetry only when the visual weights still read as intentionally balanced.

### Routing matrix

Classify the source before entering Figma:

1. **Direct proportional crop** — Use only when each crop retains at least roughly 60% of the meaningful composition and preserves all priority elements. Reject it when important content spans both the top and bottom and cannot survive together. When accepted, upload the original once, reuse one Figma `imageHash`, and apply independent `CROP` transforms/focal positions.
2. **Source-derived canvas extension** — Use when cropping would remove important content and the edge background is white, solid, or a simple gradient. Extend that background, then proportionally resize and reposition the intact subject.
3. **Light key-element movement** — Use when moving one or two elements creates a stable title zone while the source's overall relationships remain recognizable.
4. **Multi-element recomposition** — Use only when the lighter strategies still cannot preserve the subject, title readability, and compositional balance together. Separate the minimum number of elements, preserve their proportions, and retain the original visual relationships wherever possible.
5. **Image edit or generative extension** — Use only when a photograph, complex texture, or spatial scene needs content that does not exist in the source. Extend in the same image-making style before adding titles and brand elements in Figma.

Do not interpret an aspect-ratio change as permission to stretch the image. Limited non-uniform widening is acceptable only for pure texture or gradient background regions with no deformation-sensitive content. Never deform a person, product, logo, word, chart, screenshot, illustration, or geometric object.

### Native crop

Use when the source already has a strong focal point and the crop preserves all important information.

### Source-backed crop

Use when a subject can be reframed while keeping its original white, red, or other visually compatible background. A good source background is part of the composition and should not be removed merely to create transparency.

Prefer a rectangular source-backed crop when:

- its background can merge naturally into the canvas;
- it avoids fragile edge extraction;
- the crop can be scaled confidently without exposing unrelated subjects;
- embedded shadows and fine edge detail should remain untouched.

On a simple continuous background, unrelated fragments may be covered with the sampled edge color before cropping. Do not use this treatment on textured, photographic, patterned, or spatially varying backgrounds.

### Extended canvas

Use when there is one cohesive subject that should remain intact. Extend with source-derived solid color, gradient, texture, or restrained blur. Do not invent a new style.

### Element recomposition

Use when two or more subjects can be separated. Extract them from the source, keep each proportional, and rebuild their relationships around the central content.

Do not automatically use left/right symmetry. Consider:

- opposing diagonals;
- large/small counterbalance;
- foreground/background depth;
- asymmetric editorial composition;
- controlled overlap that does not harm legibility.

When the source background is white, solid, or otherwise simple and compatible, prefer rectangular source-backed regions for recomposition. Keep original object edges, shadows, texture, and embedded typography intact; let the native background merge into an extended canvas instead of forcing fragile masks.

### Restrained cleanup

Allow small corrections to spacing, edge blending, tonal balance, or background continuity. Do not redraw logos, text, products, faces, charts, screenshots, or material details.

## 4. Premium-quality test

Reject a composition when:

- the full source is simply reduced into a corner;
- the landscape's meaningful source content is confined to one side without a real source-derived counterweight;
- the layout contains more passive empty space than the hierarchy needs;
- one side feels visually empty without intentional counterbalance;
- subjects and text compete at the same visual weight;
- spacing looks accidental;
- crop edges, masks, or background seams are visible;
- a separated element still contains fragments of another subject;
- a mask halo or polygon boundary is visible at normal size or 100%;
- the result looks like a template rather than a response to the source;
- a source element is enlarged beyond useful detail.
- the treatment feels childish, toy-like, overly cute, gaudy, immature, or generically “AI designed”;
- a pure-white logo/title card or habitual white gradient sits on top of the artwork;
- gradients, rounded corners, outlines, glow, or shadows are decorative rather than necessary.

Prefer:

- clear focal hierarchy;
- confident scale;
- deliberate negative space;
- optical rather than merely mathematical centering;
- consistent light and shadow;
- restrained color;
- crisp edges and typography.
- a mature editorial tone, restrained effects, sophisticated color relationships, and materials that feel intentional.

When title or company-logo support is necessary, it should feel derived from the source rather than pasted on top of it. Match the source's geometry, palette, edge language, and degree of softness. Use the least area and opacity that reliably solves the reading problem. Remove it whenever the text or transparent logo is already clear.

Negative space must support focus, tension, or reading order. It is not automatically premium. As a practical review heuristic, enlarge or reframe the subjects when a neutral empty region dominates roughly one third of the frame without serving a clear compositional role. This is a quality check, not a fixed template rule.

## 5. Resolution

- Keep source elements at or below their native pixel density whenever possible.
- Use vector text and vector-capable logos in Figma.
- Export the three required frames at both 1× and 2×.
- Inspect the 2× files at 100% for mask halos, interpolation softness, and text clarity.
- If a source is too small, redesign with a smaller displayed subject rather than fabricating detail.
