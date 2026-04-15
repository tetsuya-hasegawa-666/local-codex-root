---
name: lt-001-skill-name-standardize
description: Define, review, and register skill names under the local-codex-root naming rule. Use when creating a new skill, renaming an existing skill, checking whether a skill ID is valid, deciding the next serial in a layer, or reviewing whether `short_function_name` is unique, precise, and allowed.
---

# Lt 001 Skill Name Standardize

skill 名を `<layer>-<serial>-<short_function_name>` の正式IDとして一貫運用する specialist とする。命名の骨格 rule は `AGENTS.md` に残し、採番、禁止語、例、rename 判定の detail はこの skill が管理する。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` が skill 名の layer / serial / `short_function_name` 命名、採番、rename、禁止語 review が主題だと判断した時だけ呼ばれる。

## 目的

- 新しい skill に衝突しない正式IDを与える。
- rename 時に変えてよい部分と固定すべき部分を守る。
- planner が実行順を管理し、skill 名に順序意味を持たせない rule を維持する。

## 入力

- 候補 skill 名
- 新規か改名かの別
- 想定 layer
- 既存 `kisaragi-skills/` 一覧
- admin が意図する機能の短い説明

## 出力

- 妥当な正式ID
- `layer` の妥当性判定
- 次に使うべき `serial`
- `short_function_name` の妥当性判定
- rename 可否の判断

## 非責務

- skill の実行順を決めること
- skill の内容そのものを設計すること
- planner の handoff を skill 名から推論して固定すること

## workflow

1. `references/skill-name-rule.md` を読む。
2. 新規 skill なら、指定 layer の既存 `serial` を確認し、未使用最大番号 + 1 を採用する。
3. 改名なら、`layer` と `serial` を固定し、`short_function_name` だけを見直す。
4. `short_function_name` が repo 内一意、小文字英数字 + `-` のみ、曖昧語・一時語禁止を満たすか確認する。
5. 正式ID全体の一意性を確認する。
6. 実行順は planner が管理し、skill 名に順序意味を持たせないことを明示する。

## close 条件

- 新規または改名対象に対して妥当な正式IDが提示済み
- `layer`、`serial`、`short_function_name` の rule 違反が無い
- rename 時に固定部を壊していない
- planner 関係の誤読が残っていない

## 参照

- `AGENTS.md`
- `kisaragi-skills/agents.md`
- `references/skill-name-rule.md`

## 更新対象

- 対象 skill directory 名
- `agents/openai.yaml`
- `kisaragi-skills/agents.md`
- 必要時の `AGENTS.md` と `AGENTSmd-RH.md`

## 禁止

- `serial` に実行順や依存順の意味を持たせること
- 廃止済み `serial` を再利用すること
- `helper`、`misc`、`temp`、`final`、`new` のような曖昧語を使うこと
