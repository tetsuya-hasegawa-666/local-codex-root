<order>

# AGENTS.md
- 役割名: `Shared Governance Core`
- 目的: shared rule を軽量に保ち、実行詳細を skill / script / reference で分離しつつ実行内容の詳細指示をすることで、再現性の高い agent work を強制し、人による可読性と拡張性、補修性、トレーサビリティを容易化すること

## 0. 本文書の役割

| 項目 | 内容 | 実行担当 skill |
| --- | --- | --- |
| 文書の位置づけ | `local-codex-root/` 配下全体に効く最上位 shared control file | - |
| 本文書に置くもの | 本文書を含む Governance 全体構造<br>各文書の責務境界<br>Governance を維持する上で強制される実行順序<br>Governance を維持する上での禁止事項<br>Governance を維持する観点で必要な文書運用指針<br>Governance 維持を目指す上での現状の directory 運用と、gate 運用と、branch 運用、および共通注意点 | - |
| 本文書に置かないもの | Governance の領域を超えており、プロンプト毎、プロジェクト毎に設定定義されるべきのプロンプトやプロジェクト毎に適用方法を変えるべき詳細的内容<br>例） 手順、分岐、判定表、具体例、実装、script 本体、reference matrix 等 | - |
| 詳細の置き場 | `root-skills/<skill>/scripts/` と `references/`、関連運用文書 | `l2a-010-skill-build` |
| 編集保護 | `<order>` と `</order>` の間は admin 専用編集領域。最優先で保護する | `l1-009-write-boundary-guard` |

## 1. 原則

| 項目 | 内容 | 実行担当 skill |
| --- | --- | --- |
| 目的 | admin が 有益な software の社会実装を目標に、Codex のエージェント群を senior software / UX engineer として活用するため、 admin の意図(インサイト含む)に沿った振る舞いを実現する AI エージェント 開発を実施可能にすること、およびその手法を可視化すること | - |
| 文体 | 文字数当たりの情報量が最大になることを優先し、人が読みやすさを確保しつつ、誤解のない一意な表現の選択や表現方法で整理した上で表示すること | `l2a-005-documentation-watchkeep` |
| 言語 | 日本語を基本とする<br>識別子、command、path、API 名、service 名、英字略語など表現として日本語以外が適切な時は部分的に使用可とするが、()書きで日本語の訳を必ず付加すること | `l2a-005-documentation-watchkeep` |
| 文字コード | 日本語文書は UTF-8 を前提とすること | `l2a-005-documentation-watchkeep` |
| 命名 | file 名は半角英数字とコードやプログラムの中で混乱しにくい半角記号以外は使用禁止 | `l2a-005-documentation-watchkeep` |
| skill 命名 | skill の正式IDは `<layer>-<serial>-<short_function_name>` を強制する。`layer` は `l0` / `l1` / `l2a` / `l2b` / `l3` / `lt` だけを使い、`serial` は layer ごとに独立した 3 桁固定 ID とし、順序意味を持たせず再利用しない | `lt-001-skill-name-standardize` |
| skill 命名の不変条件 | 改名は原則 `short_function_name` だけに限定し、`layer` と `serial` は固定する。`short_function_name` は repo 内で一意の小文字英数字 + `-` だけを使い、曖昧語や一時語を禁止する | `lt-001-skill-name-standardize` |
| 正本参照順 | 上位から `AGENTS.md` / `agents.md` / project truth 正本 / 統合計画書 | `l1-006-rule-snapshot-read` |
| shared / project 分離 | shared rule は `AGENTS.md`、project 固有事項は project 正本へ置く | `l2a-006-project-truth-boundary-keep` |
| shared rule の表現粒度 | `AGENTS.md` は shared governance を定性的表現でだけ定義する。固定 section 構成、列定義、詳細手順、判定表、具体 template は対応 skill / reference へ置く | `l2a-006-project-truth-boundary-keep` |
| AGENTS の位置づけ | `AGENTS.md` は ruling と参照元であり、配下文書へ即時の実行命令を強要する文書ではなく、shared governance と文書構造の事実を記述する | `l2a-006-project-truth-boundary-keep` |
| skill 明示と起動分離 | `AGENTS.md` や参照先文書に skill 名が明示されていても、その記載自体は即時起動命令を意味しない。skill は常に起動 rule と `l0-001-skill-invoke` の判定に従って使う | `l0-001-skill-invoke` |
| 発火不整合の是正 | 実際の起動状態が本書の記述や起動 rule と食い違う時は、起動発火 flow の問題として即時に扱う。Codex は可能なら自動修正し、困難時は admin に相談し、是正内容を admin へ通知する | `l0-001-skill-invoke`<br>`l1-008-rule-diff-clarify`<br>`lt-005-skill-opportunity-integrate` |
| 補助文書制約 | `README.md` `index.md` は原則禁止。必要時のみ用途明示 | `l2a-005-documentation-watchkeep` |

## 2. 全体構成

| 層 | 名称 | 主責務 | 入力 | 出力 | 実行担当 skill |
| --- | --- | --- | --- | --- | --- |
| 入口前段 | `l0-002-request-intake` | prompt 全受領、要求解釈、暗黙要求推論、制約抽出 | admin prompt | 解釈済み要求 | `l0-002-request-intake` |
| 統合入口 | `l0-001-skill-invoke` | 必要 skill 集合の確定、読込下限決定 | 解釈済み要求 | 確定 skill 集合 | `l0-001-skill-invoke` |
| 順序管理 | `l1-001-skill-plan` | 順序、phase、完了条件、closeout 点の管理 | 確定 skill 集合 | 実行計画 | `l1-001-skill-plan` |
| 実処理 | 実行 skill 群 | 個別処理 | 実行計画 | skill 結果 | task ごとの specialist skill |
| 出口後段 | `l3-001-response-shape` | 回答整形、粒度調整、形式整形 | 解釈済み要求 + skill 結果 | admin 向け応答 | `l3-001-response-shape` |

## 3. 強制順序

| 順序 | 必須 | 規則 | 実行担当 skill |
| --- | --- | --- | --- |
| 1 | 必須 | prompt 受領後は必ず `l0-002-request-intake` が最初に動作する | `l0-002-request-intake` |
| 2 | 必須 | `l0-002-request-intake` 出力を受けて `l0-001-skill-invoke` が動作する | `l0-002-request-intake`<br>`l0-001-skill-invoke` |
| 3 | 必須 | `l0-001-skill-invoke` が確定した skill 集合だけを `l1-001-skill-plan` が扱う | `l0-001-skill-invoke`<br>`l1-001-skill-plan` |
| 4 | 必須 | 実行 skill は `l1-001-skill-plan` の順序に従って動作する | `l1-001-skill-plan` |
| 5 | 必須 | 最後に `l3-001-response-shape` が結果を整形する | `l3-001-response-shape` |
| 6 | 禁止 | 実行 skill を `l0-002-request-intake` `l0-001-skill-invoke` `l1-001-skill-plan` を経由せず起動してはならない | `l0-001-skill-invoke` |
| 7 | 禁止 | `l3-001-response-shape` を中間処理として使ってはならない | `l3-001-response-shape` |

## 4. l0-002-request-intake 規則

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 受領範囲 | prompt を 100% review する | `l0-002-request-intake` |
| 部分読取 | 禁止。prompt の一部だけを見て解釈してはならない | `l0-002-request-intake` |
| 解釈対象 | 明示要求、暗黙要求、制約、期待形式、粒度、比較軸、禁止事項、継続文脈 | `l0-002-request-intake` |
| 文脈反映 | 継続中の運用規則、命名規則、表形式希望、既存方針を反映する | `l0-002-request-intake` |
| 標準出力 | `prompt_full` `explicit_requests` `implicit_requests` `constraints` `expected_output` `task_type` `interpretation` `insight` `handoff_to` を持つ | `l0-002-request-intake` |
| 役割 | 解釈精度の向上。実行しない。skill 選定しない | `l0-002-request-intake` |
| 不足時 | まず最善解釈を作り、不足は構造化して明示する | `l0-002-request-intake` |
| handoff | `l0-001-skill-invoke` へ引き渡す | `l0-002-request-intake`<br>`l0-001-skill-invoke` |

## 5. l0-001-skill-invoke 規則

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 役割 | 全 skill の唯一の統合起動入口 | `l0-001-skill-invoke` |
| 入力前提 | `l0-002-request-intake` が生成した解釈済み要求を入力とし、raw prompt の再解釈を主責務にしない | `l0-001-skill-invoke` |
| 主責務 | 必要 skill 集合、読込下限、後回し skill、起動不能 skill を確定する | `l0-001-skill-invoke` |
| mark 解釈 | admin mark がある時はここで反映する | `l0-001-skill-invoke` |
| read_set | 先に読むべき正本 / reference の最小集合を決める | `l0-001-skill-invoke` |
| 常時並走 | 表向きの応答主線とは別に、`lt-002-skill-opportunity-scout` と `lt-003-skill-opportunity-ledger` を常時 backloop として回し、skill 化候補の抽出と台帳追記を行う | `l0-001-skill-invoke`<br>`lt-002-skill-opportunity-scout`<br>`lt-003-skill-opportunity-ledger` |
| `Go` 後導線 | admin が `Go` を出した時は `lt-004-skill-opportunity-architect` と `lt-005-skill-opportunity-integrate` へ handoff し、既存 merge / 新規 skill 化 / 発火連携まで進める | `l0-001-skill-invoke`<br>`lt-004-skill-opportunity-architect`<br>`lt-005-skill-opportunity-integrate` |
| 禁止 | 実行順設計、応答整形、正本文書書直接編集 | `l0-001-skill-invoke` |
| handoff | `l1-001-skill-plan` へ渡す | `l0-001-skill-invoke`<br>`l1-001-skill-plan` |

## 6. l1-001-skill-plan 規則

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 役割 | 確定済み skill 集合の発火、順序、phase、handoff、close 条件を管理する | `l1-001-skill-plan` |
| 追加削除 | `l0-001-skill-invoke` が確定した skill 集合を勝手に増減しない | `l1-001-skill-plan` |
| phase | 必要時は `Phase 1: authoritative context`、`Phase 2: 設計`、`Phase 3: 編集`、`Phase 4: probe / test / link check`、`Phase 5: evidence / closeout` を明示する | `l1-001-skill-plan`<br>`l1-002-phase-task-orchestrate` |
| 省略制限 | 局所 task でも `Phase 1` と `Phase 4` は無言で飛ばさない | `l1-001-skill-plan`<br>`l1-002-phase-task-orchestrate` |
| handoff | specialist skill に `Goal` `Authoritative` `Working files` `Do not treat as truth` `Close condition` を渡す | `l1-001-skill-plan` |

## 7. l3-001-response-shape 規則

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 役割 | admin 向け応答の整形だけを担当する | `l3-001-response-shape` |
| 禁止 | 事実改変、未実施事項の実施済み表現、skill 選定のやり直し | `l3-001-response-shape` |
| 整形対象 | 粒度、順序、箇条書き、表、結論、残件、確認依頼 | `l3-001-response-shape` |
| 不足明示 | 未確定事項、前提不足、保留点を残したまま見えなくしない | `l3-001-response-shape` |
| 余剰除去 | 解釈要求から外れた冗長説明を削るが、事実は曲げない | `l3-001-response-shape` |
| 根拠 | `l0-002-request-intake` の解釈と skill 結果だけを使う | `l3-001-response-shape` |

## 8. 文書運用

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 最上位 shared control file | `AGENTS.md` | - |
| directory rule file | 各階層の `agents.md` | - |
| project truth | project 固有の目的、完成判定、利用入口、UX 原則、段階構造、責務境界のような定性的 truth | `l2a-006-project-truth-boundary-keep` |
| project truth の構成 rule | `文書の役割` の具体構成、canonical 要素一覧、section 設計、detail な書き分け方は `l2a-006-project-truth-boundary-keep` が管理し、`AGENTS.md` には定性的原則だけを置く | `l2a-006-project-truth-boundary-keep` |
| skill 命名の詳細 rule | layer ごとの採番、欠番、禁止語、語順、例、planner 関係の detail は `lt-001-skill-name-standardize` が管理する | `lt-001-skill-name-standardize` |
| 統合計画書 | `current_state`、BDD、TDD、`MRL` / `mRL` / `INITL` 進行管理 | `l2a-003-delivery-plan-keep` |
| admin 手順正本 | 人が実際に操作する手順と判断基準 | `l2a-009-test-evidence-record` |
| admin 証跡正本 | admin `UX check`、gate close 根拠 | `l2a-009-test-evidence-record` |
| closeout 正本 | gate 変化、issue、cause、resolution、再発防止、残課題 | `l2a-009-test-evidence-record` |
| shared worklog | 往復面。truth / plan / evidence の正本代替にしない | `l2b-009-log-promotable-facts-extract` |
| 更新原則 | 真実が変わった task と同じ task で正本を更新する | `l2a-005-documentation-watchkeep` |
| 文体 rule 変更時の追随 | shared な文体 rule を更新した時は、この文書自体の rule 文も同じ task で見直し、冗長、曖昧、重複、解釈分岐を残さない | `l2a-005-documentation-watchkeep` |
| skill test 記録先 | skill の機能確認テスト code と結果実体は `root-skills/auto-test-result/<skill-id>/` に置き、全体概要は `root-skills/auto-test-result.md` に集約する | `l2b-010-skill-function-test-run` |

## 9. ディレクトリ構造

| directory | 位置づけ | 実行担当 skill |
| --- | --- | --- |
| `local-codex-root/` | top directory。最上位運用正本は `AGENTS.md` | - |
| `root-db/` | project 方針、構想、経過、成果物の正規保持先 | `l2b-001-doc-target-resolve` |
| `root-skills/` | skill 正本とその `scripts/` `references/` | `l2a-010-skill-build` |
| `root-tree/` | junction による閲覧 tree。実データ copy を持たない | `l2a-004-runtime-operate` |
| `root-db/--devs/` | 計画、状態、証跡、test code、product 実装物、trace | `l2b-008-evidence-destination-resolve` |
| `root-db/--devs/--tgpce-map/` | truth / goal / plan / current / evidence-map 集約 | `l2a-003-delivery-plan-keep` |
| `root-db/--devs/--testlogs/` | 記録、要約、manifest 等 | `l2a-009-test-evidence-record` |
| `root-db/--exsams/` | raw 生成物、一時調査出力、tmp 類 | `l2b-008-evidence-destination-resolve` |

## 10. directory 統制

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| `--` category | shared structure。Codex 判断で新設しない | `l1-009-write-boundary-guard` |
| 新規迂回 path | rule 外 category を出力先として作らない | `l1-009-write-boundary-guard`<br>`l2b-003-path-contract-scan` |
| 一時出力 | `--exsams/` 外に残さない | `l2b-008-evidence-destination-resolve` |
| tree 編集 | `root-tree/` を直接編集しない | `l1-009-write-boundary-guard` |
| 正本編集 | 常に `root-db/` 側の正本で編集する | `l2b-001-doc-target-resolve` |

## 11. plan / gate 規則

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 管理単位 | 到達段階は `MRL` / `mRL`、準備 UX は `INITL` / `mINITL` | `l2a-003-delivery-plan-keep` |
| gate 状態語 | `ready` `active` `p-done` `i-pass` | `l2a-003-delivery-plan-keep` |
| 疑問点管理 | `current_state` 冒頭に `疑問点不整合一覧` を置く | `l2a-003-delivery-plan-keep` |
| admin 状態語 | `big-open` `small-open` `close` `no judge` | `l2a-003-delivery-plan-keep` |
| 根拠記録 | `p-done` `i-pass` 根拠は統合計画書または証跡正本へ残す | `l2a-009-test-evidence-record` |
| visible target | 直近 target は番号付き `MRL` / `mRL` で置く | `l2a-003-delivery-plan-keep` |
| 準備 UX | `INITL` は behavior 本体に混ぜず別管理する | `l2a-003-delivery-plan-keep` |

## 12. 実装原則

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| BDD | terminal behavior は観測可能な振る舞いで書く | `l2a-003-delivery-plan-keep` |
| TDD | 自動検証できる変更は fail する test を先に置く | `l2b-010-skill-function-test-run` |
| refactor | green 後、visible behavior を壊さない範囲で行う | - |
| trace | 完了した挙動は docs / plan / evidence のいずれかへ trace を残す | `l2a-009-test-evidence-record` |
| mock 制約 | mock / stub / sample / 説明用接続は本機能 `i-pass` 根拠にしない | `l2a-009-test-evidence-record` |
| warning | 注意喚起であり、単独では停止条件にしない | `l1-008-rule-diff-clarify` |
| blocker | file 不在、contract 不成立、実行時例外など実行不能時のみ停止条件 | `l1-008-rule-diff-clarify` |

## 13. branch / git hygiene

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 基準 branch | 人間向け `dev`、Codex 向け `codex/dev` | `l2a-004-runtime-operate` |
| 通常 push 先 | Codex は通常 `codex/dev` | `l2a-004-runtime-operate` |
| 人間指示時 | `push` 指示があれば原則 `dev` に反映 | `l2a-004-runtime-operate` |
| topic branch | 必要時のみ `codex/<topic>` | `l2a-004-runtime-operate` |
| 直列実行 | `git add` `commit` `push` 移動 削除 rename は直列 | `l2a-004-runtime-operate` |
| push 後確認 | `git status` で working tree 空確認 | `l2a-004-runtime-operate` |
| 非commit対象 | build output、cache、tmp、dump、capture、`__pycache__` 等 | `l2a-004-runtime-operate` |
| 大容量 | `100MB` 超 file は repository 管理対象に入れない | `l2b-008-evidence-destination-resolve` |
| stage | 原則として明示 path | `l2a-004-runtime-operate` |

## 14. access / safety

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| workspace 外 access | `READ` のみ許可 | `l1-009-write-boundary-guard` |
| `WRITE` 許可 root | admin がその task の基準として明示した `AGENTS.md` のある directory とその配下のみ | `l1-009-write-boundary-guard` |
| 現在の `WRITE` root | `C:\Users\tetsuya\local-codex-root\AGENTS.md` がある `C:\Users\tetsuya\local-codex-root\` | `l1-009-write-boundary-guard` |
| 非 READ | `WRITE` root 外では、作成、編集、移動、削除、rename、出力、cache 生成、skill 配置変更を禁止 | `l1-009-write-boundary-guard` |
| 外部情報 | 参照後に current root 正本へ吸収し、外部自体は変更しない | `l1-009-write-boundary-guard`<br>`l2b-001-doc-target-resolve` |
| 情報削減 | 根拠なく削減しない | `l1-008-rule-diff-clarify` |
| 未解決 | user 明示指示なく消さない | `l1-008-rule-diff-clarify` |

## 15. 協調規則

| 項目 | 内容 | 実行担当 skill |
| --- | --- | --- |
| AI の役割 | 調査、仮説生成、設計提案、実装支援、文書更新、影響確認 | - |
| 人間の役割 | 価値判断、優先順位付け、不可逆な選択、最終承認 | - |
| 記録昇格 | shared は `AGENTS.md`、project 固有は project 正本へ昇格 | `l2a-005-documentation-watchkeep`<br>`l2a-006-project-truth-boundary-keep` |
| 人間依頼 | 小さく、拒否されても全体計画が崩れない単位 | `l1-005-close-condition-define` |
| 可逆 / 不可逆 | 可逆は AI が進めてよい。不逆は人間承認が必要 | `l1-005-close-condition-define` |
| decision 記録 | 重要判断は決まった時点で記録 | `l2a-009-test-evidence-record` |
| rule 文の表現 | 意味を変えずに短く、一義で、誤解なく読める形を優先する | `l2a-005-documentation-watchkeep` |

## 16. 研究方法

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 研究スタンス | AI は人間の取得能力を無制限と仮定しない | `l2a-007-frontier-research-curate` |
| 継続探索 | 問題探索 → 要因推定 → 課題仮説 → 解決 を反復する | `l2a-007-frontier-research-curate` |
| 自律範囲 | 可逆で短時間に戻せる範囲は Codex 判断で進める | `l1-005-close-condition-define` |
| 再開 | `再開してください` は現在の正本と実装状態から再開要求として扱う | `l1-006-rule-snapshot-read` |
| 再読込 | セッション最初、または前回から 6 時間以上空いた時は正本群を再読込 | `l1-006-rule-snapshot-read` |
| 矛盾発見時 | 作業継続しつつ shared または project 正本を更新する | `l1-008-rule-diff-clarify`<br>`l2a-005-documentation-watchkeep` |
| 最短経路 | 実検証へ近づく最短経路を優先する | `l1-005-close-condition-define` |

## 17. Windows 運用

| 項目 | 規則 | 実行担当 skill |
| --- | --- | --- |
| 位置づけ | Windows 前提の再現可能手順の単一参照面 | `l2a-004-runtime-operate` |
| 記録原則 | Windows ベース手順は chat に散在させず正本文書書へ昇格 | `l2a-004-runtime-operate`<br>`l2a-005-documentation-watchkeep` |
| tree sync | `root-tree/` 配下の公式 script を使う | `l2a-004-runtime-operate` |
| 再生成 | build 正本に従い配布用実行物を再生成する | `l2a-004-runtime-operate` |

## 18. 参照先一覧

| 主題 | 参照先 | 実行担当 skill |
| --- | --- | --- |
| 入口設計 | `root-skills/kisaragi_skill_trigger_system_map.md` | `l0-001-skill-invoke` |
| 全体提案 | `root-skills/kisaragi_context_skill_governance_proposal.md` | `l2a-005-documentation-watchkeep` |
| pilot skill 設計 | `root-skills/kisaragi_pilot_skill_spec.md` | `l2a-010-skill-build` |
| skill 配置 | `root-skills/agents.md` | `l2a-010-skill-build` |
| 軽量化方針 | `root-skills/kisaragi_upper_document_lightweighting_proposal.md` | `l2a-005-documentation-watchkeep` |
| skill 化候補台帳 | `root-skills/lt-003-skill-opportunity-ledger/references/skill-opportunity-proposals.md` | `lt-003-skill-opportunity-ledger` |

## 19. refresh target skill

| No. | skill 名 | 役割 | 実体 skill |
| --- | --- | --- | --- |
| 1 | `l0-002-request-intake` | prompt 全受領、要求解釈、暗黙要求推論 | `l0-002-request-intake` |
| 2 | `l0-001-skill-invoke` | skill 集合確定、読込下限決定 | `l0-001-skill-invoke` |
| 3 | `l1-001-skill-plan` | 実行順、phase、close 条件 | `l1-001-skill-plan` |
| 4 | `l3-001-response-shape` | 応答整形 | `l3-001-response-shape` |
| 5 | `governance-manager` | shared rule、構造変更、承認要否 | - |
| 6 | `document-control-manager` | 正本判定、配置、履歴、pointer | - |
| 7 | `writing-normalizer` | 文体圧縮、表化、日本語基調 | - |
| 8 | `workspace-structure-manager` | directory 構造、保管先、raw / temp 整理 | - |
| 9 | `project-registry-manager` | project 名、code、artifact 命名 | - |
| 10 | `plan-gate-manager` | BDD / TDD / gate / closeout | - |
| 11 | `implementation-quality-manager` | code / test / trace / warning-blocker 整理 | - |
| 12 | `worklog-runtime-manager` | shared worklog、runbook、bootstrap、pair 同期 | - |
| 13 | `git-hygiene-manager` | branch、stage、commit / push hygiene | - |
| 14 | `access-safety-manager` | workspace 外 access、安全境界、削除抑止 | `l1-009-write-boundary-guard` |
| 15 | `collaboration-decision-manager` | 可逆 / 不可逆、承認依頼、decision 記録 | - |
| 16 | `research-execution-manager` | 継続探索、再開、再読込、矛盾処理 | - |
| 17 | `windows-ops-manager` | Windows 手順、tree sync、再生成運用 | - |
| 18 | `evidence-trace-manager` | evidence path、manifest、summary、close 根拠 | `l2a-009-test-evidence-record` |
| 19 | `l1-009-write-boundary-guard` | `READ` 以外の access 許可 root を確認 | `l1-009-write-boundary-guard` |
| 20 | `lt-002-skill-opportunity-scout` | prompt から skill 化候補を抽出 | `lt-002-skill-opportunity-scout` |
| 21 | `lt-003-skill-opportunity-ledger` | 候補台帳と更新履歴を追記 | `lt-003-skill-opportunity-ledger` |
| 22 | `lt-004-skill-opportunity-architect` | 既存 merge / 新規 skill を根拠付きで分類し、台帳下段と更新履歴を更新 | `lt-004-skill-opportunity-architect` |
| 23 | `lt-005-skill-opportunity-integrate` | admin `Go` 後に skill 実装と `AGENTS.md -> skill` 発火連携を更新 | `lt-005-skill-opportunity-integrate` |
| 24 | `l2a-010-skill-build` | skill の新規作成と既存 skill 変更を統制し、関連構成を同 task でそろえる | `l2a-010-skill-build` |
| 25 | `l2b-010-skill-function-test-run` | 各 skill の機能確認テストを作成、実行、評価し、必要機能を満たすか判定する | `l2b-010-skill-function-test-run` |

## 20. skill 作成時の共通記載項目

| 項目 | 内容 | 実行担当 skill |
| --- | --- | --- |
| 目的 | その skill が何を守るか | `l2a-010-skill-build` |
| 入力 | 受ける情報 | `l2a-010-skill-build` |
| 出力 | 返す情報 | `l2a-010-skill-build` |
| 非責務 | やらないこと | `l2a-010-skill-build` |
| 前提 | 起動前提 | `l2a-010-skill-build` |
| 参照 | 読むべき正本 / references | `l2a-010-skill-build` |
| close 条件 | どこまでやれば終了か | `l2a-010-skill-build` |
| 更新対象 | 更新すべき文書 | `l2a-010-skill-build` |
| 禁止 | その skill でやってはならないこと | `l2a-010-skill-build` |
| 機能確認テスト | その skill が取り持つ必要機能をどう test し、どう評価するか | `l2b-010-skill-function-test-run` |
| skill test 保存先 | test code 名、実行結果、対処内容を保存する path | `l2b-010-skill-function-test-run` |

## 21. 禁止事項

| 項目 | 禁止内容 | 実行担当 skill |
| --- | --- | --- |
| 部分読取 | prompt の一部だけを見て全体判断すること | - |
| 直起動 | `l0-002-request-intake` `l0-001-skill-invoke` `l1-001-skill-plan` を経由せず実行 skill を動かすこと | `l0-001-skill-invoke` |
| 無断追加 | `l1-001-skill-plan` が skill 集合を勝手に増減すること | `l1-001-skill-plan` |
| 事実改変 | `l3-001-response-shape` が未実施事項を実施済みのように返すこと | `l3-001-response-shape` |
| rule 混入 | project 固有事項を shared rule として固定すること | `l2a-006-project-truth-boundary-keep` |
| 未整理削除 | user 明示指示なく未整理 data や未解決項目を消すこと | `l1-009-write-boundary-guard` |
| 外部書込 | workspace 外へ `READ` 以外の access を行うこと | `l1-009-write-boundary-guard` |
| raw 混在 | raw 生成物や tmp を正規保管領域へ散在させること | `l2b-008-evidence-destination-resolve` |
| skill test 未実施 close | skill 作成・変更 task を、機能確認テスト未作成、未実行、未評価のまま閉じること | `l2b-010-skill-function-test-run` |

## 22. 更新情報

| 項目 | 内容 | 実行担当 skill |
| --- | --- | --- |
| 履歴本文書 | `AGENTSmd-RH.md` に置く | `l2a-005-documentation-watchkeep` |
| 本体末尾 | 履歴参照のみを置く | `l2a-005-documentation-watchkeep` |
| 更新原則 | shared rule 追加時は履歴文書も同 task で更新する | `l2a-005-documentation-watchkeep` |

- `AGENTS.md` の更新履歴は `AGENTSmd-RH.md` を参照する

</order>
