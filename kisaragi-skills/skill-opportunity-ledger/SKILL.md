---
name: skill-opportunity-ledger
description: skill 化候補を専用台帳 `.md` の上段へ append-only で追記し、同時に更新履歴 `.md` へ追記する hidden backloop skill。
---

# Skill Opportunity Ledger

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `skill-opportunity-scout` が候補を返した時にだけ、`skill-invoker` から起動される。

## 目的

- 候補専用 `.md` の上段へ append-only で追記する。
- 同じ内容を更新履歴 `.md` へも追記し、追記の事実を残す。

## 記録面

- 候補台帳:
  - `references/skill-opportunity-proposals.md`
- 更新履歴:
  - `references/skill-opportunity-proposals-RH.md`

## Guard

- 上段候補ログは削除しない。
- 削除は admin 手動削除または admin 明示指示時だけ許容する。
- 下段分類表の更新は行わない。分類は `skill-opportunity-architect` の責務とする。
