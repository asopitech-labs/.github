# Alopex DB video keyframes

Generated with the built-in image generation tool, one image per call. PNGs are the untouched native outputs: no code drawing, resizing, cropping, compositing or transparency. Seventeen calls total (thirteen initial frames and four retries). These are reviewable candidates, **not an approved cut-ready set**. Flagged files should be regenerated before assembly.

Both reference images were passed in every call, in this order:

1. `assets/characters/alopex/explore-cute/fox-10-portrait.png` — face and glossy rendering.
2. `assets/characters/alopex/explore-cute/fox-11-summit.png` — compact full body and enormous tail.

Every prompt was the exact unchanged prefix below, extracted from the first recorded prompt in `assets/characters/alopex/cute/README.md` under “Exact prompts and per-image assessments”, followed by its scene paragraph. The character, palette, style, facial refinement and shared production constraints were never rewritten. Scene-specific weather and aurora were explicitly requested as scenery exceptions to the prefix's plain-background instruction.

## Locked prefix used verbatim in every call

```text
Use case: logo-brand.
Asset type: one polished Alopex DB mascot illustration, flat vector style.
Character identity, invariant across scenes: the SAME cute chibi ARCTIC FOX, roughly two heads tall, large head, small round body, short stubby legs. Large round dark navy eyes set LOW and WIDE with bright white catchlights and a very faint upward OUTER tilt. A slightly LONGER FINER tapered muzzle bridge projecting forward to a SMALL NEAT dark nose; a fox's delicate pointed snout, not a kitten's flat button face or a Samoyed puppy's broad blunt muzzle. Keep it cute. Small rounded wide-based ears set LOWER and FURTHER APART, with pale ice-blue insides, never pink or tall narrow triangles. Fluffy swept cheek ruff, tiny cool blush. ENORMOUS extremely fluffy long plume tail, as big as the head and body combined, never a dog's short curled tail.
Palette: snow-white #F8FAFC, frost shadows #B8D4E3, ice blue #5FB4C9, aurora #7EC8E3, deep navy outlines #1E3A5F, night background #0B1929.
Style: preserve the reference's appealing curving silhouette and clean confident outlines, flat vector-style illustration with simple flat cel shadows, no heavy texture, no 3D, no photorealism, no watercolor, no gradient mesh. Simple navy background with minimal snow as appropriate. Silent, Adaptive, Unbreakable: calm ordinary comfort, never heroic posing or suffering.
No text, lettering, numerals, wordmarks, logos, or watermark anywhere. One coherent standalone composition, no contact sheet or collage.
A cute young ARCTIC FOX face: a broad fluffy forehead that TAPERS DOWN to a NARROW V-SHAPED lower face and a delicate elongated wedge snout. Make the muzzle noticeably longer and finer than the reference, with a narrow raised muzzle bridge and a tiny neat black nose at its tip. A single subtle closed mouth line below the nose, NOT a split double-curled cat/dog mouth. Small rounded wide-based ice-blue ears low on the sides, large round dark eyes low and wide with faint outer tilt and bright catchlights. Snow white, cool blue shadows, fluffy swept cheek ruff.
Shared production constraints: match the canonical fox-10-portrait glossy cute finish exactly, with its large glossy dark-blue eyes, bright catchlights, thick fluffy ruff, cool soft cel shading and clean dark outline. Use fox-11-summit only as the compact full-body reference. TWO HEADS TALL, tiny round body and SHORT STUBBY LEGS; tail as big as HEAD AND BODY TOGETHER. No long adult body, long legs or undersized tail. BACKGROUND IN EVERY IMAGE: opaque SOLID FLAT NIGHT NAVY #0B1929, no white canvas, no transparency, no vignette, no sky gradients, no stars or confetti. Minimal foreground snow allowed only when required by the scene; keep the navy background around it. No text or lettering. Preserve same animal, fur pattern, ears, eyes, muzzle and palette; vary only expression, pose, camera or scene as requested below.

Input images: image 1 is the canonical FACE and glossy rendering; image 2, when supplied, is the canonical compact full body and tail. Copy the identity faithfully, not the old pose.
```

## Inspection notes

Sizes below are read from the saved PNG headers, width × height. Native output is near 16:9 / 9:16, not mathematically exact. Assessment uses the strict continuity requirement: a recognizable face alone does not excuse a reduced tail. Empty-space percentages are visual estimates, not layout guarantees. Navy areas have slight rendered tonal shading, rather than perfectly uniform hexadecimal fills. No text, numbers, logos or UI were observed in the saved images. K5 has five storage layers despite a four-layer scene request; the storyboard only requires a stack, and the layer count should be considered if matching V3. All images are opaque.

## k1-blizzard.png

- Status: **REGENERATED IN PLACE — 2026-10-22 user-directed revision**.
- Exact size: **1672 × 941 pixels**.
- Storm / comfort assessment: The storm now clearly reads as a blizzard: dense diagonal snow covers the whole frame, grey-blue visibility is reduced, and ground spindrift crosses the foreground; the small fox remains visibly calm with open eyes despite windblown fur and snow dusting.
- Composition: Fox including tail occupies about a quarter of the width at lower-right. Left third contains no fox or strong object, but remains snowy and textured rather than empty; use a caption plate for legibility.
- Review scope: the user accepted the other ten frames after direct inspection; their files and README entries are unchanged. Earlier general regeneration recommendations elsewhere in this document are historical and superseded by that review.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest. EXTREME LONG SHOT: weather fills nearly the entire view; a TINY fox is seated in the distance at lower-right. Whole fox INCLUDING enormous tail occupies ONLY 25% of frame width, a small silhouette within x=64%-89%, y=66%-89%. Camera very far away; do not zoom onto the fox or enlarge its head. SAME reference animal and proportions uniformly scaled small. A REAL VIOLENT WHITEOUT BLIZZARD ACROSS THE WHOLE FRAME: scene-specific override of plain-navy backdrop rule, cold GREY-BLUE STORM SKY, dense wind-driven fine snow diagonally streaming upper-left to lower-right EVERYWHERE including visibly IN FRONT OF the small fox. Spindrift lifts off ground and sweeps sideways across the entire foreground, wind whips fur and enormous tail sideways, slightly flattens ears, snow dusts head and shoulders. Fox eyes fully open, face serene and comfortable, ordinary relaxed seat, no distress, shivering, squinting or heroism. Foreground is broad open stormy snowfield extending to the DISTANT small fox, not a close portrait. LEFT THIRD lower-contrast storm haze and evenly distributed fine diagonal snow, no fox, hard shapes, large foreground flakes or snow clumps, usable for caption plate while still visibly stormy. No clear navy or sheltered air around subject. No text, lettering, numerals, logos, slabs or UI. Opaque entire image.
```

## k2-calm.png

- Status: **FLAG — REGENERATE**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: DRIFT: face and glossy finish closely match; the plume is shorter/smaller relative to head and body than the full-body reference.
- Empty space: PARTIAL: far-right navy (roughly last third) is clear, but the tail occupies part of the requested right half and the snow contains blue facets.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. Calm snowfield under soft cool light. Seat the fox at left third, full body about 43% of frame height, full enormous tail spread beside it and contained inside margins. Quiet ordinary comfortable three-quarter front pose. Reserve RIGHT 50% as absolutely plain unmarked white snow below a single low horizon and absolutely plain solid navy above: no snow facets, tracks, flakes, objects or stray shapes. No slabs. All scenery minimal, opaque navy wherever there is no snow.
```

## k3-wind.png

- Status: **FLAG — REGENERATE**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: DRIFT: recognizable matching face and compact seated body, but plume is smaller relative to head and body than reference 2.
- Empty space: PARTIAL: upper-left navy is clear; left snow is faceted, and the enlarged fox encroaches on the planned caption width. Grey weather is localized on the right.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. Same comfortable seated pose on snow at right third, fox full body about 43% of frame height, full enormous tail visible. Wind rising, cheek ruff and tail tips streaming rightward while posture stays relaxed. Scenery exception: a flat cool grey storm sky occupies the upper-right subject area, bounded by solid night navy elsewhere. A few wind streaks confined to right half, no dense blizzard yet. LEFT 45% stays genuinely clean plain navy sky and unmarked plain snow for a caption, no streaks, facets or stray marks. No slabs.
```

## k4-aurora.png

- Status: **FLAG — REGENERATE**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: DRIFT: matching glossy eyes, rounded blue ears and tapered frontal face; tail is shorter/smaller relative to head and body than the canonical full-body reference.
- Empty space: PARTIAL: upper-left navy is clear; snow/ice below has blue facets, and the fox is larger than planned. Green aurora stays on the right.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. Comfortable seated fox at right third on a broad simple icy plain at polar night, full body about 43% of height and full enormous tail inside margins. Scenery exception: restrained GREEN aurora ribbon high in upper-right sky, above the fox, set against otherwise solid night navy. Same relaxed ordinary bearing as in calm and blizzard. LEFT 45% is absolutely plain navy sky and unmarked ice, no aurora, reflections, stars, flakes, facets or stray shapes in caption region. No slabs.
```

## k5-slabs.png

- Status: **KEEP**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: MATCH: glossy canonical face, compact body and enormous hanging plume are convincing; no material identity drift seen.
- Empty space: CLEAN on far-right about 44%: no discrete objects or lettering there; the snow base reaches slightly past center, so do not assume the entire right 52% is clear.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. Fox sits comfortably on FOUR stacked thick HORIZONTAL RECTANGULAR STORAGE LAYERS at left third, the structure and fox contained within LEFT 45% and generous margins. Stack looks like reference 2 but slab faces are entirely blank smooth ice-blue, NO indicator squares, lights, controls, lettering, numbers or UI. Clearly separate flat parallel horizontal slabs, never gems or crystal. Huge tail hangs beside stack, at least head-and-body size. RIGHT 52% and upper-right are genuinely empty solid flat night navy for a code panel, no snow, objects or stray shapes. Tiny plain snow base only directly beneath stack.
```

## k6-skulk.png

- Status: **FLAG — REGENERATE**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: DRIFT: distant animals have progressively smaller tails and less consistent fine muzzles; not uniform scaled copies of the reference. Original retained because retry weakened the receding arrangement.
- Empty space: CLEAN in upper approximately 26% navy; the snowfield is faceted rather than plain. Largest foreground silhouette comes close to left edge.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. FIVE copies of exactly the reference fox seated comfortably at evenly spaced intervals receding diagonally across a broad simple snowfield, from foreground lower-left to distant upper-right. Each is the SAME full-body model uniformly scaled in perspective; for EVERY fox including the smallest, the entire enormous plume tail is at least as large as its HEAD AND BODY TOGETHER, with delicate fine projecting wedge muzzle clearly preserved. Space foxes apart without overlap. Large heads and tiny bodies even at distance. Plain navy sky across top 30% stays perfectly blank for captions, no flakes, stars or objects. Simple plain snow, no slabs, scenery, mountains or extra decorative shapes.
```

## k7-chirps.png

- Status: **REGENERATED IN PLACE — 2026-10-22 user-directed revision**.
- Exact size: **1672 × 941 pixels**.
- Storm / comfort assessment: Storm is not applicable to this calm calling scene; both foxes look comfortable and relaxed, with glossy open eyes and softly open mouths.
- Composition: Both foxes and complete tails are inside the frame; bright subject/snow bounds are x=312–1359 on the 1672-pixel canvas, leaving about 18.7% navy margin on each side, comfortably above 8%. Three small call arcs occupy the clear gap between their heads.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest. VERY WIDE DISTANT SHOT with TWO SMALL seated reference foxes in the middle of a huge plain navy canvas. THE WHOLE GROUP INCLUDING BOTH ENORMOUS TAILS occupies ONLY THE MIDDLE 60% WIDTH, from x=20% to x=80%; outermost 20% LEFT and 20% RIGHT must contain absolutely NOTHING except plain night navy. This is mandatory crop safety for a slow push-in. Left complete animal including whole huge tail inside x=20%-43%, right complete animal including whole huge tail inside x=57%-80%; paws y=78%, ears y=48%. Do not enlarge either animal. Preserve canonical proportions uniformly scaled SMALL, with enormous plume as big as head and body together for EACH fox. Both fully contained tails sweep outward into reserved group space, never toward frame edges. Two foxes face each other across a clear gap with three small simple ice-blue call arcs between heads. Fine muzzle, glossy open eyes, relaxed comfortable faces, tiny gently open mouths. Tiny plain snow patches directly under paws must also stay INSIDE central 60%. Top and bottom generously empty navy, no other scenery. No lettering, text, numerals, logos, bubbles or UI; opaque background. Think a small pair seen at a distance, surrounded by ample unused navy.
```

## k8-walking.png

- Status: **FLAG — REGENERATE**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: DRIFT: glossy face remains recognizable, but walking body is longer and the tail is smaller relative to head and body than reference 2.
- Empty space: NOT CLEAN to requested extent: fox ears rise to about 20% height, leaving only the upper fifth fully clear rather than a large empty sky for the terminal. Prints are multi-toed paw shapes, not simple round impressions.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. Fox walking calmly LEFT TO RIGHT across a long snowfield in lower 40%, at x=70%, full enormous tail and short legs inside frame. Side three-quarter view shows fine muzzle and glossy eye. A simple trail of ROUND paw prints leads from lower-left toward the fox. Upper 55% is genuinely completely EMPTY solid flat night navy for an install terminal overlay: no stars, flakes, horizon details, objects or stray marks. Snowfield low and plain, no slabs, no heroic pose.
```

## k9-portrait.png

- Status: **FLAG — REGENERATE**
- Exact size: **1672 × 941 pixels**.
- Same fox as references: DRIFT: face and glossy finish are close, but upright tail is substantially smaller than head and body combined.
- Empty space: PARTIAL: side navy is clear, but fox paws/tail extend to about 89% height, leaving only around 11% clear below rather than the requested 22% lockup band.

Scene paragraph used for saved image:

```text
Pose/scene: WIDE LANDSCAPE 16:9, widest native output 1672x941 or nearest, never square. Quiet centered portrait pose, fox looks gently toward viewer, chest and full face visible, compact seated body and enormous tail alongside. Subject occupies central 36% of canvas width and middle 58% of height, completely within margins. Opaque solid flat night navy ground everywhere, NO scenery, snow, stars, gradients or stray shapes. Reserve entire bottom 22% and outer left/right 25% as genuinely empty navy for future lockup. Same calm glossy character as reference 1, no slabs, no text.
```

## v1-blizzard.png

- Status: **REGENERATED IN PLACE — 2026-10-22 user-directed revision**.
- Exact size: **941 × 1672 pixels**.
- Storm / comfort assessment: The storm now clearly reads as a blizzard across the entire tall frame, with diagonal snowfall, grey-blue sky and foreground spindrift; the snow-dusted fox sits low with open eyes and a relaxed, comfortable face.
- Composition: Upper third contains only storm sky and snow, with no fox or distinct object; some larger soft flakes remain, so it is not uniformly quiet and a caption plate will help. Ear flattening and sideways fur streaming are subtler than in K1.

Scene paragraph used for saved image:

```text
Pose/scene: TALL PORTRAIT 9:16, tallest native output 941x1672 or nearest. A REAL VIOLENT WHITEOUT BLIZZARD ACROSS THE WHOLE FRAME, weather is the bigger subject. This scene explicitly overrides the shared plain-navy backdrop rule: cold GREY-BLUE STORM SKY everywhere, dense diagonal wind-driven snow across every region, absolutely NO clear navy sky or sheltered clear air around the fox. Strong wind direction upper-left to lower-right, fine streaking snow crosses IN FRONT OF fox as well as behind, drifting snow lifts from ground and trails across foreground in long low sheets. Place the same comfortable seated fox LOW and SMALL, whole silhouette INCLUDING enormous tail confined to x=25%-75%, y=72%-94%, with enormous plume streaming sideways, ear tips slightly flattened by wind, snow dusting head and shoulders. Eyes fully OPEN and serene, comfortable relaxed face, no shivering, squinting, distress or heroic pose. Keep fine muzzle and glossy blue eyes readable through snow. UPPER THIRD is low-contrast grey-blue storm haze with fine evenly distributed diagonal snow, NO fox, strong cloud shapes, huge streak clumps or objects; quiet enough for a caption plate but still visibly stormy. No slabs, text, lettering, numbers, logos or UI. Opaque entire image.
```

## v2-aurora.png

- Status: **FLAG — REGENERATE**
- Exact size: **940 × 1672 pixels**.
- Same fox as references: DRIFT: glossy face remains close, but tail is smaller than head and body and fox occupies much more than the intended bottom 28%.
- Empty space: PARTIAL: upper half intentionally contains aurora; clear navy band exists around 46–55% height, narrower and higher than the requested 53–68% band.

Scene paragraph used for saved image:

```text
Pose/scene: TALL PORTRAIT 9:16, tallest native output about 941x1672 or nearest, never square or landscape. Polar night on a simple icy plain; comfortable seated fox SMALL below at x=50%, confined to bottom 28%, full enormous tail inside margins. Scenery exception: broad GREEN aurora ribbons fill UPPER HALF against opaque navy, no stars. Leave a genuinely clean plain navy band between 53% and 68% height for caption placement, no aurora, reflections or stray shapes in that band. Bottom plain ice is minimal and unmarked. No slabs.
```

## v3-slabs.png

- Status: **FLAG — REGENERATE**
- Exact size: **941 × 1672 pixels**.
- Same fox as references: MATCH: small compact storage pose, glossy eyes and large hanging tail preserve identity well; four clearly horizontal blank storage slabs read as a structure.
- Empty space: NOT CLEAN to storyboard requirement: retry gives about 54% clear navy above, but ears start around 54% height; upper two-thirds is not empty and the whole subject is not within lower third.

Scene paragraph used for saved image:

```text
Pose/scene: TALL PORTRAIT 9:16, tallest native output 941x1672 or nearest. EXTREME DISTANT PRODUCT SHOT WITH VERY LARGE NEGATIVE SPACE. UPPER 70% OF IMAGE IS ONLY SOLID FLAT NIGHT NAVY, without even one object, fur tuft, shape or mark. The ENTIRE fox AND FOUR stacked HORIZONTAL rectangular storage layers AND enormous tail must fit within a SMALL bounding rectangle x=15%-85%, y=72%-95%. Do not zoom in; keep subject small. Top of fox ears must begin BELOW y=72%, not at center of image. Fox sits comfortably on four separate flat horizontal blank ice-blue slabs, rectangular storage structure like reference 2 with all indicator lights removed. Entire enormous hanging tail visible and at least head-and-body size. No UI, text, numerals, gems, crystal, snow scattering or decorative shapes. Tiny plain snow base at y=95% only.
```

## v4-walking.png

- Status: **FLAG — REGENERATE**
- Exact size: **941 × 1672 pixels**.
- Same fox as references: DRIFT: fine wedge profile and dominant plume are good, but rear torso/neck reads taller and less compact than reference 2.
- Empty space: PARTIAL: top approximately 34% is clear navy, not the requested upper 55%; ears enter the install-caption reserve. Paw trail reaches the bottom region, but prints are multi-toed rather than simple round impressions.

Scene paragraph used for saved image:

```text
Pose/scene: TALL PORTRAIT 9:16, tallest native output about 941x1672 or nearest, never square or landscape. Fox walks calmly toward right in rear-three-quarter view in lower-middle at x=53%, y=70%; fine muzzle and one glossy eye visible in profile, enormous tail full and inside margins, tiny short legs. A narrow plain snowy path in bottom 40%, with ROUND paw prints trailing diagonally down from fox to BOTTOM EDGE. UPPER 55% genuinely absolutely empty solid flat night navy for install captions, no stars, flakes, objects, texture or stray shapes. No slabs or other scenery.
```

## Retry selection

K1, K7 and V3 use their second generated candidates. K6 retains its first candidate: the retry reduced tail size again and did not preserve the receding scale sequence. No rejected image was substituted silently or edited with code. Rejected generated originals remain in the image tool's default output location, outside this delivery folder.

## Regeneration priorities

1. V3: restore truly empty upper two-thirds; essential for code overlay.
2. K6 and K7: correct tail ratios and muzzle/body continuity at all scales.
3. K1 and K2–K4: smaller consistent character framing, larger tails, and plain caption snow where requested.
4. K8, K9, V1, V2 and V4: restore overlay reserves and compact character proportions.

K5 is the strongest candidate. Its usable clear code area begins around 56% of canvas width; review that placement against the actual code panel before assembly.

