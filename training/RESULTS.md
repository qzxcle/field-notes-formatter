# How this skill was built

We tried to train the skill automatically with [EvoSkill](https://github.com/sentient-agi/EvoSkill), which tests an AI agent on past examples, studies its mistakes and writes skills to fix them. This is what happened.

## Setup

- **Data:** 46 published items from three issues of OS AI Field Notes (25 September, 23 October and 20 November 2026). Two items became the examples in `task.md`; the other 44 became the dataset. For each item, the editor pasted the links plus the copied source text, exactly as they would on a normal week, and website clutter (menus, footers, view counts, timestamps) was removed.
- **Split:** 24 items for training, 16 held back for scoring, 4 unused (EvoSkill rounds down per section).
- **Agent and judge:** Claude Sonnet 4.6 for both. The judge compares each attempt to the published item using the rubric in `config.toml`: name format, length, links, date, and content (half the points).
- **Run:** 6 rounds, stopping early after 3 rounds without improvement.

`fieldnotes_public.csv` contains the published items, their sections and their source links. The copied source text is left out, because it belongs to the original publishers. To rerun, paste each source's text into the `question` column, the way the editor did.

## The judge bug (and the fix)

The first runs scored every item 0. EvoSkill's judge may only reply with 16 tokens and expects a bare number. With a detailed rubric, the judge starts explaining ("I'll score each criterion…") and gets cut off. A stricter rubric fixed short items, but a quarter of the long ones still failed.

`fix_judge.py` patches EvoSkill so the judge reasons first and ends with a `SCORE: 0.7` line, which EvoSkill then reads. It costs about 10 cents more per round and makes the scores more accurate. EvoSkill also lowercases both texts before judging during training rounds, so the rubric tells the judge to ignore capitalization in that case.

## Results

| Round | Score | What it tried | Outcome |
| --- | --- | --- | --- |
| Baseline | **79.4%** | `task.md` alone, no skill | **Best** |
| 1 | 73.1% | Big checklist: headline rules, link labels, dates, "pick one angle", word counts | Kept as a backup |
| 2 | 74.7% | Dates, headline patterns for Sentient items, link labels, body rules by news type | Kept as a backup |
| 3 | 72.2% | Dates, a link-label decision tree, podcast headlines with the guest only | Discarded |
| 4 | 76.9% | Only the date rule | Kept as a backup |
| 5 | 72.5% | Date rule plus "exactly as many links as pasted" | Discarded |
| 6 | 75.0% | Date rule plus "personal sites are `ref`, not `blog`" | Kept as a backup |

No round beat the baseline. `task.md` already captured most of the format, and most remaining misses were editorial judgment calls that rules made worse. With 16 scored items and a judge that doesn't score identically every time, gaps of a few points are partly noise.

## What the run taught us

The run still found mistakes the agent made again and again:

1. **Dates:** writing today's date when the pasted text didn't show one. This was the most common mistake.
2. **Links:** adding URLs found inside the copied post (like a repo link), and labeling newsletters and personal sites as `blog`.
3. **Names:** QWEN4-MAX instead of QWEN4 FAMILY, EVOSKILL V2 instead of EVOSKILL TEST, the show name where the house style uses the hook or guest.

The final skill is `task.md` plus fixes for exactly those mistakes. It also adds one fix the run never tried: X post links carry their publish time in the post ID, so `scripts/x_date.py` reads the date straight from the link. Checked against the published issues, it matched 18 of 21 X posts; the other three were off by one day because the editor dated the item by another source.

## Cost and time

About $45 in API usage in total, including two false starts caused by the judge bug. Rounds cost $6–7 each, and the full run took about 2 hours.

## Lessons

- **Test the judge before the run.** A 30-second, few-cent test would have caught the judge bug before it cost money.
- **A strong hand-written baseline is hard to beat.** When your rules already score around 80%, EvoSkill is most useful as a diagnostic: read its notes (`.evoskill/feedback_history.md`) for the mistakes it keeps finding, and fix those by hand.

# Second run: learning how drafts get edited

## Setup

- **Data:** 93 pairs of a draft item and the version that was published, from 10 issues (June to November 2026). The drafts are internal working documents, so this dataset stays private.
- **Starting point:** the editing rules written by hand from the drafts: cut examples and engagement stats, trim extra numbers, plain words, tighter headlines, checked dates.
- **Split:** 35 items held back for scoring, more than twice as many as the first run, for steadier scores.
- **Run:** 4 rounds, about $47 in total.

## Results

| Round | Score | Outcome |
| --- | --- | --- |
| Baseline | 62.1% | Hand-written editing rules only |
| 1 | 64.9% | New best |
| 2 | 64.6% | Kept as a backup |
| 3 | **68.6%** | **Best** |
| 4 | 66.7% | Kept as a backup |

This time every version EvoSkill wrote beat the baseline, a gain of 6.4 points for the best.

## What it learned

The hand-written rules made the agent over-edit. It cut details that carried the story and rewrote wording the editor would have kept. The winning skill's core idea is "earn every cut": keeping is the default, and only true asides, raw engagement counts and inline dates get cut. It also learned to keep comparisons that give a number meaning, price chains, lists that are part of a claim, named things, design intent and rankings, to leave the draft's wording alone unless it's unclear, and to keep the headline choices a draft already makes.

The final skill combines both halves: the hand-written rules for what to change, and the evolved rules for what to keep.
