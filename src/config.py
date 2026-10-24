# -*- coding: utf-8 -*-
# KONFIGURIMI I PORTALIT. Ndrysho vetëm këtu, pastaj ekzekuto: python3 src/build.py

CFG = {
    "name": "Albanian Industry Engineering and Management",
    "short": "AIEM",
    "url": "https://aiem-lyart.vercel.app",   # NDRYSHO kur lidh domenin final
    "date": "2026-10-23",
    "ga4": "",                                # p.sh. G-XXXXXXXXXX (opsionale)

    # ---- KANALI I KONTAKTIT: VETËM EMAIL ----
    # NDRYSHO: adresa kryesore e suportit (duhet të jetë e vërtetë dhe e monitoruar).
    "support_email": "support@aiem.al",
}

# Opsionale: adresa e veçantë për çdo lloj suporti. Nëse mungon, përdoret support_email.
# Çelësat: slug-et e shërbimeve + "network" + "general".
SUPPORT_EMAILS = {
    # "mechanical-engineering": "engineering@aiem.al",
    # "electrical-engineering": "engineering@aiem.al",
    # "business-plan": "business@aiem.al",
    # "market-entry-partnerships": "business@aiem.al",
    # "company-formation-albania": "company@aiem.al",
    # "dental-tourism-albania": "health@aiem.al",
    # "real-estate-investment-albania": "property@aiem.al",
    # "business-partnerships": "network@aiem.al",
    # "network": "network@aiem.al",
}

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
