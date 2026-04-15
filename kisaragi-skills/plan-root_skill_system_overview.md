# root skill system overview

## 目的

- `root-skills/` 配下の skill 体系を、主線、補助 skill、実行 specialist、hidden backloop、refresh target manager 群の関係で俯瞰できるようにする。
- `agents.md` と `root_skill_trigger_system_map.md` の読解を補助する一覧図として使う。

## 全体像

```mermaid
flowchart TD
    U["prompt / admin request"]
    U --> R["receipt-manager<br/>target"]
    R --> I["skill-invoker<br/>implemented canonical invoke gate"]
    I --> P["skill-planner<br/>implemented orchestration"]
    P --> E["execution skills"]
    E --> M["response-manager<br/>target"]
```

## 実装済み skill 体系

```mermaid
flowchart LR
    subgraph Core["Core line"]
        I["skill-invoker"]
        P["skill-planner"]
    end

    subgraph IntakeHelpers["invoke / authority helpers"]
        H1["rule-snapshot-reader"]
        H2["authoritative-doc-scope-resolver"]
        H3["rule-diff-clarifier"]
        H4["write-boundary-guard"]
    end

    subgraph PlannerHelpers["planner helpers"]
        T1["task-intent-normalizer"]
        T2["task-scope-splitter"]
        T3["close-condition-definer"]
        T4["phase-task-orchestrator"]
    end

    subgraph DocFlow["document and evidence specialists"]
        D1["documentation-watchkeeper"]
        D2["doc-target-resolver"]
        D3["script-doc-sync-enforcer"]
        D4["test-and-evidence-recorder"]
        D5["evidence-destination-resolver"]
        D6["log-promotable-facts-extractor"]
    end

    subgraph DesignFlow["design and contract specialists"]
        C1["design-first-script-builder"]
        C2["reference-rewire-operator"]
        C3["path-contract-scanner"]
        C4["artifact-handoff-mapper"]
    end

    subgraph RuntimeFlow["runtime and external compute specialists"]
        R1["runtime-operator"]
        R2["runtime-structure-dependency-mapper"]
        R3["runtime-bootstrap-scope-resolver"]
        R4["drive-input-bootstrap-checker"]
        R5["external-compute-output-keeper"]
    end

    subgraph PlanningFlow["planning and research specialists"]
        P1["delivery-planning-keeper"]
        P2["frontier-research-curator"]
    end

    subgraph HiddenLoop["hidden skill-opportunity backloop"]
        O1["skill-opportunity-scout"]
        O2["skill-opportunity-ledger"]
        O3["skill-opportunity-architect"]
        O4["skill-opportunity-integrator"]
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
    M17["skill-opportunity-manager"] --> OX["skill-opportunity-scout / ledger / architect / integrator"]
    M12["access-safety-manager"] --> AX["write-boundary-guard"]
    M8["plan-gate-manager"] --> PX["delivery-planning-keeper"]
    M16["evidence-trace-manager"] --> EX["test-and-evidence-recorder / evidence-destination-resolver / log-promotable-facts-extractor"]
    M10["worklog-runtime-manager"] --> WX["external-compute-output-keeper / drive-input-bootstrap-checker / runtime-bootstrap-scope-resolver"]
    M9["implementation-quality-manager"] --> IX["design-first-script-builder / reference-rewire-operator / path-contract-scanner / runtime-structure-dependency-mapper / runtime-operator"]
    M4["document-control-manager"] --> DX["documentation-watchkeeper / doc-target-resolver / script-doc-sync-enforcer"]
    M1["receipt-manager"] --> RX["rule-snapshot-reader / authoritative-doc-scope-resolver / rule-diff-clarifier"]
    M2["response-manager"] --> RQ["未実装"]
```

## 読み方

- `skill-invoker` が表向きの正本入口であり、`skill-planner` へ visible execution set を handoff する。
- `skill-opportunity-*` family は hidden backloop として動き、候補抽出、台帳追記、分類、admin `Go` 後反映を分担する。
- refresh target manager 群は設計上の target であり、現時点では specialist 群の束として段階的に吸収・統合していく前提で扱う。
