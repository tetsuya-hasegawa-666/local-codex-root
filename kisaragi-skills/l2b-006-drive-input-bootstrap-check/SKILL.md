---
name: l2b-006-drive-input-bootstrap-check
description: external compute task で Drive mount から input 解決までの bootstrap を確認する child skill。Drive 入力候補の発見、選択、handoff 契約を固定したい時に使う。
---

# Drive Input Bootstrap Checker

`Drive mount -> input 解決` を固定して外部 compute の初動を安定化する child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が Drive 入力 bootstrap の確認を必要と判断した時だけ呼ばれる。

## Input

- `task_summary`
- `project_code`
- `must_read_docs`

## Output

- `drive_mount_requirements`
- `input_resolution_steps`
- `selected_input_contract`

## Guard Rails

- Drive mount 前提を黙って飛ばさない。
- hardcode path を canonical route とみなさない。
- input 発見と input 採用を混同しない。

## Coordination

- `l2a-008-external-compute-output-keep` を補助する。

## 参照

- `AGENTS.md`
- `l2a-008-external-compute-output-keep`
