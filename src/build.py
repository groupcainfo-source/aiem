# -*- coding: utf-8 -*-
"""Gjeneron portalin shumëgjuhësh në rrënjën e repo-s:  python3 src/build.py"""
import os, json, shutil, hashlib, html, importlib.util, urllib.parse
from config import CFG, ROUTES, SUPPORT_EMAILS, LANGS, GROUPS, SERVICES

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(ROOT)
SITE = CFG["url"].rstrip("/")
E = html.escape
HL = {"zh": "zh-Hans"}  # kodi hreflang / lang për HTML


def load(code):
    spec = importlib.util.spec_from_file_location("L_" + code, os.path.join(ROOT, "i18n", code + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.L


def load_mod(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


_F = load_mod("forms")
FORM, TEAM = _F.FORM, _F.TEAM


def load_content(c):
    return load_mod_path("content", c, "C")


def load_mod_path(folder, code, var):
    spec = importlib.util.spec_from_file_location(f"{folder}_{code}", os.path.join(ROOT, folder, code + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return getattr(m, var)


PRO_SLUGS = {"business-partnerships"}  # shërbimi i rrjetit të profesionistëve: pika "jam profesionist" hiqet nga kryefaqja


def with_form(c):
    L = load(c)
    F = FORM[c]
    L["ui"].update(F["ui"])
    L["ui"]["steps"] = [dict(x) for x in L["ui"]["steps"]]
    L["ui"]["steps"][1] = dict(F["step2"])
    L["home"]["ticks"] = list(L["home"]["ticks"])
    L["home"]["ticks"][0] = F["tick1"]
    L["home"]["faq"] = [list(x) for x in L["home"]["faq"]]
    L["home"]["faq"][1][1] = F["faq2"]
    L["pages"]["privacy"]["sections"] = [list(x) for x in L["pages"]["privacy"]["sections"]]
    L["pages"]["privacy"]["sections"][0][1] = F["privacy1"]
    # ---- ndryshimet e reja: formular i ri, pa "për profesionistët", faqe të reja How it works dhe About
    C = load_content(c)
    L["ui"].update(C["ui"])
    L["ui"]["problems"] = [p for p in L["ui"]["problems"] if p["slug"] not in ({"mechanical-engineering", "electrical-engineering"} | PRO_SLUGS)]
    L["home"].update({k: C["home"][k] for k in ("desc", "lead")})
    L["home"]["ticks"] = list(C["home"]["ticks"])
    L["home"]["faq"] = [list(x) for x in L["home"]["faq"][:5]]      # pika e fundit ishte "si t'i bashkohem rrjetit"
    L["home"]["faq"][1][1] = C["home"]["faq1"]
    L["pages"]["contact"].update(C["contact"])
    L["pages"]["privacy"]["desc"] = C["privacy"]["desc"]
    L["pages"]["privacy"]["sections"][0] = list(C["privacy"]["s0"])
    H = dict(C["how"])
    st = [dict(x) for x in H["steps"]]
    st[2] = dict(st[2], b=list(st[1]["b"][:2]) + list(st[2]["b"]))   # hapi "arrin te desku" bashkohet me "specialisti përgjigjet": 4 hapa kudo
    H["steps"] = [st[0], st[2], st[3], st[4]]
    L["pages"]["how"] = H
    L["pages"]["about"] = C["about"]
    L["pages"].pop("network", None)
    for sv in L["services"].values():
        t = C["desc_tail"]
        for old in t["from"]:
            if sv["meta_desc"].endswith(old):
                sv["meta_desc"] = sv["meta_desc"][: -len(old)] + t["to"]
                break
    L["services"]["business-partnerships"].update(C["bp"])
    return L


LANG = {c: with_form(c) for c in LANGS if os.path.exists(os.path.join(ROOT, "i18n", c + ".py"))}
DEEP = {}  # përmbajtje e thellë për faqet e shërbimeve (opsionale për çdo gjuhë)
for _c in LANGS:
    _fp = os.path.join(ROOT, "deep", _c + ".py")
    if _c in LANG and os.path.exists(_fp):
        _spec = importlib.util.spec_from_file_location("deep_" + _c, _fp)
        _m = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_m)
        DEEP[_c] = _m.DEEP
        _bp = DEEP[_c]["services"]["business-partnerships"]   # hiqet pjesa "për profesionistët: si të aplikoni" dhe FAQ-të e anëtarësimit
        assert _bp["blocks"][9][0] == "h2" and _bp["blocks"][11][0] == "h2", _c
        _bp["blocks"] = _bp["blocks"][:9] + _bp["blocks"][11:]
        _bp["faqs"] = [f for i, f in enumerate(_bp["faqs"]) if i == 2]
STATE = {"here": False}  # True kur faqja ka formularin brenda (butonat çojnë te #request në të njëjtën faqe)
AVAIL = list(LANG)
SVC = {s["slug"]: s for s in SERVICES}
PAGES = []


def fhash(rel):
    with open(os.path.join(ROOT, "assets", rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


V = {"css": fhash("css/style.css"), "js": fhash("js/main.js")}


def hl(c): return HL.get(c, c)
def email_for(key): return SUPPORT_EMAILS.get(key) or CFG["support_email"]
def jl(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + "</script>"
def enc(s): return urllib.parse.quote(s.replace("\n", "\r\n"), safe="")


LOGO = ('<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" fill="#0F1B2A"/>'
        '<path d="M8 31 20 9l12 22" fill="none" stroke="#fff" stroke-width="3"/>'
        '<path d="M13.5 23h13" stroke="#C8102E" stroke-width="3"/></svg>')
GLOBE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/>'
         '<path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/></svg>')


# ---------------- JSON-LD ----------------
def org():
    return {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#org", "name": CFG["name"],
            "alternateName": CFG["short"], "url": SITE + "/", "logo": SITE + "/assets/img/logo.svg",
            "areaServed": {"@type": "Country", "name": "Albania"},
            "address": {"@type": "PostalAddress", "addressCountry": "AL", "addressLocality": "Tirana"},
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "url": SITE + "/en/contact/",
                             "availableLanguage": [hl(c) for c in AVAIL]}}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


# ---------------- HEAD / SHELL ----------------
def fonts(c):
    fam = {"ru": "family=Inter+Tight:wght@600;700&family=Source+Sans+3:wght@400;600;700",
           "ar": "family=IBM+Plex+Sans+Arabic:wght@400;600;700"}.get(c, "family=Archivo:wght@600;700&family=Source+Sans+3:wght@400;600;700")
    if c == "zh":
        return ""
    return ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fam}&display=swap">')


def head(c, title, desc, path, schemas=(), alts=None, noindex=False, og_type="website"):
    L = LANG[c]
    ga = ""
    if CFG["ga4"]:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={CFG["ga4"]}"></script>'
              f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{CFG["ga4"]}");</script>')
    alt = ""
    if alts:
        for l, p in alts.items():
            alt += f'<link rel="alternate" hreflang="{hl(l)}" href="{SITE}{p}">'
        alt += f'<link rel="alternate" hreflang="x-default" href="{SITE}/">'
    robots = "noindex, nofollow" if noindex else "index, follow, max-image-preview:large"
    return f"""<!doctype html>
<html lang="{hl(c)}" dir="{L['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{SITE}{path}">
{alt}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="{E(CFG['name'])}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}{path}"><meta property="og:locale" content="{L['locale']}">
<meta property="og:image" content="{SITE}/assets/img/og.png"><meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F1B2A">
<link rel="icon" href="/assets/img/logo.svg" type="image/svg+xml"><link rel="manifest" href="/site.webmanifest">
{fonts(c)}
<link rel="stylesheet" href="/assets/css/style.css?v={V['css']}">
{''.join(jl(s) for s in schemas)}
{ga}
</head>
<body>
<a class="skip" href="#main">{E(L['ui']['skip'])}</a>
"""


def switcher(c, alts):
    L = LANG[c]
    items = "".join(
        f'<li><a href="{p}" hreflang="{hl(l)}" lang="{hl(l)}" data-lang="{l}"{" aria-current=\"true\"" if l == c else ""}>{E(LANG[l]["name"])}</a></li>'
        for l, p in alts.items() if l in LANG)
    return (f'<details class="lang"><summary aria-label="{E(L["ui"]["lang_label"])}">{GLOBE}<span>{E(L["name"])}</span></summary>'
            f'<ul>{items}</ul></details>')


def top(c, alts, path):
    L = LANG[c]; u = L["ui"]
    ins = f"/{c}/insights/" if L["posts"] else "/en/insights/"
    links = [(f"/{c}/solutions/", u["nav_solutions"]), (f"/{c}/how-it-works/", u["nav_how"]), (ins, u["nav_insights"]),
             (f"/{c}/about/", u["nav_about"])]
    nav = ""
    for p, n in links:
        cur = ' aria-current="page"' if (path.startswith(p) and "#" not in p) else ""
        nav += f'<a href="{p}"{cur}>{E(n)}</a>'
    return f"""<div class="util"><div class="container"><p>{E(u['util_reply'])}</p>{switcher(c, alts)}</div></div>
<header class="site-header"><div class="container bar">
<a class="brand" href="/{c}/" aria-label="{E(CFG['name'])}">{LOGO}<span><b>AIEM</b><small>Albanian Industry Engineering and Management</small></span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{E(u['menu'])}</button>
<nav class="nav" id="nav" aria-label="{E(u['menu'])}">{nav}<a class="btn" href="{req_href(c)}" data-track="cta_header">{E(u['nav_contact'])}</a></nav>
</div></header>
<main id="main">
"""


def bottom(c):
    L = LANG[c]; u = L["ui"]
    sv = "".join(f'<li><a href="/{c}/{s["slug"]}/">{E(L["services"][s["slug"]]["name"])}</a></li>' for s in SERVICES)
    ins = f"/{c}/insights/" if L["posts"] else "/en/insights/"
    lg = "".join(f'<li><a href="/{l}/" hreflang="{hl(l)}" lang="{hl(l)}">{E(LANG[l]["name"])}</a></li>' for l in AVAIL)
    return f"""</main>
<div class="mbar"><a class="btn" href="{req_href(c)}" data-track="cta_mobile">{E(u['nav_contact'])}</a></div>
<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><h3>{E(CFG['name'])}</h3><p>{E(u['footer_about'])}</p></div>
<div><h3>{E(u['footer_solutions'])}</h3><ul>{sv}</ul></div>
<div><h3>{E(u['footer_company'])}</h3><ul><li><a href="/{c}/about/">{E(u['nav_about'])}</a></li><li><a href="/{c}/how-it-works/">{E(u['nav_how'])}</a></li><li><a href="{ins}">{E(u['nav_insights'])}</a></li><li><a href="/{c}/privacy/">{E(u['privacy_link'])}</a></li></ul></div>
<div><h3>{E(u['footer_support'])}</h3><ul><li><a href="/{c}/contact/#request">{E(u['footer_send'])}</a></li><li>{E(u['util_email'])}</li></ul></div>
<div><h3>{E(u['footer_languages'])}</h3><ul>{lg}</ul></div>
</div>
<div class="legal"><span>© 2026 {E(CFG['name'])}. {E(u['rights'])}</span><span><a href="/{c}/privacy/">{E(u['privacy_link'])}</a></span></div>
</div></footer>
<script src="/assets/js/main.js?v={V['js']}" defer></script>
</body>
</html>
"""


def crumbs_html(c, items):
    lis = ""
    for i, (n, p) in enumerate(items):
        lis += f'<li aria-current="page">{E(n)}</li>' if i == len(items) - 1 else f'<li><a href="{p}">{E(n)}</a></li>'
    return f'<nav class="crumbs container" aria-label="{E(LANG[c]["ui"]["breadcrumb"])}"><ol>{lis}</ol></nav>'


def req_href(c):
    return "#request" if STATE["here"] else f"/{c}/contact/#request"


def same_path_alts(c, path):
    return {l: path.replace(f"/{c}/", f"/{l}/", 1) for l in AVAIL}


# ---------------- COMPONENTS ----------------
def types_list(c):
    L = LANG[c]; u = L["ui"]
    t = [("general", u["type_general"])]
    t += [(s["slug"], L["services"][s["slug"]]["name"]) for s in SERVICES]
    return t


def request_form(c, pre="general", title=None):
    """Formulari i kërkesës: të dhëna të përgjithshme + përshkrimi i kërkesës. Dërgohet te Google Apps Script,
    që e dërgon me email te adresa e shërbimit të zgjedhur. Pa apps_script_url, hapet emaili i vizitorit si zgjidhje rezervë."""
    L = LANG[c]; u = L["ui"]
    types = types_list(c)
    opts = "".join(f'<option value="{i}"{" selected" if i == pre else ""}>{E(l)}</option>' for i, l in types)
    tl = "".join(f'<option value="{"" if i == 0 else E(o)}">{E(o)}</option>' for i, o in enumerate(u["f_tl_opts"]))
    cfg = {"endpoint": CFG["apps_script_url"], "lang": c, "langName": L["name"],
           "msgs": {"sending": u["f_sending"], "send": u["f_send"], "ok_title": u["f_ok_title"], "ok_text": u["f_ok_text"],
                    "err": u["f_err"], "required": u["f_err_required"], "consent": u["f_err_consent"], "fallback": u["f_fallback"]}}
    if not CFG["apps_script_url"]:   # zgjidhje rezervë: emaili i gatshëm. Adresat futen në faqe vetëm në këtë rast.
        cfg["mail"] = {i: email_for(i) for i, _ in types}
        cfg["labels"] = dict(types)
    return f"""<div class="desk req" id="request" data-req="{E(json.dumps(cfg, ensure_ascii=False))}">
<div class="desk-head"><strong>{E(title or u['desk_title'])}</strong><span>{E(u['desk_reply'])}</span></div>
<div class="desk-body">
<form novalidate>
<fieldset><legend>{E(u['f_details'])}</legend>
<div class="fld"><label for="request-n">{E(u['f_name'])}</label><input id="request-n" name="name" type="text" autocomplete="name" maxlength="100" required></div>
<div class="fld"><label for="request-e">{E(u['f_email'])}</label><input id="request-e" name="email" type="email" autocomplete="email" maxlength="254" required dir="ltr"></div>
<div class="fld-row">
<div class="fld"><label for="request-p">{E(u['f_phone'])}</label><input id="request-p" name="phone" type="tel" autocomplete="tel" maxlength="40" dir="ltr"></div>
<div class="fld"><label for="request-k">{E(u['f_country'])}</label><input id="request-k" name="country" type="text" autocomplete="country-name" maxlength="80" required></div>
</div>
<div class="fld"><label for="request-c">{E(u['f_company'])}</label><input id="request-c" name="company" type="text" autocomplete="organization" maxlength="120"></div>
</fieldset>
<fieldset><legend>{E(u['f_request'])}</legend>
<div class="fld"><label for="request-t">{E(u['f_type'])}</label><select id="request-t" name="type">{opts}</select></div>
<div class="fld"><label for="request-m">{E(u['f_message'])}</label><textarea id="request-m" name="message" rows="6" maxlength="4000" placeholder="{E(u['f_message_ph'])}" aria-describedby="request-h" required></textarea><small id="request-h">{E(u['f_hint'])}</small></div>
<div class="fld"><label for="request-l">{E(u['f_timeline'])}</label><select id="request-l" name="timeline">{tl}</select></div>
</fieldset>
<div class="hp" aria-hidden="true"><label>Website <input name="website" tabindex="-1" autocomplete="off"></label></div>
<label class="consent"><input type="checkbox" name="consent"> <span>{E(u['f_consent'])} <a href="/{c}/privacy/">{E(u['privacy_link'])}</a></span></label>
<p class="req-status" role="alert" tabindex="-1"></p>
<button class="btn btn-block" type="submit">{E(u['f_send'])}</button>
</form>
</div></div>"""


def widget(c, pre="general", title=None):
    return request_form(c, pre, title)


def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs) + "</div>"


def steps_html(c):
    return '<ol class="steps">' + "".join(f"<li><b>{E(s['t'])}</b><span>{E(s['d'])}</span></li>" for s in LANG[c]["ui"]["steps"]) + "</ol>"


def cta_band(c):
    u = LANG[c]["ui"]
    return (f'<section class="cta-band"><div class="container"><h2>{E(u["cta_band_h2"])}</h2>'
            f'<a class="btn" href="{req_href(c)}" data-track="cta_band">{E(u["cta_band_btn"])}</a></div></section>')


def groups_html(c):
    L = LANG[c]; u = L["ui"]
    out = ""
    for g in GROUPS:
        items = "".join(
            f'<li><a href="/{c}/{s["slug"]}/"><b>{E(L["services"][s["slug"]]["name"])}</b><span>{E(L["services"][s["slug"]]["short"])}</span>'
            f'<em>{E(u["services_view"])}<i class="chev"></i></em></a></li>' for s in SERVICES if s["group"] == g)
        out += f'<div class="group"><div><h2>{E(L["groups"][g]["name"])}</h2><p>{E(L["groups"][g]["desc"])}</p></div><ul class="svc-list">{items}</ul></div>'
    return f'<div class="groups">{out}</div>'


def write(path, content):
    fp = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"):
        fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


def add(path, content, alts=None, prio="0.7", freq="monthly", index=True):
    write(path, content)
    if index:
        PAGES.append({"path": path, "alts": alts or {}, "prio": prio, "freq": freq})


# ---------------- PAGES ----------------
def home(c):
    L = LANG[c]; u = L["ui"]; h = L["home"]; path = f"/{c}/"; alts = same_path_alts(c, path)
    sch = [org(), {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": CFG["name"],
                   "inLanguage": hl(c), "publisher": {"@id": SITE + "/#org"}}, faq_schema(h["faq"])]
    ticks = "".join(f"<li>{E(t)}</li>" for t in h["ticks"])
    fields = "".join(f"<li>{E(f)}</li>" for f in u["fields"])
    probs = "".join(
        f'<li><a href="/{c}/{p["slug"]}/"><span class="q">{E(p["p"])}</span>'
        f'<span class="to">{E(L["services"][p["slug"]]["name"])}<i class="chev"></i></span></a></li>' for p in u["problems"])
    body = head(c, h["title"], h["desc"], path, sch, alts) + top(c, alts, path) + f"""
<section class="hero"><div class="container hero-grid">
<div><div class="dim"><span>Tirana · Albania</span><i></i></div>
<h1>{E(h['h1'])}</h1><p class="lead">{E(h['lead'])}</p>
<ul class="ticks">{ticks}</ul></div>
{widget(c)}
</div></section>
<section class="fields-wrap" aria-label="{E(u['fields_label'])}"><div class="container"><ul class="fields">{fields}</ul></div></section>
<section aria-labelledby="pb"><div class="container"><h2 id="pb">{E(u['problems_h2'])}</h2><p class="lead">{E(u['problems_lead'])}</p><ul class="problems">{probs}</ul></div></section>
<section class="alt" id="how" aria-labelledby="hw"><div class="container"><h2 id="hw">{E(u['how_h2'])}</h2><p class="lead">{E(u['how_lead'])}</p>{steps_html(c)}<p class="more"><a class="btn btn-ghost" href="/{c}/how-it-works/" data-track="cta_how">{E(u['how_more'])}</a></p></div></section>
<section aria-labelledby="pr"><div class="container split">
<div><h2 id="pr">{E(u['principles_h2'])}</h2><div class="principles">{''.join(f'<div><h3>{E(p["t"])}</h3><p>{E(p["d"])}</p></div>' for p in u['principles'])}</div></div>
<div class="panel"><h2>{E(u['panel_h2'])}</h2><p>{E(u['panel_p'])}</p><a class="btn btn-ghost" href="/{c}/about/" data-track="cta_about">{E(u['panel_cta'])}</a></div>
</div></section>
<section class="alt" aria-labelledby="fq"><div class="container"><h2 id="fq">{E(u['faq_h2'])}</h2>{faq_html(h['faq'])}</div></section>
{cta_band(c)}""" + bottom(c)
    add(path, body, alts, "1.0", "weekly")


def solutions_hub(c):
    L = LANG[c]; p = L["pages"]["services_hub"]; path = f"/{c}/solutions/"; alts = same_path_alts(c, path)
    cr = [(L["ui"]["home_label"], f"/{c}/"), (p["h1"], path)]
    body = (head(c, p["title"], p["desc"], path, [org(), crumbs_schema(cr)], alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container"><h1>{E(p["h1"])}</h1><p class="lead" style="margin-bottom:36px">{E(p["lead"])}</p>{groups_html(c)}</div></section>' +
            cta_band(c) + bottom(c))
    add(path, body, alts, "0.9")


def rich(c, text):
    """Escape + lidhje të brendshme me sintaksën [[slug|tekst]]."""
    import re
    t = E(text)
    def sub(m):
        slug, label = m.group(1), m.group(2)
        assert slug in SVC, "slug i panjohur në [[...]]: " + slug
        return f'<a href="/{c}/{slug}/">{label}</a>'
    return re.sub(r"\[\[([a-z-]+)\|([^\]]+)\]\]", sub, t)


def deep_html(c, slug):
    """(toc_html, body_html, extra_faqs) për gjuhët që kanë përmbajtje të thellë; ndryshe bosh."""
    d = DEEP.get(c, {}).get("services", {}).get(slug)
    if not d:
        return "", "", []
    out, toc, n = "", [], 0
    for b in d["blocks"]:
        t = b[0]
        if t == "h2":
            n += 1
            toc.append((f"s{n}", b[1]))
            out += f'<h2 id="s{n}">{E(b[1])}</h2>'
        elif t == "h3": out += f"<h3>{E(b[1])}</h3>"
        elif t == "p": out += f"<p>{rich(c, b[1])}</p>"
        elif t == "ul": out += "<ul>" + "".join(f"<li>{rich(c, i)}</li>" for i in b[1]) + "</ul>"
        elif t == "ol": out += "<ol>" + "".join(f"<li>{rich(c, i)}</li>" for i in b[1]) + "</ol>"
        elif t == "note": out += f'<p class="note">{rich(c, b[1])}</p>'
        else: raise ValueError("lloj blloku i panjohur: " + t)
    toc_html = ""
    if toc:
        toc_html = (f'<nav class="toc" aria-label="{E(DEEP[c]["toc"])}"><b>{E(DEEP[c]["toc"])}</b><ol>' +
                    "".join(f'<li><a href="#{i}">{E(h)}</a></li>' for i, h in toc) + "</ol></nav>")
    return toc_html, f'<div class="deep">{out}</div>', [list(x) for x in d.get("faqs", [])]


def service_page(c, s):
    L = LANG[c]; u = L["ui"]; v = L["services"][s["slug"]]
    path = f"/{c}/{s['slug']}/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (u["nav_solutions"], f"/{c}/solutions/"), (v["name"], path)]
    sch = [org(), crumbs_schema(cr), faq_schema(v["faqs"] + deep_html(c, s["slug"])[2]),
           {"@context": "https://schema.org", "@type": "Service", "name": v["name"], "description": v["meta_desc"], "url": SITE + path,
            "inLanguage": hl(c), "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "Country", "name": "Albania"}, "serviceType": v["name"]}]
    inc = "".join(f"<li>{E(i)}</li>" for i in v["includes"])
    dl = "".join(f"<li>{E(i)}</li>" for i in v["deliver"])
    ticks = "".join(f"<li>{E(t)}</li>" for t in L["home"]["ticks"])
    toc, deep, extra = deep_html(c, s["slug"])
    faqs_all = list(v["faqs"]) + extra
    note = f'<p class="note">{E(v["note"])}</p>' if v["note"] else ""
    rel = "".join(f'<a href="/{c}/{r}/"><b>{E(L["services"][r]["name"])}</b><span>{E(L["services"][r]["short"])}</span></a>' for r in s["related"])
    posts = [(i, p) for i, p in enumerate(L["posts"]) if p["service"] == s["slug"]]
    pl = ""
    if posts:
        pl = f'<h2>{E(u["svc_read"])}</h2><ul>' + "".join(f'<li><a href="/{c}/insights/{p["slug"]}/">{E(p["title"])}</a></li>' for _, p in posts) + "</ul>"
    body = head(c, v["meta_title"], v["meta_desc"], path, sch, alts) + top(c, alts, path) + f"""
<div class="svc-hero">{crumbs_html(c, cr)}<div class="container svc-layout">
<div class="content"><h1>{E(v['h1'])}</h1><p class="lead">{E(v['lead'])}</p><ul class="ticks">{ticks}</ul>
<h2>{E(u['svc_includes'])}</h2><ul class="checks">{inc}</ul>
<div class="inline-cta"><p>{E(u['cta_band_h2'])}</p><a class="btn" href="#request" data-track="cta_inline">{E(u['cta_band_btn'])}</a></div>
<h2>{E(u['svc_audience'])}</h2><p>{E(v['audience'])}</p>
<h2>{E(u['svc_deliver'])}</h2><ul class="deliver">{dl}</ul>{note}
{toc}{deep}
<h2>{E(u['svc_how'])}</h2>{steps_html(c)}
<h2>{E(u['svc_faq'])}</h2>{faq_html(faqs_all)}{pl}</div>
<aside class="aside" aria-label="{E(u['desk_title'])}">{widget(c, s['slug'], u['svc_write'])}</aside>
</div></div>
<section class="alt"><div class="container"><h2>{E(u['svc_related'])}</h2><div class="related">{rel}</div></div></section>
{cta_band(c)}""" + bottom(c)
    add(path, body, alts, "0.9")


def how_it_works(c):
    L = LANG[c]; p = L["pages"]["how"]; u = L["ui"]; path = f"/{c}/how-it-works/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (u["nav_how"], path)]
    sch = [org(), crumbs_schema(cr), faq_schema(p["faq"]),
           {"@context": "https://schema.org", "@type": "HowTo", "name": p["h1"], "description": p["desc"], "inLanguage": hl(c),
            "step": [{"@type": "HowToStep", "position": i + 1, "name": st["t"], "text": st["d"]} for i, st in enumerate(p["steps"])]}]
    steps = "".join(
        f'<li><div class="n" aria-hidden="true">{i + 1}</div><div><h3>{E(st["t"])}</h3><p>{E(st["d"])}</p>'
        f'<ul class="checks">{"".join(f"<li>{E(b)}</li>" for b in st["b"])}</ul></div></li>' for i, st in enumerate(p["steps"]))
    need = "".join(f"<li>{E(t)}</li>" for t in p["need"])
    cards = lambda items: "".join(f'<div class="card"><h3>{E(x["t"])}</h3><p>{E(x["d"])}</p></div>' for x in items)
    body = (head(c, p["title"], p["desc"], path, sch, alts) + top(c, alts, path) + crumbs_html(c, cr) + f"""
<section class="page-hero"><div class="container"><h1>{E(p['h1'])}</h1><p class="lead">{E(p['lead'])}</p>
<p><a class="btn" href="#request" data-track="cta_how_hero">{E(p['cta_btn'])}</a></p></div></section>
<section aria-labelledby="pp"><div class="container"><h2 id="pp">{E(p['steps_h2'])}</h2><ol class="process">{steps}</ol></div></section>
<section class="alt" aria-labelledby="nd"><div class="container split">
<div><h2 id="nd">{E(p['need_h2'])}</h2><p>{E(p['need_lead'])}</p><ul class="checks">{need}</ul></div>
<div class="panel"><h2>{E(p['times_h2'])}</h2><p>{E(p['times_p'])}</p></div></div></section>
<section aria-labelledby="pm"><div class="container"><h2 id="pm">{E(p['promise_h2'])}</h2><div class="cards">{cards(p['promise'])}</div></div></section>
<section class="alt" aria-labelledby="md"><div class="container"><h2 id="md">{E(p['models_h2'])}</h2><p class="lead">{E(p['models_lead'])}</p><div class="cards c3">{cards(p['models'])}</div>
<p class="note">{E(p['limits_p'])}</p></div></section>
<section aria-labelledby="fq"><div class="container"><h2 id="fq">{E(p['faq_h2'])}</h2>{faq_html(p['faq'])}</div></section>
<section class="alt" aria-labelledby="rq"><div class="container split"><div class="prose"><h2 id="rq">{E(p['cta_h2'])}</h2><p>{E(p['cta_p'])}</p></div><div>{widget(c)}</div></div></section>
""" + bottom(c))
    add(path, body, alts, "0.9", "monthly")


def about(c):
    L = LANG[c]; p = L["pages"]["about"]; u = L["ui"]; path = f"/{c}/about/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    sch = [org(), crumbs_schema(cr), {"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + path, "name": p["title"],
                                      "inLanguage": hl(c), "about": {"@id": SITE + "/#org"}}]
    who = "".join(f"<p>{E(t)}</p>" for t in p["who"])
    cards = lambda items: "".join(f'<div class="card"><h3>{E(x["t"])}</h3><p>{E(x["d"])}</p></div>' for x in items)
    clients = "".join(f"<li>{E(t)}</li>" for t in p["clients"])
    body = (head(c, p["title"], p["desc"], path, sch, alts) + top(c, alts, path) + crumbs_html(c, cr) + f"""
<section class="page-hero"><div class="container"><h1>{E(p['h1'])}</h1><p class="lead">{E(p['lead'])}</p></div></section>
<section aria-labelledby="wh"><div class="container split">
<div class="prose"><h2 id="wh">{E(p['who_h2'])}</h2>{who}</div>
<div class="panel"><h2>{E(p['mission_h2'])}</h2><p>{E(p['mission_p'])}</p></div></div></section>
<section class="alt" aria-labelledby="wd"><div class="container"><h2 id="wd">{E(p['do_h2'])}</h2><p class="lead" style="margin-bottom:28px">{E(p['do_lead'])}</p>{groups_html(c)}</div></section>
<section aria-labelledby="wy"><div class="container"><h2 id="wy">{E(p['why_h2'])}</h2><div class="cards">{cards(p['why'])}</div></div></section>
<section class="alt" aria-labelledby="cl"><div class="container split">
<div><h2 id="cl">{E(p['clients_h2'])}</h2><ul class="checks">{clients}</ul></div>
<div><h2>{E(p['values_h2'])}</h2><div class="principles">{''.join(f'<div><h3>{E(x["t"])}</h3><p>{E(x["d"])}</p></div>' for x in p['values'])}</div></div></div></section>
<section aria-labelledby="lm"><div class="container split"><div class="prose"><h2 id="lm">{E(p['how_h2'])}</h2><p>{E(p['how_p'])}</p><p><a class="btn btn-ghost" href="/{c}/how-it-works/" data-track="cta_about_how">{E(p['how_cta'])}</a></p></div>
<div class="panel"><h2>{E(p['limits_h2'])}</h2><p>{E(p['limits_p'])}</p></div></div></section>
<section class="cta-band"><div class="container"><h2>{E(p['cta_h2'])}</h2><a class="btn" href="/{c}/contact/#request" data-track="cta_about_band">{E(p['cta_btn'])}</a></div></section>
""" + bottom(c))
    add(path, body, alts, "0.7", "monthly")


def contact(c):
    L = LANG[c]; p = L["pages"]["contact"]; u = L["ui"]; path = f"/{c}/contact/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    sch = [org(), crumbs_schema(cr), {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + path, "inLanguage": hl(c)}]
    tips = "".join(f"<li>{E(t)}</li>" for t in p["tips"])
    body = (head(c, p["title"], p["desc"], path, sch, alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container split"><div class="prose"><h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>'
            f'<h2>{E(p["tips_h2"])}</h2><ul>{tips}</ul><h2>{E(p["response_h2"])}</h2><p>{E(p["response_p"])}</p><p class="note">{E(p["confidentiality_p"])}</p></div>'
            f'<div>{widget(c)}</div></div></section>' + bottom(c))
    add(path, body, alts, "0.8", "yearly")


def privacy(c):
    L = LANG[c]; p = L["pages"]["privacy"]; u = L["ui"]; path = f"/{c}/privacy/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    secs = "".join(f"<h2>{E(a)}</h2><p>{E(b)}</p>" for a, b in p["sections"])
    body = (head(c, p["title"], p["desc"], path, [crumbs_schema(cr)], alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container prose"><h1>{E(p["h1"])}</h1><p class="note">{E(p["note"])}</p>{secs}</div></section>' + bottom(c))
    add(path, body, alts, "0.2", "yearly")


def insights(c):
    L = LANG[c]
    if not L["posts"]:
        return
    p = L["pages"]["insights"]; u = L["ui"]; path = f"/{c}/insights/"
    alts = {l: f"/{l}/insights/" for l in AVAIL if LANG[l]["posts"]}
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    items = "".join(f'<li><a href="/{c}/insights/{x["slug"]}/">{E(x["title"])}</a><p>{E(x["desc"])}</p></li>' for x in L["posts"])
    body = (head(c, p["title"], p["desc"], path, [org(), crumbs_schema(cr)], alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container"><h1>{E(p["h1"])}</h1><p class="lead" style="margin-bottom:28px">{E(p["lead"])}</p><ul class="posts">{items}</ul></div></section>' +
            cta_band(c) + bottom(c))
    add(path, body, alts, "0.6", "weekly")
    for i, x in enumerate(L["posts"]):
        path = f"/{c}/insights/{x['slug']}/"
        alts = {l: f"/{l}/insights/{LANG[l]['posts'][i]['slug']}/" for l in AVAIL if len(LANG[l]["posts"]) > i}
        cr2 = [(u["home_label"], f"/{c}/"), (p["h1"], f"/{c}/insights/"), (x["title"], path)]
        parts = ""
        for t in x["body"]:
            if t[0] == "p": parts += f"<p>{E(t[1])}</p>"
            elif t[0] == "h2": parts += f"<h2>{E(t[1])}</h2>"
            elif t[0] == "ul": parts += "<ul>" + "".join(f"<li>{E(a)}</li>" for a in t[1]) + "</ul>"
            elif t[0] == "note": parts += f'<p class="note">{E(t[1])}</p>'
        art = {"@context": "https://schema.org", "@type": "Article", "headline": x["title"], "description": x["desc"], "datePublished": CFG["date"],
               "dateModified": CFG["date"], "inLanguage": hl(c), "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"},
               "mainEntityOfPage": SITE + path, "image": SITE + "/assets/img/og.png"}
        sname = L["services"][x["service"]]["name"]
        title = x["title"] if len(x["title"]) < 52 else x["title"][:50].rsplit(" ", 1)[0]
        body = (head(c, title + " | AIEM", x["desc"], path, [org(), crumbs_schema(cr2), art], alts, og_type="article") + top(c, alts, path) + crumbs_html(c, cr2) +
                f'<article><section><div class="container prose"><p class="meta">{E(p["published"])} {CFG["date"]}</p><h1>{E(x["title"])}</h1>{parts}'
                f'<p>{E(p["cta_p"])} <a href="/{c}/{x["service"]}/">{E(sname)}</a></p></div></section></article>' + cta_band(c) + bottom(c))
        add(path, body, alts, "0.6")


def root_picker():
    alts = {l: f"/{l}/" for l in AVAIL}
    L = LANG["en"]
    items = "".join(f'<li><a href="/{l}/" hreflang="{hl(l)}" lang="{hl(l)}" data-lang="{l}">{E(LANG[l]["name"])}</a></li>' for l in AVAIL)
    title = "AIEM | Albanian Industry Engineering and Management"
    desc = L["home"]["desc"]
    body = head("en", title, desc, "/", [org()], alts).replace('<a class="skip"', '<a class="skip"') + f"""
<main id="main" class="picker"><section><div class="container">
<a class="brand" href="/" style="margin-bottom:28px">{LOGO}<span><b>AIEM</b></span></a>
<h1>Albanian Industry Engineering and Management</h1>
<p class="lead">{E(L['home']['lead'])}</p>
<ul class="langs">{items}</ul>
</div></section></main>
<script src="/assets/js/main.js?v={V['js']}" defer></script>
</body></html>"""
    add("/", body, alts, "1.0", "weekly")


def not_found():
    alts = {l: f"/{l}/" for l in AVAIL}
    u = LANG["en"]["ui"]
    body = (head("en", "Page not found | AIEM", u["not_found_p"], "/404.html", noindex=True) + top("en", alts, "/404.html") +
            f'<section><div class="container prose"><h1>{E(u["not_found_h1"])}</h1><p class="lead">{E(u["not_found_p"])}</p>'
            f'<p><a class="btn" href="/en/">{E(u["home_label"])}</a> <a class="btn btn-ghost" href="/en/solutions/">{E(u["nav_solutions"])}</a></p></div></section>' + bottom("en"))
    write("/404.html", body)


# ---------------- STATIC FILES ----------------
def clean():
    legacy = ["sherbimet", "blog", "kontakt", "rreth-nesh", "bashkohu-si-partner", "politika-e-privatesise", "multumim"]
    names = legacy + LANGS + ["assets", "index.html", "404.html", "sitemap.xml", "robots.txt", "site.webmanifest", "_headers", ".htaccess", "vercel.json"]
    for n in names:
        t = os.path.join(OUT, n)
        if os.path.isdir(t): shutil.rmtree(t)
        elif os.path.exists(t): os.remove(t)


def static_files():
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    with open(os.path.join(OUT, "assets/img/logo.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#0F1B2A"/>'
                '<path d="M8 31 20 9l12 22" fill="none" stroke="#fff" stroke-width="3"/><path d="M13.5 23h13" stroke="#C8102E" stroke-width="3"/></svg>')
    urls = ""
    for p in PAGES:
        xl = "".join(f'<xhtml:link rel="alternate" hreflang="{hl(l)}" href="{SITE}{ap}"/>' for l, ap in p["alts"].items())
        if p["alts"]:
            xl += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>'
        urls += f'<url><loc>{SITE}{p["path"]}</loc><lastmod>{CFG["date"]}</lastmod><changefreq>{p["freq"]}</changefreq><priority>{p["prio"]}</priority>{xl}</url>'
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                'xmlns:xhtml="http://www.w3.org/1999/xhtml">' + urls + "</urlset>")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(OUT, "site.webmanifest"), "w") as f:
        json.dump({"name": CFG["name"], "short_name": CFG["short"], "start_url": "/", "display": "browser", "background_color": "#F7F9FB",
                   "theme_color": "#0F1B2A", "icons": [{"src": "/assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, f)
    redirects = [{"source": "/", "has": [{"type": "header", "key": "accept-language", "value": f"^{c}.*"}],
                  "destination": f"/{c}/", "permanent": False} for c in AVAIL]
    for suffix in ("", "/"):   # faqja e hequr "për profesionistët"
        redirects.append({"source": f"/:lang/network{suffix}", "destination": "/:lang/", "permanent": True})
    for sv in SERVICES:
        for suffix in ("", "/"):
            redirects.append({"source": f"/:lang/solutions/{sv['slug']}{suffix}", "destination": f"/:lang/{sv['slug']}/", "permanent": True})
    vc = {"framework": None, "buildCommand": None, "installCommand": None, "trailingSlash": True, "redirects": redirects,
          "headers": [
              {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
              {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"},
                                              {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                                              {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]}]}
    with open(os.path.join(OUT, "vercel.json"), "w") as f:
        json.dump(vc, f, indent=2)


GS_TEMPLATE = r'''/**
 * AIEM: Google Apps Script që pranon kërkesat nga faqja dhe i dërgon me email te desku i duhur.
 *
 * KJO SKEDË GJENEROHET nga src/build.py. Mos e ndrysho me dorë: ndrysho src/config.py
 * (adresat, Sheet ID, gjuha e ekipit) dhe ekzekuto python3 src/build.py për ta rigjeneruar.
 * Udhëzimet e deploy-it: apps-script/README.md
 */
var CONFIG = {
  SHEET_ID: "__SHEET_ID__",       // opsionale: ID e Google Sheet për kopje rezervë të kërkesave
  SEND_AUTOREPLY: __AUTOREPLY_ON__,  // konfirmim automatik te vizitori
  MAX_PER_HOUR: 60,               // mbrojtje nga spami: maksimumi i kërkesave në orë
  MIN_FILL_MS: 2500               // kërkesat më të shpejta se kaq trajtohen si bot
};

// Adresa e deskut për çdo lloj suporti (nga src/config.py)
var ROUTES = __ROUTES__;

// Emrat e llojeve të suportit në secilën gjuhë
var LABELS = __LABELS__;

// Konfirmimi automatik për vizitorin, në gjuhën e tij
var AUTOREPLY = __AUTOREPLY__;

// Etiketat e emailit që merr ekipi
var TEAM = __TEAM__;

var EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/;

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
function clean_(s, max) {
  return String(s == null ? "" : s).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, "").trim().slice(0, max);
}
function oneLine_(s, max) {
  return clean_(s, max).replace(/[\r\n]+/g, " ");
}
function fill_(tpl, vars) {
  var out = String(tpl);
  for (var k in vars) out = out.split("{" + k + "}").join(vars[k]);
  return out;
}

function doGet() {
  return json_({ ok: true, service: "AIEM request desk" });
}

function doPost(e) {
  try {
    var raw = (e && e.postData && e.postData.contents) || "";
    if (!raw || raw.length > 20000) return json_({ ok: false, error: "size" });
    var d = JSON.parse(raw);

    // Honeypot: një bot plotëson fushën e fshehur. Pretendojmë sukses pa dërguar asgjë.
    if (clean_(d.website, 200)) return json_({ ok: true, ref: "AIEM-0000" });
    if (Number(d.elapsed) < CONFIG.MIN_FILL_MS) return json_({ ok: false, error: "fast" });

    var type = ROUTES[d.type] ? d.type : "general";
    var lang = LABELS[d.lang] ? d.lang : "en";
    var name = oneLine_(d.name, 100);
    var email = oneLine_(d.email, 254);
    var company = oneLine_(d.company, 120);
    var phone = oneLine_(d.phone, 40);
    var country = oneLine_(d.country, 80);
    var timeline = oneLine_(d.timeline, 60);
    var message = clean_(d.message, 4000);
    if (name.length < 2 || !EMAIL_RE.test(email) || country.length < 2 || message.length < 30) return json_({ ok: false, error: "invalid" });

    if (MailApp.getRemainingDailyQuota() < 4) return json_({ ok: false, error: "quota" });

    // Kufizime: një kërkesë në minutë për të njëjtin email dhe lloj, dhe një tavan global në orë
    var cache = CacheService.getScriptCache();
    var digest = Utilities.computeDigest(Utilities.DigestAlgorithm.MD5, email.toLowerCase() + "|" + type);
    var rlKey = "rl_" + Utilities.base64EncodeWebSafe(digest);
    if (cache.get(rlKey)) return json_({ ok: false, error: "rate" });
    var hourKey = "h_" + Utilities.formatDate(new Date(), "UTC", "yyyyMMddHH");
    var count = Number(cache.get(hourKey) || 0);
    if (count >= CONFIG.MAX_PER_HOUR) return json_({ ok: false, error: "busy" });
    cache.put(rlKey, "1", 60);
    cache.put(hourKey, String(count + 1), 3600);

    var ref = "AIEM-" + Utilities.formatDate(new Date(), "UTC", "yyMMdd") + "-" + Math.random().toString(36).slice(2, 6).toUpperCase();
    var to = ROUTES[type];
    var T = TEAM.labels;
    var typeLabel = LABELS[TEAM.lang][type] || type;
    var page = oneLine_(d.page, 300);
    var src = [d.utm_source, d.utm_medium, d.utm_campaign, d.gclid ? "gclid" : ""].map(function (x) { return oneLine_(x, 80); }).filter(String).join(" / ");

    var subject = "[" + typeLabel + "] " + T.subject + " " + ref + " | " + name;
    var body = [
      T.intro, "",
      T.type + ": " + typeLabel,
      T.ref + ": " + ref,
      T.name + ": " + name,
      T.email + ": " + email,
      T.phone + ": " + (phone || "-"),
      T.company + ": " + (company || "-"),
      T.country + ": " + country,
      T.timeline + ": " + (timeline || "-"),
      T.lang + ": " + lang,
      T.page + ": " + (page || "-"),
      T.utm + ": " + (src || "-"),
      "", T.message + ":", message, "", T.reply
    ].join("\n");

    // Emaili për ekipin: Reply-To = vizitori, ndaj "Reply" i përgjigjet atij drejtpërdrejt
    MailApp.sendEmail({ to: to, subject: subject, body: body, replyTo: email, name: "AIEM Portal" });

    // Konfirmimi për vizitorin, në gjuhën e tij. Përgjigjet e tij shkojnë te desku i duhur.
    if (CONFIG.SEND_AUTOREPLY) {
      try {
        var ar = AUTOREPLY[lang];
        var vars = { name: name, ref: ref, type: LABELS[lang][type] || type };
        MailApp.sendEmail({ to: email, subject: fill_(ar.subject, vars), body: fill_(ar.body, vars), name: "AIEM", replyTo: to });
      } catch (err1) { console.error("autoreply: " + err1); }
    }

    // Kopje rezervë në Google Sheet (opsionale)
    if (CONFIG.SHEET_ID) {
      try {
        SpreadsheetApp.openById(CONFIG.SHEET_ID).getSheets()[0].appendRow(
          [new Date(), ref, type, to, name, email, phone, company, country, timeline, message, lang, page, src]);
      } catch (err2) { console.error("sheet: " + err2); }
    }

    return json_({ ok: true, ref: ref });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: "server" });
  }
}

/** Test nga editori: Run > testSubmit. Dërgon një kërkesë provë te adresa "general" dhe te ju. */
function testSubmit() {
  var me = Session.getEffectiveUser().getEmail();
  var res = doPost({ postData: { contents: JSON.stringify({
    type: "general", name: "Test AIEM", email: me, phone: "+355 00 000 0000", company: "Test", country: "Albania", timeline: "",
    message: "Kjo është një kërkesë provë nga editori i Apps Script, për të kontrolluar që emaili arrin te adresa e duhur.",
    lang: "sq", page: "/test/", elapsed: 99999, website: ""
  }) } });
  Logger.log(res.getContent());
}
'''

GS_README = '''# Apps Script për formularin AIEM

Ky skript pranon kërkesat nga faqja dhe i dërgon me email te adresa e llojit të suportit që zgjodhi vizitori
(inxhinieri mekanike, elektrike, BPP, hyrje në treg, shoqëri, partneritete, turizëm dentar, prona). Vizitori merr automatikisht një konfirmim në gjuhën e tij.

## Si ta vësh në punë (5 minuta)
1. Hap https://script.google.com dhe kliko **New project**.
2. Fshi kodin ekzistues dhe ngjit përmbajtjen e `Code.gs` (në këtë dosje). Ruaje (Ctrl+S).
3. Zgjidh funksionin `testSubmit` dhe kliko **Run**. Google kërkon autorizim (dërgim emaili dhe, nëse e përdor, Google Sheets).
   Kontrollo që mbërrin një email provë te adresa "general" dhe te ti.
4. Kliko **Deploy > New deployment > Web app**:
   - Execute as: **Me**
   - Who has access: **Anyone**
   Kliko Deploy dhe kopjo **Web app URL** (mbaron me `/exec`).
5. Në `src/config.py` vendos URL-në te `apps_script_url`, pastaj ekzekuto `python3 src/build.py`, commit dhe push.
   Që nga ai moment formulari dërgon kërkesat përmes Apps Script. Para kësaj, formulari hap emailin e vizitorit si zgjidhje rezervë.

## Kur ndryshon adresa ose tekstet
Ndrysho `src/config.py`, ekzekuto `python3 src/build.py`, ngjit `Code.gs` të ri në Apps Script dhe bëj
**Deploy > Manage deployments > Edit > New version**. URL-ja mbetet e njëjtë.

## Opsionale
- Kopje rezervë: krijo një Google Sheet, kopjo ID-në nga adresa e tij dhe vendose te `sheet_id` në `src/config.py`.
- Gjuha e emailit që merr ekipi: `team_lang` ("sq" ose "en").
- Mos dërgo konfirmim te vizitori: `send_autoreply: False`.

## Limite që duhet t'i dish
- Llogaria e zakonshme Gmail dërgon deri rreth 100 marrës në ditë, Google Workspace rreth 1500. Çdo kërkesë përdor 1 deri 2 marrës
  (ekipi plus konfirmimi). Skripti ndalon kur mbeten pak kuota.
- Emailet dërgohen nga llogaria që zotëron skriptin (emri shfaqet si "AIEM Portal"). Për një dërgues me domenin tuaj, përdorni
  një llogari Workspace me aliasin përkatës.
- Mbrojtja nga spami: fushë e fshehur, kohë minimale plotësimi, një kërkesë në minutë për të njëjtin email dhe lloj, tavan 60 në orë.
  Konfirmimi automatik dërgohet te adresa që jep vizitori, ndaj tavani është i qëllimshëm. Nëse e do më të sigurt, vendos
  `send_autoreply: False`.
- Këto adresa duhet të ekzistojnë dhe të monitorohen: një email te adresë që nuk ekziston humbet pa njoftim.
'''


def apps_script():
    team_lang = CFG["team_lang"] if CFG["team_lang"] in TEAM else "en"
    values = {"__ROUTES__": dict(SUPPORT_EMAILS), "__LABELS__": {c: dict(types_list(c)) for c in AVAIL},
              "__AUTOREPLY__": {c: {"subject": LANG[c]["ui"]["autoreply_subject"], "body": LANG[c]["ui"]["autoreply_body"]} for c in AVAIL},
              "__TEAM__": {"lang": team_lang, "labels": TEAM[team_lang]}}
    code = GS_TEMPLATE
    for k, v in values.items():
        code = code.replace(k, json.dumps(v, ensure_ascii=False, indent=2))
    code = code.replace("__SHEET_ID__", CFG["sheet_id"]).replace("__AUTOREPLY_ON__", "true" if CFG["send_autoreply"] else "false")
    d = os.path.join(OUT, "apps-script")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "Code.gs"), "w", encoding="utf-8") as f:
        f.write(code)
    with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
        f.write(GS_README)


if __name__ == "__main__":
    clean()
    root_picker()
    for c in AVAIL:
        STATE["here"] = True
        home(c)
        for s in SERVICES: service_page(c, s)
        contact(c); how_it_works(c)
        STATE["here"] = False
        solutions_hub(c); about(c); privacy(c); insights(c)
    not_found()
    static_files()
    apps_script()
    print(f"OK: {len(PAGES)} faqe, {len(AVAIL)} gjuhë ({', '.join(AVAIL)}).")
    miss = [c for c in LANGS if c not in LANG]
    if miss: print("KUJDES: mungojnë gjuhët:", ", ".join(miss))
    if any("@" not in v for v in ROUTES.values()):
        print("KUJDES: ROUTES ka adresa pa @ (përdorin mail_domain shembull). Vendos adresat e plota.")
    if not CFG["apps_script_url"]:
        print("KUJDES: apps_script_url është bosh: formulari hap emailin e vizitorit (zgjidhje rezervë) në vend ta dërgojë përmes Apps Script.")
