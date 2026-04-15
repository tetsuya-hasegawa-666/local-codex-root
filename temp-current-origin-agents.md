# agents.md

## kisaragi-skills の構成

- この directory は skill 正本 directory とする。
- `1 skill = 1 directory` を原則とする。
- skill 群の親子関係は filesystem の入れ子ではなく、`agents.md` と各 `SKILL.md` の責務記述で表す。
- 同名 skill は 1 つだけを正本として置くものとする。
- 役割が近い skill は、観点を失わない範囲で既存 skill へ吸収してよい。
- `l0-001-skill-invoke` と `l1-001-skill-plan` を主線とし、それ以外は原則として child skill または specialist skill として配置する。


## 収録 skill

- `l1-007-authoritative-doc-scope-resolve`
- `l2b-004-artifact-handoff-map`
- `l1-005-close-condition-define`
- `l2a-001-design-first-script-build`
- `l2a-005-documentation-watchkeep`
- `l2b-001-doc-target-resolve`
- `l2b-006-drive-input-bootstrap-check`
- `l2a-003-delivery-plan-keep`
- `l2b-008-evidence-destination-resolve`
- `l2a-008-external-compute-output-keep`
- `l2a-007-frontier-research-curate`
- `l2b-009-log-promotable-facts-extract`
- `l2b-003-path-contract-scan`
- `l1-002-phase-task-orchestrate`
- `l2a-002-reference-rewire-operate`
- `l1-008-rule-diff-clarify`
- `l1-006-rule-snapshot-read`
- `l2a-004-runtime-operate`
- `l2b-007-runtime-bootstrap-scope-resolve`
- `l2b-005-runtime-structure-dependency-map`
- `l2b-002-script-doc-sync-enforce`
- `l0-001-skill-invoke`
- `l1-001-skill-plan`
- `l1-003-task-intent-normalize`
- `l1-004-task-scope-split`
- `l2a-009-test-evidence-record`


## 役割境界

- `l0-001-skill-invoke` を開発 prompt の最上位入口とし、prompt 全体 review、skill 要否判断、mark 解釈、および今回使う最終 skill 集合の確定までを担うものとする。skill 不要判断もこの skill が行う。
- `l1-001-skill-plan` を `l0-001-skill-invoke` の直下に置き、確定済み skill 集合の実行順、phase 配置、handoff、完了条件、検証順、closeout 順を管理する orchestration skill とする。skill の追加削除は行わない。
- `l0-001-skill-invoke` 配下の child skill は `l1-006-rule-snapshot-read`、`l1-007-authoritative-doc-scope-resolve`、`l1-008-rule-diff-clarify` とし、必要時にだけ参照するものとする。
- `l1-001-skill-plan` 配下の child skill は `l1-003-task-intent-normalize`、`l1-004-task-scope-split`、`l1-005-close-condition-define` とし、必要時にだけ参照するものとする。
- `script / docs` family の child skill は `l2b-001-doc-target-resolve`、`l2a-009-test-evidence-record` とし、`l2b-002-script-doc-sync-enforce` と `l2a-005-documentation-watchkeep` を補助するものとする。
- `runtime / structure` family の child skill は `l2b-004-artifact-handoff-map`、`l2b-003-path-contract-scan` とし、`l2b-005-runtime-structure-dependency-map` を補助するものとする。
- `external compute` family の child skill は `l2b-006-drive-input-bootstrap-check`、`l2b-007-runtime-bootstrap-scope-resolve` とし、`l2a-008-external-compute-output-keep` を補助するものとする。
- `closeout / evidence` family の child skill は `l2b-008-evidence-destination-resolve`、`l2b-009-log-promotable-facts-extract` とし、evidence 反映と shared log 昇格を補助するものとする。
- `l1-002-phase-task-orchestrate` は開発入口ではなく、`l1-001-skill-plan` から呼ばれる phase 構成 specialist とし、authoritative doc check、phase header、完了条件、closeout ひな形を提供するものとする。
- `l2a-001-design-first-script-build` は、設計審査票、責務分離、関数一覧表、docs ID 対応、validation / error handling 契約を先に固定してから script や notebook を書く観点を扱うものとする。
- `l2a-005-documentation-watchkeep` は docs drift、文書 topology、version 整合、encoding 健全性をまとめて扱うものとする。
- `l2a-003-delivery-plan-keep` は BDD、TDD、release gate、handover をまとめて扱うものとする。
- `l2a-008-external-compute-output-keep` は `Colab`、remote notebook、remote GPU job の final output を永続 visible storage へ固定し、cleanup 対象を分離する観点を扱うものとする。
- `l2a-004-runtime-operate` は branch 同期、Docker 安定化、FastAPI 実装運用をまとめて扱うものとする。
- `l2a-007-frontier-research-curate` は外部研究調査を扱うものとする。
- `l2b-002-script-doc-sync-enforce` は script / notebook / runbook の変更と、関連正本文書更新、test、記録反映を同一 task で閉じる specialist とする。
- `l2b-005-runtime-structure-dependency-map` は import、path、artifact、directory の依存棚卸しと runtime 契約確認を扱う specialist とする。
- 発火条件の ownership は `l0-001-skill-invoke` が持ち、他 skill は自分で発火判断を持たず、受入前提、処理責務、完了条件、失敗条件に集中するものとする。
- `l2a-001-design-first-script-build`、`l2a-002-reference-rewire-operate`、`l2a-005-documentation-watchkeep`、`l2a-003-delivery-plan-keep` は `l1-001-skill-plan` または `l1-002-phase-task-orchestrate` の各 phase で併用する専門 skill とする。
- `l2a-002-reference-rewire-operate` は、設計変更で path、ID、helper 所有、contract、generated output 名などの参照先を切り替える時の棚卸し、切替順、grep 検査、文書同期、下流確認を扱うものとする。
