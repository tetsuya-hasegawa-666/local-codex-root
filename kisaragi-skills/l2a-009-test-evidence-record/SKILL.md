---
name: l2a-009-test-evidence-record
description: task で要求された test 実行と、既存 evidence 正本への反映を同時に閉じる child skill。結果が log にしか残らない状態を避けたい時に使う。
---

# Test And Evidence Recorder

test 実行結果を既存 evidence 面へ昇格させる child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が test 実行と evidence 反映を同 task で閉じる必要があると判断した時だけ呼ばれる。

## Input

- `required_tests`
- `required_evidence`
- `working_files`

## Output

- `test_execution_summary`
- `evidence_update_targets`
- `recorded_results`

## Guard Rails

- log だけで close しない。
- 新しい evidence file を勝手に増やさない。
- test 未実行を実行済みとして記録しない。

## Coordination

- `l2b-002-script-doc-sync-enforce` と `l2b-008-evidence-destination-resolve` を補助する。

## 参照

- `AGENTS.md`
- `l2b-002-script-doc-sync-enforce`
- `l2b-008-evidence-destination-resolve`
