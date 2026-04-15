# root skill system overview

## 目的

- `root-skills/` 配下の skill 体系を、主線、補助 skill、実行 specialist、hidden backloop、refresh target manager 群の関係で俯瞰できるようにする。
- `agents.md` と `root_skill_trigger_system_map.md` の読解を補助する一覧図として使う。

## 全体像

```mermaid
flowchart TD
    U["prompt / admin request"]
    U --> R["receipt-manager<br/>target"]
    R --> I["l0-001-skill-invoke<br/>implemented canonical invoke gate"]
    I --> P["l1-001-skill-plan<br/>implemented orchestration"]
    P --> E["execution skills"]
    E --> M["response-manager<br/>target"]
```

## 実装済み skill 体系

```mermaid
flowchart LR
    subgraph Core["Core line"]
        I["l0-001-skill-invoke"]
        P["l1-001-skill-plan"]
    end

    subgraph IntakeHelpers["invoke / authority helpers"]
        H1["l1-006-rule-snapshot-read"]
        H2["l1-007-authoritative-doc-scope-resolve"]
        H3["l1-008-rule-diff-clarify"]
        H4["l1-009-write-boundary-guard"]
    end

    subgraph PlannerHelpers["planner helpers"]
        T1["l1-003-task-intent-normalize"]
        T2["l1-004-task-scope-split"]
        T3["l1-005-close-condition-define"]
        T4["l1-002-phase-task-orchestrate"]
    end

    subgraph DocFlow["document and evidence specialists"]
        D1["l2a-005-documentation-watchkeep"]
        D2["l2b-001-doc-target-resolve"]
        D3["l2b-002-script-doc-sync-enforce"]
        D4["l2a-009-test-evidence-record"]
        D5["l2b-008-evidence-destination-resolve"]
        D6["l2b-009-log-promotable-facts-extract"]
    end

    subgraph DesignFlow["design and contract specialists"]
        C1["l2a-001-design-first-script-build"]
        C2["l2a-002-reference-rewire-operate"]
        C3["l2b-003-path-contract-scan"]
        C4["l2b-004-artifact-handoff-map"]
    end

    subgraph RuntimeFlow["runtime and external compute specialists"]
        R1["l2a-004-runtime-operate"]
        R2["l2b-005-runtime-structure-dependency-map"]
        R3["l2b-007-runtime-bootstrap-scope-resolve"]
        R4["l2b-006-drive-input-bootstrap-check"]
        R5["l2a-008-external-compute-output-keep"]
    end

    subgraph PlanningFlow["planning and research specialists"]
        P1["l2a-003-delivery-plan-keep"]
        P2["l2a-007-frontier-research-curate"]
    end

    subgraph HiddenLoop["hidden skill-opportunity backloop"]
        O1["lt-002-skill-opportunity-scout"]
        O2["lt-003-skill-opportunity-ledger"]
        O3["lt-004-skill-opportunity-architect"]
        O4["lt-005-skill-opportunity-integrate"]
    end

    I --> H1
    I --> H2
    I --> H3
    I --> H4
    I --> O1
    O1 --> O2
    O2 --> O3
    O3 --> O4

    I --> P
    P --> T1
    P --> T2
    P --> T3
    P --> T4
    P --> D1
    P --> D2
    P --> D3
    P --> D4
    P --> D5
    P --> D6
    P --> C1
    P --> C2
    P --> C3
    P --> C4
    P --> R1
    P --> R2
    P --> R3
    P --> R4
    P --> R5
    P --> P1
    P --> P2
```

## refresh target manager 群

```mermaid
flowchart TB
    subgraph TargetManagers["refresh target managers"]
        M1["receipt-manager"]
        M2["response-manager"]
        M3["governance-manager"]
        M4["document-control-manager"]
        M5["writing-normalizer"]
        M6["workspace-structure-manager"]
        M7["project-registry-manager"]
        M8["plan-gate-manager"]
        M9["implementation-quality-manager"]
        M10["worklog-runtime-manager"]
        M11["git-hygiene-manager"]
        M12["access-safety-manager"]
        M13["collaboration-decision-manager"]
        M14["research-execution-manager"]
        M15["windows-ops-manager"]
        M16["evidence-trace-manager"]
        M17["skill-opportunity-manager"]
    end
```

## target manager と現行実装の対応

```mermaid
flowchart LR
    M17["skill-opportunity-manager"] --> OX["lt-002-skill-opportunity-scout / ledger / architect / integrator"]
    M12["access-safety-manager"] --> AX["l1-009-write-boundary-guard"]
    M8["plan-gate-manager"] --> PX["l2a-003-delivery-plan-keep"]
    M16["evidence-trace-manager"] --> EX["l2a-009-test-evidence-record / l2b-008-evidence-destination-resolve / l2b-009-log-promotable-facts-extract"]
    M10["worklog-runtime-manager"] --> WX["l2a-008-external-compute-output-keep / l2b-006-drive-input-bootstrap-check / l2b-007-runtime-bootstrap-scope-resolve"]
    M9["implementation-quality-manager"] --> IX["l2a-001-design-first-script-build / l2a-002-reference-rewire-operate / l2b-003-path-contract-scan / l2b-005-runtime-structure-dependency-map / l2a-004-runtime-operate"]
    M4["document-control-manager"] --> DX["l2a-005-documentation-watchkeep / l2b-001-doc-target-resolve / l2b-002-script-doc-sync-enforce"]
    M1["receipt-manager"] --> RX["l1-006-rule-snapshot-read / l1-007-authoritative-doc-scope-resolve / l1-008-rule-diff-clarify"]
    M2["response-manager"] --> RQ["未実装"]
```

## 読み方

- `l0-001-skill-invoke` が表向きの正本入口であり、`l1-001-skill-plan` へ visible execution set を handoff する。
- `skill-opportunity-*` family は hidden backloop として動き、候補抽出、台帳追記、分類、admin `Go` 後反映を分担する。
- refresh target manager 群は設計上の target であり、現時点では specialist 群の束として段階的に吸収・統合していく前提で扱う。
