# skill trigger matrix

## 目的

- `l0-001-skill-invoke` が prompt review 後に、必要 skill 候補を過不足なく選ぶための基準表とする。
- trigger ownership は `l0-001-skill-invoke` が持ち、この表はその判断根拠の軽量 reference とする。

## 基本方針

- まず `skill を使わない` 選択肢を残したまま review する。
- 複数条件に当てはまる時は、最小 skill 集合を優先する。
- specialist skill の発火条件はここで判断し、各 specialist 側へ持ち込まない。

## trigger matrix

| 案件 | `l0-001-skill-invoke` | `l1-001-skill-plan` | 既定 child / specialist | 終点 |
| --- | --- | --- | --- | --- |
| codex への prompt すべて | ◎ | ○ | `l1-006-rule-snapshot-read` / `l1-007-authoritative-doc-scope-resolve` / `l1-008-rule-diff-clarify` | skill 要否と最終集合確定 |
| 複数 task のとき | ◎ | ◎ | `l1-003-task-intent-normalize` / `l1-004-task-scope-split` / `l1-005-close-condition-define` / `l1-002-phase-task-orchestrate` | phase 固定 |
| code 編集 ipynb 含む / runbook 編集 | ◎ | ◎ | `l2a-001-design-first-script-build` / `l2a-002-reference-rewire-operate` / `l2b-002-script-doc-sync-enforce` | code / docs / test / evidence 同 task close |
| skill の新規作成または既存 skill 変更 | ◎ | ◎ | `l2a-010-skill-build` / `l2b-010-skill-function-test-run` | skill 本体更新と機能確認テストを同 task close |
| 文書同期作業のとき | ◎ | ○ | `l2a-005-documentation-watchkeep` / `l2b-001-doc-target-resolve` | 正本整合 |
| `READ` 以外の access を伴う | ◎ | ○ | `l1-009-write-boundary-guard` | write 許可 root 確定 |
| path / artifact / directory 契約変更 | ◎ | ◎ | `l2b-005-runtime-structure-dependency-map` / `l2b-004-artifact-handoff-map` / `l2b-003-path-contract-scan` | 依存棚卸し完了 |
| BDD / TDD / gate 更新 | ◎ | ◎ | `l2a-003-delivery-plan-keep` / `l2a-009-test-evidence-record` | plan と gate 更新 |
| external compute / Colab | ◎ | ◎ | `l2a-008-external-compute-output-keep` / `l2b-006-drive-input-bootstrap-check` / `l2b-007-runtime-bootstrap-scope-resolve` | bootstrap / persistent output 固定 |
| runtime / branch / Docker / FastAPI | ◎ | ◎ | `l2a-004-runtime-operate` | runtime 安定化 |
| shared worklog 昇格 / reset | ◎ | ○ | `l2b-009-log-promotable-facts-extract` / `l2b-008-evidence-destination-resolve` | 正本昇格後 reset 可否確定 |
| frontier 調査 | ◎ | ○ | `l2a-007-frontier-research-curate` | reference 更新 |
| skill 化候補を拾えそう | ◎ | hidden | `lt-002-skill-opportunity-scout` / `lt-003-skill-opportunity-ledger` | 候補台帳と更新履歴追記 |
| 候補整理または admin `Go` | ◎ | ○ | `lt-004-skill-opportunity-architect` / `lt-005-skill-opportunity-integrate` | 既存 merge / 新規 skill / 発火連携更新 |

- 記号は `◎=必須`、`○=条件付き` とする。

## mark 補正

| mark | 追加作用 |
| --- | --- |
| `//s` | code と文書と記録の同期を planner に要求する |
| `//d` | 依存 / path / artifact / directory の棚卸し担当を planner に要求する |
| `//c` | admin 確認待ち論点を plan に残す |
| `//m` | 対応処理を省略不可にする |

## skill 不要判断の例

- 単純な説明だけで code / docs 編集が無い
- 現状確認だけで編集や実行を伴わない
- skill を使うより通常応答の方が明らかに軽い

## 注意

- `l1-001-skill-plan` は execution order owner であり、選定 owner ではない。
- 迷った時は skill を増やしすぎず、`l1-001-skill-plan` と specialist 1 本から始める。
- skill 作成・変更 task では、`l2a-010-skill-build` と `l2b-010-skill-function-test-run` の片方だけを選ばない。
- `lt-002-skill-opportunity-scout` と `lt-003-skill-opportunity-ledger` は、表向きの主線とは別に hidden backloop として毎回回してよい。

## skillification candidate check

| 条件 | 既存 route | 追加検討 |
| --- | --- | --- |
| `AGENTS.md` に project 固有 path / code / URL / 現時点判断が混入していそう | `l2a-005-documentation-watchkeep` | 新規 `shared-rule-scope-guard` |
| shared rule と project truth の混在を分離したい | `l2a-005-documentation-watchkeep` | 新規 `shared-project-boundary-splitter` |
| `shared worklog` が 50k 上限へ近い / rotate 判断が必要 | `l2b-009-log-promotable-facts-extract` | 新規 `worklog-rotator` |
| `# admin` / `# codex` template と append-only を強制したい | `l2b-009-log-promotable-facts-extract` | 新規 `worklog-template-enforcer` |
| `kisaragi-tree` の sync / exe 再生成 / 確認を定型化したい | `l2a-004-runtime-operate` | 新規 `tree-sync-operator` |

- 上記条件に当てはまる時は、`l0-001-skill-invoke` は既存 skill だけで閉じるか、新規 skill 候補が必要かを必ず short note で明示する。
- 新規 skill 候補が必要でも、その場で自動新設はせず、まず候補名と不足理由を handoff または review 文書へ残す。

## candidate ledger routing

- scout が候補を返した時は `../lt-003-skill-opportunity-ledger/references/skill-opportunity-proposals.md` の上段へ append する。
- architect は同 file の下段表を更新し、同時に `../lt-003-skill-opportunity-ledger/references/skill-opportunity-proposals-RH.md` へ更新履歴を追記する。
- architect の更新履歴 entry には、少なくとも `対象 skill 名` と `対象候補標題` を含める。
