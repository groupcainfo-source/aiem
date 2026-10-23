# -*- coding: utf-8 -*-
import json,shutil,os
BASE="https://aiem-lyart.vercel.app"; EMAIL="info@aiem.al"   # NDRYSHO
LANGS=["en","sq","de","fr","it","es"]; NAMES={"en":"English","sq":"Shqip","de":"Deutsch","fr":"Français","it":"Italiano","es":"Español"}
SLUGS={"eng":"engineering","biz":"business-plan","co":"company-setup","par":"partnerships","prop":"property-investment","dent":"dental-tourism","oth":"other"}
F=list(SLUGS)
T=json.load(open("T.json"))
D={
"en":["Design, calculations and supervision for production lines, electrical systems and industrial facilities.","Business plans with market analysis and a financial model for banks, investors or market entry.","Company registration and setup, from legal structure and documents to launch.","Vetted partners, distributors and suppliers, matched to your goals and checked before you commit.","Due diligence, valuation and purchase support for foreign and local property investors.","Coordinated dental treatment abroad: verified clinics, written quotes, transfers and translation.","Something not listed? Describe it and we route it to the right expert."],
"sq":["Projektim, llogaritje dhe mbikëqyrje për linja prodhimi, sisteme elektrike dhe objekte industriale.","Plane biznesi me analizë tregu dhe model financiar për bankë, investitor ose hyrje në treg.","Regjistrim dhe krijim shoqërie, nga struktura ligjore dhe dokumentet deri te nisja.","Partnerë, distributorë dhe furnitorë të verifikuar, të përputhur me qëllimet tuaja para çdo angazhimi.","Kontroll, vlerësim dhe mbështetje blerjeje për investitorë të huaj dhe vendas në prona.","Trajtim dentar i koordinuar: klinika të verifikuara, ofertë me shkrim, transferim dhe përkthim.","Diçka që nuk është në listë? Përshkruajeni dhe e drejtojmë te eksperti i duhur."],
"de":["Planung, Berechnung und Bauüberwachung für Produktionslinien, Elektrosysteme und Industrieanlagen.","Businesspläne mit Marktanalyse und Finanzmodell für Bank, Investor oder Markteintritt.","Firmenregistrierung und -gründung, von Rechtsform und Unterlagen bis zum Start.","Geprüfte Partner, Händler und Lieferanten, passend zu Ihren Zielen und vor Vertragsabschluss verifiziert.","Due Diligence, Bewertung und Kaufbegleitung für ausländische und lokale Immobilieninvestoren.","Koordinierte Zahnbehandlung im Ausland: geprüfte Kliniken, schriftliche Angebote, Transfers und Übersetzung.","Nicht aufgeführt? Beschreiben Sie es, wir leiten es an den richtigen Experten weiter."],
"fr":["Conception, calculs et suivi pour lignes de production, systèmes électriques et sites industriels.","Business plans avec étude de marché et modèle financier pour banque, investisseur ou entrée sur un marché.","Immatriculation et création de société, de la structure juridique aux documents jusqu'au lancement.","Partenaires, distributeurs et fournisseurs vérifiés, adaptés à vos objectifs avant tout engagement.","Due diligence, évaluation et accompagnement à l'achat pour investisseurs immobiliers étrangers et locaux.","Soins dentaires coordonnés à l'étranger : cliniques vérifiées, devis écrits, transferts et traduction.","Autre besoin ? Décrivez-le et nous l'orientons vers le bon expert."],
"it":["Progettazione, calcoli e supervisione per linee di produzione, impianti elettrici e siti industriali.","Business plan con analisi di mercato e modello finanziario per banca, investitore o ingresso nel mercato.","Registrazione e costituzione di società, dalla struttura legale ai documenti fino all'avvio.","Partner, distributori e fornitori verificati, in linea con i tuoi obiettivi prima di ogni impegno.","Due diligence, valutazione e supporto all'acquisto per investitori immobiliari stranieri e locali.","Cure dentali coordinate all'estero: cliniche verificate, preventivi scritti, transfer e traduzione.","Altro? Descrivilo e lo indirizziamo all'esperto giusto."],
"es":["Diseño, cálculos y supervisión de líneas de producción, sistemas eléctricos e instalaciones industriales.","Planes de negocio con análisis de mercado y modelo financiero para banco, inversor o entrada en el mercado.","Registro y constitución de empresas, desde la estructura legal y documentos hasta el inicio.","Socios, distribuidores y proveedores verificados, alineados con sus objetivos antes de comprometerse.","Due diligence, valoración y apoyo en la compra para inversores inmobiliarios extranjeros y locales.","Tratamiento dental coordinado en el extranjero: clínicas verificadas, presupuestos escritos, traslados y traducción.","¿Otro asunto? Descríbalo y lo derivamos al experto adecuado."]}
JS=r'''<script>(()=>{const C=@@C@@;let ti=0,fi=C.fi;const $=s=>document.querySelector(s);
function ch(el,items,cur,set){if(!el)return;el.innerHTML="";items.forEach((n,i)=>{const b=document.createElement("button");b.type="button";b.className="chip";b.textContent=n;b.setAttribute("aria-pressed",i===cur);b.onclick=()=>{set(i);r()};el.appendChild(b)})}
function r(){ch($("#fields"),C.f,fi,i=>fi=i);ch($("#types"),C.t,ti,i=>ti=i);
$("#send").href="mailto:"+C.e+"?subject="+encodeURIComponent("[AIEM] "+C.f[fi]+" – "+C.t[ti])+"&body="+encodeURIComponent(C.b)}r()})()</script>'''
def alts(path):
    return "".join(f'<link rel="alternate" hreflang="{l}" href="{BASE}/{l}/{path}">' for l in LANGS)+f'<link rel="alternate" hreflang="x-default" href="{BASE}/en/{path}">'
def page(l,slug=None):
    d=T[l]; fi=F.index([k for k in F if SLUGS[k]==slug][0]) if slug else 0
    fname=[d["f"][k] for k in F]; desc=D[l][fi] if slug else d["sub"]
    path=(slug+"/") if slug else ""
    title=(fname[fi]+" | AIEM") if slug else "AIEM — "+d["eyebrow"]
    h1=fname[fi] if slug else d["h1"]; sub=desc if slug else d["sub"]
    subj_fields=json.dumps(fname,ensure_ascii=False)
    C=json.dumps({"e":EMAIL,"f":fname,"t":d["t"],"b":d["b"],"fi":fi},ensure_ascii=False)
    langs="".join(f'<a href="/{x}/{path}" hreflang="{x}" lang="{x}"{" aria-current=true" if x==l else ""}>{NAMES[x]}</a>' for x in LANGS)
    fields_block='' if slug else f'<p class="step"><b>1</b>{d["s1"]}</p><div class="chips" id="fields"></div>'
    n2="2" if not slug else "1"; n3="3" if not slug else "2"
    cards="".join(f'<a class="card" href="/{l}/{SLUGS[k]}/"><h3>{fname[i]}</h3><p>{D[l][i]}</p></a>' for i,k in enumerate(F))
    why="".join(f'<div class="card"><h3>{d[a]}</h3><p>{d[a+"d"]}</p></div>' for a in("a1","a2","a3"))
    back=f'<p><a href="/{l}/">← AIEM</a></p>' if slug else ''
    ld=json.dumps({"@context":"https://schema.org","@type":"ProfessionalService","name":"AIEM — Albanian Industry Engineering and Management","url":BASE,"email":EMAIL,"areaServed":"Worldwide","availableLanguage":["English","Albanian","German","French","Italian","Spanish"]})
    return f'''<!DOCTYPE html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{BASE}/{l}/{path}">{alts(path)}
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{BASE}/assets/img/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/img/logo.svg"><link rel="stylesheet" href="/assets/css/portal.css"><script type="application/ld+json">{ld}</script></head><body>
<header><div class="w"><a class="logo" href="/{l}/"><img src="/assets/img/logo.svg" alt="">AIEM</a><nav class="langs" aria-label="Language">{langs}</nav></div></header>
<main class="w"><section class="hero">{back}<div class="eyebrow">{d["eyebrow"]}</div><h1>{h1}</h1><p class="sub">{sub}</p>
<div class="panel">{fields_block}<p class="step"><b>{n2}</b>{d["s2"]}</p><div class="chips" id="types"></div>
<p class="step"><b>{n3}</b>{d["s3"]}</p><div class="row"><a class="go" id="send" href="mailto:{EMAIL}">{d["cta"]}</a><span class="note">{d["or"]} <span class="mail">{EMAIL}</span></span></div>
<p class="note" style="margin:16px 0 0">{d["resp"]}</p></div></section>
<h2>{"AIEM" if slug else ""}</h2><div class="grid">{cards if not slug else ""}</div>
<h2>{d["whyh"]}</h2><div class="grid">{why}</div></main>
<footer><div class="w">© 2026 AIEM — Albanian Industry Engineering and Management · {d["foot"]}</div></footer>{JS.replace("@@C@@",C)}</body></html>'''
out="site"; shutil.rmtree(out,ignore_errors=True); os.makedirs(out+"/assets/css")
shutil.copytree("repo/assets/img",out+"/assets/img")
css=open("portal.css").read()+".langs{display:flex;gap:4px;flex-wrap:wrap}.langs a{padding:4px 8px;border-radius:4px;color:var(--steel);text-decoration:none;font-size:14px}.langs a[aria-current]{background:var(--ink);color:#fff}a.card{text-decoration:none;color:inherit}a.card:hover{outline:2px solid var(--signal)}a{color:var(--signal)}h2:empty{display:none}.hero p a{font-size:14px}"
open(out+"/assets/css/portal.css","w").write(css)
urls=[]
for l in LANGS:
    for s in [None]+list(SLUGS.values()):
        p=(s+"/") if s else ""; os.makedirs(f"{out}/{l}/{p}",exist_ok=True)
        open(f"{out}/{l}/{p}index.html","w",encoding="utf-8").write(page(l,s)); urls.append(p)
root='''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>AIEM</title><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="canonical" href="@B@/en/">@A@
<script>var L=(navigator.language||"en").slice(0,2);location.replace("/"+("@L@".split(",").indexOf(L)>-1?L:"en")+"/")</script></head><body style="font-family:system-ui;padding:40px"><p>@N@</p></body></html>'''
open(out+"/index.html","w").write(root.replace("@B@",BASE).replace("@A@",alts("")).replace("@L@",",".join(LANGS)).replace("@N@"," · ".join(f'<a href="/{l}/">{NAMES[l]}</a>' for l in LANGS)))
sm='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
for l in LANGS:
    for p in dict.fromkeys(urls):
        sm+=f'<url><loc>{BASE}/{l}/{p}</loc>'+"".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{BASE}/{x}/{p}"/>' for x in LANGS)+'</url>'
open(out+"/sitemap.xml","w").write(sm+"</urlset>")
open(out+"/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
shutil.copy("repo/vercel.json",out); shutil.copy("repo/site.webmanifest",out)
open(out+"/404.html","w").write(page("en").replace("<title>","<meta name=robots content=noindex><title>"))
open(out+"/README.md","w").write("# AIEM portal\nStatic, no dependencies. Edit EMAIL/BASE and texts in build_portal.py (+ T.json), run `python3 build_portal.py`, deploy `site/` to Vercel/Netlify/Cloudflare Pages.\nRoutes: /{en,sq,de,fr,it,es}/ and /{lang}/{engineering,business-plan,company-setup,partnerships,property-investment,dental-tourism,other}/\n")
shutil.copy("build_portal.py",out); shutil.copy("T.json",out)
print(sum(len(f) for _,_,f in os.walk(out)),"files")
