---
name: l0-002-request-intake
description: prompt を 100% 受領し、明示要求、暗黙要求、制約、期待出力、粒度、継続文脈を抽出して解釈済み要求へ正規化する前段 skill。実行や skill 選定は行わず、`l0-001-skill-invoke` へ handoff する。
---

# Request Intake

prompt をそのまま skill 判定へ入れず、解釈済み要求へ一段抽出してから後段へ渡す前段 skill とする。

## Trigger Ownership

- prompt を受けた時の最初の前段 intake として動く。
- この skill 自身は skill 選定を持たない。
- 実行や応答整形も持たない。

## Core Workflow

1. prompt 全体を 100% review する。
2. 明示要求を列挙する。
3. 暗黙要求、比較期待、欲しい粒度、期待形式、継続文脈を推定する。
4. 禁止事項、命名制約、形式制約、write 境界制約を抽出する。
5. task type を仮分類する。
6. `interpretation` を 1 段落または短い箇条書きで要約する。
7. 明言されていないが高確率で必要な `insight` を必要最小限で整理する。
8. `handoff_to: l0-001-skill-invoke` を付けて後段へ渡す。

## Input

- `prompt_full`
- `conversation_context`
- `active_rules`

## Output

- `prompt_full`
- `explicit_requests`
- `implicit_requests`
- `constraints`
- `expected_output`
- `task_type`
- `interpretation`
- `insight`
- `handoff_to`

## Non-Goals

- skill を選定しない。
- 実行順を決めない。
- code / docs を編集しない。
- admin への最終応答を作らない。

## Preconditions

- prompt 全文へ access できる。
- 上位 shared rule を読める。

## Coordination

- raw prompt を読む前段 intake として使う。
- `l0-001-skill-invoke` はこの skill の出力を前提に skill 選定する。

## References

- `references/request-intake-output-schema.md`
- `../l0-001-skill-invoke/SKILL.md`
- `../l1-006-rule-snapshot-read/SKILL.md`
- `../l1-007-authoritative-doc-scope-resolve/SKILL.md`

## Close Conditions

- prompt 全体が未読なく review 済みである。
- 明示要求、暗黙要求、制約、期待形式、task type、interpretation が揃っている。
- `l0-001-skill-invoke` へ渡す handoff 情報が揃っている。

## Update Targets

- `AGENTS.md`
- `../agents.md`
- 必要時は `../l0-001-skill-invoke/SKILL.md`

## Forbidden

- prompt の一部だけで全体解釈を固定しない。
- 暗黙要求推定を広げすぎて勝手な方針追加をしない。
- skill 要否判断をここで確定しない。
- 未確認事項を確定事実として handoff しない。

## Capability Test

- prompt から `explicit_requests` `implicit_requests` `constraints` `expected_output` `task_type` `interpretation` を欠落なく抽出できるかを確認する。
- 制約付き prompt で、制約が `constraints` に残るかを確認する。
- skill 選定や応答整形を出力へ混入させないかを確認する。

## Skill Test Storage

- `../auto-test-result/`
