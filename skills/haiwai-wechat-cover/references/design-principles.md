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

## 3. Choose a strategy

Use the least destructive strategy that creates a balanced cover:

### Routing matrix

Classify the source before entering Figma:

1. **Direct proportional crop** — Use only when each crop retains at least roughly 60% of the meaningful composition and preserves all priority elements. Reject it when important content spans both the top and bottom and cannot survive together. When accepted, upload the original once, reuse one Figma `imageHash`, and apply independent `CROP` transforms/focal positions.
2. **Source-derived canvas extension** — Use when cropping would remove important content and the edge background is white, solid, or a simple gradient. Extend that background, then proportionally resize and reposition the intact subject.
3. **Element recomposition** — Use when multiple meaningful elements need new relationships. Separate only what is needed, preserve every element’s proportions, and recompose on an extended canvas or in Figma.
4. **Image edit or generative extension** — Use only when a photograph, complex texture, or spatial scene needs content that does not exist in the source. Extend in the same image-making style before adding titles and brand elements in Figma.

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
- the layout contains more passive empty space than the hierarchy needs;
- one side feels visually empty without intentional counterbalance;
- subjects and text compete at the same visual weight;
- spacing looks accidental;
- crop edges, masks, or background seams are visible;
- a separated element still contains fragments of another subject;
- a mask halo or polygon boundary is visible at normal size or 100%;
- the result looks like a template rather than a response to the source;
- a source element is enlarged beyond useful detail.

Prefer:

- clear focal hierarchy;
- confident scale;
- deliberate negative space;
- optical rather than merely mathematical centering;
- consistent light and shadow;
- restrained color;
- crisp edges and typography.

When title support is necessary, it should feel derived from the source rather than pasted on top of it. Match the source's geometry, palette, edge language, and degree of softness. Use the least area and opacity that reliably solves the reading problem. Remove it when direct text is already clear.

Negative space must support focus, tension, or reading order. It is not automatically premium. As a practical review heuristic, enlarge or reframe the subjects when a neutral empty region dominates roughly one third of the frame without serving a clear compositional role. This is a quality check, not a fixed template rule.

## 5. Resolution

- Keep source elements at or below their native pixel density whenever possible.
- Use vector text and vector-capable logos in Figma.
- Export the three required frames at both 1× and 2×.
- Inspect the 2× files at 100% for mask halos, interpolation softness, and text clarity.
- If a source is too small, redesign with a smaller displayed subject rather than fabricating detail.
