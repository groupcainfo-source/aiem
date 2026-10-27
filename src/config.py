# -*- coding: utf-8 -*-
# KONFIGURIMI I PORTALIT. Ndrysho vetëm këtu, pastaj ekzekuto: python3 src/build.py

CFG = {
    "name": "Albanian Industry Engineering and Management",
    "short": "AIEM",
    "url": "https://aiem-lyart.vercel.app",   # NDRYSHO kur lidh domenin final
    "date": "2026-10-23",
    "ga4": "",                                # p.sh. G-XXXXXXXXXX (opsionale)

    # ---- GOOGLE APPS SCRIPT (marrja e kërkesave nga formulari) ----
    # Pas deploy-it të skriptit (shih apps-script/README.md) ngjit këtu URL-në që mbaron me /exec.
    # Nëse mbetet bosh, faqja përdor emailin e gatshëm (mailto) në vend të formularit.
    "apps_script_url": "",
    "sheet_id": "",          # opsionale: ID e një Google Sheet ku ruhen të gjitha kërkesat (kopje rezervë)
    "team_lang": "sq",       # gjuha e emailit që merr ekipi: "sq" ose "en"
    "send_autoreply": True,  # konfirmim automatik te vizitori (në gjuhën e tij)

    # ---- ADRESAT E EMAILIT ----
    # NDRYSHO domenin. Për Gmail mund të përdorësh alias: ps. "emri+dental@gmail.com" te ROUTES poshtë.
    "mail_domain": "aiem.al",
}

# Çdo lloj suporti ka adresën e vet. Çelësi = slug i shërbimit (ose general).
# Vlera: pjesa para @ (përdoret me mail_domain) ose adresë e plotë me @.
ROUTES = {
    "general": "albanianindustry@gmail.com",
    "mechanical-engineering": "albanianindustry@gmail.com",
    "electrical-engineering": "albanianindustry@gmail.com",
    "business-plan": "enejdsaliaj@eufin.al",
    "market-entry-partnerships": "enejdsaliaj@eufin.al",
    "company-formation-albania": "enejdsaliaj@eufin.al",
    "business-partnerships": "enejdsaliaj@eufin.al",
    "dental-tourism-albania": "luminedent@gmail.com",
    "real-estate-investment-albania": "albanianindustry@gmail.com",
}
SUPPORT_EMAILS = {k: (v if "@" in v else f"{v}@{CFG['mail_domain']}") for k, v in ROUTES.items()}
CFG["support_email"] = SUPPORT_EMAILS["general"]

# Gjuhët (renditja = renditja në menu). Kodi = dosja /xx/
LANGS = ["en", "sq", "it", "de", "fr", "es", "tr", "ar", "ru", "zh"]

# Struktura e shërbimeve (e pavarur nga gjuha). Tekstet jetojnë në i18n/<gjuha>.py
GROUPS = ["engineering", "business", "invest"]
SERVICES = [
    {"slug": "mechanical-engineering", "group": "engineering",
     "related": ["electrical-engineering", "business-plan", "market-entry-partnerships"]},
    {"slug": "electrical-engineering", "group": "engineering",
     "related": ["mechanical-engineering", "business-plan", "real-estate-investment-albania"]},
    {"slug": "business-plan", "group": "business",
     "related": ["market-entry-partnerships", "company-formation-albania", "real-estate-investment-albania"]},
    {"slug": "market-entry-partnerships", "group": "business",
     "related": ["business-partnerships", "business-plan", "company-formation-albania"]},
    {"slug": "company-formation-albania", "group": "business",
     "related": ["business-plan", "market-entry-partnerships", "real-estate-investment-albania"]},
    {"slug": "business-partnerships", "group": "business",
     "related": ["market-entry-partnerships", "business-plan", "mechanical-engineering"]},
    {"slug": "dental-tourism-albania", "group": "invest",
     "related": ["real-estate-investment-albania", "business-partnerships", "market-entry-partnerships"]},
    {"slug": "real-estate-investment-albania", "group": "invest",
     "related": ["dental-tourism-albania", "company-formation-albania", "mechanical-engineering"]},
]
