# skill opportunity proposals

## 上段 候補ログ

- この section は append-only とする。
- admin 手動削除または admin 明示指示が無い限り、既存 entry を削除しない。

### 2026-04-15 候補 `WRITE` 境界監視を独立 skill 化

- 概要: `READ` 以外の access を、admin が基準として示した `AGENTS.md` directory とその配下だけに限定して確認する。
- 汎化理由: file 編集、生成物出力、skill 配置変更の前に毎回同じ確認が必要で、規則が機械的に判定しやすい。

### 2026-04-15 候補 skill 化候補の常時 backloop 監視

- 概要: prompt 処理中に、汎化して機械的に処理できそうな作業候補を抽出し、台帳へ追記し、admin へ短く提案する。
- 汎化理由: 候補抽出、台帳追記、分類、`Go` 後反映の 4 段は反復性が高く、main line と切り分けやすい。

## 下段 分類表

| 対象 skill 名 | 候補標題 | 既存 / 新規 | 反映方法詳細 | 根拠 | 状態 |
| --- | --- | --- | --- | --- | --- |
| `write-boundary-guard` | `WRITE` 境界監視を独立 skill 化 | `新規` | `skill-invoker` が `READ` 以外の access を検知した時に必須候補へ入れ、planner 前提へ固定する | safety 境界、`AGENTS.md` 連携、機械判定のしやすさが独立している | `反映済み` |
| `skill-opportunity-scout` | skill 化候補の常時 backloop 監視 | `新規` | `skill-invoker` の hidden backloop で every prompt 起動し、候補抽出だけを担当する | 候補抽出は main line から分離した反復作業で、独立責務がある | `反映済み` |
| `skill-opportunity-ledger` | skill 化候補の常時 backloop 監視 | `新規` | scout の結果を上段候補ログへ append し、同時に更新履歴へ記録する | append-only 台帳管理と履歴管理は独立責務として再利用しやすい | `反映済み` |
| `skill-opportunity-architect` | skill 化候補の常時 backloop 監視 | `新規` | 候補を既存 merge / 新規 skill に根拠付きで分類し、下段表と同じ更新履歴へ記録する | 分類と台帳下段更新は ledger 追記とは別責務であり、評価基準も必要 | `反映済み` |
| `skill-opportunity-integrator` | skill 化候補の常時 backloop 監視 | `新規` | admin `Go` 後に skill 実装と `AGENTS.md -> skill` 発火連携まで更新する | 実装と連携更新は architect の判断後フェーズで、別責務に分ける方が安全 | `反映済み` |
