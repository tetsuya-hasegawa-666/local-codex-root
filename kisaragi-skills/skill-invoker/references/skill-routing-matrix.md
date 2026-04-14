# skill routing matrix

## 基本

| 条件 | 優先 skill |
| --- | --- |
| 複数 task を含む | `phase-task-orchestrator` |
| script / notebook / runbook の大改修 | `design-first-script-builder` |
| path / contract / output 切替 | `reference-rewire-operator` |
| 文書同期が必要 | `documentation-watchkeeper` |
| `READ` 以外の access がある | `write-boundary-guard` |
| BDD / TDD / gate 更新 | `delivery-planning-keeper` |
| external compute | `external-compute-output-keeper` |
| 外部調査 | `frontier-research-curator` |
| runtime 安定化 | `runtime-operator` |
| skill 化候補の抽出 | `skill-opportunity-scout` |
| 候補台帳追記 | `skill-opportunity-ledger` |
| 候補分類 / admin `Go` 後整理 | `skill-opportunity-architect` |
| skill 実装と発火連携反映 | `skill-opportunity-integrator` |

## 選定ルール

- 入口は原則 1 つにする。
- 複数 task 開発依頼なら `phase-task-orchestrator` を入口にし、残りは phase 内専門 skill に落とす。
- 局所 task なら `phase-task-orchestrator` を省略して専門 skill だけでもよい。
- `documentation-watchkeeper` は単独より、他 skill の後段で文書同期用に付けることが多い。
- `reference-rewire-operator` は設計変更が無い task では選ばない。
- `skill-opportunity-scout` と `skill-opportunity-ledger` は hidden backloop として `skill-invoker` 配下で常時回す。
- `skill-opportunity-architect` と `skill-opportunity-integrator` は admin `Go` または候補整理要求が出た時だけ前面化する。

## 非推奨

- 入口 skill を 2 つ同時に選ぶ
- 全 skill を保険で並べる
- 順序を書かない
