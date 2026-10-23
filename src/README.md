# AIEM — Albanian Industry Engineering and Management

Site statik (HTML/CSS/JS), pa varësi, i shpejtë dhe i gatshëm për SEO.

## Struktura
- `content.py`  → I GJITHA tekstet (shërbimet, FAQ, blogu) dhe konfigurimi (CFG)
- `build.py`    → gjeneron rrënjën e repo-s (python3 src/build.py)
- `assets/`     → CSS, JS, logo, imazhi OG
- rrënjën e repo-s       → faqja e gatshme për ngarkim në hosting

## 1. Para publikimit (detyrueshme)
Hap `content.py`, ndrysho `CFG`: domeni (`url`), email, telefon, WhatsApp, adresa.
Pastaj: `python3 src/build.py`

## 2. Formulari i leads
Vendos në `CFG["form_endpoint"]` një endpoint (Formspree, Basin, Getform, ose backend yti).
Formulari dërgon JSON me: emër, telefon, email, shërbim, mesazh, faqe, UTM/gclid.
Pas dërgimit çon te /multumim/ (faqe noindex për konvertime GA4/Ads).

## 3. Hosting
Ngarko përmbajtjen e rrënjën e repo-s në rrënjën e domenit (Netlify, Cloudflare Pages, Vercel, ose cPanel).
Përfshihen `_headers` (Netlify/Cloudflare) dhe `.htaccess` (Apache: HTTPS, gzip, cache).

## 4. SEO pas publikimit
1. Google Search Console → shto domenin → dërgo `https://DOMENI/sitemap.xml`
2. Google Business Profile për Tiranën (rëndësi e madhe për kërkime lokale)
3. Vendos `ga4` në CFG (G-XXXX) dhe shëno `generate_lead` si konvertim
4. Publiko 2-4 artikuj/muaj te `POSTS` (çdo artikull lidhet me një shërbim)
5. Testo me PageSpeed Insights dhe Rich Results Test (FAQ, Service, Article, Breadcrumb)

## Çfarë përmban për SEO/CRO
- 1 faqe e dedikuar për çdo shërbim (title, meta, H1, FAQ, schema Service/FAQPage/Breadcrumb)
- Organization/ProfessionalService, WebSite, Article JSON-LD; canonical; hreflang sq/en; OG/Twitter
- sitemap.xml, robots.txt, lidhje të brendshme mes shërbimeve dhe blogut
- Formular në çdo faqe shërbimi (sticky), shiritat mobile "Kërko ofertë" + WhatsApp
- Honeypot kundër spam-it, validim, ndjekje UTM, ngjarje dataLayer (cta_*, generate_lead)

## Kujdes
- Premtimet (p.sh. "përgjigje brenda 1 dite pune", "konsultim pa detyrim") duhet të jenë të vërteta për biznesin.
- Politika e privatësisë është model; rishikoje me avokat.
- Faqet shërbimore janë vetëm në shqip; /en/ është faqe hyrëse në anglisht.
