# skill structure checklist

## 目的

- skill の新規作成または変更時に、必要な構成要素と確認順を漏らさずそろえるための確認表とする。

## 最小構成

- `SKILL.md`
- 必要な `references/`
- 必要時の `scripts/`
- 必要時の `agents/openai.yaml`
- `kisaragi-skills/agents.md` への登録
- trigger / routing reference への反映
- 機能確認テスト仕様と実行結果

## 確認観点

- 何を担当し、何を担当しないかが明示されているか
- 発火判断 ownership が上位 skill に残っているか
- 参照先が実在し、相対 path が崩れていないか
- close 条件に機能確認テスト pass が入っているか
- shared rule 変更を伴う時、`AGENTS.md` と `AGENTSmd-RH.md` が追随しているか
