# What 18 issues of Field Notes show

An analysis of every published issue from 19 March to 20 November 2026: 18 issues and 238 items. The items are in `published_items.csv`. Findings that held up became rules in the skill.

## How the format evolved

| Period | What the issues looked like |
| --- | --- |
| March–April 2026 | No sections. A "What's Cooking at Sentient" block at the end. Company names as headlines (ANTHROPIC, NETFLIX, GOOGLE). Casual verbs ("dropped", "drops"). Dates with the full month: [8 APRIL 2026]. |
| May–July 2026 | Sections appear, with changing names (Tools & Infrastructure, Podcasts & Talks, Policy & Governance, Industry & Funding). Short-month dates start to appear. From July, every issue opens with "This Week In OS AI Field Notes: [date]". |
| August–November 2026 | Five fixed sections: Open-Source Models, Tools & Frameworks, Policy & Security, Podcasts & Media, What's new at Sentient? Short-month dates only: [16 NOV 2026]. Headlines name the product more often than the company. |

## Rules the archive confirmed

- **Length:** news items have a median of 52 words, and 80% fall between about 40 and 64. Sentient items are shorter, with a median of 39. This matches the skill's 40–65 rule.
- **Verbs:** "released" appears about 70 times. "Drops" and "dropped" appear only in March and April.
- **Item order:** in 28 of 39 sections with three or more dated items, the items run from oldest to newest.
- **Link labels**, counted in the early issues, where labels survived as plain text: `ref` 152, `ref2` 65, `github` 37, `huggingface` 25, `blog` 11, `RSVP` 11, `ref3` 10, `paper` 7, `youtube` 5, `APPLY` 4. Calls to action are in caps, and repeated labels are numbered.
- **Issue size:** 9–16 items, with 13–16 in recent issues.

## Naming

Headline naming changed more than anything else. It went from company names in the spring, to "COMPANY, PRODUCT" in the 9 October issue (NVIDIA, KUMO TABULAR), to mostly product names in November (INKLING 2 SMALL, PAN 2). Because there is no fixed past rule, the skill uses the editor's current one: the name most people are using right now.

## Subject lines

Past subjects run 29–78 characters, with a median of 54, and follow three patterns: the week's big theme for open-source AI, one striking number, or the biggest story as a question. The preview text was "Brought to you by Sentient Foundation" until the 20 November issue, which listed its three lead stories instead. Both are written up for the skill in `field-notes-formatter/references/issue-and-subject-lines.md`.

## What editing changes

Comparing 93 draft items from 10 issues with their published versions shows what the editing pass does. 77 of 93 items were edited, 53 of them heavily. Items got shorter, from a median of 60 words to 55: 51 got shorter, and only 4 got longer. 28 headlines changed, and 20 dates were corrected, mostly by one day.

The most common edits: cutting example sentences, keeping only the one or two benchmark numbers that carry the story, removing engagement stats (Hacker News points and Reddit upvotes never survived) and inline dates, moving "what it is" into the first sentence, giving lesser-known organizations a short descriptor, and choosing plainer words. These became the skill's editor's pass.
