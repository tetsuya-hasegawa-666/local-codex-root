# agents.md
- 概案名: `Skill Structure Ledger`

## 0. 位置づけ

- この directory は `local-codex-root/` refresh 版における skill 正本 directory とする。
- `1 skill = 1 directory` を原則とする。
- 実装済み skill と target skill を混同しない。
- 上位 shared rule は `AGENTS.md` に従う。

## 1. 新主線

| 層 | owner | 役割 |
| --- | --- | --- |
| prompt intake | `l0-002-request-intake` | prompt 全受領、要求解釈、暗黙要求推論 |
| invoke gate | `l0-001-skill-invoke` | 必要 skill 集合、読込下限、defer / block 判定 |
| orchestration | `l1-001-skill-plan` | 発火、実行順、phase、handoff、close 条件 |
| execution | specialist / manager skill | 個別処理 |
| response | `l3-001-response-shape` | admin 向け応答整形 |

- `l0-002-request-intake` は prompt 全受領と要求解釈を担当する前段 skill とする。
- `l0-001-skill-invoke` は実装済み正本入口であり、旧単一入口の役割を吸収した current invoke gate として扱う。
- `l3-001-response-shape` は skill 結果を admin 向け応答へ統合整形する後段 skill とする。
- 現行 directory 群は、新主線の execution 層で使う specialist 群として扱う。

## 2. 実装済み skill 在庫

- `l1-007-authoritative-doc-scope-resolve`
- `l2b-004-artifact-handoff-map`
- `l1-005-close-condition-define`
- `l2a-003-delivery-plan-keep`
- `l2a-001-design-first-script-build`
- `l2b-001-doc-target-resolve`
- `l2a-005-documentation-watchkeep`
- `l2b-006-drive-input-bootstrap-check`
- `l2b-008-evidence-destination-resolve`
- `l2a-008-external-compute-output-keep`
- `l2a-007-frontier-research-curate`
- `l2b-009-log-promotable-facts-extract`
- `lt-001-skill-name-standardize`
- `l2b-003-path-contract-scan`
- `l1-002-phase-task-orchestrate`
- `l2a-006-project-truth-boundary-keep`
- `l2a-002-reference-rewire-operate`
- `l1-008-rule-diff-clarify`
- `l1-006-rule-snapshot-read`
- `l2b-007-runtime-bootstrap-scope-resolve`
- `l2a-004-runtime-operate`
- `l2b-005-runtime-structure-dependency-map`
- `l2b-002-script-doc-sync-enforce`
- `l0-001-skill-invoke`
- `l0-002-request-intake`
- `l1-001-skill-plan`
- `l3-001-response-shape`
- `l1-003-task-intent-normalize`
- `l1-004-task-scope-split`
- `l2a-009-test-evidence-record`
- `l2a-010-skill-build`
- `l1-009-write-boundary-guard`
- `lt-002-skill-opportunity-scout`
- `lt-003-skill-opportunity-ledger`
- `lt-004-skill-opportunity-architect`
- `lt-005-skill-opportunity-integrate`
- `l2b-010-skill-function-test-run`

## 3. refresh target manager 群

| skill 名 | 状態 | 役割 |
| --- | --- | --- |
| `l0-002-request-intake` | implemented | prompt 全受領、要求解釈、暗黙要求と制約の補正 |
| `l0-001-skill-invoke` | implemented | skill 集合確定、読込下限決定、常時候補監視 backloop 起動 |
| `l1-001-skill-plan` | implemented | 実行順、phase、close 条件 |
| `l3-001-response-shape` | implemented | 応答整形、粒度調整、余剰除去 |
| `governance-manager` | target | shared rule、承認要否、構造変更 |
| `document-control-manager` | target | 文書正本、履歴、pointer、配置整合 |
| `writing-normalizer` | target | 文体圧縮、表化、日本語基調 |
| `workspace-structure-manager` | target | directory 構造、保管先整理 |
| `project-registry-manager` | target | project code / name / artifact 命名 |
| `plan-gate-manager` | target | BDD / TDD / gate / closeout |
| `implementation-quality-manager` | target | code / test / trace / warning-blocker 整理 |
| `worklog-runtime-manager` | target | shared worklog、runbook、bootstrap、pair 同期 |
| `git-hygiene-manager` | target | branch、stage、commit / push hygiene |
| `access-safety-manager` | target | workspace 外 access、安全境界 |
| `collaboration-decision-manager` | target | 可逆 / 不可逆、承認依頼、decision 記録 |
| `research-execution-manager` | target | 継続探索、再読込、矛盾処理 |
| `windows-ops-manager` | target | Windows 手順、tree sync、再生成 |
| `evidence-trace-manager` | target | evidence path、manifest、summary、close 根拠 |
| `skill-opportunity-manager` | target | skill 化候補の抽出、台帳化、分類、Go 後反映 |

## 4. 現行 skill の再配置

| execution family | 現行 skill | refresh target manager との関係 |
| --- | --- | --- |
| rule / authority helper | `l1-006-rule-snapshot-read` / `l1-007-authoritative-doc-scope-resolve` / `l1-008-rule-diff-clarify` / `l1-009-write-boundary-guard` | `l0-002-request-intake` と `l0-001-skill-invoke` の内部補助 |
| task structuring helper | `l1-003-task-intent-normalize` / `l1-004-task-scope-split` / `l1-005-close-condition-define` | `l1-001-skill-plan` の内部補助 |
| doc / sync specialist | `l2a-005-documentation-watchkeep` / `l2b-001-doc-target-resolve` / `l2b-002-script-doc-sync-enforce` / `l2a-009-test-evidence-record` | `document-control-manager` / `writing-normalizer` / `evidence-trace-manager` 候補 |
| naming specialist | `lt-001-skill-name-standardize` | `project-registry-manager` / `writing-normalizer` 候補 |
| truth boundary specialist | `l2a-006-project-truth-boundary-keep` | `document-control-manager` / `writing-normalizer` / `plan-gate-manager` 候補 |
| design / contract specialist | `l2a-001-design-first-script-build` / `l2a-002-reference-rewire-operate` / `l2b-003-path-contract-scan` / `l2b-004-artifact-handoff-map` | `implementation-quality-manager` / `workspace-structure-manager` 候補 |
| runtime / structure specialist | `l2b-005-runtime-structure-dependency-map` / `l2a-004-runtime-operate` | `implementation-quality-manager` / `research-execution-manager` 候補 |
| planning / gate specialist | `l2a-003-delivery-plan-keep` | `plan-gate-manager` 候補 |
| external compute specialist | `l2b-006-drive-input-bootstrap-check` / `l2b-007-runtime-bootstrap-scope-resolve` / `l2a-008-external-compute-output-keep` | `worklog-runtime-manager` / `windows-ops-manager` / `evidence-trace-manager` 候補 |
| skill build specialist | `l2a-010-skill-build` / `l2b-010-skill-function-test-run` | `implementation-quality-manager` / `document-control-manager` / `evidence-trace-manager` 候補 |
| phase specialist | `l1-002-phase-task-orchestrate` | `l1-001-skill-plan` が必要時に使う phase 補助 |
| closeout helper | `l2b-008-evidence-destination-resolve` / `l2b-009-log-promotable-facts-extract` | `evidence-trace-manager` の内部補助 |
| skill opportunity family | `lt-002-skill-opportunity-scout` / `lt-003-skill-opportunity-ledger` / `lt-004-skill-opportunity-architect` / `lt-005-skill-opportunity-integrate` | `skill-opportunity-manager` 候補 |
| invoke gate | `l0-001-skill-invoke` | 旧単一入口吸収済みの current invoke gate |

## 5. 移行原則

- 既存単一入口 skill は `l0-001-skill-invoke` 名へ統一し、旧単一入口の role はこの skill へ吸収済みとする。
- `l0-002-request-intake` は skill 選定前の要求解釈専用とし、skill 選定を持たない。
- `l1-001-skill-plan` は存続するが、skill 集合の追加削除を持たず orchestration に専念する。
- `l3-001-response-shape` は skill 結果整形専用とし、skill 選定や処理本体を持たない。
- specialist skill は自分で発火判断を持たず、`l0-001-skill-invoke` と `l1-001-skill-plan` の handoff を前提とする。
- `skill-opportunity-*` family は表向きの主線とは別系統の backloop として扱い、表向きには `l0-001-skill-invoke` が動いているように見える構成を維持する。
- skill 作成・変更 task では、`l2a-010-skill-build` と `l2b-010-skill-function-test-run` を同時に使い、対象 skill の機能確認テストまで同 task で閉じる。
- 実装済み skill の削除や rename は、人間承認なしに行わない。

## 6. 実装時の共通 rule

- 各 skill は `目的` `入力` `出力` `非責務` `前提` `参照` `close 条件` `更新対象` `禁止` を `SKILL.md` に持つ。
- `scripts/` は実行手順、`references/` は詳細仕様、`SKILL.md` は責務境界に集中する。
- trigger detail は skill 本体へ重複記載せず、上位 shared rule と対応 reference へ寄せる。
- 各 skill は、自身が取り持つ機能に対する機能確認テストの設計と評価導線を持つ。
