---
name: l2b-008-evidence-destination-resolve
description: task 結果を既存の evidence 正本へどう振り分けるかを決める child skill。refresh では `realtime-compass-and-status.md` と `--testlogs/` を主な記録先として扱い、旧 separate evidence 文書へ戻らないようにする時に使う。
---

# Evidence Destination Resolver

既存 evidence 面のどこへ何を残すかを決める child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が evidence 記録先の確定を必要と判断した時だけ呼ばれる。

## Input

- `required_evidence`
- `project_code`
- `must_read_docs`

## Output

- `evidence_destinations`
- `recording_rules`

## Guard Rails

- 記録先を勝手に新設しない。
- admin 面と codex 面の証跡を混同しない。
- log の保存と evidence 反映を同一視しない。

## Coordination

- `l2a-009-test-evidence-record` と closeout 系 specialist を補助する。

## 参照

- `AGENTS.md`
- `l2a-009-test-evidence-record`
