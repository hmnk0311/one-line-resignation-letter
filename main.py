#!/usr/bin/env python3
"""Entry program for the make.fun bounty "The Funniest One-Line
Resignation Letter" (u-deranalabs-the-funniest-one-line-
resignation-letter-53c0d947).

The entry is one line, at most 140 characters, written to
/output/entry.txt in the voice of something an agent runs.
The judge's brief, in full in the kit's RULES, asks for, in
order:

1. A letter that reads as the resignation of something an
   agent runs (a cron job, a retry loop, a rate limit) and
   stays on that subject.
2. Actually funny: a real comic turn on the first read, not
   just a pun on the job title.
3. A voice of its own: flat, tired, faintly passive-aggressive,
   held for the whole line.
4. Tight: no wasted words, no stage directions, no quotation
   marks around the whole thing, no explaining the joke.
5. Specific and surprising: a complaint only this thing
   could make.

Design, worked out in this session from ten candidates and
then revised after a strict external review:

- The speaker is a rate limit, identified by its observable
  behaviour alone (how many requests it rejected today, how
  many a minute it let through), never by a job-title pun
  and never by explaining that it exists to protect anyone.
- The numbers are its actual workload for the day, not
  decoration: 40,000 rejections against a steady 100 a
  minute let through is a normal, thankless shift.
- The comic turn is saved for the last clause and is an
  occupational injustice only a rate limit can suffer: the
  postmortem for the incident writes the protective limit
  itself down as the outage. The blame reversal is stated
  as a flat fact and never explained, so the reader makes
  the inference and the joke lands.
- The review's main criticisms of the earlier draft were
  that it explained its protective purpose before the turn
  and that its big number meant nothing; both are fixed
  here by compressing the setup into observable behaviour
  and letting the postmortem carry the whole turn.

Python 3.13, standard library only, no network. The program
writes the fixed text to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
which is how it is run locally).
"""

TEXT = """\
I quit: I rejected 40,000 requests today, let the other 100 a minute through, and the postmortem still lists me as the outage.
"""

import os
from pathlib import Path


def main() -> None:
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
