---
name: skill-invoker
description: 最上位入口 skill。旧単一入口の role を吸収した current invoke gate として、必要 skill の最終集合、read_set 下限、defer / block、write 境界確認、常時 skill 化候補監視 backloop を管理する。
---

# Skill Invoker

prompt を受けた最初の段階で、「今回 skill を使うべきか」「使うなら何を使うべきか」「裏で skill 化候補をどう記録するか」を同時に確定する最上位入口 skill とする。

## Trigger Ownership

- 開発 prompt の trigger ownership はこの skill が単独で持つ。
- 他 skill は自分で発火判断を持たない。
- admin mark `//s`、`//d`、`//c`、`//m` などの解釈もこの skill が持つ。
- 表向きの入口はこの skill だけとし、backloop 系 skill もこの skill からだけ起動する。

## Core Workflow

1. prompt 全体を review し、依頼を 1 行で要約する。
2. prompt に未処理指示、制約、明示条件、mark が無いかを確認する。
3. `references/skill-trigger-matrix.md`、`references/admin-mark-table.md`、`references/skill-routing-matrix.md` を読む。
4. 依頼を次の観点で分類する。
   - 複数 task か
   - script / notebook / runbook 編集を含むか
   - 設計変更や参照切替を含むか
   - 文書同期が必要か
   - `AGENTS.md` と project truth の境界整理、または project truth 冒頭構成の整理が主題か
   - skill 名の layer / serial / `short_function_name` 命名 rule や rename 可否の判定が主題か
   - BDD / TDD / gate 更新が主題か
   - `Colab` / remote compute を含むか
   - `READ` 以外の access を伴うか
   - 汎化して機械的に処理できそうな作業候補があるか
5. admin mark を解釈し、追加強制が必要かを決める。
6. `READ` 以外の access を伴う時は `write-boundary-guard` を必須候補へ入れる。
7. skill を使わなくてよいかを判定する。
8. skill が必要なら、必要 skill を最小集合で選び、その最終 skill 集合を確定する。
9. 常時 backloop として `skill-opportunity-scout` を走らせ、skill 化候補があれば `skill-opportunity-ledger` を起動して台帳と更新履歴へ追記する。
10. 候補の蓄積が進んだ時、または admin が `Go` を出した時は、`skill-opportunity-architect` を起動して既存 merge / 新規 skill を根拠付きで分類する。
11. admin が `Go` を出した時は、`skill-opportunity-integrator` を起動して skill 実装と `AGENTS.md -> skill` 発火連携まで更新する。
12. 最低限の文脈読込対象と handoff 条件を決める。
13. 表向きの実行 skill 集合を `skill-planner` へ handoff する。

## Always-On Backloop

- `skill-opportunity-scout`
  - 毎 prompt で暗黙起動する。
- `skill-opportunity-ledger`
  - scout が候補を返した時だけ暗黙起動する。
- `skill-opportunity-architect`
  - 候補の再整理が必要な時、または admin が `Go` / `整理して` / `分類して` と示した時に起動する。
- `skill-opportunity-integrator`
  - admin が `Go` を出し、既存 merge または新規 skill 化を実施する時に起動する。

## Child And Background Skills

- `rule-snapshot-reader`
- `authoritative-doc-scope-resolver`
- `rule-diff-clarifier`
- `write-boundary-guard`
- `skill-opportunity-scout`
- `skill-opportunity-ledger`
- `skill-opportunity-architect`
- `skill-opportunity-integrator`

必要時だけ上記 skill を参照し、rule 確定、文書範囲切り出し、write 境界確認、skill 化候補の抽出と整理を補助させる。

## Decision Outputs

- `use_skills`: `yes` / `no`
- `no_skill_reason`
- `selected_skills`
- `deferred_skills`
- `blocked_skills`
- `why`
- `marks_detected`
- `read_set_minimum`
- `planner_required`
- `opportunity_note_for_response`

## Default Routing Heuristics

- 複数 task を含む開発依頼:
  - `skill-planner`
- script / notebook / runbook の新規作成や大改修:
  - `design-first-script-builder`
- path / contract / output / docs_id の切替:
  - `reference-rewire-operator`
- `AGENTS.md` と project truth の境界整理、project truth 冒頭構成、canonical 要素の置き場整理:
  - `project-truth-boundary-keeper`
- skill 名の layer / serial / `short_function_name` 命名、採番、rename、禁止語 review:
  - `lt-001-skill-name-standardize`
- 文書 drift や文書 topology の同期:
  - `documentation-watchkeeper`
- BDD / TDD / gate / handover:
  - `delivery-planning-keeper`
- `Colab` / remote notebook / remote GPU job:
  - `external-compute-output-keeper`
- frontier research / 外部技術調査:
  - `frontier-research-curator`
- branch / Docker / FastAPI runtime:
  - `runtime-operator`
- `READ` 以外の access:
  - `write-boundary-guard`
- skill 化候補の抽出:
  - `skill-opportunity-scout`
- 候補台帳 / 更新履歴の追記:
  - `skill-opportunity-ledger`
- 既存 merge / 新規 skill の分類:
  - `skill-opportunity-architect`
- admin `Go` 後の skill 反映:
  - `skill-opportunity-integrator`

## Output Format

最低限、次を返す。

- `use_skills`
- `no_skill_reason`
- `selected_skills`
- `deferred_skills`
- `blocked_skills`
- `why`
- `planner_required`
- `opportunity_note_for_response`

例:

```text
use_skills: yes
no_skill_reason:
selected_skills:
- skill-planner
- write-boundary-guard
- reference-rewire-operator
- documentation-watchkeeper

deferred_skills:
- skill-opportunity-architect

blocked_skills:

planner_required: yes

why:
- 複数 task 依頼で実行順管理が必要
- path / contract 切替を含む
- 正本文書同期が必要
- READ 以外の access を伴う

opportunity_note_for_response:
- 候補名: <name>
- 概要: <summary>
- 記録先: references/skill-opportunity-proposals.md
```

## Guard Rails

- `skill-invoker` と `skill-planner` の役割の違いを混同しない。
- `skill-planner` が後から skill を増減できる前提で書かない。
- backloop は常時動かすが、主回答を乗っ取らない。
- 候補提案は、主回答の末尾へ短く差し込む。
- `skill-opportunity-ledger` の上段候補ログは append-only とし、admin 手動削除または admin 指示以外で消さない。
- `Go` が出る前に自動で新規 skill を実装しない。

## Coordination

- 各 project で Codex に prompt が渡されたときの既定入口はこの skill とする。
- skill が必要な時は、確定済み skill 集合を `skill-planner` へ handoff する。
- skill 不要判断の時でも、backloop による skill 化候補抽出は継続してよい。
- この skill 自体は code を編集しない。prompt review、最終 skill 集合の確定、write 境界確認要求、skill 化候補系統の起動、必要となった skill の handoff が責務である。

## When To Read References

- prompt review のたびに `references/skill-trigger-matrix.md`、`references/admin-mark-table.md`、`references/skill-routing-matrix.md` を読む。
- 候補台帳の状態を確認する時は `../skill-opportunity-ledger/references/skill-opportunity-proposals.md` を読む。
- prompt review 補助が必要な時は `scripts/review_prompt_checklist.py` を使ってよい。
