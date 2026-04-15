---
name: l2a-010-skill-build
description: skill の新規作成または既存 skill 変更を扱う specialist skill。対象 skill の責務、trigger、workflow、reference、metadata、関連 shared rule をそろえ、同じ task で `l2b-010-skill-function-test-run` による機能確認テスト作成、実行、評価まで完了させる時に使う。
---

# Skill Builder

skill を「文書だけ置く」状態で終えず、作成または変更した skill が必要機能を持つかまで閉じる specialist skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` が skill の新規作成または既存 skill 変更を検知し、`l1-001-skill-plan` が skill 作成担当として割り当てた時だけ呼ばれる。

## Core Workflow

1. 対象 skill の目的、利用場面、不足、変更理由を短く整理する。
2. `AGENTS.md`、`kisaragi-skills/agents.md`、関連 skill、関連 reference を読み、上位 rule と責務境界を固定する。
3. 対象 skill の `SKILL.md`、`references/`、`scripts/`、`agents/openai.yaml` に必要な更新面を洗い出す。
4. 新規作成時は、`references/skill-structure-checklist.md` に沿って最小構成をそろえる。
5. 既存変更時は、旧責務と新責務の差分、影響 skill、影響 reference を明示する。
6. skill 本体と関連文書を更新する。
7. `l2b-010-skill-function-test-run` へ、対象 skill の必要機能、想定 prompt、pass 条件を handoff する。
8. `l2b-010-skill-function-test-run` が作成した機能確認テストを同じ task で実行し、評価結果を確認する。
9. test 失敗時は、skill 本体へ戻して修正し、再度 test を実行する。
10. pass 条件を満たした時だけ closeout へ進める。

## 必須成果物

- 対象 skill の `SKILL.md`
- 必要な `references/` または `scripts/`
- 必要時の `agents/openai.yaml`
- 機能確認テスト仕様
- 機能確認テスト実行結果
- pass / fail 評価

## 固定ルール

- skill 作成・変更 task では、`l2b-010-skill-function-test-run` を必ず同時に使う。
- skill 本体だけ更新して、機能確認テスト未作成のまま close してはならない。
- 機能確認テスト未実行、または評価未記録のまま close してはならない。
- skill の責務、trigger、非責務、参照、close 条件を曖昧にしない。
- 上位 shared rule と矛盾する skill を作らない。

## 参照

- `references/skill-structure-checklist.md`
- `../l2b-010-skill-function-test-run/SKILL.md`
