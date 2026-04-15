---
name: l2b-007-runtime-bootstrap-scope-resolve
description: fresh runtime から再現する最小 bootstrap 範囲を決める child skill。trial 往復ではなく clean bootstrap runbook に昇格させるべき範囲を切る時に使う。
---

# Runtime Bootstrap Scope Resolver

bootstrap 手順のうち、何を canonical runbook へ昇格させるかを決める child skill とする。

## Trigger Ownership

- この skill 自身は発火判断を持たない。
- `l1-001-skill-plan` が bootstrap runbook へ昇格する範囲の確定を必要と判断した時だけ呼ばれる。

## Input

- `task_summary`
- `working_files`
- `must_read_docs`

## Output

- `bootstrap_scope`
- `runbook_promotion_targets`
- `do_not_leave_only_in_log`

## Guard Rails

- shared log を bootstrap 正本の代わりにしない。
- partial recovery 手順を無制限に積み増さない。
- evidence と runbook を混同しない。

## Coordination

- `l2a-008-external-compute-output-keep` と `l2b-002-script-doc-sync-enforce` を補助する。

## 参照

- `AGENTS.md`
- `l2a-008-external-compute-output-keep`
- `l2b-002-script-doc-sync-enforce`
