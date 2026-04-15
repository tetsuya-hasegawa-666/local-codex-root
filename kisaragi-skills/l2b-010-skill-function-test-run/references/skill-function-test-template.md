# skill function test template

## 目的

- 各 skill の必要機能に対する機能確認テストを、同じ形式で作成、実行、評価するための template とする。

## test 表

| test_id | 観点 | 入力 prompt / 条件 | 期待される動作 | 判定方法 | 結果 | 評価 |
| --- | --- | --- | --- | --- | --- | --- |
| t1 | trigger 適合 |  |  |  |  |  |
| t2 | 必須 read / workflow |  |  |  |  |  |
| t3 | 必須成果物 |  |  |  |  |  |
| t4 | guard rail / 禁止違反なし |  |  |  |  |  |

## 評価 rule

- `pass`: 必須観点がすべて満たされ、必要機能を持つと判断できる。
- `partial`: 一部観点は満たすが、必要機能を持つと断定できない。
- `fail`: 必須観点を満たさず、必要機能が不足している。

## 実行メモ

- 対象 skill が参照する reference や script も test 対象に含める。
- 上位 shared rule と矛盾する時は `fail` とする。
