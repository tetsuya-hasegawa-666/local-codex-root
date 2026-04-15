# response-shape checklist

## Checkpoints

| checkpoint | rule |
| --- | --- |
| requirement fit | `interpreted_request.expected_output` に沿う |
| fact safety | 実施済みと未実施を混同しない |
| noise trim | 要求外説明を減らす |
| open points | 未確定事項を残す |
| shape | 表、規則文、要約などの形式を明示する |

## Guard

- 事実圧縮はしてよいが事実改変はしない。
- 省略したものは `omitted_noise` へ残す。
