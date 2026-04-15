# skill name rule

## 正式ID

| 要素 | ルール |
| --- | --- |
| 形式 | `<layer>-<serial>-<short_function_name>` |
| `layer` | `l0` / `l1` / `l2a` / `l2b` / `l3` / `lt` のみ使用可 |
| `serial` 採番単位 | `layer` ごとに独立連番 |
| `serial` 桁数 | `001` 始まりの 3 桁固定 |
| `serial` 意味 | 識別用 ID であり、実行順・遷移順を意味しない |
| `serial` 採番基準 | 新規登録時に、その `layer` 内の未使用最大番号 + 1 を付与 |
| 欠番 | 許可 |
| 再利用 | 禁止 |
| 廃止時 | `serial` は欠番化または `retired` / `deprecated` 扱いで保持し、再割当しない |
| `short_function_name` | repo 内で重複禁止 |
| `short_function_name` 文字種 | 小文字英数字 + `-` のみ |
| `short_function_name` 語順 | 対象 → 動作 → 必要時のみ補足 |
| `short_function_name` 禁止 | 曖昧語・一時語・状態語は禁止 |
| 改名 | 原則 `short_function_name` のみ可。`layer` と `serial` は固定 |
| 一意性 | 正式ID全体 `<layer>-<serial>-<short_function_name>` で一意 |
| planner 関係 | skill 自身は遷移先を定義しない。実行順は planner が管理する |

## 禁止語例

- `helper`
- `misc`
- `temp`
- `final`
- `new`

## 実例

| 用途 | 例 |
| --- | --- |
| admin リクエスト受付 | `l0-001-admin-request-receive` |
| リクエスト解析 | `l1-001-request-parse` |
| リクエスト分類 | `l1-002-request-classify` |
| BDD 作成 | `l2a-001-bdd-create` |
| release line 構築 | `l2a-002-release-line-build` |
| 表整形支援 | `l2b-001-table-normalize` |
| 命名統一支援 | `l2b-002-name-standardize` |
| レスポンス整形 | `l3-001-response-shape` |
| skill 棚卸し | `lt-001-skill-inventory` |
