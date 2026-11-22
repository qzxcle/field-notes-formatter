---
name: field-notes-formatter
description: Format news items for OS AI Field Notes, Sentient Foundation's weekly open-source AI newsletter. Use this whenever the user pastes a link plus copied post, article or podcast transcript and wants it turned into a newsletter item, a Field Notes entry or "a paragraph for the newsletter", or says "format this", "write this up" or "make an item", even if they don't mention Field Notes by name. Also use it to assemble a full issue in the right section order, to write the issue's subject line and preview text, and to edit draft items the editor already wrote into publish-ready form.
---

# Field Notes Formatter

Turns raw news (the links the editor pasted plus the copied post, article or transcript) into finished items for OS AI Field Notes. The format below comes from the published issues. Follow it exactly, because the editor pastes these straight into the newsletter doc.

## Workflow

For each item:

1. **Separate the input.** The links pasted at the top are the item's links. URLs inside the copied text are part of the source, not links for the item.
2. **Pick the headline name** (see Naming). In Claude Code with last30days installed, run the name check for model and tool items where the name could go either way.
3. **Find the date** (see Date).
4. **Write the body** for the item's type (see Body).
5. **Add the links and the date.**
6. **Run the editor's pass** (see below), then the final check.

**Editing drafts:** if the editor pastes items that are already written in newsletter form (a bold ALL-CAPS name, text, links and a date), treat them as drafts. Edit lightly: keep their facts, wording and links, fix the name and date where needed, and apply the editor's pass. Return the edited items, then one short line per item saying what changed (for example: “Cut the example sentence and two benchmark numbers; date corrected to 12 NOV”). Change nothing that already follows the rules.

Return the finished items, with no headings or notes of your own. If the editor pastes several sources, write one item per source, in the order given, separated by a blank line.

**Subject lines come with every batch.** Whenever the editor pastes three or more items, whether sources or drafts, end with a block headed "Subject line options": three subject lines for the issue (one per pattern) and one preview text. The editor needs one for every issue and shouldn't have to ask. Skip it only if they say so. Read `references/issue-and-subject-lines.md` for the patterns, and also for a full issue (header, section order, item order).

## Item format

**NAME:** Body sentences. [[label](url)] [[label](url)] [D MON YYYY]

The name is bold ALL CAPS with the colon inside the bold.

## Naming

- **Use the name people know it by right now.** If people talk about the product, use the product (INKLING 2 SMALL, NEMOTRON-LABS-SIGMA). If the product name is a version string nobody repeats, use the company (LIQUID AI for LFM2.5-24B-A2B). For news without a product, name the news itself (EUROPA, OPENCODE INCIDENT, CLOUD COMPUTING RESTRICTIONS).
- **Families:** when the source launches a flagship and says smaller or open versions are coming, name the family: QWEN4 FAMILY, not QWEN4-MAX.
- **What's New at Sentient:** name what happened, not only the product: EVOSKILL TEST, EVOSKILL AT COLM 2026, JULIE BELIÃO JOINS SENTIENT FOUNDATION.
- **Podcasts and shows:** the show plus the episode hook or the guest: ALL-IN PODCAST’S JENSEN OUT, THE PRAGMATIC ENGINEER WITH SATYA NADELLA. A talk at an event, rather than a show episode, can use the speaker alone: JENSEN HUANG.
- **Our own podcast:** OPEN COMMONS PODCAST, [EPISODE TITLE IN CAPS].

### Name check with last30days

The editor wants the name that is most mentioned online right now, and the source alone can't show that.

- **When:** model and tool items where the name could go either way (product or company, or two product names). Skip policy, podcast and Sentient items, whose names are the news itself or our own.
- **How:** if the last30days skill is available, run it once on the product name, for example `/last30days Nemotron 3.5 Super VL`. Look at how the most-engaged posts and threads in its results refer to the release, and use the name most of them use, in ALL CAPS.
- **Without it** (for example in the claude.ai chat), judge from how the source and its coverage name it.

## Body

Use only facts and numbers from the pasted text, never invent any, and keep names, numbers, rankings and comparisons exactly as the source states them (#1, 4.7x cheaper, $0.26 per task). Keep the tone neutral and factual, with no hype words. Use plain verbs: released, launched, open-sourced, announced. Casual verbs like “drops” appeared only in the newsletter's first issues.

**News items** (models, tools, policy): 2–3 sentences, about 40–65 words.
- Open with who did what: “[Who] released / launched / open-sourced / announced [name], a [what it is].” Give lesser-known organizations a short descriptor (“Sequoia-backed startup Unreal Labs”).
- For tools and frameworks, say what it is and how it works (license, where it runs, key capability) before any benchmark numbers, unless a benchmark is the headline claim.
- Then give the key numbers or why it matters.
- When the reader needs it, explain a technical idea in one plain sentence (“Most models write text one word at a time. Sigma refines blocks of text all at once.”).
- For policy, if the source gives timing context (it landed two days after another event), that context is often the story.

**Podcasts:** 1–2 sentences, about 40–60 words, in the present tense: “[Guest] joins host [Host] to discuss…” or “[Hosts] discuss…”. Pick the most striking claims rather than listing every topic.

**What's New at Sentient:** 20–60 words. “We” and “our” are fine.
- Experiments: what was tested, the surprising finding, and the takeaway.
- Milestones (a paper accepted, a listing, a hire): state the fact and briefly say what the venue or platform is. Don't re-explain the product.
- Calls to action (a survey, an event): what to do and why, plainly.

## Links

Use exactly the links the editor pasted at the top of the input, one `[[label](url)]` each, in the same order. Don't add URLs found inside the copied text, and never invent one. Adding a repo link mentioned inside a post was a common mistake in testing.

Labels:
- `huggingface`, `github`, `paper` (arXiv), `youtube` (podcast and video episodes)
- `docs` only for real technical documentation
- `blog` only for an official company or product blog or announcement page
- `ref` for X posts, news articles, Substack and newsletters, personal sites (darioamodei.com is `ref`, not `blog`) and anything else
- Number repeats of any label: `ref2`, `ref3`, `github2`
- Sentient calls to action in caps: `SUBMIT`, `SURVEY`, `RSVP`, `APPLY` or `JOIN`

## Date

Use the date of the news, not the issue date, and never today's date. Defaulting to today's date was the most common mistake in testing.

1. If the pasted text states the release, publication or event date, use it.
2. Otherwise, if a pasted link is an X post, read the date from the post's ID with `python3 scripts/x_date.py <link>` (the script is in this skill's folder). It prints the date in US Pacific time, for example `16 NOV 2026`, and it matched the published date for 18 of 21 past items.
3. Otherwise, write the placeholder `[D MON YYYY]` so the editor fills it in.

Format: no leading zero and the month in caps, `[9 OCT 2026]`, `[16 NOV 2026]`. Events can use a range: `[29-30 SEP 2026]`.

## Editor's pass

Run this on every item, whether you wrote it from sources or you're editing a draft. It has two halves, and both matter. Tested on 93 real drafts, the cutting rules alone made Claude over-edit and matched the published versions 62% of the time. Adding the second half, "earn every cut", raised that to 69%. The editor's real edits are small and targeted (drafts averaged 60 words, published items 55), not rewrites.

### What to change

1. **Cut examples and asides.** Sentences like “For example, simulate Jenga for each move” go.
2. **Cut raw engagement counts and inline dates.** Hacker News points, Reddit upvotes and “14k GitHub stars” never made it into a published item. Dates like “on June 3” come out of the text, because the date goes at the end.
3. **Trim repetition.** When several benchmark scores make the same point, keep the one that carries the claim, plus the competitor it's compared to. Shorten long lists of places or generic partners (“partners from France, Germany, the UK and Spain” becomes “European partners”).
4. **Say what it is in the first sentence.** If the description of the product comes late, move it up. Give a lesser-known organization a short descriptor (“RadixArk, founded by AI infrastructure veterans from xAI and NVIDIA”).
5. **Use plain words where the draft's word is jargon or awkward.** “See”, not “visualize”. “Act”, not “commit to an action”. Spell out abbreviations readers may not know (“Amazon Web Services”, not “AWS”).
6. **Fix the headline where it breaks a rule.** Give a bare podcast name its episode hook or guest. Spell out abbreviations (SUPER INTELLIGENCE VS ARTIFICIAL INTELLIGENCE SAGA, not SI VS AI SAGA). Drop words that repeat the obvious (EUROPA, not EUROPA AI). Join two partner companies with “&” (HUGGING FACE & OPENROUTER).
7. **Check the date.** Drafts were often a day off. For X links, confirm the date with the script.

### Earn every cut

Keeping is the default. Cut only what rules 1–3 clearly name. These details carry the story, so keep them even when they look like extras:

- **Comparisons that give a number meaning:** “level with Grok 4.7, ahead of Kimi K3 at 44”.
- **Price chains:** “$0.435 per 1M input tokens, working out to $0.13 per task”.
- **Lists that are the claim itself:** “agentic, coding, multimodal, and safety benchmarks”, or “leads all US and European open-weight models”. Every item in such a list is part of the claim.
- **Named things and the technical idea the item is about:** product nicknames, named frameworks, “recursive self-improvement”.
- **Design intent:** “built for long-horizon tasks”.
- **Rankings and significance, as opposed to raw counts:** “one of the most starred repos”, “#1 US open model”.

**Wording:** change a word only when it's jargon, unclear or wrong. Don't swap in synonyms (“compress” stays “compress”, “discuss” stays “discuss”), and don't reorder phrases that already read well.

**Headlines in drafts:** keep the structure the draft has unless it breaks a rule above.
- Keep words that carry voice, like SHOCKER or CRASH.
- Keep a podcast's episode hook when the draft has one. Write a new hook only when the draft has none.
- Keep a company prefix the draft already has (META MUSE GLIMMER, ALIBABA QWEN3.8-MAX). When the parent company isn't obvious from the product name, add it (XIAOMI + MIMO CODE).
- Lead with the show and episode when the episode is the story (THE ALL-IN PODCAST, ANTHROPIC S-1 SHOCKER). Lead with the guest or topic when they are the story (MATT POCOCK ON AGENT SKILLS).

## Final check

- The name is bold ALL CAPS with the colon inside the bold.
- The length fits the item's type.
- Every pasted link appears once, with the right label, and nothing was added.
- The date is in the right format and isn't today's date unless the source says so.
- Every number appears in the source.
- Nothing that carried the story was cut, and no word was changed without a reason.

## Examples

More examples, two or three per section, are in `references/examples.md`.

Model release:

**NEMOTRON-LABS-SIGMA:** NVIDIA released open weights for Sigma, the first large-scale continuous diffusion language model. Most models write text one word at a time. Sigma manipulates and refines blocks of text all at once, which makes its output easier to steer and faster to generate. On math and coding, Sigma-3B outperforms the open diffusion models LLaDA-8B and Dream-7B—half their size and 3.5 times faster. [[paper](https://arxiv.org/abs/2610.02665)] [[huggingface](https://huggingface.co/collections/nvidia/nemotron-labs-sigma)] [16 NOV 2026]

Tool launch:

**NOD:** n8n Labs released Nod, a standalone open-source personal agent free under the Apache 2.0 license. It runs on your own computer with a sandboxed virtual machine and browser, works inside connected apps and on websites, asks before taking actions, and can use any model provider you bring, including local models. [[ref](https://x.com/n8n_io/status/2120431328458076315?a=70Fg5NxR40buGQxwv4k&s=20)] [[github](http://github.com/n8n-io/nod)] [11 NOV 2026]

Podcast:

**OPEN COMMONS PODCAST, DON'T LET AI SPEND YOUR MONEY WITHOUT PERMISSION:** Coinbase Developer Platform’s Kevin Leffew joins host Sachi Kamiya to discuss x402, the open standard that revives HTTP’s 402 “Payment Required” code from 1997 so AI agents can pay for data and APIs on the spot. He explains why Coinbase handed x402 to the Linux Foundation and how AI is breaking the ad-funded web. [[youtube](https://www.youtube.com/watch?v=icSLXWKeElw)] [17 NOV 2026]

Sentient experiment:

**EVOSKILL TEST:** Sentient researchers used the upcoming EvoSkill v2 to test Dario Amodei's concern about agents gaming their graders. On a spreadsheet-repair test, an agent turned a grader loophole the team had missed into a cheat sheet other agents could use. The takeaway: the lesson isn't about dangerous AI or to pace the frontier, it's that test hygiene is harder than it looks. [[ref](https://x.com/SentientAGI/status/2100961363527147673?s=20)] [18 SEP 2026]
