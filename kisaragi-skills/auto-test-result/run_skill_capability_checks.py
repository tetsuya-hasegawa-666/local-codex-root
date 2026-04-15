from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKILL_ID_PATTERN = re.compile(r"^(l0|l1|l2a|l2b|l3|lt)-\d{3}-[a-z0-9-]+$")
FRONTMATTER_NAME = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
FRONTMATTER_DESCRIPTION = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
CODE_PATH_PATTERN = re.compile(r"`((?:\.\./|references/|scripts/|agents/)[^`]+)`")


@dataclass
class TestResult:
    test_id: str
    description: str
    passed: bool
    detail: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_skill_dirs(skills_root: Path) -> list[Path]:
    return sorted(
        [
            path
            for path in skills_root.iterdir()
            if path.is_dir() and SKILL_ID_PATTERN.match(path.name)
        ],
        key=lambda p: p.name,
    )


def extract_name(text: str) -> str | None:
    match = FRONTMATTER_NAME.search(text)
    return match.group(1).strip() if match else None


def extract_description(text: str) -> str | None:
    match = FRONTMATTER_DESCRIPTION.search(text)
    return match.group(1).strip() if match else None


def has_any_heading(text: str, headings: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(f"## {heading}".lower() in lowered for heading in headings)


def has_trigger_ownership(text: str) -> bool:
    return has_any_heading(text, ["Trigger Ownership"]) or any(
        phrase in text
        for phrase in [
            "発火判断を持たない",
            "必要時にだけ参照される",
            "時だけ呼ばれる",
            "時だけ起動する",
            "hidden backloop",
        ]
    )


def has_workflow(text: str) -> bool:
    if has_any_heading(text, ["Core Workflow", "Workflow"]):
        return True
    if bool(re.search(r"^\d+\.\s", text, re.MULTILINE)):
        return True
    return all(marker in text for marker in ["## Input", "## Output", "## Coordination"])


def has_reference_section(text: str) -> bool:
    if has_any_heading(text, ["参照", "References", "When To Read References"]):
        return True
    if any(token in text for token in ["`references/", "`../", "参照する時は"]):
        return True
    return "## Coordination" in text and bool(re.search(r"`[^`]+`", text))


def collect_path_refs(text: str, skill_dir: Path) -> list[Path]:
    refs: list[Path] = []
    for rel in CODE_PATH_PATTERN.findall(text):
        if "<" in rel or ">" in rel:
            continue
        refs.append((skill_dir / rel).resolve())
    return refs


def build_expectation_checks(skill_id: str, skills_root: Path) -> list[tuple[str, str, list[Path] | list[str]]]:
    invoke_skill = skills_root / "l0-001-skill-invoke" / "SKILL.md"
    invoke_trigger = skills_root / "l0-001-skill-invoke" / "references" / "skill-trigger-matrix.md"
    plan_skill = skills_root / "l1-001-skill-plan" / "SKILL.md"
    checks: list[tuple[str, str, list[Path] | list[str]]] = []
    if skill_id == "l2a-010-skill-build":
        checks.append(("t8", "invoke と planner に登録されている", [invoke_skill, invoke_trigger, plan_skill]))
    if skill_id == "l2b-010-skill-function-test-run":
        checks.append(("t8", "invoke と planner に登録されている", [invoke_skill, invoke_trigger, plan_skill]))
    if skill_id == "l2a-005-documentation-watchkeep":
        checks.append(("t8", "文体 governance reference を持つ", [skills_root / skill_id / "references" / "writing-style-governance.md"]))
    return checks


def run_skill_checks(skill_dir: Path, agents_text: str, skills_root: Path) -> list[TestResult]:
    skill_id = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    results: list[TestResult] = []

    if not skill_md.exists():
        return [TestResult("t0", "SKILL.md が存在する", False, "SKILL.md missing")]

    text = read_text(skill_md)
    name = extract_name(text)
    description = extract_description(text)

    results.append(
        TestResult(
            "t1",
            "frontmatter name が directory 名と一致する",
            name == skill_id,
            f"name={name!r}",
        )
    )
    results.append(
        TestResult(
            "t2",
            "frontmatter description が存在する",
            bool(description),
            "description present" if description else "description missing",
        )
    )
    results.append(
        TestResult(
            "t3",
            "Trigger Ownership section を持つ",
            has_trigger_ownership(text),
            "trigger ownership found" if has_trigger_ownership(text) else "section missing",
        )
    )
    results.append(
        TestResult(
            "t4",
            "Workflow section を持つ",
            has_workflow(text),
            "workflow found" if has_workflow(text) else "workflow section missing",
        )
    )
    results.append(
        TestResult(
            "t5",
            "reference section を持つ",
            has_reference_section(text),
            "reference section found" if has_reference_section(text) else "reference section missing",
        )
    )

    refs = collect_path_refs(text, skill_dir)
    missing_refs = [str(path) for path in refs if not path.exists()]
    results.append(
        TestResult(
            "t6",
            "SKILL.md 内で参照する relative path が存在する",
            not missing_refs,
            "all referenced paths exist" if not missing_refs else "\n".join(missing_refs),
        )
    )
    results.append(
        TestResult(
            "t7",
            "skill registry に登録されている",
            f"`{skill_id}`" in agents_text,
            "registered in kisaragi-skills/agents.md" if f"`{skill_id}`" in agents_text else "missing from registry",
        )
    )

    for test_id, description_text, paths in build_expectation_checks(skill_id, skills_root):
        missing = [str(path) for path in paths if isinstance(path, Path) and not path.exists()]
        results.append(
            TestResult(
                test_id,
                description_text,
                not missing,
                "expected integration exists" if not missing else "\n".join(missing),
            )
        )

    return results


def render_test_spec(skill_id: str) -> str:
    return "\n".join(
        [
            f"# {skill_id} capability test spec",
            "",
            "- test_code_name: `run_skill_capability_checks.py::structural_capability_suite`",
            "- scope: `SKILL.md` / references / scripts / registry / required integration points",
            "",
            "## test items",
            "",
            "| test_id | 観点 | pass 条件 |",
            "| --- | --- | --- |",
            "| t1 | frontmatter name 整合 | `name` が skill directory 名と一致する |",
            "| t2 | description 存在 | `description` が空でない |",
            "| t3 | trigger ownership | `Trigger Ownership` section を持つ |",
            "| t4 | workflow | `Core Workflow` または `Workflow` section を持つ |",
            "| t5 | references section | `参照` または `References` section を持つ |",
            "| t6 | relative path integrity | `SKILL.md` が参照する relative path が存在する |",
            "| t7 | registry integration | `kisaragi-skills/agents.md` に登録されている |",
            "| t8 | special integration | 対象 skill に必要な特別導線が存在する |",
            "",
        ]
    )


def write_per_skill_outputs(out_dir: Path, skill_id: str, results: list[TestResult]) -> tuple[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    test_code_name = "run_skill_capability_checks.py::structural_capability_suite"
    spec = render_test_spec(skill_id)
    status = "pass" if all(result.passed for result in results) else "fail"
    remediation = [result.detail for result in results if not result.passed]
    result_json = {
        "skill_id": skill_id,
        "test_code_name": test_code_name,
        "status": status,
        "results": [
            {
                "test_id": result.test_id,
                "description": result.description,
                "passed": result.passed,
                "detail": result.detail,
            }
            for result in results
        ],
        "remediation": remediation,
    }
    result_md_lines = [
        f"# {skill_id} capability test result",
        "",
        f"- test_code_name: `{test_code_name}`",
        f"- status: `{status}`",
        "",
        "## result",
        "",
        "| test_id | 観点 | 結果 | detail |",
        "| --- | --- | --- | --- |",
    ]
    for result in results:
        outcome = "pass" if result.passed else "fail"
        detail = result.detail.replace("\n", "<br>")
        result_md_lines.append(f"| {result.test_id} | {result.description} | `{outcome}` | {detail} |")

    (out_dir / "test-code-name.txt").write_text(test_code_name + "\n", encoding="utf-8")
    (out_dir / "test-spec.md").write_text(spec + "\n", encoding="utf-8")
    (out_dir / "test-result.json").write_text(json.dumps(result_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "test-result.md").write_text("\n".join(result_md_lines) + "\n", encoding="utf-8")
    remediation_text = "なし" if not remediation else "; ".join(remediation)
    return status, remediation_text


def main() -> int:
    auto_test_root = Path(__file__).resolve().parent
    skills_root = auto_test_root.parent
    agents_text = read_text(skills_root / "agents.md")
    skill_dirs = find_skill_dirs(skills_root)

    summary_lines = [
        "# auto-test-result",
        "",
        "| skill | test code | result | 対処 |",
        "| --- | --- | --- | --- |",
    ]
    failed_skills: list[str] = []

    for skill_dir in skill_dirs:
        results = run_skill_checks(skill_dir, agents_text, skills_root)
        status, remediation_text = write_per_skill_outputs(auto_test_root / skill_dir.name, skill_dir.name, results)
        summary_lines.append(
            f"| `{skill_dir.name}` | `run_skill_capability_checks.py::structural_capability_suite` | `{status}` | {remediation_text} |"
        )
        if status != "pass":
            failed_skills.append(skill_dir.name)

    (skills_root / "auto-test-result.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    if failed_skills:
        print("FAILED:", ", ".join(failed_skills))
        return 1
    print("ALL_SKILL_TESTS_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
