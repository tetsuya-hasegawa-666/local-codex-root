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
| prompt intake | `receipt-manager` | prompt 全受領、要求解釈、暗黙要求推論 |
| invoke gate | `skill-invoker` | 必要 skill 集合、読込下限、defer / block 判定 |
| orchestration | `skill-planner` | 発火、実行順、phase、handoff、close 条件 |
| execution | specialist / manager skill | 個別処理 |
| response | `response-manager` | admin 向け応答整形 |

- `receipt-manager` と `response-manager` は refresh target skill として未実装である。
- `skill-invoker` は実装済み正本入口であり、旧単一入口の役割を吸収した current invoke gate として扱う。
- 現行 directory 群は、新主線の execution 層で使う specialist 群として扱う。

## 2. 実装済み skill 在庫

- `authoritative-doc-scope-resolver`
- `artifact-handoff-mapper`
- `close-condition-definer`
- `delivery-planning-keeper`
- `design-first-script-builder`
- `doc-target-resolver`
- `documentation-watchkeeper`
- `drive-input-bootstrap-checker`
- `evidence-destination-resolver`
- `external-compute-output-keeper`
- `frontier-research-curator`
- `log-promotable-facts-extractor`
- `path-contract-scanner`
- `phase-task-orchestrator`
- `reference-rewire-operator`
- `rule-diff-clarifier`
- `rule-snapshot-reader`
- `runtime-bootstrap-scope-resolver`
- `runtime-operator`
- `runtime-structure-dependency-mapper`
- `script-doc-sync-enforcer`
- `skill-invoker`
- `skill-planner`
- `task-intent-normalizer`
- `task-scope-splitter`
- `test-and-evidence-recorder`
- `write-boundary-guard`
- `skill-opportunity-scout`
- `skill-opportunity-ledger`
- `skill-opportunity-architect`
- `skill-opportunity-integrator`

## 3. refresh target manager 群

| skill 名 | 状態 | 役割 |
| --- | --- | --- |
| `receipt-manager` | target | prompt 全受領、要求解釈 |
| `skill-invoker` | implemented | skill 集合確定、読込下限決定、常時候補監視 backloop 起動 |
| `skill-planner` | implemented | 実行順、phase、close 条件 |
| `response-manager` | target | 応答整形 |
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
| rule / authority helper | `rule-snapshot-reader` / `authoritative-doc-scope-resolver` / `rule-diff-clarifier` / `write-boundary-guard` | `receipt-manager` と `skill-invoker` の内部補助 |
| task structuring helper | `task-intent-normalizer` / `task-scope-splitter` / `close-condition-definer` | `skill-planner` の内部補助 |
| doc / sync specialist | `documentation-watchkeeper` / `doc-target-resolver` / `script-doc-sync-enforcer` / `test-and-evidence-recorder` | `document-control-manager` / `writing-normalizer` / `evidence-trace-manager` 候補 |
| design / contract specialist | `design-first-script-builder` / `reference-rewire-operator` / `path-contract-scanner` / `artifact-handoff-mapper` | `implementation-quality-manager` / `workspace-structure-manager` 候補 |
| runtime / structure specialist | `runtime-structure-dependency-mapper` / `runtime-operator` | `implementation-quality-manager` / `research-execution-manager` 候補 |
| planning / gate specialist | `delivery-planning-keeper` | `plan-gate-manager` 候補 |
| external compute specialist | `drive-input-bootstrap-checker` / `runtime-bootstrap-scope-resolver` / `external-compute-output-keeper` | `worklog-runtime-manager` / `windows-ops-manager` / `evidence-trace-manager` 候補 |
| phase specialist | `phase-task-orchestrator` | `skill-planner` が必要時に使う phase 補助 |
| closeout helper | `evidence-destination-resolver` / `log-promotable-facts-extractor` | `evidence-trace-manager` の内部補助 |
| skill opportunity family | `skill-opportunity-scout` / `skill-opportunity-ledger` / `skill-opportunity-architect` / `skill-opportunity-integrator` | `skill-opportunity-manager` 候補 |
| invoke gate | `skill-invoker` | 旧単一入口吸収済みの current invoke gate |

## 5. 移行原則

- 既存単一入口 skill は `skill-invoker` 名へ統一し、旧単一入口の role はこの skill へ吸収済みとする。
- `skill-planner` は存続するが、skill 集合の追加削除を持たず orchestration に専念する。
- specialist skill は自分で発火判断を持たず、`skill-invoker` と `skill-planner` の handoff を前提とする。
- `skill-opportunity-*` family は表向きの主線とは別系統の backloop として扱い、表向きには `skill-invoker` が動いているように見える構成を維持する。
- 実装済み skill の削除や rename は、人間承認なしに行わない。

## 6. 実装時の共通 rule

- 各 skill は `目的` `入力` `出力` `非責務` `前提` `参照` `close 条件` `更新対象` `禁止` を `SKILL.md` に持つ。
- `scripts/` は実行手順、`references/` は詳細仕様、`SKILL.md` は責務境界に集中する。
- trigger detail は skill 本体へ重複記載せず、上位 shared rule と対応 reference へ寄せる。
