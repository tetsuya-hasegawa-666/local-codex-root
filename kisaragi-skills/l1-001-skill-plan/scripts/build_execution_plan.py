from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class ExecutionPlan:
    execution_order: list[str]
    phase_layout: str


def build_execution_plan(selected_skills: list[str]) -> ExecutionPlan:
    if "l1-002-phase-task-orchestrate" in selected_skills or len(selected_skills) > 2:
        phase_layout = "multi-phase"
    elif len(selected_skills) == 2:
        phase_layout = "multi-step"
    else:
        phase_layout = "single-step"
    return ExecutionPlan(execution_order=selected_skills, phase_layout=phase_layout)


if __name__ == "__main__":
    print(asdict(build_execution_plan(["l1-001-skill-plan", "l2a-005-documentation-watchkeep"])))
