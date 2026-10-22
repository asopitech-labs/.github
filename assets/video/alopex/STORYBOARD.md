# Alopex DB — commercial and short videos

Concept: **"Survives in every scene."** One fox, unchanged in bearing, placed in conditions that
escalate. The environment changes; the animal does not. That is the product claim — one engine,
from a single embedded file to a cluster — told as weather.

Register: the **glossy cute character** (media surfaces: video, social, asopi.tech). Reference
images: `../../characters/alopex/cute/face-neutral.png`, `family-alopex.png`.

## Claims policy

Only what ships today (Alopex DB v0.8.16). No graph, no Enterprise, no distributed-parity claims.
Everything on screen that is text or code is real: the SQL is the hybrid-search example from the
README, the install lines are the published ones.

| On screen | Source |
|:--|:--|
| "SQL + Vector + Columnar" | README, "What it does today" |
| "Skulk: time series. Chirps: messaging." | the two projects' own descriptions. Chirps is independent of Alopex DB, so the video does not say they share a foundation. |
| the hybrid-search query | README, "Hello, hybrid search", abridged to the category filter and wrapped at `AS score` so it can be set large |
| `cargo add alopex-embedded alopex-sql` / `pip install alopex` | README, Install |
| "From an embedded file to a distributed cluster." | the project tagline |
| "Silent. Adaptive. Unbreakable." | the project tagline |

## Commercial — 30 s, 16:9, 1920×1080, 30 fps

| t | Beat | Picture | Caption (EN / JA) |
|:--|:--|:--|:--|
| 0–4 s | Storm | K1 — the fox sits calm in a blizzard, small in frame | Every scene has its storm. / どんな現場にも、嵐はある。 |
| 4–9 s | The engine | K5 — the fox on a stack of storage slabs | One database engine. / ひとつのデータベースエンジン。 |
| 9–15 s | Escalation | K2 → K3 → K1 → K4 — the same fox, four conditions, quick dissolves | From an embedded file / to a distributed cluster. / 組み込みの1ファイルから、分散クラスタまで。 |
| 15–21 s | One query | K5 with a code panel: the real hybrid-search SQL | SQL. Vector search. Columnar. / One engine. / SQL、ベクトル検索、列指向。ひとつのエンジンで。 |
| 21–25 s | The family | K6 skulk, K7 chirps | Skulk: time series. Chirps: messaging. / Skulk：時系列。Chirps：メッセージング。 |
| 25–27.6 s | Install | terminal card over K8 | `cargo add alopex-embedded alopex-sql` / `pip install alopex` |
| 27.6–30 s | Close | K9 portrait, then dissolve to a plain navy ground with the lockup | Silent. Adaptive. Unbreakable. · alopex-db.github.io · a small GitHub Sponsors line |

## Shorts — 9:16, 1080×1920, 30 fps, no voice-over (captions carry it)

| # | Length | Hook (first second) | Beats |
|:--|:--|:--|:--|
| S1 | 15 s | "Survives in every scene." | V1 blizzard → V2 aurora → V3 slabs → lockup |
| S2 | 18 s | "One query. SQL and vectors." | V3 fox on slabs, code panel builds line by line, result |
| S3 | 12 s | "Two lines." | V4 fox walking, the two install lines type in, lockup |

## Keyframes to generate (wide = 16:9, tall = 9:16)

| id | Format | Scene |
|:--|:--|:--|
| K1 | wide | fox sitting calm in a blizzard, wind streaming, small in the frame, empty snow on the left |
| K2 | wide | the same fox on a calm snowfield, soft light, space on the right |
| K3 | wide | the same fox with wind rising, fur streaming, grey sky |
| K4 | wide | the same fox on an icy plain at night under a green aurora |
| K5 | wide | the fox sitting on a stack of layered storage slabs, empty space on the right for a code panel |
| K6 | wide | several of the same fox spread across a snowfield at even intervals, receding |
| K7 | wide | two of the same fox facing each other across a gap, the call drawn as a few simple arcs |
| K8 | wide | the fox walking left to right across a long snowfield leaving round paw prints, empty sky above |
| K9 | wide | the fox in a quiet portrait pose, centred, deep navy ground, space for a lockup |
| V1 | tall | blizzard, the fox low in the frame, empty storm above for a caption |
| V2 | tall | polar night with aurora filling the upper half, the fox small below |
| V3 | tall | the fox on a stack of slabs in the lower third, empty upper two-thirds for code |
| V4 | tall | the fox walking, paw prints trailing down to the bottom edge, empty top |

No text or lettering in any generated image: every caption, line of code and lockup is composed later.

## Sound

Music: D minor to D major, lifting at the end card (27.6 s in the commercial). Effects, in the order they
are heard: wind under the storm, a whoosh on each cut, a tick per caption, a keystroke per typed
character, a chime when the query or the command is done, a bell chord on the logo. Both languages share
one soundtrack. Full notes in `README.md`.

