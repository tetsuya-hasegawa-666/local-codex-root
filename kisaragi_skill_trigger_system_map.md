# kisaragi skill trigger system map

## 目的

- `prompt -> receipt-manager -> l0-001-skill-invoke -> l1-001-skill-plan -> execution -> response-manager` の主線を図で固定する。
- ownership と handoff の境界を図で読めるようにする。

## 全体構造

```mermaid
flowchart TD
    U["prompt"] --> R["receipt-manager / 解釈と要求整理"]
    R --> I["l0-001-skill-invoke / skill 集合確定 + hidden backloop"]
    I -->|selected skills| P["l1-001-skill-plan / 発火と順序管理"]
    P --> E["execution skills / manager と specialist"]
    E --> M["response-manager / 応答整形"]
```

## ownership map

```mermaid
flowchart LR
    R["receipt-manager"] --> A1["prompt review"]
    R --> A2["明示要求抽出"]
    R --> A3["暗黙要求抽出"]
    R --> A4["制約整理"]

    I["l0-001-skill-invoke"] --> B1["skill 要否判断"]
    I --> B2["read_set_minimum 決定"]
    I --> B3["defer / block 判定"]
    I --> B4["skill 集合確定"]
    I --> B5["write 境界確認要求"]
    I --> B6["skill 化候補 backloop 起動"]

    P["l1-001-skill-plan"] --> C1["実行順管理"]
    P --> C2["phase 管理"]
    P --> C3["handoff 固定"]
    P --> C4["close 条件固定"]

    M["response-manager"] --> D1["粒度調整"]
    M --> D2["形式整形"]
    M --> D3["残件提示"]
```

## 現行 skill の位置づけ

```mermaid
flowchart TD
    I["l0-001-skill-invoke"] --> H1["l1-006-rule-snapshot-read"]
    I --> H2["l1-007-authoritative-doc-scope-resolve"]
    I --> H3["l1-008-rule-diff-clarify"]

    P["l1-001-skill-plan"] --> T1["l1-003-task-intent-normalize"]
    P --> T2["l1-004-task-scope-split"]
    P --> T3["l1-005-close-condition-define"]
    P --> T4["l1-002-phase-task-orchestrate"]

    I --> G1["l1-009-write-boundary-guard"]
    I --> O1["lt-002-skill-opportunity-scout"]
    I --> O2["lt-003-skill-opportunity-ledger"]
    I --> O3["lt-004-skill-opportunity-architect"]
    I --> O4["lt-005-skill-opportunity-integrate"]

    P --> S1["l2a-005-documentation-watchkeep"]
    P --> S2["l2a-001-design-first-script-build"]
    P --> S3["l2a-002-reference-rewire-operate"]
    P --> S4["l2a-003-delivery-plan-keep"]
    P --> S5["l2b-005-runtime-structure-dependency-map"]
    P --> S6["l2a-008-external-compute-output-keep"]
    P --> S7["l2a-004-runtime-operate"]
    P --> S8["l2a-009-test-evidence-record"]
```

## 旧構成との対応

| 旧 | 新 |
| --- | --- |
| 旧単一入口の prompt review 部分 | `receipt-manager` |
| 旧単一入口の最終選定部分 | `l0-001-skill-invoke` |
| `l1-001-skill-plan` | `l1-001-skill-plan` のまま維持 |
| 応答整形の暗黙処理 | `response-manager` |

## 標準 handoff 順

```mermaid
sequenceDiagram
    participant U as prompt
    participant R as receipt-manager
    participant I as l0-001-skill-invoke
    participant P as l1-001-skill-plan
    participant O as hidden opportunity loop
    participant E as execution skills
    participant M as response-manager

    U->>R: prompt
    R->>I: 解釈済み要求
    I->>O: scout / ledger / architect / integrator when needed
    I->>P: selected / deferred / blocked / read_set
    P->>E: execution plan
    E-->>M: results
    M-->>U: formatted response
```
