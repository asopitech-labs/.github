# Alopex キャラクター（メディア圏）

ここに置いてあるのは、**asopi.tech・動画・SNS・ステッカー・ノベルティ向け**の
Alopex キャラクターです。光沢のある可愛いトーンで統一しています。/
The Alopex character in its **glossy, cute register**, for asopi.tech, video, social media,
stickers, and merchandise.

## 使い分け / Which register goes where

同じ1匹のホッキョクギツネを、場に合わせてトーンで出し分けています。/
One arctic fox, two registers, chosen by surface.

| 面 / Surface | 使うもの / What to use | 置き場 / Where it lives |
|:--|:--|:--|
| **GitHub**（リポジトリ、組織プロフィール、ドキュメントサイト） | **マーク**＋**落ち着いたトーンのキャラクター** | [alopex-db.github.io](https://github.com/alopex-db/alopex-db.github.io/tree/main/docs/assets/images/brand) と同リポジトリの `assets/brand/character/` |
| **asopi.tech・動画・SNS・ステッカー** | **光沢トーンのキャラクター**（このディレクトリ） | ここ |

GitHub 面に光沢版を出さないでください。技術文書の中では浮きます。逆に、SNS や動画で
落ち着いた版を使うと目を引きません。/ Do not put the glossy register on GitHub surfaces, and do
not use the calm register where the point is to catch an eye.

## 中身 / Contents

| ファイル群 | 内容 |
|:--|:--|
| `cute/face-*.png` | 表情5種（neutral / happy / sleepy / curious / surprised）。画角が揃っているので差し替え可能 |
| `cute/pose-*.png` | ポーズ5種（座る / 歩く / 指し示す / データを運ぶ / 眠る） |
| `cute/family-*.png` | ファミリー5種（Alopex / Skulk / Chirps / Trail / Data UI） |
| `cute/hero-banner.png` | 16:9 のヒーローバナー。片側に余白を取ってあるので、後からタイトルを置けます |
| `explore-cute/` | 採用に至るまでの検討16枚（記録） |

基準は `cute/face-neutral.png`（検討段階の `explore-cute/fox-10-portrait.png` 由来）です。
新しい絵を足すときは、この顔に合わせてください。/ The reference face is `cute/face-neutral.png`.

## 由来 / Provenance

ファミリーの意味づけは、名前が既に持っているものをそのまま使っています。/
The family meanings are not invented; the names already carry them.

- **skulk** — 英語でキツネの群れを指す集合名詞。だから時系列DBは「地形に散って継続的に観測する群れ」
- **chirps** — ホッキョクギツネが実際に交わす短い鳴き声。だからメッシュは「距離を越えて群れをつなぐ呼び交わし」
- **trail** — 雪に残る足跡。だからログは「通過した痕跡、後から読める記録」

画像は生成物です。再生成や追加は、同じ基準画像のプロンプトから character 節と style 節を
そのまま流用し、ポーズ節だけ差し替えてください（毎回キャラクターを記述し直すと別個体になります）。/
These are generated images; reuse the reference prompt's character and style clauses verbatim
and vary only the pose clause.
