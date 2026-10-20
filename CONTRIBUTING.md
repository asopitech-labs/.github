# Contributing to Asopitech Labo

ラボのプロジェクトへの関心をありがとうございます。このファイルは organization の
既定です。各リポジトリに固有の `CONTRIBUTING.md` があれば、そちらが優先されます。/
Thanks for your interest. This file is the organization default; a repository's own
`CONTRIBUTING.md` wins if it has one.

## まずプロジェクトの段階を確認してください / Check the stage first

ラボは「まず作って確かめる」場所なので、リポジトリごとに成熟度がまったく違います。
[org プロフィール](https://github.com/asopitech-labs) の区分を見てから動くと空振りしません。/
This is a lab: maturity differs sharply per repository. Check the sections on the
[org profile](https://github.com/asopitech-labs) before you start.

| 段階 / Stage | 歓迎される関わり方 / What helps most |
|:--|:--|
| **いま動いているもの** (Nimino, Nimculus, NAVISOMA, Global Executables, Buzz, Noetide) | バグ報告、再現手順、小さな修正 PR / Bug reports, reproductions, small fixes |
| **公開済みの構想** (LAMINARIA, GUDGEON, Theatora, Rhyzora, Poiera, Setup State Delivery, TUBUSA) | 設計への異論、ユースケースの持ち込み。**コードより先に Issue** / Argue with the design, bring a use case — issues before code |
| **実験ノート** (asmati-lab) | Issue での議論と最小再現コード / Discussion and minimal reproductions in issues |

構想段階のリポジトリは API も境界もまだ動きます。大きな実装 PR をいきなり送ると、
設計変更で丸ごと無駄になることがあります。先に Issue をください。/
Concept-stage repositories can still change shape. A large unsolicited
implementation PR can be invalidated by a design change — open an issue first.

## Pull request

- 1 PR = 1 関心事 / one concern per pull request
- 命令形の件名（`fix(parser): reject duplicate keys`）/ imperative subject lines
- 何を・なぜ変えたか、どう確認したかを書く。実行したコマンドも添えてください /
  say what changed, why, and how you verified it, with the commands you ran
- 振る舞いが変わるなら、テストを足してください / behavior changes need tests

言語ごとの基本（各リポジトリの指示が優先）/ Language defaults, unless a repository says otherwise:

```bash
# Rust
cargo fmt --all && cargo clippy --all-targets -- -D warnings && cargo test

# Nim
nimble test
```

## バグ報告 / Reporting bugs

対象リポジトリの Issues へ、バージョン（またはコミット）、OS とアーキテクチャ、
再現手順、期待した結果と実際の結果を添えてください。どのリポジトリか判断できない
場合は、どこでも構いません。こちらで移します。/
File in the repository's Issues with the version or commit, OS and architecture,
reproduction steps, and expected versus actual behavior. Not sure which repository?
File anywhere in the org and it will be moved.

セキュリティ上の問題は Issue ではなく [SECURITY.md](./SECURITY.md) の手順で。/
Security problems go through [SECURITY.md](./SECURITY.md), not Issues.

## ライセンス / Licensing

各リポジトリの `LICENSE` に従います。ライセンスファイルが見当たらない場合は、
コントリビュート前に Issue で確認してください。/
Each repository's own `LICENSE` applies. If a repository has none, ask in an issue
before contributing.

## コード以外の貢献 / Other ways to help

正確なバグ報告、ドキュメントの改善、スターも助かります。開発そのものを支えたい方は
[GitHub Sponsors](https://github.com/sponsors/asopitech) からどうぞ。/
Precise bug reports, documentation, and stars all help. To fund the work directly,
see [GitHub Sponsors](https://github.com/sponsors/asopitech).
