# AIEM — Albanian Industry Engineering and Management

Portal shumëgjuhësh (10 gjuhë), site statik, pa varësi. Kërkesat arrijnë me email te desku i llojit të zgjedhur.

## Struktura
- `src/config.py`    → domeni, adresat e emailit për çdo lloj suporti (ROUTES), URL e Apps Script, GA4, gjuhët
- `src/i18n/*.py`    → tekstet për çdo gjuhë (en është master; artikujt vetëm en dhe sq)
- `src/forms.py`     → tekstet e formularit dhe të konfirmimit automatik (10 gjuhë)
- `src/build.py`     → gjeneron faqet në rrënjën e repo-s dhe `apps-script/Code.gs`: `python3 src/build.py`
- `src/check_lang.py`→ validon përkthimet kundrejt anglishtes
- `apps-script/`     → `Code.gs` (gjeneruar) dhe udhëzimet e deploy-it

## Faqet
Çdo shërbim ka URL të vetën, p.sh. `/en/business-plan/`, me title, meta, H1, FAQ, schema Service/FAQPage/BreadcrumbList,
formular sticky, CTA në mes dhe shërbime të lidhura. `/en/solutions/` është vetëm faqja përmbledhëse.

## Si vjen kërkesa
Formulari → Google Apps Script → email te adresa e atij shërbimi (`ROUTES` në `config.py`) me Reply-To = vizitori,
plus konfirmim automatik te vizitori në gjuhën e tij. Nëse `apps_script_url` është bosh, faqja përdor emailin e gatshëm (mailto).

## Para publikimit
1. `config.py`: `mail_domain` ose adresat e plota te `ROUTES` (duhet të ekzistojnë dhe të monitorohen).
2. Apps Script: ndiq `apps-script/README.md`, pastaj vendos URL-në te `apps_script_url`.
3. `python3 src/build.py`, commit, push.

## Premtimi "përgjigje brenda pak minutash"
Faqja e premton. Duhet dikush që i ndjek kutitë, ose zbute tekstin te `desk_reply`/`util_reply` në `src/i18n/*.py`.

## Përmbajtje e thellë (SEO)
`src/deep/<gjuha>.py` ka seksionet e gjata (800+ fjalë) për çdo shërbim: blloqet `h2/h3/p/ul/ol/note`, lidhje të brendshme `[[slug|tekst]]` dhe FAQ shtesë. Gjuhët e gatshme: të gjitha 10 (en, sq, it, de, fr, es, tr, ar, ru, zh). Një gjuhë pa skedar shfaq versionin e shkurtër. Kontroll: `python3 src/check_deep.py en sq it de fr es tr ar ru zh`.

## Faqet dhe formulari (versioni i fundit)
- `src/content/<gjuha>.py`: formulari, faqet "How it works" (`/<gjuha>/how-it-works/`) dhe "About", teksti i kryefaqes dhe i kontaktit. Kontroll: `python3 src/check_content.py all`.
- Faqja "For professionals" (`/network/`) u hoq; adresat e vjetra ridrejtohen te kryefaqja (vercel.json).
- Formulari merr: emër, email, telefon, kompani, shtet, lloj suporti, përshkrim (min. 40 shkronja), afat. Dërgohet te Google Apps Script,
  që e dërgon te adresa e shërbimit (`ROUTES` te `src/config.py`). Pa `apps_script_url`, formulari hap emailin e vizitorit (zgjidhje rezervë).
