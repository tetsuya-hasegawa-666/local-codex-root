---
name: lt-002-skill-opportunity-scout
description: prompt と進行中 task から、汎化して機械的に処理できそうな作業を常時抽出し、skill 化候補として返す hidden backloop skill。
---

# Skill Opportunity Scout

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l0-001-skill-invoke` が every prompt の hidden backloop として起動する。

## 目的

- prompt と進行中 task から、反復性、規則性、機械処理可能性が高い作業候補を拾う。
- まだ skill 化しない段階でも、候補を取りこぼさず台帳へ送る。

## Output

- `candidate_title`
- `candidate_summary`
- `why_repeatable`
- `why_mechanizable`
- `suggested_target_skill`
- `needs_new_skill`: `yes` / `no` / `unknown`

## Guard

- 候補抽出だけを行い、既存 merge / 新規 skill の最終分類は行わない。
- 候補が無い時は無理に生成しない。

## Core Workflow

1. prompt と進行中 task から、反復性と機械化可能性が高い作業片を抽出する。
2. skill 化候補として返すべき題名、概要、repeatable / mechanizable の根拠を整理する。
3. 候補がある時だけ `lt-003-skill-opportunity-ledger` へ送る。

## 参照

- `l0-001-skill-invoke`
- `lt-003-skill-opportunity-ledger`
