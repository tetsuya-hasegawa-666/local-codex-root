---
name: write-boundary-guard
description: admin が基準として明示した `AGENTS.md` の directory とその配下だけを `READ` 以外の access 許可範囲として扱い、編集や出力前に write 境界を確認する。
---

# Write Boundary Guard

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `skill-invoker` が `READ` 以外の access を伴うと判断した時だけ起動する。

## 中核規則

- `READ` 以外の access を行ってよい path は、admin がその task の基準として明示した `AGENTS.md` が存在する directory と、その配下だけに限定する。
- path がその範囲外なら、作成、編集、移動、削除、rename、生成物出力、cache 出力、skill 配置変更を行ってはならない。

## Workflow

1. task が `READ` 以外の access を含むかを判定する。
2. その task の基準 `AGENTS.md` path を確定する。
3. `AGENTS.md` の parent directory を write root として固定する。
4. 対象 path が write root 配下かを確認する。
5. 配下なら planner へ `allowed` を返す。
6. 配下でなければ `blocked` を返し、実行を止める。

## Current default

- active `AGENTS.md`
  - `C:\Users\tetsuya\local-codex-root\AGENTS.md`
- active write root
  - `C:\Users\tetsuya\local-codex-root\`

## References

- `references/allowed-write-scope.md`
