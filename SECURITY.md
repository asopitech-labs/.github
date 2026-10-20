# Security Policy

## 対象バージョン / Supported versions

Asopitech Labo のプロジェクトは大半が 1.0 未満で、活発に変化しています。
セキュリティ修正は各プロジェクトの**最新のリリースまたは `main`** に対して行います。
長期サポートブランチはありません。/
Most lab projects are pre-1.0 and move quickly. Security fixes land on the latest
release, or on `main` where a project has no releases yet. There are no long-term
support branches.

## 報告方法 / Reporting a vulnerability

**公開 Issue には書かないでください。/ Please do not open a public issue.**

対象リポジトリの GitHub Security Advisory
（`Security` タブ → `Report a vulnerability`）から非公開で報告してください。
利用できない場合は <https://asopi.tech/contact> から「セキュリティ報告」と明記して
連絡してください。その最初の連絡には攻撃手順を書かないでください。/
Report privately through the repository's GitHub security advisory form
(`Security` tab → `Report a vulnerability`). If that is unavailable, contact
<https://asopi.tech/contact> and say it is a security report — do not include
exploit details in that first message.

可能な範囲で次を含めてください / Please include what you can:

- 対象プロジェクトとバージョン（またはコミット）/ project and version or commit
- 実行環境（OS・アーキテクチャ・ランタイム）/ environment
- 攻撃者が何をできるのか / what an attacker can achieve
- 再現手順、または再現可能な最小の説明 / a reproduction, or the smallest description that lets us reproduce it

## 対応の流れ / What to expect

- 数営業日以内の受領連絡 / acknowledgement within a few business days
- 脆弱性と判断するかどうか、修正方針とリリース経路の共有 / our assessment, planned fix, and release path
- 希望がなければ、アドバイザリで報告者としてクレジット / credit in the advisory unless you prefer otherwise

公開前に修正をリリースする時間をいただけると助かります。/
Please give us a reasonable window to publish a fix before disclosing publicly.

## 対象外 / Out of scope

- **構想段階のリポジトリ**（org プロフィールで「公開済みの構想」に分類されるもの）は、
  設計文書と試作であり、本番利用を想定していません。/ Concept-stage repositories are
  design documents and prototypes, not production software.
- 実験ノート [asmati-lab](https://github.com/asopitech-labs/asmati-lab) の
  実験コード / the experiment code in asmati-lab
- 1.0 未満であることに起因する API・フォーマットの非互換変更 / pre-1.0 API and format
  changes, which are documented limitations rather than vulnerabilities

[Alopex DB](https://github.com/alopex-db) と [jv-lang](https://github.com/project-jvlang)
は別 organization です。それぞれの SECURITY ポリシーに従ってください。/
Alopex DB and jv-lang are separate organizations with their own policies.
