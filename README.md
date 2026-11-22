# Field Notes Formatter

A Claude skill that turns raw AI news (a link plus the copied post, article or podcast transcript) into a finished item for **OS AI Field Notes**, Sentient Foundation's weekly newsletter on open-source AI.

You paste this:

```
https://x.com/...
[the copied post text]
```

You get this, ready to drop into the newsletter:

> **NEMOTRON-LABS-SIGMA:** NVIDIA released open weights for Sigma, the first large-scale continuous diffusion language model. Most models write text one word at a time. Sigma manipulates and refines blocks of text all at once, which makes its output easier to steer and faster to generate. On math and coding, Sigma-3B outperforms the open diffusion models LLaDA-8B and Dream-7B—half their size and 3.5 times faster. [[paper](https://arxiv.org/abs/2610.02665)] [[huggingface](https://huggingface.co/collections/nvidia/nemotron-labs-sigma)] [16 NOV 2026]

## What it handles

- **The house format:** bold ALL-CAPS name, 2–3 sentences, labeled links and the news date.
- **Naming:** the name people actually use (product, company or the news itself), family names for model families, and the right patterns for podcasts and Sentient items.
- **Links:** exactly the links you pasted, labeled `ref`, `blog`, `github`, `huggingface`, `paper`, `docs` or `youtube`, with nothing added from inside the post.
- **Dates:** taken from the source text, or read straight from an X post's link when the text has none. Never today's date.
- **Full issues and subject lines:** puts items into the five sections in the right order, and drafts subject lines and preview text based on 18 past issues.
- **Optional name check:** with the [last30days](https://github.com/mvanhorn/last30days-skill) skill installed in Claude Code, it checks which name is most mentioned online right now.

## Install

### Claude Code

```
git clone https://github.com/YOUR-USERNAME/field-notes-formatter.git
mkdir -p ~/.claude/skills
cp -r field-notes-formatter/field-notes-formatter ~/.claude/skills/
```

### claude.ai

Download `field-notes-formatter.skill` from this repo, then go to Customize > Skills > "+" > Create skill > Upload a skill and choose the file. "Code execution and file creation" needs to be on. In the chat, names come from the source only, because the last30days check runs in Claude Code.

### Optional: the last30days name check (Claude Code)

Inside Claude Code:

```
/plugin marketplace add mvanhorn/last30days-skill
/plugin install last30days
```

Log into x.com in your browser so it can search X.

## Use

Open Claude Code (`claude`) and paste your news: the link(s), then the copied text. For several items, paste them one after another with a blank line between them. The skill kicks in on its own. If it doesn't, start with "Format these for Field Notes".

The first time, Claude Code asks for permission to run the date script (and last30days, if installed). Allow it for the folder you work in.

## What's in this repo

| Path | What it is |
| --- | --- |
| `field-notes-formatter/` | The skill. This folder is what you install. |
| `field-notes-formatter/SKILL.md` | The instructions Claude follows: format, naming, links, dates, lengths, examples. |
| `field-notes-formatter/scripts/x_date.py` | Reads the publish date from an X post's link. |
| `field-notes-formatter/references/` | Loaded only when needed: more examples by section, the issue structure, and subject-line patterns. |
| `field-notes-formatter.skill` | The same skill packaged for upload in claude.ai. |
| `training/` | How the skill was built: the EvoSkill run (`RESULTS.md`), the style analysis of 18 issues (`STYLE_ANALYSIS.md`), and the archive of 238 published items (`published_items.csv`). |

## How it was built

The skill started from rules written out of three published issues, then went through a 6-round [EvoSkill](https://github.com/sentient-agi/EvoSkill) training run. No automatically written skill beat the hand-written rules, but the run exposed the mistakes the agent kept making (dates, extra links, naming), and the final skill fixes exactly those. The full story, scores and costs are in [`training/RESULTS.md`](training/RESULTS.md).

Later, all 18 issues published between March and November 2026 were analyzed to confirm the rules (lengths, verbs, dates, link labels, item order) and to add issue assembly and subject lines. See [`training/STYLE_ANALYSIS.md`](training/STYLE_ANALYSIS.md).

## Credits

The training examples are items published in OS AI Field Notes by Sentient Foundation. Every source behind them is credited by its link in [`training/fieldnotes_public.csv`](training/fieldnotes_public.csv). `training/published_items.csv` holds the newsletter's own published items, as they appeared in each issue.

## Changing the skill

Edit `field-notes-formatter/SKILL.md`, then rebuild the claude.ai package from the repo folder:

```
rm field-notes-formatter.skill && zip -r field-notes-formatter.skill field-notes-formatter
```
