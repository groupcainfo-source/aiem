# -*- coding: utf-8 -*-
"""Gjeneron portalin shumëgjuhësh në rrënjën e repo-s:  python3 src/build.py"""
import os, json, shutil, hashlib, html, importlib.util, urllib.parse
from config import CFG, SUPPORT_EMAILS, LANGS, GROUPS, SERVICES

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


LANG = {c: load(c) for c in LANGS if os.path.exists(os.path.join(ROOT, "i18n", c + ".py"))}
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
            "alternateName": CFG["short"], "url": SITE + "/", "logo": SITE + "/assets/img/logo.svg", "email": CFG["support_email"],
            "areaServed": {"@type": "Country", "name": "Albania"},
            "address": {"@type": "PostalAddress", "addressCountry": "AL", "addressLocality": "Tirana"},
            "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "email": CFG["support_email"],
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
    links = [(f"/{c}/solutions/", u["nav_solutions"]), (f"/{c}/#how", u["nav_how"]), (ins, u["nav_insights"]),
             (f"/{c}/about/", u["nav_about"]), (f"/{c}/network/", u["nav_network"])]
    nav = ""
    for p, n in links:
        cur = ' aria-current="page"' if (path.startswith(p) and "#" not in p) else ""
        nav += f'<a href="{p}"{cur}>{E(n)}</a>'
    return f"""<div class="util"><div class="container"><p>{E(u['util_reply'])}</p>{switcher(c, alts)}</div></div>
<header class="site-header"><div class="container bar">
<a class="brand" href="/{c}/" aria-label="{E(CFG['name'])}">{LOGO}<span><b>AIEM</b><small>Albanian Industry Engineering and Management</small></span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{E(u['menu'])}</button>
<nav class="nav" id="nav" aria-label="{E(u['menu'])}">{nav}<a class="btn" href="/{c}/contact/#desk" data-track="cta_header">{E(u['nav_contact'])}</a></nav>
</div></header>
<main id="main">
"""


def bottom(c):
    L = LANG[c]; u = L["ui"]
    sv = "".join(f'<li><a href="/{c}/solutions/{s["slug"]}/">{E(L["services"][s["slug"]]["name"])}</a></li>' for s in SERVICES)
    ins = f"/{c}/insights/" if L["posts"] else "/en/insights/"
    lg = "".join(f'<li><a href="/{l}/" hreflang="{hl(l)}" lang="{hl(l)}">{E(LANG[l]["name"])}</a></li>' for l in AVAIL)
    em = CFG["support_email"]
    return f"""</main>
<div class="mbar"><a class="btn" href="/{c}/contact/#desk" data-track="cta_mobile">{E(u['nav_contact'])}</a></div>
<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><h3>{E(CFG['name'])}</h3><p>{E(u['footer_about'])}</p></div>
<div><h3>{E(u['footer_solutions'])}</h3><ul>{sv}</ul></div>
<div><h3>{E(u['footer_company'])}</h3><ul><li><a href="/{c}/about/">{E(u['nav_about'])}</a></li><li><a href="{ins}">{E(u['nav_insights'])}</a></li><li><a href="/{c}/network/">{E(u['nav_network'])}</a></li><li><a href="/{c}/privacy/">{E(u['privacy_link'])}</a></li></ul></div>
<div><h3>{E(u['footer_support'])}</h3><ul><li><a href="mailto:{em}">{E(em)}</a></li><li>{E(u['util_email'])}</li><li><a href="/{c}/contact/#desk">{E(u['nav_contact'])}</a></li></ul></div>
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


def same_path_alts(c, path):
    return {l: path.replace(f"/{c}/", f"/{l}/", 1) for l in AVAIL}


# ---------------- COMPONENTS ----------------
def types_list(c):
    L = LANG[c]; u = L["ui"]
    t = [("general", u["type_general"])]
    t += [(s["slug"], L["services"][s["slug"]]["name"]) for s in SERVICES]
    t.append(("network", u["type_network"]))
    return t


def desk(c, fid, pre="general", title=None):
    L = LANG[c]; u = L["ui"]
    types = types_list(c)
    label = dict(types)[pre]
    em = email_for(pre)
    subj = u["mail_subject"].replace("{type}", label)
    body = u["mail_body"].replace("{type}", label).replace("{lang}", L["name"])
    mailto = f"mailto:{em}?subject={enc(subj)}&body={enc(body)}"
    gm = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(em)}&su={enc(subj)}&body={enc(body)}"
    ol = f"https://outlook.office.com/mail/deeplink/compose?to={urllib.parse.quote(em)}&subject={enc(subj)}&body={enc(body)}"
    cfg = {"types": [{"id": i, "label": l, "email": email_for(i)} for i, l in types], "subject": u["mail_subject"],
           "body": u["mail_body"], "lang": L["name"], "copied": u["desk_copied"], "copy": u["desk_copy"]}
    opts = "".join(f'<option value="{i}"{" selected" if i == pre else ""}>{E(l)}</option>' for i, l in types)
    return f"""<div class="desk" id="{fid}" data-desk="{E(json.dumps(cfg, ensure_ascii=False))}">
<div class="desk-head"><strong>{E(title or u['desk_title'])}</strong><span>{E(u['desk_reply'])}</span></div>
<div class="desk-body">
<label class="desk-step" for="{fid}-t">{E(u['desk_pick'])}</label>
<select id="{fid}-t" name="type">{opts}</select>
<span class="desk-step">{E(u['desk_to'])}</span>
<output class="desk-email" aria-live="polite">{E(em)}</output>
<a class="btn btn-block" data-desk-mail href="{E(mailto)}">{E(u['desk_write'])}</a>
<div class="desk-alt"><a data-desk-gmail href="{E(gm)}" target="_blank" rel="noopener">{E(u['desk_gmail'])}</a><a data-desk-outlook href="{E(ol)}" target="_blank" rel="noopener">{E(u['desk_outlook'])}</a><button type="button" data-desk-copy>{E(u['desk_copy'])}</button></div>
<p class="desk-note">{E(u['desk_note'])}</p>
</div></div>"""


def faq_html(faqs):
    return '<div class="faq">' + "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs) + "</div>"


def steps_html(c):
    return '<ol class="steps">' + "".join(f"<li><b>{E(s['t'])}</b><span>{E(s['d'])}</span></li>" for s in LANG[c]["ui"]["steps"]) + "</ol>"


def cta_band(c):
    u = LANG[c]["ui"]
    return (f'<section class="cta-band"><div class="container"><h2>{E(u["cta_band_h2"])}</h2>'
            f'<a class="btn" href="/{c}/contact/#desk" data-track="cta_band">{E(u["cta_band_btn"])}</a></div></section>')


def groups_html(c):
    L = LANG[c]; u = L["ui"]
    out = ""
    for g in GROUPS:
        items = "".join(
            f'<li><a href="/{c}/solutions/{s["slug"]}/"><b>{E(L["services"][s["slug"]]["name"])}</b><span>{E(L["services"][s["slug"]]["short"])}</span>'
            f'<em>{E(u["services_view"])}<i class="chev"></i></em></a></li>' for s in SERVICES if s["group"] == g)
        out += f'<div class="group"><div><h3>{E(L["groups"][g]["name"])}</h3><p>{E(L["groups"][g]["desc"])}</p></div><ul class="svc-list">{items}</ul></div>'
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
        f'<li><a href="/{c}/solutions/{p["slug"]}/"><span class="q">{E(p["p"])}</span>'
        f'<span class="to">{E(L["services"][p["slug"]]["name"])}<i class="chev"></i></span></a></li>' for p in u["problems"])
    body = head(c, h["title"], h["desc"], path, sch, alts) + top(c, alts, path) + f"""
<section class="hero"><div class="container hero-grid">
<div><div class="dim"><span>Tirana · Albania</span><i></i></div>
<h1>{E(h['h1'])}</h1><p class="lead">{E(h['lead'])}</p>
<ul class="ticks">{ticks}</ul></div>
{desk(c, 'desk')}
</div></section>
<section class="fields-wrap" aria-label="{E(u['fields_label'])}"><div class="container"><ul class="fields">{fields}</ul></div></section>
<section aria-labelledby="pb"><div class="container"><h2 id="pb">{E(u['problems_h2'])}</h2><p class="lead">{E(u['problems_lead'])}</p><ul class="problems">{probs}</ul></div></section>
<section class="alt" id="how" aria-labelledby="hw"><div class="container"><h2 id="hw">{E(u['how_h2'])}</h2><p class="lead">{E(u['how_lead'])}</p>{steps_html(c)}</div></section>
<section aria-labelledby="pr"><div class="container split">
<div><h2 id="pr">{E(u['principles_h2'])}</h2><div class="principles">{''.join(f'<div><h3>{E(p["t"])}</h3><p>{E(p["d"])}</p></div>' for p in u['principles'])}</div></div>
<div class="panel"><h2>{E(u['net_h2'])}</h2><p>{E(u['net_p'])}</p><a class="btn btn-ghost" href="/{c}/network/" data-track="cta_network">{E(u['net_cta'])}</a></div>
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


def service_page(c, s):
    L = LANG[c]; u = L["ui"]; v = L["services"][s["slug"]]
    path = f"/{c}/solutions/{s['slug']}/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (u["nav_solutions"], f"/{c}/solutions/"), (v["name"], path)]
    sch = [org(), crumbs_schema(cr), faq_schema(v["faqs"]),
           {"@context": "https://schema.org", "@type": "Service", "name": v["name"], "description": v["meta_desc"], "url": SITE + path,
            "inLanguage": hl(c), "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "Country", "name": "Albania"}, "serviceType": v["name"]}]
    inc = "".join(f"<li>{E(i)}</li>" for i in v["includes"])
    dl = "".join(f"<li>{E(i)}</li>" for i in v["deliver"])
    note = f'<p class="note">{E(v["note"])}</p>' if v["note"] else ""
    rel = "".join(f'<a href="/{c}/solutions/{r}/"><b>{E(L["services"][r]["name"])}</b><span>{E(L["services"][r]["short"])}</span></a>' for r in s["related"])
    posts = [(i, p) for i, p in enumerate(L["posts"]) if p["service"] == s["slug"]]
    pl = ""
    if posts:
        pl = f'<h2>{E(u["svc_read"])}</h2><ul>' + "".join(f'<li><a href="/{c}/insights/{p["slug"]}/">{E(p["title"])}</a></li>' for _, p in posts) + "</ul>"
    body = head(c, v["meta_title"], v["meta_desc"], path, sch, alts) + top(c, alts, path) + f"""
<div class="svc-hero">{crumbs_html(c, cr)}<div class="container svc-layout">
<div class="content"><h1>{E(v['h1'])}</h1><p class="lead">{E(v['lead'])}</p>
<h2>{E(u['svc_includes'])}</h2><ul class="checks">{inc}</ul>
<h2>{E(u['svc_audience'])}</h2><p>{E(v['audience'])}</p>
<h2>{E(u['svc_deliver'])}</h2><ul class="deliver">{dl}</ul>{note}
<h2>{E(u['svc_how'])}</h2>{steps_html(c)}
<h2>{E(u['svc_faq'])}</h2>{faq_html(v['faqs'])}{pl}</div>
<aside class="aside" aria-label="{E(u['desk_title'])}">{desk(c, 'desk', s['slug'], u['svc_write'])}</aside>
</div></div>
<section class="alt"><div class="container"><h2>{E(u['svc_related'])}</h2><div class="related">{rel}</div></div></section>
{cta_band(c)}""" + bottom(c)
    add(path, body, alts, "0.9")


def about(c):
    L = LANG[c]; p = L["pages"]["about"]; u = L["ui"]; path = f"/{c}/about/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    paras = "".join(f"<p>{E(t)}</p>" for t in p["paras"])
    body = (head(c, p["title"], p["desc"], path, [org(), crumbs_schema(cr)], alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container split"><div class="prose"><h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>{paras}</div>'
            f'<div class="panel"><h2>{E(u["desk_title"])}</h2><p>{E(u["how_lead"])}</p><a class="btn btn-ghost" href="/{c}/contact/#desk">{E(p["cta"])}</a></div></div></section>' + bottom(c))
    add(path, body, alts, "0.5", "yearly")


def contact(c):
    L = LANG[c]; p = L["pages"]["contact"]; u = L["ui"]; path = f"/{c}/contact/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    sch = [org(), crumbs_schema(cr), {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + path, "inLanguage": hl(c)}]
    types = types_list(c)
    types_html = ""
    if len({email_for(i) for i, _ in types}) > 1:
        types_html = (f'<h2>{E(u["contact_types_h2"])}</h2><ul class="types">' +
                      "".join(f'<li><span>{E(l)}</span><a href="mailto:{email_for(i)}">{E(email_for(i))}</a></li>' for i, l in types) + "</ul>")
    tips = "".join(f"<li>{E(t)}</li>" for t in p["tips"])
    body = (head(c, p["title"], p["desc"], path, sch, alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container split"><div class="prose"><h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>'
            f'<h2>{E(p["tips_h2"])}</h2><ul>{tips}</ul><h2>{E(p["response_h2"])}</h2><p>{E(p["response_p"])}</p><p class="note">{E(p["confidentiality_p"])}</p>{types_html}</div>'
            f'<div>{desk(c, "desk")}</div></div></section>' + bottom(c))
    add(path, body, alts, "0.8", "yearly")


def network(c):
    L = LANG[c]; p = L["pages"]["network"]; u = L["ui"]; path = f"/{c}/network/"; alts = same_path_alts(c, path)
    cr = [(u["home_label"], f"/{c}/"), (p["h1"], path)]
    who = "".join(f"<li>{E(t)}</li>" for t in p["who"])
    body = (head(c, p["title"], p["desc"], path, [org(), crumbs_schema(cr)], alts) + top(c, alts, path) + crumbs_html(c, cr) +
            f'<section><div class="container split"><div class="prose"><h1>{E(p["h1"])}</h1><p class="lead">{E(p["lead"])}</p>'
            f'<h2>{E(p["who_h2"])}</h2><ul>{who}</ul><h2>{E(p["how_h2"])}</h2><p>{E(p["how_p"])}</p></div>'
            f'<div>{desk(c, "desk", "network", p["cta"])}</div></div></section>' + bottom(c))
    add(path, body, alts, "0.6", "yearly")


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
                f'<p>{E(p["cta_p"])} <a href="/{c}/solutions/{x["service"]}/">{E(sname)}</a></p></div></section></article>' + cta_band(c) + bottom(c))
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
    vc = {"framework": None, "buildCommand": None, "installCommand": None, "trailingSlash": True, "redirects": redirects,
          "headers": [
              {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
              {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"},
                                              {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                                              {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]}]}
    with open(os.path.join(OUT, "vercel.json"), "w") as f:
        json.dump(vc, f, indent=2)


if __name__ == "__main__":
    clean()
    root_picker()
    for c in AVAIL:
        home(c); solutions_hub(c)
        for s in SERVICES: service_page(c, s)
        about(c); contact(c); network(c); privacy(c); insights(c)
    not_found()
    static_files()
    print(f"OK: {len(PAGES)} faqe, {len(AVAIL)} gjuhë ({', '.join(AVAIL)}).")
    miss = [c for c in LANGS if c not in LANG]
    if miss: print("KUJDES: mungojnë gjuhët:", ", ".join(miss))
    if CFG["support_email"] == "support@aiem.al":
        print("KUJDES: CFG['support_email'] është ende adresa shembull. Vendos adresën e vërtetë.")
