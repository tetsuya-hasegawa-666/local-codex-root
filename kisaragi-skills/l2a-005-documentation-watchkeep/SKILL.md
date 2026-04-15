---
name: l2a-005-documentation-watchkeep
description: 会話起点の文書影響を検知し、新しい判断、前提、範囲変更、統治更新、実装方針変更、重要な暫定規則を project 文書へ同期する。docs drift だけでなく、文書 topology、version 整合、encoding 健全性、shared 文体 rule に対する表現整合も同じ turn で扱う。
---

# Documentation Watchkeeper

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` と `l1-001-skill-plan` が、文書同期または docs drift close が必要と判断した時だけ呼ばれる。

## 吸収した観点

- `l2a-005-documentation-watchkeep` の docs drift 検知
- `document-topology-keeper` の authoritative / pointer 整理
- `doc-governor` の version / archive 整合
- `encoding-integrity-keeper` の UTF-8 preflight と mojibake 防止
- `writing-normalizer` 相当の文体整合確認

作業中の documentation drift を防ぐために使う。

## 中核規則
会話によって project truth が変わったら、その turn のうちに文書更新が必要かを確認する。
可読性が壊れている文書を、そのまま真実として扱わない。

## 呼び出し対象となる典型条件
次のいずれかが起きた時に、通常は distributor / planner からこの skill が呼ばれる。
- 新しい policy、rule、approval gate が決まった
- 実装範囲や進め方が変わった
- 新しい branch、release、deployment rule が導入された
- 新しい report、process file、evidence file が workflow に入った
- 文書で支えていた assumption が、より良い decision に置き換わった
- code 変更により既存文書が不完全または誤解を招く状態になった
- shared な文体 rule、表現 rule、用語 rule が更新された

## Workflow
1. 会話または code 変更から、新しい project truth を抽出する。
2. その truth を分類する。
   - concept / principle
   - branch / release governance
   - test または execution process
   - reference knowledge
   - handover または operational log
3. 編集前に、対象文書の encoding が信頼できるかを確認する。必要なら `scripts/` で UTF-8 正規化する。
4. どれか 1 つを編集する前に、影響を受ける文書と authoritative / pointer の役割を洗い出す。
5. 最上位の source of truth を先に更新し、その後で下流の運用文書を更新する。
6. archive や旧版を持つ場合は current / archive の整合を確認する。
7. 作業中に route や process が変わった場合は、関連する進行中の process log も更新する。
8. 編集後は、次を明示的に確認する。
   - 記載漏れ
   - 矛盾
   - 古い参照
   - 上位文書に集約すべき重複記述
   - UTF-8 可読性
   - shared 文体 rule との表現整合
   - 冗長、曖昧、解釈分岐の残存

## 文体整合 rule

- shared 文体 rule が更新された時は、対象文書の truth だけでなく表現も同じ task で見直す。
- 文体整合では、意味保持を前提に次を確認する。
  - 文字数当たりの情報量
  - 人が追える可読性
  - 誤解のない一意な表現
  - 重複語、曖昧語、回りくどい言い回しの削減
- 文体 rule は decorative な統一ではなく、truth の誤読防止を優先して適用する。
- 文体の見直しだけで意味が変わる恐れがある時は、上位文書を先に確認し、意味確定後に書き換える。

## project reference resolution

- 対象 project に project-specific reference map がある時は、文書 target を決める前にそれを読む。
- project-specific reference は project ごとの `references/<project-code>-reference-map.md` に記載し、skill 本体へ個別 project 名や個別 file 名を直書きしない。
- project-specific map は、その project で `READ` / 編集対象にしてよい reference の範囲、authoritative file、legacy alias、temporary file の意味、解決順だけを持つ。
- project-specific map と generic 参照が異なる時は、project-specific map を優先する。

## 優先順
1. `docs/artifact/north_star.md` and `docs/artifact/problem_and_assumptions.md` for principles and assumptions
2. `docs/artifact/architecture.md` and `docs/artifact/decision_log.md` for design and important decisions
3. `docs/process/*` for collaboration rules, decision policy, and documentation policy
4. `docs/artifact/current_state.md` for ongoing work, confirmations, and next actions
5. `docs/observability/*` and `docs/metrics/*` for short-term logs and quality indicators
6. `docs/reference/*` for frontier knowledge articles

## 編集規則
- source-of-truth 文書も変わるなら、log 追記だけで済ませない。
- 新しい運用規則を chat にだけ残さない。
- 複数 file にまたがる記述なら、理由は上位文書に、具体 rule は下位文書に置く。
- 一時的 assumption が決定済み rule になったら、rule として書き直す。
- 文書更新が不要だった場合も、確認したうえで不要と明示する。

## 参照

- `references/`
- `references/writing-style-governance.md`
- `scripts/check_text_runtime_utf8.py`
- `scripts/check_markdown_encoding.py`
- `scripts/normalize_markdown_utf8.py`
