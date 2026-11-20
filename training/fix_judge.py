"""Patch EvoSkill's AI judge so detailed rubrics work, then test it.

Why: EvoSkill's LLM judge may only reply with 16 tokens and expects a bare
number. With a detailed rubric, the judge starts explaining ("I'll score each
criterion...") and is cut off, so every item scores 0. This patch lets the judge
reason first and reads the number from a final "SCORE: 0.7" line. It keeps a
backup of the original file (shared.py.bak).

Run with EvoSkill's own Python, from your EvoSkill project folder, in a
terminal where ANTHROPIC_API_KEY is set:
  /path/to/EvoSkill/.venv/bin/python /path/to/fix_judge.py
"""
import csv, importlib.util, os, re, shutil, sys
from pathlib import Path

PROJECT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

# 1. Patch the judge
path = importlib.util.find_spec("src.cli.shared").origin
code = open(path).read()
if "SCORE:" in code:
    print("EvoSkill judge already patched:", path)
else:
    old_prompt = '"Reply with only a number between 0.0 and 1.0."'
    new_prompt = '"Check each point briefly, then end with a final line in exactly this form: SCORE: 0.7"'
    old_parse = "return float(text.strip())"
    new_parse = r'''import re as _re
                _m = _re.findall(r"SCORE:\s*\**\s*([01](?:\.\d+)?)", text)
                return float(_m[-1]) if _m else float(text.strip())'''
    if code.count("max_tokens=16,") != 4 or old_prompt not in code or old_parse not in code:
        sys.exit("EvoSkill's code looks different than expected (maybe a newer version). Nothing was changed.")
    shutil.copy(path, path + ".bak")
    code = code.replace("max_tokens=16,", "max_tokens=1024,").replace(old_prompt, new_prompt).replace(old_parse, new_parse)
    compile(code, path, "exec")
    open(path, "w").write(code)
    print("Patched EvoSkill judge:", path)

# 2. Test it with EvoSkill's own scorer on your two shortest items
from src.cli.config import load_config
from src.cli.shared import make_scorer
cfg = load_config(PROJECT)
score = make_scorer(cfg)
csv.field_size_limit(10**8)
rows = [r for r in csv.DictReader(open(cfg.dataset.path, encoding="utf-8")) if r["question"].strip()]
for r in sorted(rows, key=lambda r: len(r["question"]))[:2]:
    exp = r["ground_truth"]
    no_links = re.sub(r"\[\[[^\]]+\]\([^)]+\)\]\s*", "", exp)
    print(exp[:60] + "...")
    print("  exact copy    (expect ~1.0):", score(r["question"], exp, exp))
    print("  links removed (expect less):", score(r["question"], no_links, exp))
