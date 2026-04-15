# project truth role pattern

## shared rule として `AGENTS.md` に置くもの

- project truth が project 固有の定性的 truth を保持する、という原則
- current / gate / evidence との ownership 境界
- `AGENTS.md` 自身は定性的原則だけを持ち、detail は skill / reference へ置く、という rule

## project truth に残す最小記述

- この文書が保持する truth の範囲
- 対になる current / gate 文書が持つ範囲
- active judgement は current 側に置き、adopted truth はこの文書へ戻す、という戻し先 rule

## skill / reference に逃がすもの

- `文書の役割` の固定 section 構成
- canonical 要素一覧
- 各要素の列定義
- detail な table template
- どの見出しに何を書くかの cookbook

## project truth 冒頭の最小 template

```md
## 文書の役割

- この文書は `<project-code>` の方向性、価値、責務境界、canonical 採用済み定義のような project 固有の定性的 truth を保持する。
- 定量的に追跡する current、gate、next action、evidence、履歴は `<current-doc>` が持つ。
- active な判断は `<current-doc>` に置き、採用済み定義はこの文書へ戻す。
- `文書の役割` の detail な構成 rule は `<skill-name>` に従う。
```
