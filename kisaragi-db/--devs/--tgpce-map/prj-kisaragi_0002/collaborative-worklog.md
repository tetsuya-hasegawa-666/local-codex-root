# collaborative-worklog.md
- 概案名: `Collaborative Worklog`

## 役割

- この file は、admin と Codex が notebook cell、script、error、観測結果を往復するための ring-buffer worklog とする。
- この file は `project-truth-core.md`、`realtime-compass-and-status.md`、`admin-ux-method.md` の代替ではない。
- durable fact は速やかに `project-truth-core.md` または `realtime-compass-and-status.md` へ昇格する。
- reference ownership は `documentation-watchkeeper` が持ち、持続価値のある記述を正本文書へ昇格する責務を持つ。

## 容量制限

- 本文は `50k` 文字を上限とする。
- 上限を超える前に、持続価値のある内容を正本へ昇格する。
- 昇格後は、固定 header を残しつつ古い本文を削除し、最新往復だけを保持する。
- old log を唯一の保持場所にしてはならない。

## 読み方

- 固定 header はこの節までとする。
- これより下は `# codex` または `# admin` 見出しによる時系列追記だけを置く。
- 正規読み順は「最下部から上へ」とする。

## 記載ルール

- 途中挿入、途中修正、本文中ほどへの要約追記を禁止する。
- 既存本文は原則として書き換えず、必ず最下部へ追記する。
- `# codex` の追記は、必ず単調増加の通し番号 `v**` を付ける。
- 長い code と error は code block のまま貼る。
- shared rule 変更は `AGENTS.md`、project truth / plan / gate / current / evidence 変更は `project-truth-core.md` と `realtime-compass-and-status.md` へ別途反映する。

# admin

```text
collaborative-worklog.md、については、この時点で、名称変更などが入っているため、過去の書き方をいまの書き方からreferenceしたら本文は削除して、このプロンプトを先頭に、バージョンNoは連番で継続するようにしてください
referenceは適切なskillが持ってください
```

# codex v132

- 現時点の file 名、正本名、参照面に合わせて header を現行化した。
- 過去本文は ring-buffer 運用へ合わせて削除し、この prompt を先頭の起点として再開する。
- version 連番は旧本文の最終 `v131` から継続し、この entry を `v132` とした。
- durable fact の保持先は `project-truth-core.md` と `realtime-compass-and-status.md`、reference ownership は `documentation-watchkeeper` とする。
