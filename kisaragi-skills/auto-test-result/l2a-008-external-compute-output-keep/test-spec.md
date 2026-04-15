# l2a-008-external-compute-output-keep capability test spec

- test_code_name: `run_skill_capability_checks.py::structural_capability_suite`
- scope: `SKILL.md` / references / scripts / registry / required integration points

## test items

| test_id | 観点 | pass 条件 |
| --- | --- | --- |
| t1 | frontmatter name 整合 | `name` が skill directory 名と一致する |
| t2 | description 存在 | `description` が空でない |
| t3 | trigger ownership | `Trigger Ownership` section を持つ |
| t4 | workflow | `Core Workflow` または `Workflow` section を持つ |
| t5 | references section | `参照` または `References` section を持つ |
| t6 | relative path integrity | `SKILL.md` が参照する relative path が存在する |
| t7 | registry integration | `kisaragi-skills/agents.md` に登録されている |
| t8 | special integration | 対象 skill に必要な特別導線が存在する |

