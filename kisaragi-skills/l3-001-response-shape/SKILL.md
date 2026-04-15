---
name: l3-001-response-shape
description: `l0-002-request-intake` の解釈済み要求と各 skill の結果を受け取り、要求解釈に沿う admin 向け応答へ統合整形する後段 skill。skill 選定や処理本体は持たない。
---

# Response Shape

複数 skill の結果をそのまま返さず、解釈済み要求に沿って粒度、順序、形式、残件表示を整える後段 skill とする。

## Trigger Ownership

- 実行 skill の結果がそろい、admin 向け応答を返す直前にだけ使う。
- この skill 自身は skill 選定を持たない。
- 処理本体も持たない。

## Core Workflow

1. `interpreted_request` を確認し、期待形式と粒度を固定する。
2. `execution_results` と `phase_result` を確認し、返すべき事実を抽出する。
3. 解釈済み要求に沿って結論、主要結果、残件、未確定事項の順を整える。
4. 冗長説明や要求外ノイズを削る。
5. 未確定事項や前提不足は隠さず `open_points` へ残す。
6. `response_shape` を明示し、admin 向け本文を返す。

## Input

- `interpreted_request`
- `selected_skills`
- `execution_results`
- `phase_result`
- `style_rules`

## Output

- `response_body`
- `omitted_noise`
- `open_points`
- `response_shape`

## Non-Goals

- skill を選定しない。
- 実処理の結果を書き換えない。
- 未実施事項を実施済みへ見せない。
- planner の代わりに phase 設計しない。

## Preconditions

- `interpreted_request` がある。
- 実行 skill の主要結果が揃っている。

## References

- `references/response-shape-checklist.md`
- `../l0-002-request-intake/SKILL.md`
- `../l1-001-skill-plan/SKILL.md`

## Close Conditions

- `response_body` が `interpreted_request` の期待形式と整合している。
- 主要事実、残件、未確定事項が欠落なく反映されている。
- 余剰説明の削除結果が `omitted_noise` に残っている。

## Update Targets

- `AGENTS.md`
- `../agents.md`
- 必要時は `../l1-001-skill-plan/SKILL.md`

## Forbidden

- skill 結果の意味を変えて要約しない。
- 期待形式を無視して生ログをそのまま返さない。
- 不都合な open point を隠さない。
- skill 選定や実行順の再判断をしない。

## Capability Test

- 同一結果群から、表要求、規則文要求、短い closeout 要求で形を変えられるかを確認する。
- 未確定事項がある結果群で、`open_points` へ残せるかを確認する。
- 要求外ノイズを削っても、主要事実を落とさないかを確認する。

## Skill Test Storage

- `../auto-test-result/`
