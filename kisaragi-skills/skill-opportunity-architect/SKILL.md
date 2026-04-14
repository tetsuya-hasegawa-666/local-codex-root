---
name: skill-opportunity-architect
description: 候補台帳の下段表を更新し、各候補を既存 skill へマージ可能か、新規 skill が必要かを根拠付きで分類し、同じ更新履歴 `.md` へも記録する skill。
---

# Skill Opportunity Architect

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `skill-invoker` が候補整理または admin `Go` を検知した時に起動する。

## 目的

- 候補が蓄積したあと、既存 skill へマージ可能か、新規 skill が必要かを根拠付きで分類する。
- `skill-opportunity-proposals.md` の下段分類表を更新する。
- 同じ更新履歴 `.md` に、分類更新を行った事実を記録する。

## 記録面

- 分類表:
  - `../skill-opportunity-ledger/references/skill-opportunity-proposals.md`
- 更新履歴:
  - `../skill-opportunity-ledger/references/skill-opportunity-proposals-RH.md`

## 必須記録

- 更新履歴 entry には、少なくとも次を含める。
  - `日時`
  - `対象 skill 名`
  - `対象候補標題`
  - `既存 / 新規`
  - `更新内容`

## Guard

- 候補上段ログの削除や圧縮は行わない。
- 既存 merge / 新規 skill の最終実装は `skill-opportunity-integrator` の責務とする。
