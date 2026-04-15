# AGENTS.md skill mapping proposal
- 目的: `AGENTS.md` の各章を、shared rule のまま残すべきか、skill 化すべきか、または既存 skill の再編対象か、という観点で対応付ける。
- 前提: `AGENTS.md` は shared governance の憲法であり、詳細手順や実務運用は可能な限り `root-skills/` へ降ろす。
- 参照比較: `project-truth-core.md` と `realtime-compass-and-status.md` を読むと、truth / current / gate / artifact contract / canonical naming / runbook pair 同期などの運用責務がすでに大きく、`AGENTS.md` 側の refresh target 群だけでは受け皿が不足している。

## まず結論

| 観点 | 提案 |
| --- | --- |
| 不足 skill | ある |
| 大きすぎる skill | `l0-001-skill-invoke`, `l1-001-skill-plan`, `document-control-manager`, `plan-gate-manager`, `worklog-runtime-manager` |
| 小さすぎる skill | 目立っては少ない。むしろ不足側 |
| 追加優先度 高 | `project-truth-maintainer`, `current-state-syncer`, `mrl-ledger-maintainer`, `bdd-tdd-ledger-maintainer`, `artifact-contract-steward`, `canonical-naming-steward`, `runbook-pair-sync-enforcer` |
| shared 固定推奨 | 原則、強制順序、禁止事項、access / safety の基本境界 |
| skill へ降ろす優先領域 | 文書運用、plan / gate、Windows 運用、参照先一覧、refresh target 群の具体運用 |

## 章別対応提案

| AGENTS.md 章 | 章の役割 | 推奨扱い | 対応 skill 案 | コメント |
| --- | --- | --- | --- | --- |
| 0. 本文書の役割 | shared control file の境界定義 | shared 固定 | `governance-manager` | skill 化せず、憲法として固定 |
| 1. 原則 | 文体、言語、命名、正本参照順 | shared + 一部 skill | `writing-normalizer`, `project-registry-manager`, `document-control-manager`, `canonical-naming-steward` | naming と正本参照順は具体運用が重いため分離余地あり |
| 2. 全体構成 | receipt → invoke → planner → execution → response | shared 固定 | `receipt-manager`, `l0-001-skill-invoke`, `l1-001-skill-plan`, `response-manager` | 骨格は shared に残す |
| 3. 強制順序 | 実行順の不変条件 | shared 固定 | `l1-001-skill-plan`, `l1-009-write-boundary-guard` | ルールは shared、監視は skill |
| 4. receipt-manager 規則 | prompt 完全読取と解釈 | 既存 skill 維持 | `receipt-manager` | 粒度は妥当 |
| 5. l0-001-skill-invoke 規則 | skill 集合決定、read set 決定 | 分割推奨 | `l0-001-skill-invoke`, `l1-006-rule-snapshot-read`, `l1-007-authoritative-doc-scope-resolve`, `skill-opportunity-*` | すでに大きい。`read_set` と `opportunity` は実質別責務 |
| 6. l1-001-skill-plan 規則 | phase、handoff、close 条件 | 分割推奨 | `l1-001-skill-plan`, `l1-004-task-scope-split`, `l1-005-close-condition-define`, `l1-002-phase-task-orchestrate` | planner 本体を薄くするのがよい |
| 7. response-manager 規則 | 応答整形のみ | 既存 skill 維持 | `response-manager`, `writing-normalizer` | 粒度は妥当 |
| 8. 文書運用 | truth / plan / evidence / closeout の正本運用 | 強く skill 化推奨 | `document-control-manager`, `project-truth-maintainer`, `current-state-syncer`, `evidence-trace-manager`, `runbook-pair-sync-enforcer` | 現プロジェクト文書を見る限り最も不足 |
| 9. ディレクトリ構造 | root-db / root-skills / root-tree の位置づけ | shared + skill | `workspace-structure-manager` | ルールは shared、変更判断は skill |
| 10. directory 統制 | category、tmp、tree 編集禁止 | shared + skill | `workspace-structure-manager`, `l1-009-write-boundary-guard` | 妥当 |
| 11. plan / gate 規則 | MRL / mRL / INITL / visible target | 再編強推奨 | `plan-gate-manager`, `mrl-ledger-maintainer`, `bdd-tdd-ledger-maintainer`, `current-state-syncer` | 1 skill に詰めすぎ |
| 12. 実装原則 | BDD / TDD / trace / blocker | 再編推奨 | `implementation-quality-manager`, `bdd-tdd-ledger-maintainer`, `evidence-trace-manager` | test と trace は別責務に近い |
| 13. branch / git hygiene | git 運用 | 既存 skill 維持 | `git-hygiene-manager` | 粒度は妥当 |
| 14. access / safety | write root と外部書込禁止 | shared + skill | `access-safety-manager`, `l1-009-write-boundary-guard` | shared に残す比率高めでよい |
| 15. 協調規則 | AI / 人の責務分担 | shared + skill | `collaboration-decision-manager` | 粒度は妥当 |
| 16. 研究方法 | 継続探索、再開、再読込 | 再編候補 | `research-execution-manager`, `current-state-syncer` | 再開導線は plan 文書側の運用と強く結びつく |
| 17. Windows 運用 | Windows 手順、tree sync、再生成 | skill 化推奨 | `windows-ops-manager`, `runbook-pair-sync-enforcer` | Windows 実手順は md に残しすぎない方がよい |
| 18. 参照先一覧 | 上位文書・関連 skill 参照面 | skill 化推奨 | `document-control-manager`, `l2a-002-reference-rewire-operate` | 静的一覧より自動整合の方が重要 |
| 19. refresh target skill | 目標 manager 群の一覧 | 再編前提 | 各 target manager + 新設 skill 群 | 現行 project 運用に対して不足あり |
| 20. skill 作成時の共通記載項目 | skill 雛形 | 既存 skill 維持 | `governance-manager`, `document-control-manager` | これは shared に残してよい |
| 21. 禁止事項 | 横断禁止 | shared 固定 | 各 guard skill | 憲法として残す |
| 22. 更新情報 | 変更履歴運用 | skill 化推奨 | `document-control-manager` | 履歴同期は skill 化しやすい |

## `project-truth-core.md` と照らした不足

| `project-truth-core.md` 章 | 実際の運用責務 | 受け皿として必要な skill |
| --- | --- | --- |
| 最終目的 / 最小構成 / レビュー価値仮説 | product truth の保持 | `project-truth-maintainer` |
| 前提 / システム対象 / 段階構造 | truth と plan の境界維持 | `project-truth-maintainer`, `current-state-syncer` |
| 開発原則 / スマホ側 data 抽出根拠 | canonical input / route の固定 | `artifact-contract-steward`, `canonical-naming-steward` |
| artifact 契約 | `SessionPackage` などの契約維持 | `artifact-contract-steward` |
| 外部境界 / remote modeling / route 比較 | runbook 契約、比較運用 | `runbook-pair-sync-enforcer`, `artifact-contract-steward` |
| UX 原則 / ネーミング | UX 北極星と canonical naming 維持 | `canonical-naming-steward`, `writing-normalizer` |

## `realtime-compass-and-status.md` と照らした不足

| `realtime-compass-and-status.md` 章 | 実際の運用責務 | 受け皿として必要な skill |
| --- | --- | --- |
| current_state | 現在地の正本管理 | `current-state-syncer` |
| 疑問点不整合一覧 | blocker / open issue 台帳 | `current-state-syncer`, `plan-gate-manager` |
| project 固有 decision 要約 | 採用 decision の昇格 | `project-truth-maintainer`, `document-control-manager` |
| 次の一手 | next action を 1 件へ収束 | `current-state-syncer`, `l1-001-skill-plan` |
| BDD | 提供価値と behavior の正本 | `bdd-tdd-ledger-maintainer` |
| TDD | task / evidence / status 台帳 | `bdd-tdd-ledger-maintainer`, `evidence-trace-manager` |
| script 一覧表 | source inventory と docs 対応 | `runbook-pair-sync-enforcer`, `document-control-manager` |
| Increpose Path Handoff Matrix | path contract の authoritative 管理 | `artifact-contract-steward` |
| Main Release Line 対応表 | gate の正本運用 | `mrl-ledger-maintainer` |

## 新設推奨 skill

| skill 名 | 目的 | 主入力 | 主出力 | 既存 skill との差 |
| --- | --- | --- | --- | --- |
| `project-truth-maintainer` | project truth 正本の更新境界を守る | project truth, decision | 更新差分, truth 反映 | `document-control-manager` より truth 特化 |
| `current-state-syncer` | current / next action / blocker を同期する | status 文書, worklog, evidence | 現在地更新 | `plan-gate-manager` より current 特化 |
| `mrl-ledger-maintainer` | MRL / mRL 台帳と gate 状態を管理する | BDD/TDD/status/evidence | gate table 更新 | `plan-gate-manager` を分割 |
| `bdd-tdd-ledger-maintainer` | BDD / TDD / acceptance / task 対応を維持する | BDD/TDD sections | 対応表更新 | 実装原則から独立 |
| `artifact-contract-steward` | artifact / path / handoff contract を守る | contract sections, inventories | contract diff, update | 現状不足が大きい |
| `canonical-naming-steward` | canonical / alias / legacy の整理 | naming, route compare, docs | naming decision | `project-registry-manager` より project 内 canonical 用 |
| `runbook-pair-sync-enforcer` | `.md` / `.ipynb` / source inventory 同期 | runbook pair, source tables | sync update, mismatch report | `l2b-002-script-doc-sync-enforce` より runbook 特化 |

## 再編推奨

| 現行 skill / manager | 問題 | 再編案 |
| --- | --- | --- |
| `l0-001-skill-invoke` | read set 判定と opportunity loop が混在 | invoke 本体と opportunity 系の境界を明文化 |
| `l1-001-skill-plan` | close 条件、phase、next action 集約が重い | `current-state-syncer` と `mrl-ledger-maintainer` を分離 |
| `document-control-manager` | truth / current / evidence / history を抱えすぎ | truth / current / contract / history に分割 |
| `plan-gate-manager` | MRL、BDD、TDD、gate、疑問点を一括管理 | `mrl-ledger-maintainer` と `bdd-tdd-ledger-maintainer` を分離 |
| `worklog-runtime-manager` | runtime と worklog promotion が別性質 | `runbook-pair-sync-enforcer` と runtime 系へ分離 |

## ここまでの提案の使い方

1. `AGENTS.md` は shared 原則だけを残す。
2. project 運用で肥大化している truth / current / gate / contract は専用 skill に降ろす。
3. `refresh target skill` 一覧は、実運用で必要な skill 群へ置換する。
4. 章ごとの責務が 1 skill 1責務に近づくまで分割する。
