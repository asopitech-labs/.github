# Glossy cute Alopex DB character variations

Sixteen illustrations generated with the built-in `image_gen` tool for README art, the product site, videos, social and stickers. The owner selected this glossy register for the character role; the calm figures and the separate plated mark remain untouched.

## Canonical reference and prompt consistency

- Face and glossy rendering: [fox-10-portrait.png](../explore/generated/fox-10-portrait.png).
- Compact full-body proportions, enormous tail and product pose: [fox-11-summit.png](../explore/generated/fox-11-summit.png).
- Recorded source prompt: the **final correction** under `fox-10-portrait.png` in [the original generated README](../explore/generated/README.md).

Every prompt below starts with the same locked block: the source prompt's character, palette and style paragraphs are copied **word for word**. The character-description sentences from its composition paragraph are also copied verbatim and repeated unchanged. The old instruction calling its earlier input too puppy-like was omitted because it referred to a rejected predecessor, not the approved canonical image. A shared production-constraints paragraph explicitly asks for the approved glossy finish, two-head proportions, short limbs, full-size plume and navy background. Only the expression/pose/scene clause varies. Walking received one additional direction-correction clause after an initial left-facing result.

The five expressions use the canonical portrait; expressions after neutral also receive the generated neutral as a framing reference. All full-body/family/hero calls use the canonical portrait first and the glossy summit second. No calm reference image was supplied to any call.

## Background and files

**Opaque navy background for every image**, requested as solid flat night `#0B1929`, with `transparent_background: false` on every call. There are no transparent or white-canvas variants mixed into the set. White snow is foreground scenery only where needed. The earlier transparent generation produced ragged edges, so this set deliberately uses navy throughout.

The tool retained slight tonal variation in the navy: these unchanged RGB outputs are visually in the same navy register, but they are not pixel-exact flat `#0B1929` fields. Sampled upper-left colors range approximately from `(10,28,48)` to `(13,34,57)`. Do not assume seamless color matching to a CSS background without subsequent cleanup. This is a remaining background-spec limitation, not a hidden alternate background treatment.

Fifteen square PNGs are **1254 × 1254**. `hero-banner.png` is **1672 × 941**, the tool's native wide output, very close to but not mathematically exact 16:9. No crop, resize, compositing or programmatic drawing was applied to the deliverable artwork; generated files were copied unchanged. Pillow was used only for read-only dimension/mode/pixel inspection.

## Consistency review

**Flagged drift:** `pose-carrying.png` has a slightly broader/shorter-looking muzzle against the slab; `family-skulk.png` reduces tail-to-body ratios, especially in the distance; `family-dataui.png` has a rounder/blunter muzzle. These are candidates requiring character refinement before strict simultaneous use. None reverts to the long-legged calm body, but preserving chibi proportions alone does not make every face an exact match.

The remaining images show no material character drift in visual comparison, subject to pose occlusion and normal generated variation. Fur tufts, highlights and feature placement are not pixel-identical. The expression images share the same framing target and canvas dimensions but are **not pixel-registered animation frames**; curious intentionally tilts the head.

The first walking attempt faced left. It was regenerated with the same character/style block plus a direction-only correction; only the saved right-facing version is a deliverable. Carrying also faces left in its saved image, a scene-direction deviation from its prompt that does not change the user's carrying composition request.

## Three for the README

1. **[hero-banner.png](hero-banner.png)** — top-of-page product identity, storage context and empty left side for a separately rendered title.
2. **[pose-presenting.png](pose-presenting.png)** — an architecture/feature figure with the fox indicating structured storage.
3. **[pose-sleeping.png](pose-sleeping.png)** — a quieter supporting illustration expressing comfortable resilience without repeating the storage perch.

`family-alopex.png` is the strongest square alternative when a banner is unsuitable.

## Exact prompts and per-image assessments

### face-neutral.png

[View image](face-neutral.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait.

Assessment: MATCH — closely preserves fox-10-portrait's tapered muzzle, wide glossy eyes, rounded blue ears, cheek ruff and tail-shoulder framing; no material character drift.

Exact prompt:

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
Pose/scene: SQUARE 1:1, SAME HEAD-AND-SHOULDERS FRAMING as fox-10-portrait: face fills most of frame, fixed head scale, fixed camera, head centered, ears fully inside margin, fluffy chest cropped at lower edge, giant tail hinted behind viewer-right shoulder, no props or snow. Change expression only: calm neutral gaze straight at viewer, glossy eyes open, tiny relaxed closed mouth.
```

### face-happy.png

[View image](face-happy.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then generated `face-neutral.png`.

Assessment: MATCH — same head silhouette, muzzle and fur treatment with contented closed eye curves; no material character drift, but tiny generated placement differences remain.

Exact prompt:

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
Pose/scene: SQUARE 1:1, SAME HEAD-AND-SHOULDERS FRAMING as fox-10-portrait: face fills most of frame, fixed head scale, fixed camera, head centered, ears fully inside margin, fluffy chest cropped at lower edge, giant tail hinted behind viewer-right shoulder, no props or snow. Change expression only: both eyes CLOSED in soft upward contented curves, small happy smile, no catchlights in closed eyes. Friendly contentment, no big grin.
```

### face-sleepy.png

[View image](face-sleepy.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then generated `face-neutral.png`.

Assessment: MATCH — same canonical face with glossy half-closed eyes; no material character drift, although the expression can read mildly knowing as well as sleepy.

Exact prompt:

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
Pose/scene: SQUARE 1:1, SAME HEAD-AND-SHOULDERS FRAMING as fox-10-portrait: face fills most of frame, fixed head scale, fixed camera, head centered, ears fully inside margin, fluffy chest cropped at lower edge, giant tail hinted behind viewer-right shoulder, no props or snow. Change expression only: eyes HALF CLOSED with gently drooping eyelids, glossy dark-blue eye slivers and catchlights still visible, about to doze, relaxed mouth, not sad.
```

### face-curious.png

[View image](face-curious.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then generated `face-neutral.png`.

Assessment: MATCH — the tilted head preserves canonical eyes, muzzle, ear shapes and ruff; no material identity drift, but the intentional rotation changes the outer bounds.

Exact prompt:

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
Pose/scene: SQUARE 1:1, SAME HEAD-AND-SHOULDERS FRAMING as fox-10-portrait: face fills most of frame, fixed head scale, fixed camera, head centered, ears fully inside margin, fluffy chest cropped at lower edge, giant tail hinted behind viewer-right shoulder, no props or snow. Change expression only: head tilted slightly to one side, ears directed forward, open glossy eyes alert and curious. Keep head center and scale unchanged as far as tilt allows.
```

### face-surprised.png

[View image](face-surprised.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then generated `face-neutral.png`.

Assessment: MATCH — canonical face remains recognizable with wider eyes, raised ears and a small open mouth; no material character drift; the small pink mouth interior is an incidental generated accent.

Exact prompt:

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
Pose/scene: SQUARE 1:1, SAME HEAD-AND-SHOULDERS FRAMING as fox-10-portrait: face fills most of frame, fixed head scale, fixed camera, head centered, ears fully inside margin, fluffy chest cropped at lower edge, giant tail hinted behind viewer-right shoulder, no props or snow. Change expression only: eyes WIDE OPEN with glossy highlights, small rounded ears raised in alert surprise, tiny slightly open mouth. Cute mild surprise, not fear or distress.
```

### pose-sitting.png

[View image](pose-sitting.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH — compact two-head chibi proportions, short paws and large curled tail preserve the character in three-quarter view; no material identity drift.

Exact prompt:

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
Pose/scene: SQUARE 1:1, full-body three-quarter view, fox sits upright, ENORMOUS tail curled around its feet. All paws and whole tail visible in clean margins. Head large, body tiny and round, SHORT STUBBY LEGS, strictly TWO HEADS TALL. Calm open glossy eyes. No props or ground patch.
```

### pose-walking.png

[View image](pose-walking.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH after direction retry — right-facing profile keeps a large glossy eye, fine snout, very short legs, compact torso and enormous tail; no material character drift, though tail lifts higher than requested.

Exact prompt:

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
Pose/scene: SQUARE 1:1, full-body SIDE PROFILE walking LEFT TO RIGHT with gentle gait, one front paw raised. Fine muzzle profile, ONE large glossy eye, tiny compact round torso and very short stubby legs, TWO HEADS TALL. ENORMOUS plume tail carried low behind, volume at least head plus body combined. Do not lengthen legs or torso to suggest walking; pose the same short-legged chibi body. Entire fox inside margins, no props or paw prints.
Pose correction: the nose MUST point toward the RIGHT edge of the image and the enormous tail MUST be on the LEFT. This is a right-facing profile walking to the right. Keep short chibi proportions. Nose on viewer-right, tail on viewer-left. Do not face left.
```

Rejected first walking attempt: same two canonical image inputs, same opaque-navy setting; it faced left. Exact first prompt:

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
Pose/scene: SQUARE 1:1, full-body SIDE PROFILE walking LEFT TO RIGHT with gentle gait, one front paw raised. Fine muzzle profile, ONE large glossy eye, tiny compact round torso and very short stubby legs, TWO HEADS TALL. ENORMOUS plume tail carried low behind, volume at least head plus body combined. Do not lengthen legs or torso to suggest walking; pose the same short-legged chibi body. Entire fox inside margins, no props or paw prints.
```

### pose-presenting.png

[View image](pose-presenting.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH — canonical face and compact seated body remain, with a clear indicating paw and structured slab stack; no material identity drift, though some paw placement reads as resting against the slab edge.

Exact prompt:

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
Pose/scene: SQUARE 1:1, full-body fox sits BESIDE a stack of four horizontal storage slabs, ONE FRONT PAW RAISED TOWARD the stack as if indicating it. Other forepaw grounded, huge tail curls comfortably beside feet. Strict two-head proportions and tiny short limbs. Storage is visibly parallel thick rectangular horizontal layers with navy gaps and rows of small glowing ice-blue square indicators, never jewel or crystal. Full fox and stack inside margins.
```

### pose-carrying.png

[View image](pose-carrying.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: DRIFT (minor muzzle shape) — the head looks a little broader and flatter where it meets the slab than fox-10-portrait; short legs and enormous tail are retained, but the saved pose faces left rather than the prompt's rightward direction and the slab has a visible seam.

Exact prompt:

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
Pose/scene: SQUARE 1:1, full-body fox carries ONE SINGLE GLOWING DATA SLAB carefully IN ITS MOUTH while walking gently left to right in side-three-quarter view. Slab is a wide thin horizontal rectangle with parallel edges, flat layered form and tiny regular square indicators; not a gem/crystal. Muzzle gently grips upper edge; face still visible. Keep strict TWO-HEAD-TALL compact torso, SHORT STUBBY legs and enormous tail as large as head/body together. No adult long-legged anatomy. Whole fox and slab inside margins.
```

### pose-sleeping.png

[View image](pose-sleeping.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH within sleeping-pose limits — ruff, ears and oversized tail remain consistent with the canonical fox; eyes are closed and muzzle is mostly hidden, so full facial equivalence cannot be judged; nose rests at the tail edge rather than being fully buried.

Exact prompt:

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
Pose/scene: SQUARE 1:1, fox curled ASLEEP in natural arctic-fox posture, ENORMOUS fluffy tail DRAPED OVER ITS OWN NOSE. Gentle closed eye curves, fine muzzle tucked under tail, small blue ears visible. Tiny round body inside the tail curl, minimal small snow bed. Deeply comfortable and cute, not a cat loaf. Clean navy margins.
```

### family-alopex.png

[View image](family-alopex.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH — very close continuity with fox-10-portrait's face and fox-11-summit's compact storage pose, four slab layers and hanging plume; no material character drift.

Exact prompt:

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
Pose/scene: SQUARE 1:1, fox sits ON TOP OF FOUR LAYERED STORAGE SLABS with huge plume tail hanging down the side almost to base. Match fox-11-summit compact product pose: head large, torso tiny, short paws, strict TWO HEADS TALL, tail as large as head/body combined. Four parallel thick rectangular data layers, distinct navy gaps, rows of glowing blue square data indicators. Minimal snow base, full fox and stack within clean margins.
```

### family-skulk.png

[View image](family-skulk.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: DRIFT (tail ratio) — faces and compact chibi bodies remain recognizably related, but the tails are too small relative to head/body, especially on the more distant copies; the regular receding arrangement works.

Exact prompt:

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
Pose/scene: SQUARE 1:1, FIVE copies of the EXACT SAME short-legged TWO-HEAD-TALL CHIBI FOX across a simple snowfield at EVEN INTERVALS receding diagonally into distance. Near fox bottom-left, others at regular positions in perspective toward upper-right. SAME HEAD/BODY/TAIL RATIOS on all five, only uniformly scaled; each tail at least as big as its head/body together. All comfortably seated or standing, never long-legged or smaller-tailed distant variants. Small bounded snowfield island with plain navy around it, no trees/mountains or sky decoration.
```

### family-chirps.png

[View image](family-chirps.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH — both profiles share the glossy eyes, fine snouts, short limbs, blue ears and large plumes; call arcs and the gap read clearly; no material character drift, though the outer tails are close to the frame edges.

Exact prompt:

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
Pose/scene: SQUARE 1:1, TWO copies of EXACT SAME FOX in facing side profiles across a clear gap, softly CALLING. Three simple ice-blue curved call ARCS in gap between muzzles, no bubbles or lettering. Tiny open mouths, glossy eyes, small rounded ears, huge tails sweep outward. Both strictly TWO HEADS TALL with tiny compact round body and short stubby legs. Full tails inside generous margins, minimal snow patch.
```

### family-trail.png

[View image](family-trail.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH — rear-three-quarter profile retains compact proportions and a dominant oversized tail, with a readable print trail; no material identity drift; prints are stylized paw shapes rather than plain circular dots.

Exact prompt:

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
Pose/scene: SQUARE 1:1, fox viewed FROM BEHIND walking AWAY toward upper-center, rear-three-quarter angle allows small fine muzzle and one glossy eye in profile. CLEAN LINE OF ROUND PAW PRINTS leads from fox back toward viewer at bottom foreground on narrow simple snowy path. Keep same compact TWO-HEAD-TALL character, enormous plume tail dominating rear silhouette, SHORT STUBBY rear legs, no long neck or adult slender body. No trees/mountains, navy around snowy path.
```

### family-dataui.png

[View image](family-dataui.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: DRIFT (muzzle shape) — proportions remain compact and the tail stays large, but the visible muzzle is rounder/blunter and slightly more puppy-like than fox-10-portrait; terrain overview works, with less of the terrain visible than the scene ideally calls for.

Exact prompt:

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
Pose/scene: SQUARE 1:1, SAME CHIBI FOX on a small foreground ridge, rear-three-quarter or side view, LOOKING OUT OVER THE WHOLE SNOWFIELD. Terrain ahead visible as a few clean broad frost/white snow planes, bounded low snowfield with navy above. Fox at lower-right foreground, enormous plume tail, large head and tiny round body, strictly TWO HEADS TALL with SHORT STUBBY legs. Do not make an adult naturalistic fox or heroic scenic pose. Calm observing gaze. No trees, mountains, aurora or stars. Terrain reads as overview, fox remains the canonical cute animal.
```

### hero-banner.png

[View image](hero-banner.png)

Background argument: `transparent_background: false` (navy requested).

Reference image arguments: canonical glossy fox-10-portrait, then canonical glossy fox-11-summit.

Assessment: MATCH — glossy canonical face and compact storage pose carry into the wide scene, with a large hanging tail and generous empty left side; no material character drift; native output is near, not mathematically exact, 16:9.

Exact prompt:

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
Pose/scene: WIDE LANDSCAPE 16:9 BANNER, NOT SQUARE. Fox with FOUR HORIZONTAL STORAGE SLABS, compact seated product pose ON or BESIDE stack at RIGHT THIRD. ENORMOUS fluffy tail, large glossy-eyed head, tiny round body, SHORT STUBBY legs, strict TWO HEADS TALL. Full stack reads as separate thick rectangular layers with regular glowing blue data-block indicators, never crystal. LEFT HALF and upper-left are GENEROUS EMPTY SOLID NAVY for future title placement. NO TEXT NOW. No stars, confetti, background gradients, large snowfield or distracting extra objects. Small snow base under right-side subject only. Leave whole fox/tail/stack inside margins. Actual wide 16:9 composition essential.
```

