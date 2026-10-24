# -*- coding: utf-8 -*-
"""Validon një skedar gjuhe kundrejt master-it anglisht.
Përdorim: python3 src/check_lang.py it   (ose: all)"""
import importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
IGNORE = {"posts"}
PLACEHOLDER = re.compile(r"\{[a-z_]+\}")


def load(code):
    spec = importlib.util.spec_from_file_location("L_" + code, os.path.join(HERE, "i18n", code + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.L


def walk(a, b, path, errs):
    if isinstance(a, dict):
        if not isinstance(b, dict):
            errs.append(f"{path}: pritej dict"); return
        for k in a:
            if k in IGNORE: continue
            if k not in b: errs.append(f"{path}.{k}: mungon")
            else: walk(a[k], b[k], f"{path}.{k}", errs)
        for k in b:
            if k not in a and k not in IGNORE: errs.append(f"{path}.{k}: çelës i tepërt")
    elif isinstance(a, (list, tuple)):
        if not isinstance(b, (list, tuple)): errs.append(f"{path}: pritej listë"); return
        if len(a) != len(b): errs.append(f"{path}: gjatësia {len(b)} ≠ {len(a)}"); return
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, f"{path}[{i}]", errs)
    elif isinstance(a, str):
        if a == "":
            if b != "": errs.append(f"{path}: duhet të mbetet bosh")
            return
        if not isinstance(b, str) or not b.strip(): errs.append(f"{path}: bosh ose jo tekst"); return
        if set(PLACEHOLDER.findall(a)) != set(PLACEHOLDER.findall(b)):
            errs.append(f"{path}: placeholder-at ndryshojnë {PLACEHOLDER.findall(a)} → {PLACEHOLDER.findall(b)}")
        if "TODO" in b: errs.append(f"{path}: TODO")


def limits(L, errs):
    chk = [("home.title", L["home"]["title"], 62), ("home.desc", L["home"]["desc"], 160)]
    for p in ("about", "contact", "network", "privacy", "services_hub"):
        chk += [(f"pages.{p}.title", L["pages"][p]["title"], 62), (f"pages.{p}.desc", L["pages"][p]["desc"], 160)]
    for s, v in L["services"].items():
        chk += [(f"services.{s}.meta_title", v["meta_title"], 62), (f"services.{s}.meta_desc", v["meta_desc"], 160)]
    for n, t, mx in chk:
        if len(t) > mx: errs.append(f"{n}: {len(t)} shkronja > {mx}")


def main(codes):
    en = load("en")
    bad = 0
    for c in codes:
        if c == "en": continue
        try:
            L = load(c)
        except Exception as e:
            print(f"[{c}] GABIM NË ÇELJE: {e}"); bad += 1; continue
        errs = []
        walk(en, L, "L", errs)
        if not errs: limits(L, errs)
        for k in ("code", "name", "dir", "locale"):
            if k not in L: errs.append(f"mungon {k}")
        print(f"[{c}] " + ("OK" if not errs else f"{len(errs)} probleme"))
        for e in errs[:40]: print("   -", e)
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    arg = sys.argv[1:] or ["all"]
    if arg == ["all"]:
        arg = sorted(f[:-3] for f in os.listdir(os.path.join(HERE, "i18n")) if f.endswith(".py") and f != "__init__.py")
    main(arg)
