# AIEM — Albanian Industry Engineering and Management

Portal shumëgjuhësh (10 gjuhë) me suport vetëm me email. Site statik, pa varësi.

## Si funksionon
Vizitori zgjedh llojin e suportit (inxhinieri, BPP, shoqëri, turizëm dentar, prona, rrjet, pyetje e përgjithshme)
dhe hapet aplikacioni i emailit me shabllon të gatshëm drejtuar adresës së atij deskut (ose Gmail / Outlook / kopjo adresën).
Nuk ka formularë, telefon apo WhatsApp.

## Struktura
- `src/config.py`   → adresa e suportit, adresa sipas llojit, domeni, GA4, gjuhët
- `src/i18n/*.py`   → tekstet për çdo gjuhë (en është master; blogu vetëm en dhe sq)
- `src/build.py`    → gjeneron faqet në rrënjën e repo-s: `python3 src/build.py`
- `src/check_lang.py` → validon përkthimet kundrejt anglishtes

## Para publikimit (detyrueshme)
1. `src/config.py` → `support_email`: adresa e vërtetë dhe e monitoruar. Opsionale: `SUPPORT_EMAILS` për adresa të ndara sipas llojit.
2. Kur lidh domenin final: ndrysho `url`.
3. `python3 src/build.py`, pastaj commit dhe push (Vercel e shërben vetë).

## Premtimi "përgjigje brenda pak minutash"
Faqja e premton këtë. Duhet të jetë e vërtetë: monitoroni kutitë, vendosni përgjigje automatike me konfirmim
dhe caktoni dikë që i ndjek kërkesat. Përndryshe zbutni tekstin te `desk_reply`/`util_reply` në `src/i18n/*.py`.

## SEO pas publikimit
Search Console (dërgo `/sitemap.xml`), Google Business Profile, GA4 në `config.py` (ngjarje: `support_email_click`),
2-4 artikuj/muaj te `posts` (en dhe sq).
