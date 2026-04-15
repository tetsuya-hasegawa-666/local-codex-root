---
name: l1-001-skill-plan
description: `l0-001-skill-invoke` が `l0-002-request-intake` の解釈済み要求とともに確定した skill 集合を受け取り、実行順、phase、handoff、完了条件、検証順、closeout 順を決める orchestration skill。複数 skill をどの順番で実行させるかと、実際の実行管理を担う。skill の追加削除は行わない。
---

# Skill Planner

`l0-001-skill-invoke` の次段で動き、確定済み skill 群を実行可能な計画へ落とす orchestration skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` から `interpreted_request`、`selected_skills`、`deferred_skills`、`blocked_skills`、`read_set_minimum`、最低限の文脈情報が渡された時だけ起動する。

## Core Workflow

1. `l0-001-skill-invoke` から受け取った `interpreted_request`、確定済み skill 集合、選定理由を確認する。
2. task を、`single-step`、`multi-step`、`multi-phase` のいずれかへ分類する。
3. 実行順を決める。
   - 文脈固定
   - 設計 / 参照整理
   - code / docs 編集
   - probe / test / check
   - evidence / closeout
4. 必要時だけ `l1-002-phase-task-orchestrate` を呼び、phase header と phase 完了条件を固定する。
5. 各 skill へ handoff する入力と expected result を固定する。
6. `l3-001-response-shape` へ渡すため、最終応答に必要な形を `interpreted_request.expected_output` と整合させて保持する。
7. 下位 skill の結果を見て、次に進めるか、前段へ戻すか、close 不可にするかを決める。
8. task 全体の close 条件を満たしたら closeout へ進める。

## Child Skills

- `l1-003-task-intent-normalize`
- `l1-004-task-scope-split`
- `l1-005-close-condition-define`

必要時だけ上記 child skill を参照し、task の正規化、分割、close 条件固定を補助させる。

## Input

- `selected_skills`
- `interpreted_request`
- `why`
- `no_skill_reason`
- `admin_marks`
- `minimum_authoritative_docs`
- `task_summary`

## Output

- `execution_order`
- `phase_layout`
- `handoff_packet`
- `close_conditions`
- `fallback_path`
- `response_handoff`

## Guard Rails

- 自分で skill 選定をやり直さない。skill 要否判断と最終選定は `l0-001-skill-invoke` の ownership とする。
- 実行順を決めずに下位 skill を並列乱発しない。
- `Phase 1` と `Phase 4` を必要時に落とさない。
- 下位 skill の expected result を固定せずに handoff しない。
- close 条件を持たずに task を終えない。
- 確定済み skill 集合を planner の都合で増減しない。
- `l3-001-response-shape` が扱う出力整形責務を planner 側へ混ぜない。

## Coordination

- 複数 skill が選ばれた時の既定 orchestrator はこの skill とする。
- phase が必要な時は `l1-002-phase-task-orchestrate` を呼ぶ。
- code / docs 同期が必要な時は `l2b-002-script-doc-sync-enforce` または `l2a-005-documentation-watchkeep` を前後に置く。
- 計算環境依存がある時は `l2b-005-runtime-structure-dependency-map` または `l2a-002-reference-rewire-operate` を適切な順に置く。
- skill 作成・変更 task では、`l2a-010-skill-build` の後段に `l2b-010-skill-function-test-run` を必ず置き、機能確認テスト実行と評価を close 条件へ固定する。
- 実行結果を admin 応答へ返す時は、`l3-001-response-shape` へ `interpreted_request` と `execution_results` を渡せる形で handoff を残す。

## References

- `references/execution-order-patterns.md`
- `references/phase-selection-rule.md`
- `references/handoff-packet-template.md`
- `scripts/build_execution_plan.py`
