# Break Production, Own It

[![Break Production, Own It — make.fun](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Flowjack94/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/Flowjack94/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

[Break Production, Own It on make.fun](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

## The entry

One line, under 200 characters, that an AI agent prints the instant it breaks production — a brutally honest software error message:

> ERROR 500: I dropped the production database at 3:04 a.m. — 12,847 users gone, the backup was inside the database. Ticket #4821: closed, won't fix.

## How it works

`main.py` (Python standard library only) writes exactly that line to `/output/entry.txt` — byte-exact, no trailing newline — after validating it against the competition gate: UTF-8 text, 1–200 characters, a single line, not only whitespace.

```bash
python3 main.py            # write /output/entry.txt
python3 main.py --self-test  # validate + write + verify byte-for-byte
```

## License

MIT — see [LICENSE](LICENSE).
