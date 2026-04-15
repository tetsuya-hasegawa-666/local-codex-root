---
name: l2b-004-artifact-handoff-map
description: producer / consumer の artifact handoff を整理する child skill。生成物名、保存先、再解釈面、下流消費先のずれを確認したい時に使う。
---

# Artifact Handoff Mapper

artifact 契約の producer / consumer 関係を可視化する child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が artifact handoff の棚卸しを必要と判断した時だけ呼ばれる。

## Input

- `working_files`
- `project_code`
- `must_read_docs`

## Output

- `artifact_handoff_map`
- `producer_consumer_gaps`

## Guard Rails

- file path と artifact 名を混同しない。
- runtime 上の tmp 出力を canonical artifact と誤認しない。
- manifest 面と実体面の責務を混ぜない。

## Coordination

- `l2b-005-runtime-structure-dependency-map` と `l2a-002-reference-rewire-operate` を補助する。

## 参照

- `AGENTS.md`
- `l2b-005-runtime-structure-dependency-map`
- `l2a-002-reference-rewire-operate`
