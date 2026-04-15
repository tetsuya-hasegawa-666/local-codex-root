# execution order patterns

## 目的

- `l1-001-skill-plan` が specialist skill の実行順を決める時の既定 pattern を持つ。

## pattern 1: script 変更 + 文書同期

1. 文脈固定
2. 設計 / 参照整理
3. code / docs 編集
4. test / probe
5. evidence / closeout

推奨 skill:
- `l1-002-phase-task-orchestrate`
- `l2a-001-design-first-script-build`
- `l2a-002-reference-rewire-operate`
- `l2a-005-documentation-watchkeep`

## pattern 2: script 変更 + 依存棚卸し

1. 文脈固定
2. 依存棚卸し
3. 必要なら参照切替
4. code / docs 編集
5. probe / unittest
6. evidence / closeout

## pattern 3: external compute

1. 文脈固定
2. runbook / input contract 確認
3. output tree / persistent storage 確認
4. 実行
5. final output 保存
6. cleanup 判断

## pattern 4: BDD / TDD / gate 更新

1. 文脈固定
2. story / behavior 整理
3. TDD task 化
4. gate 状態更新
5. handover / closeout

## pattern 5: skill 作成または変更

1. 文脈固定
2. skill 責務、参照、metadata 設計
3. skill 本体、reference、関連文書更新
4. 機能確認テスト作成
5. 機能確認テスト実行と評価
6. evidence / closeout

推奨 skill:
- `l1-002-phase-task-orchestrate`
- `l2a-010-skill-build`
- `l2b-010-skill-function-test-run`
- `l2a-005-documentation-watchkeep`
