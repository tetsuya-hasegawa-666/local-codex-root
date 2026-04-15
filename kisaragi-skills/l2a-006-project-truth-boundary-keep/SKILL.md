---
name: l2a-006-project-truth-boundary-keep
description: Keep `AGENTS.md`, project truth documents, and current/gate documents aligned when deciding what belongs in shared governance versus project-specific truth. Use when editing `project-truth-core.md`, `project-truth.md`, or similar truth documents, especially for `文書の役割`, ownership boundaries, canonical element lists, or when moving structural detail out of truth docs into reusable skills or references.
---

# Project Truth Boundary Keeper

project truth の冒頭で shared rule と project 固有 truth が混ざり始めた時に、shared 側へ上げるもの、truth に残すもの、skill / reference へ逃がす detail を切り分ける specialist とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` と `l1-001-skill-plan` が、`AGENTS.md` と project truth の境界整理や truth 冒頭構成の整理が必要と判断した時だけ呼ばれる。

## 目的

- `AGENTS.md` には shared governance の定性的原則だけを残す。
- project truth には project 固有の定性的 truth だけを残す。
- 文書ごとの固定構成、canonical 要素の整理方法、冒頭 section の detail な書き方は reusable skill / reference へ寄せる。

## 入力

- 編集対象の `AGENTS.md`
- 対象 project truth
- 対になる current / gate 文書
- 既存 skill / reference の構造
- admin が追加したい rule、または project truth 冒頭に現れた新しい構成 detail

## 出力

- `AGENTS.md` に上げるべき定性的原則
- truth 文書に残すべき最小記述
- 新設または更新すべき skill / reference
- `l0-001-skill-invoke` に追加すべき trigger 条件

## 非責務

- project 固有の価値定義そのものを決めること
- current / gate / evidence の実データ更新内容を決めること
- `AGENTS.md` に詳細手順、列定義、長い template を直書きすること

## 判断原則

1. その内容が複数 project に再利用される governance rule なら `AGENTS.md` へ上げる。
2. その内容が 1 project の方向性、価値、責務境界なら project truth に残す。
3. その内容が section 構成、列定義、canonical 要素一覧、冒頭 template、判定順のような reusable detail なら skill / reference へ寄せる。
4. `AGENTS.md` には detail を入れず、何を守る rule かだけを定性的に書く。
5. project truth には「この文書は何を保持するか」「対になる文書が何を持つか」だけを短く残し、detail な構成法は参照先 skill に委ねる。

## workflow

1. 対象 truth 冒頭に shared rule が混入していないか確認する。
2. shared rule なら `AGENTS.md` に 1 行から数行の定性的原則として昇格する。
3. project 固有 truth なら、project truth に短く残す。
4. reusable detail なら `references/project-truth-role-pattern.md` を更新し、必要なら skill 本体も更新する。
5. `l0-001-skill-invoke` に「どの依頼でこの skill を呼ぶか」を追記する。
6. shared rule を変えた時は `AGENTSmd-RH.md` を同じ task で更新する。

## close 条件

- `AGENTS.md` に shared の定性的 rule が追加済み
- truth 文書から shared rule と reusable detail が除去済み
- 必要な reference が更新済み
- `l0-001-skill-invoke` の発火条件が更新済み
- shared rule を変えた時は `AGENTSmd-RH.md` も更新済み

## 参照

- `AGENTS.md`
- `AGENTSmd-RH.md`
- `references/project-truth-role-pattern.md`
- 対象 project truth
- 対になる current / gate 文書

## 更新対象

- `AGENTS.md`
- `AGENTSmd-RH.md`
- 対象 project truth
- `l0-001-skill-invoke`
- この skill と関連 references

## 禁止

- `AGENTS.md` に table schema、詳細列定義、長い template を戻すこと
- project 固有 truth を shared rule として一般化すること
- current / gate 文書が持つべき定量情報を project truth へ戻すこと
