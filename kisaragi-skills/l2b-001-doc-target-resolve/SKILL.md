---
name: l2b-001-doc-target-resolve
description: code / notebook / runbook 変更から、同 task で更新すべき正本文書と補助文書を特定する child skill。文書更新漏れを避けたい時に使う。
---

# Doc Target Resolver

変更対象から、更新すべき文書群を洗い出す child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が文書更新対象の特定を必要と判断した時だけ呼ばれる。

## Input

- `working_files`
- `must_read_docs`
- `likely_write_docs`

## Output

- `doc_update_targets`
- `doc_sync_rationale`

## Guard Rails

- 正本と補助文書の優先順位を崩さない。
- 変更理由のない文書を広げすぎない。
- 逆に関連文書を取りこぼさない。

## Coordination

- `l2b-002-script-doc-sync-enforce` と `l2a-005-documentation-watchkeep` を補助する。

## 参照

- `AGENTS.md`
- `l2b-002-script-doc-sync-enforce`
- `l2a-005-documentation-watchkeep`
