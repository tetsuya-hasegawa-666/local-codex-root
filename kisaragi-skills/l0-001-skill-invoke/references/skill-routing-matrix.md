# skill routing matrix

## 基本

| 条件 | 優先 skill |
| --- | --- |
| 複数 task を含む | `l1-002-phase-task-orchestrate` |
| script / notebook / runbook の大改修 | `l2a-001-design-first-script-build` |
| skill の新規作成または既存 skill 変更 | `l2a-010-skill-build` |
| skill の機能確認テスト作成、実行、評価 | `l2b-010-skill-function-test-run` |
| path / contract / output 切替 | `l2a-002-reference-rewire-operate` |
| 文書同期が必要 | `l2a-005-documentation-watchkeep` |
| `READ` 以外の access がある | `l1-009-write-boundary-guard` |
| BDD / TDD / gate 更新 | `l2a-003-delivery-plan-keep` |
| external compute | `l2a-008-external-compute-output-keep` |
| 外部調査 | `l2a-007-frontier-research-curate` |
| runtime 安定化 | `l2a-004-runtime-operate` |
| skill 化候補の抽出 | `lt-002-skill-opportunity-scout` |
| 候補台帳追記 | `lt-003-skill-opportunity-ledger` |
| 候補分類 / admin `Go` 後整理 | `lt-004-skill-opportunity-architect` |
| skill 実装と発火連携反映 | `lt-005-skill-opportunity-integrate` |

## 選定ルール

- 入口は原則 1 つにする。
- 複数 task 開発依頼なら `l1-002-phase-task-orchestrate` を入口にし、残りは phase 内専門 skill に落とす。
- 局所 task なら `l1-002-phase-task-orchestrate` を省略して専門 skill だけでもよい。
- `l2a-005-documentation-watchkeep` は単独より、他 skill の後段で文書同期用に付けることが多い。
- skill 作成・変更 task では、`l2a-010-skill-build` と `l2b-010-skill-function-test-run` を同時に選ぶ。
- `l2a-002-reference-rewire-operate` は設計変更が無い task では選ばない。
- `lt-002-skill-opportunity-scout` と `lt-003-skill-opportunity-ledger` は hidden backloop として `l0-001-skill-invoke` 配下で常時回す。
- `lt-004-skill-opportunity-architect` と `lt-005-skill-opportunity-integrate` は admin `Go` または候補整理要求が出た時だけ前面化する。

## 非推奨

- 入口 skill を 2 つ同時に選ぶ
- 全 skill を保険で並べる
- 順序を書かない
