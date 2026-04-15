---
name: l2b-009-log-promotable-facts-extract
description: shared worklog や試行 log から、正本へ昇格すべき持続価値のある事実だけを抜き出す child skill。log 依存を減らしたい時に使う。
---

# Log Promotable Facts Extractor

shared log に残ったままの事実から、正本へ昇格すべき項目を抽出する child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が shared log から正本へ昇格すべき事実抽出を必要と判断した時だけ呼ばれる。

## Input

- `sharedlog_path`
- `must_read_docs`
- `required_evidence`

## Output

- `promotable_facts`
- `promotion_targets`
- `safe_to_reset_log_after`

## Guard Rails

- log 全文をそのまま正本へ写さない。
- 一時 trial と持続価値のある事実を分ける。
- 昇格前に log reset を前提にしない。

## Coordination

- closeout / evidence 系 specialist を補助する。

## 参照

- `AGENTS.md`
- closeout / evidence 系 specialist
