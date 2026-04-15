# kisaragi pilot skill spec

## 文書の目的

- refresh 主線の pilot として、最初に具体化する core skill を定義する。
- 対象は `receipt-manager`、`l0-001-skill-invoke`、`response-manager` とする。
- `l1-001-skill-plan` は既存実装を流用する前提で、pilot 文書では新規 3 skill の責務を先に固定する。

## 共通前提

- 正本は文書であり、skill は文書を置き換えない。
- project task の `READ` 下限は、常に project truth 正本と統合計画書とする。
- `receipt-manager -> l0-001-skill-invoke -> l1-001-skill-plan -> response-manager` の順序は固定する。
- specialist skill は自分で発火判断を持たず、`l0-001-skill-invoke` と `l1-001-skill-plan` の handoff を前提とする。
- `l0-001-skill-invoke` は表向きの統合入口であり、裏では `skill-opportunity-*` family を hidden backloop として常時回してよい。

## pilot skill 一覧

| skill | 主目的 | 位置づけ |
| --- | --- | --- |
| `receipt-manager` | prompt 全体の解釈を固定する | 常時入口前段 |
| `l0-001-skill-invoke` | 必要 skill 集合と読込下限を確定する | 常時統合入口 |
| `response-manager` | 最終応答を整形する | 常時出口後段 |

## skill 1. `receipt-manager`

### 目的

- prompt を部分読取せず全件 review する。
- 明示要求、暗黙要求、制約、禁止事項、期待形式を抽出する。
- 実行に入る前の解釈精度を固定する。

### 入力

- `prompt_full`
- 継続文脈
- admin mark

### 出力

- `explicit_requests`
- `implicit_requests`
- `constraints`
- `expected_output`
- `task_type`
- `interpretation`
- `handoff_to: l0-001-skill-invoke`

### 非責務

- skill 選定
- 実行順設計
- 文書や code の直接編集
- admin 向け最終応答の整形

## skill 2. `l0-001-skill-invoke`

### 目的

- `receipt-manager` の解釈結果から、必要 skill 集合を確定する。
- `read_set_minimum` と `deferred_skills` と `blocked_skills` を分離する。
- trigger ownership を一箇所に集約する。
- `READ` 以外の access では `l1-009-write-boundary-guard` を必須化する。
- `lt-002-skill-opportunity-scout` と `lt-003-skill-opportunity-ledger` を hidden backloop として毎 prompt で起動し、候補台帳を更新する。
- admin `Go` 後は `lt-004-skill-opportunity-architect` と `lt-005-skill-opportunity-integrate` を起動し、既存 merge / 新規 skill / 発火連携を更新する。

### 入力

- `receipt-manager` の出力
- 現在文脈
- 管理下の skill registry

### 出力

- `selected_skills`
- `deferred_skills`
- `blocked_skills`
- `read_set_minimum`
- `opportunity_note_for_response`
- `decision_log`
- `handoff_to: l1-001-skill-plan`

### 非責務

- 実行順設計
- 応答整形
- 正本文書直接編集

## skill 3. `response-manager`

### 目的

- `l1-001-skill-plan` と specialist skill の結果を admin 向けに整形する。
- 粒度、表現、箇条書き、要約順を整える。
- 未実施事項を実施済みに見せない。

### 入力

- `receipt-manager` の解釈結果
- `l1-001-skill-plan` の実行結果
- specialist skill の結果

### 出力

- admin 向け応答本文
- 残件
- 必要時の確認依頼

### 非責務

- skill 選定や再選定
- 事実改変
- 直接編集

## `l1-001-skill-plan` との関係

- `l1-001-skill-plan` は既存の orchestration owner として維持する。
- `l1-001-skill-plan` は `l0-001-skill-invoke` が確定した集合だけを扱う。
- `l1-001-skill-plan` は skill 集合の追加削除を行わない。

## 次段で決めること

1. 現行単一入口をどの段階で `receipt-manager` と `l0-001-skill-invoke` へ分解するか。
2. `response-manager` を独立 skill として実装するか、応答整形 helper から始めるか。
3. `read_set_minimum` の schema をどこに置くか。
4. 既存 specialist skill の handoff packet を新主線にどう合わせるか。
