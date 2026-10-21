# asopitech / Asopitech Labo brand assets

このディレクトリの画像は生成物です。PNG を直接編集しないでください。/
Everything here is generated. Do not hand-edit a PNG.

```bash
python3 scripts/render_brand_book.py    # design-book.png と manifest.json を描く
python3 scripts/export_brand_assets.py  # そこから配布用アセットを切り出す
```

## マーク本体は生成物ではありません / The marks themselves are not generated

`source/` にある2つのアバターが**正本**です。デザインブックはこれを合成しているだけで、
描き直していません。マークを変えるときは `source/` を差し替えてから再生成してください。/
The two avatars in `source/` are the originals. The design book composites them; it does
not redraw them. To change a mark, replace the file in `source/` and regenerate.

| File | What it is |
|:--|:--|
| `source/avatar-asopitech-512.png` | 個人アカウントのマーク（ピンクのクラッカー、黒地） |
| `source/avatar-asopitech-labs-512.png` | ラボのマーク（ピンクの A、白地） |

## どれをどこで使うか / Which file to use where

| 用途 / Use | File |
|:--|:--|
| 個人プロフィール README のヒーロー（ダーク） | `lockup-asopitech-dark-800.png` |
| 個人プロフィール README のヒーロー（ライト） | `lockup-asopitech-light-800.png` |
| ラボ org プロフィールのヒーロー（ダーク / ライト） | `lockup-labo-dark-800.png` / `lockup-labo-light-800.png` |
| リポジトリの Social preview（1280×640） | `social-asopitech-1280.png` / `social-labo-1280.png` |
| 横長バナー（README 上部、スライド見出し） | `banner-asopitech-1280.png` / `banner-labo-1280.png` |
| 入稿用の原寸（2560px 系） | 同名の `-1280` なしファイル |

Social preview は GitHub の Settings → Social preview から手動アップロードです（API なし）。/
Social previews are uploaded by hand in Settings → Social preview; there is no API.

## 色 / Palette

| Token | Hex |
|:--|:--|
| pink | `#E57FC1` |
| pale pink | `#E7C0DD` |
| deep pink | `#C9569F` |
| maroon field | `#4A1F26` → `#7A2E35` |
| near-black | `#0B0B0F` |
| white | `#FFFFFF` |

## 既知の制約 / Known limitation

個人マークの「あそびテック」の文字は、元画像の時点で黒地に暗色で描かれており、
左右も切れています。カードサイズに拡大すると判読できません。デザインブックは元画像を
忠実に扱うため、この性質もそのまま残ります。直すならマーク自体（`source/`）の更新が必要です。/
In the personal mark, the あそびテック lettering is drawn in a dark color on black and is
clipped at both edges in the original image, so it is unreadable at card scale. The design
book reproduces the mark faithfully, so this carries through. Fixing it means updating the
mark in `source/`.
