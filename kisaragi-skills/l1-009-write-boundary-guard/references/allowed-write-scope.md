# allowed write scope

## rule

- `READ` 以外の access を行ってよい root は、admin がその task の基準として明示した `AGENTS.md` がある directory と、その配下だけである。

## current default

- active `AGENTS.md`
  - `C:\Users\tetsuya\local-codex-root\AGENTS.md`
- active write root
  - `C:\Users\tetsuya\local-codex-root\`

## deny examples

- `C:\Users\tetsuya\kisaragi\...` への編集
- `C:\Users\tetsuya\.codex\...` への編集

## allow examples

- `C:\Users\tetsuya\local-codex-root\AGENTS.md`
- `C:\Users\tetsuya\local-codex-root\AGENTSmd-RH.md`
- `C:\Users\tetsuya\local-codex-root\kisaragi-skills\...`
- `C:\Users\tetsuya\local-codex-root\kisaragi-db\...`
