# request-intake output schema

## Required Fields

| field | role |
| --- | --- |
| `prompt_full` | 受領した prompt 全体 |
| `explicit_requests` | 明示要求一覧 |
| `implicit_requests` | 暗黙要求一覧 |
| `constraints` | 禁止、命名、形式、粒度、境界制約 |
| `expected_output` | 表、規則文、差分、提案など期待形式 |
| `task_type` | 文書改訂、設計、実装、検証、調査など |
| `interpretation` | 解釈要約 |
| `insight` | 高確率で求められている補助意図 |
| `handoff_to` | 原則 `l0-001-skill-invoke` |

## Guard

- `interpretation` は短く一義に書く。
- `insight` は推定だと分かる形に保つ。
- skill 名が prompt に含まれても、それ自体を即時起動命令として確定しない。
