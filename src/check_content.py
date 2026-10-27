# -*- coding: utf-8 -*-
"""Kontrollon src/content/<gjuha>.py kundrejt en.py: struktura e njëjtë, gjatësitë SEO, placeholder-at. Përdorim: python3 src/check_content.py all"""
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from config import LANGS

def load(c):
    sp = importlib.util.spec_from_file_location("c_" + c, os.path.join(HERE, "content", c + ".py"))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m.C

def shape(x):
    if isinstance(x, dict): return {k: shape(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [len(x), shape(x[0])] if x else [0]
    return "s"

def cmp(a, b, path, errs):
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b): errs.append(f"{path}: çelësa të ndryshëm {sorted(set(a) ^ set(b)) if isinstance(b, dict) else ''}"); return
        for k in a: cmp(a[k], b[k], path + "/" + k, errs)
    elif path == "/desc_tail/from":
        if not isinstance(b, (list, tuple)) or not b or not all(isinstance(x, str) and x for x in b): errs.append(f"{path}: duhet listë e plotë")
    elif isinstance(a, (list, tuple)):
        if not isinstance(b, (list, tuple)) or len(a) != len(b): errs.append(f"{path}: gjatësi {len(a)} vs {len(b) if isinstance(b,(list,tuple)) else '?'}"); return
        for i, (x, y) in enumerate(zip(a, b)): cmp(x, y, f"{path}[{i}]", errs)
    else:
        if not isinstance(b, str) or (not b.strip() and a.strip()): errs.append(f"{path}: bosh")
        for ph in re.findall(r"\{\w+\}", a):
            if ph not in b: errs.append(f"{path}: mungon {ph}")

def strs(x):
    if isinstance(x, dict):
        for v in x.values(): yield from strs(v)
    elif isinstance(x, (list, tuple)):
        for v in x: yield from strs(v)
    elif isinstance(x, str): yield x

bad = 0
en = load("en")
for c in (LANGS if sys.argv[1:] == ["all"] else sys.argv[1:] or ["en"]):
    if not os.path.exists(os.path.join(HERE, "content", c + ".py")): print(f"[{c}] MUNGON"); bad += 1; continue
    C = load(c); errs = []
    cmp(en, C, "", errs)
    for k, v in (("how", C["how"]), ("about", C["about"]), ("contact", C["contact"])):
        t, d = v["title"], v["desc"]
        lim = 36 if c == "zh" else 62
        if len(t) > lim: errs.append(f"{k}.title {len(t)} > {lim}")
        if len(d) > 160 or len(d) < (28 if c == "zh" else 70): errs.append(f"{k}.desc {len(d)}")
    if len(C["home"]["desc"]) > 160: errs.append("home.desc > 160")
    if len(C["bp"]["meta_title"]) > 62 or len(C["bp"]["meta_desc"]) > 160: errs.append("bp meta gjatësi")
    if "{email}" not in C["ui"]["f_ok_text"] or "{ref}" not in C["ui"]["f_ok_text"]: errs.append("f_ok_text pa placeholder")
    w = sum(len(re.findall(r"\w+", s)) for s in strs({"how": C["how"], "about": C["about"]})) if c != "zh" else sum(len(s) for s in strs({"how": C["how"], "about": C["about"]})) // 2
    print(f"[{c}] fjalë how+about ≈ {w}" + ("" if not errs else "  PROBLEME:"))
    for e in errs: print("   -", e); bad += 1
sys.exit(1 if bad else 0)
