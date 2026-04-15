---
name: l2b-010-skill-function-test-run
description: 各 skill が取り持つ機能に対する機能確認テストを作成し、実行し、必要機能を満たすか評価する specialist skill。skill の新規作成または既存 skill 変更を含む task では必須で使う。
---

# Skill Function Test Runner

skill の存在ではなく、skill が必要機能を実際に担えるかを同じ task で確認する specialist skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` が skill 作成・変更 task を検知した時、`l2a-010-skill-build` と同時に必須選定される。
- `l1-001-skill-plan` は `l2a-010-skill-build` の後段にこの skill を必ず置く。

## Core Workflow

1. 対象 skill の目的、想定 prompt、必須機能、禁止事項、close 条件を整理する。
2. `references/skill-function-test-template.md` に沿って機能確認テスト表を作る。
3. test 観点を少なくとも次で定義する。
   - trigger 適合
   - 必須 read / workflow の実施
   - 必須成果物または expected result
   - guard rail / 禁止違反の不在
4. 対象 skill の `SKILL.md`、reference、scripts、metadata を用いて test を実行する。
5. 実行結果を `pass` / `fail` / `partial` で評価し、必要機能を満たすか判定する。
6. fail または partial があれば、`l2a-010-skill-build` へ修正観点を返す。
7. 再実行後に全必須観点が `pass` になった時だけ close 可と判断する。

## 必須成果物

- 機能確認テスト表
- 実行結果
- pass / fail / partial 評価
- 不足時の修正要求

## 固定ルール

- skill 作成・変更 task では省略しない。
- test を作るだけで終えず、必ず実行し評価する。
- 必要機能の定義が曖昧な時は、上位 rule と対象 skill の目的から判定軸を先に固定する。
- `pass` 判定は、対象 skill が必要機能を担う根拠を test 結果で示せる時だけ付ける。

## 参照

- `references/skill-function-test-template.md`
- `../l2a-010-skill-build/SKILL.md`
