# -*- coding: utf-8 -*-
"""Gjeneron faqen statike të AIEM: python3 build.py  ->  dist/"""
import json, os, shutil, html
from content import CFG, GROUPS, SERVICES, POSTS

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "dist")
SITE = CFG["url"].rstrip("/")
E = html.escape
SVC = {s["slug"]: s for s in SERVICES}
PAGES = []  # (path, priority, changefreq, lastmod) për sitemap


def jl(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def org_schema():
    o = {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#org",
         "name": CFG["name"], "alternateName": CFG["short"], "url": SITE + "/",
         "logo": SITE + "/assets/img/logo.svg", "email": CFG["email"],
         "areaServed": {"@type": "Country", "name": "Albania"},
         "address": {"@type": "PostalAddress", "addressCountry": "AL", "addressLocality": "Tiranë"},
         "knowsLanguage": ["sq", "en"]}
    if "000 0000" not in CFG["phone"]:
        o["telephone"] = CFG["phone"]
    return o


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)]}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


LOGO = ('<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" fill="#16202A"/>'
        '<path d="M8 31 20 9l12 22" fill="none" stroke="#fff" stroke-width="3"/>'
        '<path d="M13.5 23h13" stroke="#C8102E" stroke-width="3"/></svg>')


def head(title, desc, path, schemas=(), noindex=False, lang="sq", og_type="website", alternates=None):
    url = SITE + path
    ga = ""
    if CFG["ga4"]:
        ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={CFG["ga4"]}"></script>'
              f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}'
              f'gtag("js",new Date());gtag("config","{CFG["ga4"]}");</script>')
    alt = ""
    for hl, hp in (alternates or []):
        alt += f'<link rel="alternate" hreflang="{hl}" href="{SITE}{hp}">'
    robots = "noindex, nofollow" if noindex else "index, follow, max-image-preview:large"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
{alt}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{E(CFG['name'])}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{'sq_AL' if lang == 'sq' else 'en_US'}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#16202A">
<link rel="icon" href="/assets/img/logo.svg" type="image/svg+xml">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100,600;100,700;112,700&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/assets/css/style.css">
{''.join(jl(s) for s in schemas)}
{ga}
</head>
<body>
<a class="skip" href="#main">Kalo te përmbajtja</a>
"""


NAV = [("/sherbimet/", "Shërbimet"), ("/blog/", "Blog"), ("/rreth-nesh/", "Rreth nesh"),
       ("/bashkohu-si-partner/", "Për profesionistët"), ("/kontakt/", "Kontakt")]


def header(path):
    links = ""
    for p, n in NAV:
        cur = ' aria-current="page"' if path.startswith(p) else ""
        links += f'<a href="{p}"{cur}>{n}</a>'
    return f"""<header class="site-header"><div class="container bar">
<a class="brand" href="/" aria-label="{E(CFG['name'])} — ballina">{LOGO}<span><b>AIEM</b><small>Albanian Industry Engineering and Management</small></span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menuja</button>
<nav class="nav" id="nav" aria-label="Menuja kryesore">{links}<a class="btn" href="/kontakt/#oferta" data-track="cta_header">Kërko ofertë</a></nav>
</div></header>
<main id="main">
"""


def footer():
    sv = "".join(f'<li><a href="/sherbimet/{s["slug"]}/">{E(s["name"])}</a></li>' for s in SERVICES)
    wa = f'https://wa.me/{CFG["whatsapp"]}'
    return f"""</main>
<div class="mbar"><a href="/kontakt/#oferta" data-track="cta_mobile">Kërko ofertë</a><a href="{wa}" data-track="whatsapp_mobile" rel="noopener">WhatsApp</a></div>
<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><h3>{E(CFG['name'])}</h3><p>Inxhinieri mekanike dhe elektrike, plane biznesi, partneritete, krijim shoqërie, turizëm dentar dhe investime në prona në Shqipëri.</p></div>
<div><h3>Shërbimet</h3><ul>{sv}</ul></div>
<div><h3>Kompania</h3><ul><li><a href="/rreth-nesh/">Rreth nesh</a></li><li><a href="/blog/">Blog</a></li><li><a href="/bashkohu-si-partner/">Bashkohu si profesionist</a></li><li><a href="/kontakt/">Kontakt</a></li><li><a href="/en/">English</a></li></ul></div>
<div><h3>Kontakt</h3><ul><li><a href="mailto:{CFG['email']}">{E(CFG['email'])}</a></li><li><a href="tel:{CFG['phone'].replace(' ', '')}">{E(CFG['phone'])}</a></li><li><a href="{wa}" rel="noopener">WhatsApp</a></li><li>{E(CFG['address'])}</li></ul></div>
</div>
<div class="legal"><span>© 2026 {E(CFG['name'])}. Të gjitha të drejtat e rezervuara.</span><span><a href="/politika-e-privatesise/">Politika e privatësisë</a></span></div>
</div></footer>
<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def crumbs_html(items):
    lis = ""
    for i, (n, p) in enumerate(items):
        if i == len(items) - 1:
            lis += f'<li aria-current="page">{E(n)}</li>'
        else:
            lis += f'<li><a href="{p}">{E(n)}</a></li>'
    return f'<nav class="crumbs container" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'


L_SQ = dict(title="Kërko ofertë", sub=CFG["response_promise"], service="Shërbimi", pick="Zgjidhni shërbimin", name="Emri",
            phone="Telefon ose WhatsApp", email="Email (opsionale)", msg="Përshkruani shkurt nevojën tuaj", btn="Dërgo kërkesën",
            consent='Pranoj <a href="/politika-e-privatesise/">politikën e privatësisë</a>.',
            note="Konsultimi i parë është pa detyrim. Të dhënat tuaja trajtohen me konfidencialitet.", thanks="/multumim/")
L_EN = dict(title="Request a proposal", sub="Reply within 1 business day", service="Service", pick="Choose a service", name="Name",
            phone="Phone or WhatsApp", email="Email (optional)", msg="Briefly describe what you need", btn="Send request",
            consent='I accept the <a href="/politika-e-privatesise/">privacy policy</a> (Albanian).',
            note="The first consultation is free of obligation. Your data is handled confidentially.", thanks="/en/thank-you/")
EN_NAMES = {"inxhinieri-mekanike": "Mechanical engineering", "inxhinieri-elektrike": "Electrical engineering",
            "plan-biznesi-bpp": "Business plan (BPP)", "hyrje-ne-treg-partneritete": "Market entry and partnerships",
            "krijim-shoqerie-shqiperi": "Company formation in Albania", "turizem-dentar-shqiperi": "Dental tourism in Albania",
            "investime-prona-te-paluajtshme": "Real estate investment", "partneritete-biznesi": "Business partnerships"}


def form(fid, service="", variant="client", lang="sq"):
    L = L_SQ if lang == "sq" else L_EN
    if variant == "pro":
        opts = ["Inxhinier mekanik", "Inxhinier elektrik", "Konsulent biznesi", "Avokat", "Kontabilist", "Furnitor ose prodhues",
                "Investitor", "Agjent pronash", "Klinikë dentare", "Tjetër"]
        label = "Profili juaj"
        pick = "Zgjidhni profilin"
        title, sub, btn = "Aplikim për rrjetin", "Shqyrtojmë çdo aplikim", "Dërgo aplikimin"
        msg = "Aftësitë, përvoja dhe lloji i projekteve që kërkoni"
        fieldname = "profile"
    else:
        opts = [s["name"] for s in SERVICES] if lang == "sq" else [EN_NAMES[s["slug"]] for s in SERVICES]
        opts.append("Tjetër" if lang == "sq" else "Other")
        label, pick, title, sub, btn, msg = L["service"], L["pick"], L["title"], L["sub"], L["btn"], L["msg"]
        fieldname = "service"
    sel = "".join(f'<option value="{E(o)}">{E(o)}</option>' for o in opts)
    pre = ""
    if service:
        pre = E(SVC[service]["name"] if lang == "sq" else EN_NAMES[service])
    return f"""<div class="tb" id="{fid}-box">
<div class="tb-head"><strong>{E(title)}</strong><span>{E(sub)}</span></div>
<form data-lead data-service="{pre}" action="{E(CFG['form_endpoint'])}" method="post" novalidate data-thanks="{L['thanks']}" data-lang="{lang}">
<input type="hidden" name="form_type" value="{variant}">
<div class="cell"><label for="{fid}-s">{E(label)}</label><select id="{fid}-s" name="{fieldname}"><option value="">{E(pick)}</option>{sel}</select></div>
<div class="cell"><label for="{fid}-n">{E(L['name'])}</label><input id="{fid}-n" name="name" type="text" autocomplete="name" required></div>
<div class="row2">
<div class="cell"><label for="{fid}-p">{E(L['phone'])}</label><input id="{fid}-p" name="phone" type="tel" autocomplete="tel" inputmode="tel"></div>
<div class="cell"><label for="{fid}-e">{E(L['email'])}</label><input id="{fid}-e" name="email" type="email" autocomplete="email"></div>
</div>
<div class="cell"><label for="{fid}-m">{E(msg)}</label><textarea id="{fid}-m" name="message" rows="3"></textarea></div>
<div class="hp" aria-hidden="true"><label>Website <input name="website" tabindex="-1" autocomplete="off"></label></div>
<p class="form-msg" role="alert" tabindex="-1"></p>
<div class="tb-foot">
<label style="display:flex;gap:8px;align-items:flex-start;font-size:.9rem;margin-bottom:12px"><input type="checkbox" name="consent" style="margin-top:4px"> <span>{L['consent']}</span></label>
<button class="btn btn-block" type="submit">{E(btn)}</button>
<small>{E(L['note'])}</small>
</div>
</form></div>"""


def faq_html(faqs):
    return '<div class="faq">' + "".join(
        f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs) + "</div>"


def cta_band(text="Keni një projekt ose një ide? Na tregoni dhe do t'ju themi nga ku të nisni."):
    return f'<section class="cta-band" aria-label="Kontakt"><div class="container"><h2>{E(text)}</h2><a class="btn" href="/kontakt/#oferta" data-track="cta_band">Kërko ofertë</a></div></section>'


def write(path, content):
    fp = os.path.join(OUT, path.lstrip("/"))
    if path.endswith("/"):
        fp = os.path.join(fp, "index.html")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)


def add(path, content, prio="0.7", freq="monthly", index=True):
    write(path, content)
    if index:
        PAGES.append((path, prio, freq))


def steps_html():
    return """<ol class="steps">
<li><b>Brifi</b><span>Dëgjojmë qëllimin, buxhetin dhe afatin tuaj. Pa detyrim.</span></li>
<li><b>Analizë</b><span>Shqyrtojmë teknikisht dhe tregtarisht dhe saktësojmë çfarë duhet.</span></li>
<li><b>Propozim</b><span>Merrni ofertë me shkrim: çfarë bëhet, kur dhe sa kushton.</span></li>
<li><b>Zbatim</b><span>Punojmë me ju dhe me partnerët, me një person kontakti.</span></li>
</ol>"""


# ---------------- FAQJA KRYESORE ----------------
def home():
    title = "AIEM | Inxhinieri, plan biznesi dhe partneritete në Shqipëri"
    desc = ("Inxhinieri mekanike dhe elektrike, plan biznesi (BPP), krijim shoqërie, turizëm dentar dhe investime në prona "
            "në Shqipëri. Kërkoni ofertë falas.")
    sch = [org_schema(), {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/",
                           "name": CFG["name"], "inLanguage": "sq", "publisher": {"@id": SITE + "/#org"}}, faq_schema(HOME_FAQ)]
    groups = ""
    for gid, gname, gdesc in GROUPS:
        items = "".join(
            f'<li><a href="/sherbimet/{s["slug"]}/"><b>{E(s["name"])}</b><span>{E(s["short"])}</span><em>Shiko shërbimin</em></a></li>'
            for s in SERVICES if s["group"] == gid)
        groups += f'<div class="group"><div><h3>{E(gname)}</h3><p>{E(gdesc)}</p></div><ul class="svc-list">{items}</ul></div>'
    body = head(title, desc, "/", sch, alternates=[("sq", "/"), ("en", "/en/"), ("x-default", "/")]) + header("/") + f"""
<section class="hero"><div class="container hero-grid">
<div>
<div class="dim"><span>Tiranë, Shqipëri</span><i></i></div>
<h1>Inxhinieri, plan biznesi dhe partneritete në Shqipëri</h1>
<p class="lead">Albanian Industry Engineering and Management bashkon inxhinierë, konsulentë dhe partnerë në një vend: nga projekti mekanik dhe elektrik te plani i biznesit, shoqëria, turizmi dentar dhe investimet në prona.</p>
<div class="hero-actions"><a class="btn" href="#oferta" data-track="cta_hero">Kërko ofertë</a><a class="btn btn-ghost" href="/sherbimet/">Shiko shërbimet</a></div>
<ul class="ticks"><li>{E(CFG['response_promise'])}</li><li>Konsultimi i parë pa detyrim</li><li>Konfidencialitet për idenë dhe të dhënat tuaja</li></ul>
</div>
<div id="oferta">{form('h1f')}</div>
</div></section>

<section aria-labelledby="sh"><div class="container">
<h2 id="sh">Shërbimet tona</h2>
<p class="lead" style="margin-bottom:36px">Çdo shërbim ka një ekip dhe një person kontakti. Zgjidhni fushën dhe shihni çfarë përfshihet, çfarë merrni dhe si punojmë.</p>
<div class="groups">{groups}</div>
</div></section>

<section class="alt" aria-labelledby="pr"><div class="container">
<h2 id="pr">Si punojmë</h2>
<p class="lead">Katër hapa, me çmim dhe afat të shkruar para se të angazhoheni.</p>
{steps_html()}
</div></section>

<section aria-labelledby="pse"><div class="container split">
<div><h2 id="pse">Pse të punoni me AIEM</h2>
<div class="points">
<div><h3>Inxhinieri dhe biznes në një ekip</h3><p>Plani i biznesit bazohet në kosto teknike reale, jo në supozime. Kjo e bën më të besueshëm para bankës dhe partnerëve.</p></div>
<div><h3>Kontroll para vendimit</h3><p>Para se të blini një pronë, të zgjidhni një klinikë ose të nënshkruani me një partner, kryejmë kontrollet që e bëjnë vendimin të sigurt.</p></div>
<div><h3>Ofertë e qartë me shkrim</h3><p>Çdo propozim tregon çfarë përfshihet, çfarë nuk përfshihet dhe sa kushton. Pa kosto të fshehura.</p></div>
</div></div>
<div class="panel"><h2>Jeni profesionist në fushën tuaj?</h2><p>Inxhinierë, konsulentë, avokatë, kontabilistë, furnitorë dhe investitorë mund të aplikojnë në rrjetin tonë për të marrë projekte dhe partnerë të rinj.</p><a class="btn btn-ghost" href="/bashkohu-si-partner/" data-track="cta_pro">Aplikoni në rrjet</a></div>
</div></section>

<section class="alt" aria-labelledby="fq"><div class="container"><h2 id="fq">Pyetje të shpeshta</h2>{faq_html(HOME_FAQ)}</div></section>
{cta_band()}
""" + footer()
    add("/", body, "1.0", "weekly")


HOME_FAQ = [
    ("Çfarë është Albanian Industry Engineering and Management?", "Është një platformë shërbimesh dhe partneritetesh që bashkon inxhinierë, konsulentë biznesi dhe partnerë profesionistë për projekte në Shqipëri, nga inxhinieria mekanike dhe elektrike te plani i biznesit, krijimi i shoqërisë, turizmi dentar dhe investimet në prona."),
    ("A është konsultimi i parë pa pagesë?", "Po, konsultimi i parë është pa detyrim. Pas tij merrni një ofertë me shkrim me çfarë përfshihet, afatin dhe koston."),
    ("A punoni me klientë nga jashtë Shqipërisë?", "Po. Punojmë me kompani, investitorë dhe pacientë nga jashtë vendit dhe mund të përgatisim dokumentet në shqip dhe anglisht."),
    ("Si mund të bëhem pjesë e rrjetit të profesionistëve?", "Plotësoni formularin e aplikimit te faqja Për profesionistët. Shqyrtojmë profilin dhe referencat dhe ju kontaktojmë."),
]


# ---------------- SHËRBIMET ----------------
def services_hub():
    title = "Shërbimet | Inxhinieri, BPP, shoqëri, turizëm dentar, prona | AIEM"
    desc = "Të gjitha shërbimet e AIEM: inxhinieri mekanike dhe elektrike, plan biznesi, hyrje në treg, krijim shoqërie, turizëm dentar dhe investime në prona."
    cr = [("Ballina", "/"), ("Shërbimet", "/sherbimet/")]
    groups = ""
    for gid, gname, gdesc in GROUPS:
        items = "".join(
            f'<li><a href="/sherbimet/{s["slug"]}/"><b>{E(s["name"])}</b><span>{E(s["short"])}</span><em>Shiko shërbimin</em></a></li>'
            for s in SERVICES if s["group"] == gid)
        groups += f'<div class="group"><div><h3>{E(gname)}</h3><p>{E(gdesc)}</p></div><ul class="svc-list">{items}</ul></div>'
    body = head(title, desc, "/sherbimet/", [org_schema(), crumbs_schema(cr)]) + header("/sherbimet/") + crumbs_html(cr) + f"""
<section><div class="container"><h1>Shërbimet tona</h1><p class="lead" style="margin-bottom:36px">Inxhinieri, biznes dhe investime nën një çati. Zgjidhni shërbimin që ju duhet.</p><div class="groups">{groups}</div></div></section>
{cta_band()}""" + footer()
    add("/sherbimet/", body, "0.9", "monthly")


def service_page(s):
    path = f"/sherbimet/{s['slug']}/"
    cr = [("Ballina", "/"), ("Shërbimet", "/sherbimet/"), (s["name"], path)]
    sch = [org_schema(), crumbs_schema(cr), faq_schema(s["faqs"]),
           {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["meta_desc"],
            "url": SITE + path, "provider": {"@id": SITE + "/#org"}, "areaServed": {"@type": "Country", "name": "Albania"},
            "serviceType": s["name"]}]
    inc = "".join(f"<li>{E(i)}</li>" for i in s["includes"])
    dl = "".join(f"<li>{E(i)}</li>" for i in s["deliver"])
    note = f'<p class="note">{E(s["note"])}</p>' if s.get("note") else ""
    rel = "".join(f'<a href="/sherbimet/{r}/"><b>{E(SVC[r]["name"])}</b><span>{E(SVC[r]["short"])}</span></a>' for r in s["related"])
    posts = [p for p in POSTS if p["service"] == s["slug"]]
    pl = ""
    if posts:
        pl = "<h2>Lexoni më shumë</h2><ul>" + "".join(f'<li><a href="/blog/{p["slug"]}/">{E(p["title"])}</a></li>' for p in posts) + "</ul>"
    body = head(s["meta_title"], s["meta_desc"], path, sch) + header("/sherbimet/") + f"""
<div class="svc-hero">{crumbs_html(cr)}<div class="container svc-layout" style="padding-top:20px">
<div class="content"><h1>{E(s['h1'])}</h1><p class="lead">{E(s['lead'])}</p>
<h2>Çfarë përfshin</h2><ul class="checks">{inc}</ul>
<h2>Për kë është</h2><p>{E(s['audience'])}</p>
<h2>Çfarë merrni</h2><ul class="deliver">{dl}</ul>{note}
<h2>Si punojmë</h2>{steps_html()}
<h2>Pyetje të shpeshta</h2>{faq_html(s['faqs'])}{pl}
</div>
<aside class="aside" id="oferta" aria-label="Formulari i ofertës">{form('sf', s['slug'])}</aside>
</div></div>
<section class="alt"><div class="container"><h2>Shërbime të lidhura</h2><div class="related">{rel}</div></div></section>
{cta_band()}""" + footer()
    add(path, body, "0.9", "monthly")


# ---------------- BLOG ----------------
def blog():
    cr = [("Ballina", "/"), ("Blog", "/blog/")]
    items = "".join(f'<li><a href="/blog/{p["slug"]}/">{E(p["title"])}</a><p>{E(p["desc"])}</p></li>' for p in POSTS)
    body = head("Blog | Biznes, investime dhe inxhinieri në Shqipëri | AIEM",
                "Udhëzues praktikë për krijimin e shoqërisë, planin e biznesit, turizmin dentar dhe blerjen e pronës në Shqipëri.",
                "/blog/", [org_schema(), crumbs_schema(cr)]) + header("/blog/") + crumbs_html(cr) + f"""
<section><div class="container"><h1>Blog</h1><p class="lead" style="margin-bottom:28px">Udhëzues praktikë për biznes, investime dhe inxhinieri në Shqipëri.</p><ul class="posts">{items}</ul></div></section>
{cta_band()}""" + footer()
    add("/blog/", body, "0.6", "weekly")
    for p in POSTS:
        path = f"/blog/{p['slug']}/"
        c = [("Ballina", "/"), ("Blog", "/blog/"), (p["title"], path)]
        sv = SVC[p["service"]]
        parts = ""
        for t in p["body"]:
            if t[0] == "p": parts += f"<p>{E(t[1])}</p>"
            elif t[0] == "h2": parts += f"<h2>{E(t[1])}</h2>"
            elif t[0] == "ul": parts += "<ul>" + "".join(f"<li>{E(i)}</li>" for i in t[1]) + "</ul>"
            elif t[0] == "note": parts += f'<p class="note">{E(t[1])}</p>'
        art = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["desc"],
               "datePublished": CFG["date"], "dateModified": CFG["date"], "inLanguage": "sq",
               "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"},
               "mainEntityOfPage": SITE + path, "image": SITE + "/assets/img/og.png"}
        body = head(p.get("seo_title", p["title"]) + " | AIEM", p["desc"], path, [org_schema(), crumbs_schema(c), art], og_type="article") + header("/blog/") + crumbs_html(c) + f"""
<article><section><div class="container prose"><p class="meta">Publikuar më {CFG['date']}</p><h1>{E(p['title'])}</h1>{parts}
<p>Nëse keni nevojë për ndihmë konkrete: <a href="/sherbimet/{sv['slug']}/">{E(sv['name'])}</a>.</p></div></section></article>
{cta_band()}""" + footer()
        add(path, body, "0.6", "monthly")


# ---------------- FAQE TË TJERA ----------------
def about():
    cr = [("Ballina", "/"), ("Rreth nesh", "/rreth-nesh/")]
    body = head("Rreth nesh | Albanian Industry Engineering and Management", "Kush jemi dhe si punojmë: një ekip inxhinierësh dhe konsulentësh që lidh biznese, investitorë dhe profesionistë në Shqipëri.",
                "/rreth-nesh/", [org_schema(), crumbs_schema(cr)]) + header("/rreth-nesh/") + crumbs_html(cr) + f"""
<section><div class="container split"><div class="prose"><h1>Rreth nesh</h1>
<p class="lead">Albanian Industry Engineering and Management (AIEM) lidh biznese, investitorë dhe profesionistë në Shqipëri, me bazë inxhinierinë.</p>
<p>Besojmë se vendimet e mira në biznes nisin me kontroll teknik dhe llogari të sakta. Prandaj ekipi ynë përfshin inxhinierë mekanikë dhe elektrikë, së bashku me konsulentë biznesi dhe partnerë ligjorë, kontabël dhe mjekësorë për fushat që kërkojnë ekspertizë të veçantë.</p>
<h2>Si e ndërtojmë besimin</h2>
<ul><li>Çdo ofertë është me shkrim, me çfarë përfshihet dhe çfarë jo.</li><li>Nuk premtojmë rezultate që s'mund t'i garantojmë, si miratimi i një kredie ose fitimi nga një investim.</li><li>Për çështje ligjore, tatimore dhe mjekësore punojmë vetëm me profesionistë të licencuar.</li></ul>
<p><a class="btn" href="/kontakt/#oferta">Na kontaktoni</a></p></div>
<div class="panel"><h2>Shërbimet tona</h2><p>Nga projekti teknik te regjistrimi i shoqërisë dhe blerja e pronës.</p><a class="btn btn-ghost" href="/sherbimet/">Shiko shërbimet</a></div></div></section>""" + footer()
    add("/rreth-nesh/", body, "0.5", "yearly")


def contact():
    cr = [("Ballina", "/"), ("Kontakt", "/kontakt/")]
    wa = f"https://wa.me/{CFG['whatsapp']}"
    sch = [org_schema(), crumbs_schema(cr), {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/kontakt/"}]
    body = head("Kontakt | Kërko ofertë falas | AIEM", "Na shkruani ose na telefononi për një ofertë. Përgjigje brenda 1 dite pune. Tiranë, Shqipëri.",
                "/kontakt/", sch) + header("/kontakt/") + crumbs_html(cr) + f"""
<section><div class="container split"><div><h1>Kontakt</h1><p class="lead">Na tregoni çfarë keni nevojë dhe do t'ju përgjigjemi me hapat e radhës. {E(CFG['response_promise'])}.</p>
<ul class="checks"><li>Email: <a href="mailto:{CFG['email']}">{E(CFG['email'])}</a></li><li>Telefon: <a href="tel:{CFG['phone'].replace(' ', '')}">{E(CFG['phone'])}</a></li><li>WhatsApp: <a href="{wa}" rel="noopener" data-track="whatsapp_click">Shkruani në WhatsApp</a></li><li>Adresa: {E(CFG['address'])}</li></ul></div>
<div id="oferta">{form('cf')}</div></div></section>""" + footer()
    add("/kontakt/", body, "0.8", "yearly")


def partner():
    cr = [("Ballina", "/"), ("Për profesionistët", "/bashkohu-si-partner/")]
    body = head("Bashkohu si profesionist | Rrjeti i partnerëve AIEM", "Inxhinierë, konsulentë, avokatë, kontabilistë, furnitorë dhe investitorë: aplikoni në rrjetin AIEM për projekte dhe partnerë të rinj në Shqipëri.",
                "/bashkohu-si-partner/", [org_schema(), crumbs_schema(cr)]) + header("/bashkohu-si-partner/") + crumbs_html(cr) + f"""
<section><div class="container split"><div class="prose"><h1>Bashkohu në rrjetin e profesionistëve</h1>
<p class="lead">Marrim projekte nga biznese dhe investitorë që kërkojnë ekspertë të fushës. Nëse keni aftësi dhe përvojë, aplikoni.</p>
<h2>Kë kërkojmë</h2><ul><li>Inxhinierë mekanikë dhe elektrikë</li><li>Konsulentë biznesi dhe financiarë</li><li>Avokatë dhe kontabilistë</li><li>Furnitorë, prodhues dhe distributorë</li><li>Agjentë pronash dhe klinika dentare</li><li>Investitorë që kërkojnë projekte</li></ul>
<h2>Si funksionon</h2><p>Shqyrtojmë profilin dhe referencat, ju kontaktojmë dhe, kur ka një projekt të përshtatshëm, ju prezantojmë me klientin. Kushtet i dakordësojmë me shkrim para çdo projekti.</p></div>
<div id="oferta">{form('pf', variant='pro')}</div></div></section>""" + footer()
    add("/bashkohu-si-partner/", body, "0.6", "yearly")


def privacy():
    cr = [("Ballina", "/"), ("Politika e privatësisë", "/politika-e-privatesise/")]
    body = head("Politika e privatësisë | AIEM", "Si i mbledhim, i përdorim dhe i mbrojmë të dhënat tuaja personale.", "/politika-e-privatesise/",
                [crumbs_schema(cr)]) + header("") + crumbs_html(cr) + f"""
<section><div class="container prose"><h1>Politika e privatësisë</h1>
<p class="note">Model fillestar. Para publikimit, rishikojeni me një avokat sipas ligjit shqiptar për mbrojtjen e të dhënave personale.</p>
<h2>Çfarë të dhënash mbledhim</h2><p>Emrin, telefonin, emailin dhe mesazhin që na dërgoni në formular, si dhe të dhëna teknike bazë të vizitës (faqja, burimi i vizitës).</p>
<h2>Si i përdorim</h2><p>Vetëm për t'ju përgjigjur, për t'ju dërguar ofertën dhe për të përmirësuar shërbimin. Nuk i shesim të dhënat tuaja.</p>
<h2>Të drejtat tuaja</h2><p>Mund të kërkoni qasje, korrigjim ose fshirje të të dhënave tuaja duke na shkruar në <a href="mailto:{CFG['email']}">{E(CFG['email'])}</a>.</p>
<h2>Kontakt</h2><p>{E(CFG['name'])}, {E(CFG['address'])}.</p></div></section>""" + footer()
    add("/politika-e-privatesise/", body, "0.2", "yearly")


def thanks():
    body = head("Faleminderit | AIEM", "Kërkesa u dërgua.", "/multumim/", noindex=True) + header("") + """
<section><div class="container prose"><h1>Faleminderit, kërkesa u dërgua</h1><p class="lead">Do t'ju kontaktojmë së shpejti. Ndërkohë mund të shihni shërbimet ose artikujt tanë.</p>
<p><a class="btn" href="/sherbimet/">Shiko shërbimet</a> <a class="btn btn-ghost" href="/blog/">Lexo blogun</a></p></div></section>""" + footer()
    add("/multumim/", body, index=False)
    body = head("Thank you | AIEM", "Request sent.", "/en/thank-you/", noindex=True, lang="en") + header("") + """
<section><div class="container prose"><h1>Thank you, your request was sent</h1><p class="lead">We will contact you shortly.</p>
<p><a class="btn" href="/en/">Back to home</a></p></div></section>""" + footer()
    add("/en/thank-you/", body, index=False)


def english():
    title = "Engineering, business plans and partnerships in Albania | AIEM"
    desc = ("Mechanical and electrical engineering, business plans, company formation, dental tourism and "
            "real estate investment in Albania.")
    sch = [org_schema(), {"@context": "https://schema.org", "@type": "WebPage", "url": SITE + "/en/", "inLanguage": "en", "name": title}]
    items = "".join(f'<li><a href="/sherbimet/{s["slug"]}/"><b>{E(EN_NAMES[s["slug"]])}</b><span>{E(s["short"])}</span><em>View (Albanian)</em></a></li>' for s in SERVICES)
    body = head(title, desc, "/en/", sch, lang="en", alternates=[("sq", "/"), ("en", "/en/"), ("x-default", "/")]) + header("") + f"""
<section class="hero"><div class="container hero-grid"><div>
<div class="dim"><span>Tirana, Albania</span><i></i></div>
<h1>Engineering, business plans and partnerships in Albania</h1>
<p class="lead">AIEM brings engineers, business consultants and partners together: from mechanical and electrical design to business plans, company formation, dental tourism and property investment.</p>
<ul class="ticks"><li>Reply within 1 business day</li><li>First consultation free of obligation</li><li>Business plans and documents in English or Albanian</li></ul></div>
<div id="oferta">{form('enf', lang='en')}</div></div></section>
<section><div class="container"><h2>Services</h2><p class="lead" style="margin-bottom:24px">Detailed service pages are currently in Albanian.</p><ul class="svc-list">{items}</ul></div></section>""" + footer()
    add("/en/", body, "0.7", "monthly")


def not_found():
    body = head("Faqja nuk u gjet | AIEM", "Faqja që kërkuat nuk ekziston.", "/404.html", noindex=True) + header("") + """
<section><div class="container prose"><h1>Faqja nuk u gjet</h1><p class="lead">Lidhja mund të jetë e vjetër. Provoni një nga faqet kryesore.</p>
<p><a class="btn" href="/">Ballina</a> <a class="btn btn-ghost" href="/sherbimet/">Shërbimet</a></p></div></section>""" + footer()
    write("/404.html", body)


def static_files():
    for sub in ("assets/css", "assets/js", "assets/img"):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)
    for f in ("assets/css/style.css", "assets/js/main.js", "assets/img/og.png"):
        shutil.copy(os.path.join(ROOT, f), os.path.join(OUT, f))
    with open(os.path.join(OUT, "assets/img/logo.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" fill="#16202A"/>'
                '<path d="M8 31 20 9l12 22" fill="none" stroke="#fff" stroke-width="3"/><path d="M13.5 23h13" stroke="#C8102E" stroke-width="3"/></svg>')
    urls = "".join(
        f"<url><loc>{SITE}{p}</loc><lastmod>{CFG['date']}</lastmod><changefreq>{fq}</changefreq><priority>{pr}</priority></url>"
        for p, pr, fq in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /multumim/\nDisallow: /en/thank-you/\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(OUT, "site.webmanifest"), "w") as f:
        json.dump({"name": CFG["name"], "short_name": CFG["short"], "start_url": "/", "display": "browser",
                   "background_color": "#FAFBFC", "theme_color": "#16202A",
                   "icons": [{"src": "/assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, f)
    with open(os.path.join(OUT, "_headers"), "w") as f:
        f.write("/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n\n/*\n  X-Content-Type-Options: nosniff\n"
                "  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n")
    with open(os.path.join(OUT, ".htaccess"), "w") as f:
        f.write("ErrorDocument 404 /404.html\nRewriteEngine On\n"
                "RewriteCond %{HTTPS} off\nRewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]\n"
                "<IfModule mod_deflate.c>\nAddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml\n</IfModule>\n"
                "<IfModule mod_expires.c>\nExpiresActive On\nExpiresByType text/css \"access plus 1 year\"\nExpiresByType application/javascript \"access plus 1 year\"\nExpiresByType image/svg+xml \"access plus 1 year\"\n</IfModule>\n")


if __name__ == "__main__":
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    home(); services_hub()
    for s in SERVICES: service_page(s)
    blog(); about(); contact(); partner(); privacy(); thanks(); english(); not_found()
    static_files()
    print(f"OK: {len(PAGES)} faqe në sitemap, dist/ gati.")
    for k in ("email", "phone", "whatsapp", "form_endpoint"):
        if CFG[k] in ("#", "info@aiem.al", "+355 00 000 0000", "355000000000"):
            print(f"KUJDES: CFG['{k}'] është ende vlerë shembull.")
