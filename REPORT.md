# REPORT — Angry Judge: The Short Rant Contest

- **Bounty:** u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046 — $2 total (1st $1, 2nd $0.50, 3rd $0.50)
- **Deadline:** 26 Nov 2026 02:05 WIB (25 Nov 19:05Z). Entry free, Force_Last.
- **Judge:** pairwise, z-ai/glm-5.3-flash. Criteria in order: (1) funny rant about an
  everyday annoyance, not an essay or list; (2) actually funny; (3) specific,
  concrete annoyance; (4) sharp, economical wording; (5) fresh angle.
  Tie-breaks: playoff games won, then smaller text, then earlier receipt.
- **Loss-log lessons applied:** provisional/dev score is never a result; never
  submit a weaker variant after the best (Force_Last); submit early; micro-text
  program is trivial — if the gate rejects it, note it and move on, no identical
  retry. `main.py` + `README.md` written fresh in this session, no starter read,
  no lines copied from any other entry.

## Candidates (each one annoyance only, no list, no throat-clearing)

### A — The printer (255 chars)
> The office printer has printed one page in four years, and it was a test page. It jams on plain paper, demands magenta to print black text, and blinks PC LOAD LETTER like a riddle from a dying robot. I have apologised to it out loud. It knows what it did.

### B — The man in the queue (343 chars)
> The man ahead of me in the queue waited until the cashier read out the total, then discovered, to his own visible amazement, that he owns a wallet. He opened it like an archaeologist unsealing a tomb, examined each card as though meeting it for the first time, and then asked if we take cash. We are in a cash-only queue. There are nine of us.

### C — The self-checkout accusation (305 chars) — CHOSEN
> The self-checkout machine just told twelve strangers there is an unexpected item in the bagging area. The unexpected item is the rice I scanned thirty seconds ago. It has now summoned a human to confirm I am not stealing my own groceries, and the human is strolling over like justice runs on his schedule.

## Pairwise reasoning

- **A vs B — B wins.** B is a concrete human scene with a visible behaviour
  (discovering his own wallet at the till); A is the printer, the exact example
  the rules themselves name, and "PC LOAD LETTER" is a thirty-year-old joke —
  it fails criterion 5 (freshness) before the others are weighed.
- **B vs C — C wins.** Both are concrete and funny, but C has the sharper
  single image: a machine publicly accusing you of stealing your own groceries,
  in front of twelve strangers. The anger is shared rather than performed —
  everyone has been beeped at by that machine. C's punch lands in sentence
  one; B needs a longer setup and its "forgot his wallet" trope is familiar.
  C is also the smaller text (305 vs 343 bytes), which wins an exact tie.
- **Chosen: C.** One annoyance, one image, no throat-clearing, 305 chars
  (well under the 400 cap).

## Verification (local)

- `python3 main.py` run twice: `/output/entry.txt` byte-identical both runs.
- Output: exactly one line, 305 characters + trailing newline, UTF-8, not
  whitespace-only — passes the 1–400 char gate.

## Deliverable

- Repo: https://github.com/Chapo1245/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046-chapo124574
- `main.py` (Python 3.13, stdlib only) writes the chosen rant to `/output/entry.txt`.
