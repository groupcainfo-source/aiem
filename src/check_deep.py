# -*- coding: utf-8 -*-
"""Numëron fjalët unike të përmbajtjes së thellë dhe kontrollon lidhjet [[slug|tekst]]. Përdorim: python3 src/check_deep.py en sq"""
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from config import SERVICES
SLUGS = {s["slug"] for s in SERVICES}

def load(code, folder, var):
    spec = importlib.util.spec_from_file_location(folder + code, os.path.join(HERE, folder, code + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return getattr(m, var)

def words(t): return len(re.findall(r"\w+", re.sub(r"\[\[[a-z-]+\|([^\]]+)\]\]", r"\1", t), re.U))

def blocks_text(bl):
    out = []
    for b in bl:
        out += b[1] if b[0] in ("ul", "ol") else [b[1]]
    return out

bad = 0
for code in sys.argv[1:] or ["en"]:
    D = load(code, "deep", "DEEP"); L = load(code, "i18n", "L")
    print(f"[{code}]")
    for slug in sorted(SLUGS):
        d = D["services"].get(slug)
        if not d: print("  MUNGON", slug); bad += 1; continue
        deep = sum(words(t) for t in blocks_text(d["blocks"])) + sum(words(q) + words(a) for q, a in d["faqs"])
        v = L["services"][slug]
        base = sum(words(t) for t in [v["lead"], v["audience"], *v["includes"], *v["deliver"], *(x for f in v["faqs"] for x in f)])
        links = [m for b in d["blocks"] for t in (b[1] if b[0] in ("ul", "ol") else [b[1]]) for m in re.findall(r"\[\[([a-z-]+)\|", t)]
        unk = [l for l in links if l not in SLUGS or l == slug]
        h2 = sum(1 for b in d["blocks"] if b[0] == "h2")
        flag = "" if deep >= 800 and not unk and len(links) >= 2 else "  <-- KONTROLLO"
        if flag: bad += 1
        print(f"  {slug:34s} deep={deep:5d} total~{deep + base:5d} h2={h2:2d} links={len(links)}{flag} {unk or ''}")
sys.exit(1 if bad else 0)
