---
name: skill-opportunity-integrator
description: admin `Go` 後に、分類済み候補を既存 skill へ反映するか、新規 skill を実装するかを実行し、`AGENTS.md -> skill` 発火連携まで更新する skill。
---

# Skill Opportunity Integrator

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- admin が `Go` を出し、`skill-invoker` が実装フェーズへ進めると判断した時だけ起動する。

## 目的

- 分類済み候補を既存 skill へマージするか、新規 skill を作る。
- `AGENTS.md`、skill registry、trigger matrix、pilot spec などの連携面を更新し、適切に発火する状態を作る。

## 主な更新対象

- `AGENTS.md`
- `AGENTSmd-RH.md`
- `kisaragi-skills/agents.md`
- `skill-invoker`
- 関連 specialist skill
- `skill-opportunity-ledger` の分類状態

## Guard

- admin `Go` が無いのに実装へ進めない。
- 既存 skill へマージする場合も、目的、非責務、trigger ownership を壊さない。
