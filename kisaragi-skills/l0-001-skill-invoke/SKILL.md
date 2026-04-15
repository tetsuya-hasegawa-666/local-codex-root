---
name: l0-001-skill-invoke
description: 最上位入口 skill。`l0-002-request-intake` が生成した解釈済み要求を入力として、必要 skill の最終集合、read_set 下限、defer / block、write 境界確認、常時 skill 化候補監視 backloop を管理する current invoke gate。
---

# Skill Invoker

`l0-002-request-intake` が渡した解釈済み要求を受け取り、「今回 skill を使うべきか」「使うなら何を使うべきか」「裏で skill 化候補をどう記録するか」を同時に確定する最上位入口 skill とする。

## Trigger Ownership

- 開発 prompt に対する skill 選定の trigger ownership はこの skill が単独で持つ。
- 他 skill は自分で発火判断を持たない。
- admin mark `//s`、`//d`、`//c`、`//m` などの解釈もこの skill が持つ。
- `l0-002-request-intake` は前段解釈を担当するが、skill 選定は持たない。
- 表向きの skill 選定入口はこの skill だけとし、backloop 系 skill もこの skill からだけ起動する。

## Core Workflow

1. `l0-002-request-intake` から `prompt_full`、`explicit_requests`、`implicit_requests`、`constraints`、`expected_output`、`task_type`、`interpretation`、`insight` を受け取る。
2. 渡された解釈済み要求に未処理指示、制約、明示条件、mark が無いかを確認する。
3. `references/skill-trigger-matrix.md`、`references/admin-mark-table.md`、`references/skill-routing-matrix.md` を読む。
4. 解釈済み要求を次の観点で分類する。
   - 複数 task か
   - script / notebook / runbook 編集を含むか
   - skill の新規作成または既存 skill 変更を含むか
   - 設計変更や参照切替を含むか
   - 文書同期が必要か
   - `AGENTS.md` と project truth の境界整理、または project truth 冒頭構成の整理が主題か
   - skill 名の layer / serial / `short_function_name` 命名 rule や rename 可否の判定が主題か
   - BDD / TDD / gate 更新が主題か
   - `Colab` / remote compute を含むか
   - `READ` 以外の access を伴うか
   - 汎化して機械的に処理できそうな作業候補があるか
5. admin mark を解釈し、追加強制が必要かを決める。
6. `READ` 以外の access を伴う時は `l1-009-write-boundary-guard` を必須候補へ入れる。
7. skill を使わなくてよいかを判定する。
8. skill が必要なら、必要 skill を最小集合で選び、その最終 skill 集合を確定する。
   - skill の新規作成または既存 skill 変更を含む時は、`l2a-010-skill-build` と `l2b-010-skill-function-test-run` を必須で同時に確定する。
9. 常時 backloop として `lt-002-skill-opportunity-scout` を走らせ、skill 化候補があれば `lt-003-skill-opportunity-ledger` を起動して台帳と更新履歴へ追記する。
10. 候補の蓄積が進んだ時、または admin が `Go` を出した時は、`lt-004-skill-opportunity-architect` を起動して既存 merge / 新規 skill を根拠付きで分類する。
11. admin が `Go` を出した時は、`lt-005-skill-opportunity-integrate` を起動して skill 実装と `AGENTS.md -> skill` 発火連携まで更新する。
12. 最低限の文脈読込対象と handoff 条件を決める。
13. 解釈済み要求と表向きの実行 skill 集合を `l1-001-skill-plan` へ handoff する。

## Always-On Backloop

- `lt-002-skill-opportunity-scout`
  - 毎 prompt で暗黙起動する。
- `lt-003-skill-opportunity-ledger`
  - scout が候補を返した時だけ暗黙起動する。
- `lt-004-skill-opportunity-architect`
  - 候補の再整理が必要な時、または admin が `Go` / `整理して` / `分類して` と示した時に起動する。
- `lt-005-skill-opportunity-integrate`
  - admin が `Go` を出し、既存 merge または新規 skill 化を実施する時に起動する。

## Child And Background Skills

- `l1-006-rule-snapshot-read`
- `l1-007-authoritative-doc-scope-resolve`
- `l1-008-rule-diff-clarify`
- `l1-009-write-boundary-guard`
- `lt-002-skill-opportunity-scout`
- `lt-003-skill-opportunity-ledger`
- `lt-004-skill-opportunity-architect`
- `lt-005-skill-opportunity-integrate`

必要時だけ上記 skill を参照し、rule 確定、文書範囲切り出し、write 境界確認、skill 化候補の抽出と整理を補助させる。

## Decision Outputs

- `use_skills`: `yes` / `no`
- `interpreted_request`
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
  - `l1-001-skill-plan`
- script / notebook / runbook の新規作成や大改修:
  - `l2a-001-design-first-script-build`
- skill の新規作成または既存 skill 変更:
  - `l2a-010-skill-build`
- skill の機能確認テスト作成、実行、評価:
  - `l2b-010-skill-function-test-run`
- path / contract / output / docs_id の切替:
  - `l2a-002-reference-rewire-operate`
- `AGENTS.md` と project truth の境界整理、project truth 冒頭構成、canonical 要素の置き場整理:
  - `l2a-006-project-truth-boundary-keep`
- skill 名の layer / serial / `short_function_name` 命名、採番、rename、禁止語 review:
  - `lt-001-skill-name-standardize`
- 文書 drift や文書 topology の同期:
  - `l2a-005-documentation-watchkeep`
- BDD / TDD / gate / handover:
  - `l2a-003-delivery-plan-keep`
- `Colab` / remote notebook / remote GPU job:
  - `l2a-008-external-compute-output-keep`
- frontier research / 外部技術調査:
  - `l2a-007-frontier-research-curate`
- branch / Docker / FastAPI runtime:
  - `l2a-004-runtime-operate`
- `READ` 以外の access:
  - `l1-009-write-boundary-guard`
- skill 化候補の抽出:
  - `lt-002-skill-opportunity-scout`
- 候補台帳 / 更新履歴の追記:
  - `lt-003-skill-opportunity-ledger`
- 既存 merge / 新規 skill の分類:
  - `lt-004-skill-opportunity-architect`
- admin `Go` 後の skill 反映:
  - `lt-005-skill-opportunity-integrate`

## Output Format

最低限、次を返す。

- `use_skills`
- `interpreted_request`
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
interpreted_request:
  interpretation: "<summary>"
  expected_output:
  - "<shape>"
no_skill_reason:
selected_skills:
- l1-001-skill-plan
- l1-009-write-boundary-guard
- l2a-002-reference-rewire-operate
- l2a-005-documentation-watchkeep

deferred_skills:
- lt-004-skill-opportunity-architect

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

- `l0-001-skill-invoke` と `l1-001-skill-plan` の役割の違いを混同しない。
- `l0-002-request-intake` の解釈済み要求を無視して raw prompt の再解釈を主処理にしない。
- `l1-001-skill-plan` が後から skill を増減できる前提で書かない。
- skill 作成・変更 task では、`l2a-010-skill-build` だけを選んで `l2b-010-skill-function-test-run` を外さない。
- backloop は常時動かすが、主回答を乗っ取らない。
- 候補提案は、主回答の末尾へ短く差し込む。
- `lt-003-skill-opportunity-ledger` の上段候補ログは append-only とし、admin 手動削除または admin 指示以外で消さない。
- `Go` が出る前に自動で新規 skill を実装しない。

## Coordination

- 各 project で Codex に prompt が渡されたとき、skill 選定前段では `l0-002-request-intake` が動き、その次段の選定入口をこの skill とする。
- skill が必要な時は、確定済み skill 集合を `l1-001-skill-plan` へ handoff する。
- skill 不要判断の時でも、backloop による skill 化候補抽出は継続してよい。
- この skill 自体は code を編集しない。解釈済み要求の受領、最終 skill 集合の確定、write 境界確認要求、skill 化候補系統の起動、必要となった skill の handoff が責務である。

## When To Read References

- 解釈済み要求 review のたびに `references/skill-trigger-matrix.md`、`references/admin-mark-table.md`、`references/skill-routing-matrix.md` を読む。
- 候補台帳の状態を確認する時は `../lt-003-skill-opportunity-ledger/references/skill-opportunity-proposals.md` を読む。
- prompt review 補助が必要な時は `scripts/review_prompt_checklist.py` を使ってよい。
