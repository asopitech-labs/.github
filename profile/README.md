<p align="center">
  <a href="https://asopi.tech/labo">
    <img src="https://avatars.githubusercontent.com/u/247176946?s=200" alt="Asopitech Labo" width="120">
  </a>
</p>

<h1 align="center">Asopitech Labo 🧪</h1>

<p align="center">
  <b>まず作って確かめる R&D ラボ。</b><br>
  手応えを得た実験だけが OSS プロジェクトと製品構想へ進みます。
</p>

<p align="center">
  <b>An R&D lab that prototypes first and validates second.</b><br>
  Only the experiments that hold up graduate into OSS projects and product concepts.
</p>

<p align="center">
  <a href="https://asopi.tech/labo">ラボ紹介 / About</a> &bull;
  <a href="#いま動いているもの--in-development">In development</a> &bull;
  <a href="#公開済みの構想--published-concepts">Concepts</a> &bull;
  <a href="https://zenn.dev/asopitech">Zenn</a> &bull;
  <a href="https://github.com/sponsors/asopitech">Sponsor</a>
</p>

<p align="center">
  <a href="https://asopi.tech"><img alt="Website" src="https://img.shields.io/badge/web-asopi.tech-E87EB4"></a>
  <a href="https://zenn.dev/asopitech"><img alt="Zenn" src="https://img.shields.io/badge/Zenn-技術記事-3EA8FF?logo=zenn&logoColor=white"></a>
  <a href="https://x.com/asopitech_iot"><img alt="X" src="https://img.shields.io/badge/X-@asopitech__iot-000000?logo=x&logoColor=white"></a>
  <a href="https://github.com/sponsors/asopitech"><img alt="Sponsor" src="https://img.shields.io/badge/sponsor-%E2%9D%A4-db61a2"></a>
</p>

---

## はじめに見るなら / Start here

| | |
|:--|:--|
| **動くものを触りたい** | [Nimino](https://github.com/asopitech-labs/nimino)（Nim製デスクトップ基盤）、[NAVISOMA](https://github.com/asopitech-labs/navisoma-nim-container-toolchain)（コンテナツールチェーン）、[Global Executables](https://github.com/asopitech-labs/global-executables)（MCP公開データセット） |
| **設計を読みたい** | [LAMINARIA](https://github.com/asopitech-labs/laminaria-rust-nim-toolchain)、[GUDGEON](https://asopitech-labs.github.io/gudgeon-nif-execution-platform/)、[Theatora](https://asopitech-labs.github.io/theatora/)、[Rhyzora](https://asopitech-labs.github.io/rhyzora/) |
| **実験ノートを覗きたい** | [asmati-lab](https://github.com/asopitech-labs/asmati-lab) |
| **ラボの外の本体** | [Alopex DB](https://github.com/alopex-db)（データベース）、[jv-lang](https://github.com/project-jvlang)（言語） |

## いま動いているもの / In development

実装が進行中のプロジェクト。バッジは最終コミット日を自動表示します。/
Implementation under way; the badge shows the real last-commit date.

| Project | 概要 / Summary | |
| --- | --- | --- |
| [**Nimino**](https://github.com/asopitech-labs/nimino) | Nim 製の軽量クロスプラットフォーム WebView デスクトップアプリ基盤<br>A lightweight cross-platform WebView desktop framework in Nim | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/nimino?label=) |
| [**Nimculus**](https://github.com/asopitech-labs/nimculus) | NimNUI + Metal の GPU ネイティブコードエディタ<br>A GPU-native code editor built with Nim and NimNUI | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/nimculus?label=) |
| [**NAVISOMA**](https://github.com/asopitech-labs/navisoma-nim-container-toolchain) | Nim製のクロスプラットフォームコンテナツールチェーン。containerd・WSL Containers 等のランタイム上に Compose と OCI のセマンティクスをネイティブ実装<br>Cross-platform container toolchain in Nim, with native Compose and OCI implementations | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/navisoma-nim-container-toolchain?label=) |
| [**Global Executables**](https://github.com/asopitech-labs/global-executables) | パッケージエコシステム横断で実行ファイル名を収集し、MCP 経由で AI エージェントに公開する公開データセット<br>A public cross-ecosystem dataset of executable names, exposed to AI agents via MCP | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/global-executables?label=) |
| [**Buzz**](https://github.com/asopitech-labs/buzz-nim) | 人と AI エージェントが同じ部屋で共同作業する、自分で運用できるセルフホスト型ワークスペース<br>A self-hostable workspace where humans and AI agents share the same rooms | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/buzz-nim?label=) |
| [**Noetide**](https://github.com/asopitech-labs/noetide-research-planning-engine) | 計画を研究課題に、検証結果を意思決定に変える継続的リサーチ・プランニングエンジン<br>A continuous research and planning engine turning plans into questions and evidence into decisions | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/noetide-research-planning-engine?label=) |

## 公開済みの構想 / Published concepts

設計と考え方を先に公開しているもの。コードが固まる前なので、議論でまだ変えられます。/
Design published before the code freezes — comments can still change these.

| Project | 概要 / Summary | |
| --- | --- | --- |
| [**LAMINARIA**](https://github.com/asopitech-labs/laminaria-rust-nim-toolchain) | Rust と Nim をひとつの計算グラフとして扱う統合ツールチェーン。依存解決・コンパイラパイプライン・バックエンド選択・成果物生成・リンク・キャッシュ・実行を、説明可能な単一のアクショングラフへ分解する<br>A unified toolchain modeling Rust and Nim as one explainable action graph | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/laminaria-rust-nim-toolchain?label=) |
| [**GUDGEON**](https://github.com/asopitech-labs/gudgeon-nif-execution-platform) | NIF プログラムの実行基盤。同じプログラムモデルを、インタプリタ実行・事前ネイティブコンパイル・デバッガ検査・計装のすべてで扱う<br>One program model, interpreted, compiled ahead of time, inspected, and instrumented（[Website](https://asopitech-labs.github.io/gudgeon-nif-execution-platform/)） | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/gudgeon-nif-execution-platform?label=) |
| [**Theatora**](https://github.com/asopitech-labs/theatora) | アプリケーションコードを変えずに、プロバイダー・ランタイム・構成を組み替えられるコンポーザブルなバックエンド構築キット<br>A composable backend kit for swapping providers, runtimes, and topology without rewriting the app（[Website](https://asopitech-labs.github.io/theatora/)） | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/theatora?label=) |
| [**Rhyzora**](https://github.com/asopitech-labs/rhyzora) | 宣言的なアプリケーションとエンジン契約から、CLI・TUI・Web・デスクトップ・MCP インターフェースを構築する Nim フレームワーク<br>A Nim framework building CLI, TUI, web, desktop, and MCP interfaces from declarative contracts（[Website](https://asopitech-labs.github.io/rhyzora/)） | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/rhyzora?label=) |
| [**Poiera**](https://github.com/asopitech-labs/poiera) | AI エージェントに承認済みの実行経路・限定権限・明確な成功条件を与え、変更から配備・検証までを制御するコントロールプレーン<br>A control plane giving AI agents an approved path, limited authority, and explicit success criteria（[Website](https://asopitech-labs.github.io/poiera/)） | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/poiera?label=) |
| [**Setup State Delivery**](https://github.com/asopitech-labs/setup-state-delivery) | 設定ファイル・環境変数・ツールプロファイル・AI エージェント設定を、マシン・プロジェクト・CI・コンテナへ一貫して配送する<br>Keeps working setups consistent across machines, projects, CI, and containers（[Website](https://asopitech-labs.github.io/setup-state-delivery/)） | ![last commit](https://img.shields.io/github/last-commit/asopitech-labs/setup-state-delivery?label=) |
| [**TUBUSA/備 (Contexum)**](https://asopitech-labs.github.io/tubusa-contexum-pages/) | 人材・案件・作業・売上・資金をひとつながりの仕事として扱う業務アプリケーション構想<br>A business-app concept connecting people, projects, work, revenue, and cash（[English](https://asopitech-labs.github.io/tubusa-contexum-pages/en/)） | — |

## 実験ノート / Research notebook

[**asmati-lab**](https://github.com/asopitech-labs/asmati-lab) — アスマティ・辰巳の公開実験ノート。
言語・コンパイラ・FFI・ツールチェーンの検証を、Issue と最小の実験コードとして残しています。/
A public notebook where experiments on languages, compilers, FFI, and toolchains stay as issues and minimal code.

## ラボの外のプロジェクト / Beyond the lab

ラボで手応えを得たものは、専用の Organization へ移って育ちます。/
What holds up moves to its own organization and grows there.

| Organization | 概要 / Summary |
|:--|:--|
| [**alopex-db**](https://github.com/alopex-db) | Alopex DB・Skulk・Chirps — Rust のデータベースエコシステム / The Rust database ecosystem |
| [**project-jvlang**](https://github.com/project-jvlang) | jv-lang の言語仕様・コンパイラ・ドキュメント / Language spec, compiler, and docs for jv-lang |

## Links

- 🌐 ラボ紹介 / About the lab: <https://asopi.tech/labo>
- 📚 Nim Architecture Guide: <https://asopitech.github.io/nim/>
- 📝 Zenn（技術記事 / tech articles in Japanese）: <https://zenn.dev/asopitech>
- 🐦 X: <https://x.com/asopitech_iot>
- 👤 開発者 / The developer: [@asopitech](https://github.com/asopitech)

## Support

開発を応援していただける方はこちらから。上位ティアでは、公開前の設計メモや試作を先に見られます。/
If you'd like to support the work. Higher tiers follow the experiments before they are public.

| Tier | 内容 / What you get |
|:--|:--|
| **$3 / month** | OSS Support — 継続的な開発・更新・リリースを支える / Back ongoing development, updates, and releases |
| **$12 / month** | Early Access — 実験・設計ドラフト・内部メモ・試作を公開前に / Experiments, design drafts, internal notes, and prototypes before they are public |
| **$99 / month** | Enterprise-focused Early Access — セキュリティと配備に向けた先行機能 / Pre-release capabilities aimed at security and deployment |

<p align="center">
  <a href="https://github.com/sponsors/asopitech?metadata_source=asopitech_labs_profile&metadata_campaign=sponsor_early_access&metadata_content=org_profile_sponsor_section"><img alt="Sponsor @asopitech on GitHub Sponsors" src="https://img.shields.io/badge/GitHub%20Sponsors-%E2%9D%A4%20Sponsor%20%40asopitech-db61a2?logo=githubsponsors&logoColor=white&style=for-the-badge"></a>
  <a href="https://buymeacoffee.com/asopitechia"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%E2%98%95-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black"></a>
</p>
