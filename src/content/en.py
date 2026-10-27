# -*- coding: utf-8 -*-
# MASTER (anglisht) i përmbajtjes së re: formulari, faqja "How it works", faqja "About", korrigjimet e kryefaqes.
# Çdo gjuhë tjetër ndjek saktësisht këtë strukturë (python3 src/check_content.py all).
C = {
 "ui": {
  # ---- formulari i kërkesës
  "f_details": "Your details",
  "f_request": "Your request",
  "f_type": "Type of support",
  "f_name": "Full name",
  "f_email": "Email",
  "f_phone": "Phone (optional)",
  "f_company": "Company (optional)",
  "f_country": "Country",
  "f_timeline": "Timeline (optional)",
  "f_tl_opts": ["Select a timeline", "As soon as possible", "Within 1 month", "In 1 to 3 months", "Just exploring"],
  "f_message": "Describe your request",
  "f_message_ph": "What exactly do you need? Include the location or site, the scale (size, capacity or budget range, if you have one), the documents you already have and the result you expect.",
  "f_hint": "The more precise your description, the more precise our first reply. Minimum 40 characters.",
  "f_consent": "I agree that AIEM uses these details to reply to my request.",
  "f_send": "Send request",
  "f_sending": "Sending…",
  "f_ok_title": "Request received",
  "f_ok_text": "We sent a confirmation to {email}. Your reference is {ref}. A specialist replies, typically within minutes, depending on volume.",
  "f_err": "Sending failed. Check your connection and try again.",
  "f_err_required": "Please enter your name, a valid email, your country and a description of at least 40 characters.",
  "f_err_consent": "Please tick the consent box to continue.",
  "f_fallback": "Your email app has opened with your request ready to send. If nothing opened, check that an email app is set up on this device.",
  "desk_title": "Send your request",
  "desk_reply": "First reply typically within minutes, depending on volume",
  "svc_write": "Request a proposal for this service",
  # ---- kryefaqja dhe shell
  "util_reply": "Send your request: first reply typically within minutes",
  "util_email": "Written proposal before any work starts",
  "footer_send": "Send a request",
  "footer_about": "An international support portal for engineering, business and investment projects in Albania. In ten languages.",
  "how_h2": "How it works",
  "how_lead": "From your request to a written proposal in four clear steps.",
  "how_more": "See the full process",
  "steps": [
   {"t": "Describe your request", "d": "Choose the type of support and tell us what you need. A precise request gets a precise first answer."},
   {"t": "A specialist replies", "d": "Your request reaches the dedicated desk for that service. A specialist replies, typically within minutes."},
   {"t": "Review a written proposal", "d": "Scope, timeline and price in writing, with no obligation and no pressure."},
   {"t": "Work and delivery", "d": "A named lead coordinates the work and hands over documents you can use as they are."}
  ],
  "problems_lead": "Start from what you want to achieve, not from our service list.",
  "panel_h2": "Who is behind AIEM",
  "panel_p": "Engineers, business consultants and licensed partners working as one team, with one point of contact for you.",
  "panel_cta": "About AIEM",
  "cta_band_h2": "Describe your request. We reply with a clear next step.",
  "cta_band_btn": "Send your request"
 },
 "home": {
  "desc": "International support portal for engineering, business plans, company formation, dental tourism and property in Albania. Send your request.",
  "lead": "AIEM connects you with the right expert for engineering, business and investment projects in Albania. Describe your request, and a specialist replies, typically within minutes.",
  "ticks": ["One request, routed to the right specialist desk", "Written proposal before any work starts", "Ten languages, confidential by default"],
  "faq1": "Use the request form on any page. Choose the type of support, add your details and describe what you need. Your request goes to the dedicated desk for that service, and you receive a confirmation straight away."
 },
 "contact": {
  "title": "Send your request | Contact AIEM",
  "desc": "Send your request to the AIEM support desk. Choose the service, describe what you need, and a specialist replies, typically within minutes. Ten languages.",
  "h1": "Send your request",
  "lead": "Choose the type of support and describe what you need. Your request goes straight to the dedicated desk for that service. The first reply typically arrives within minutes, depending on volume.",
  "tips_h2": "What to include in your request",
  "tips": [
   "What you want to achieve, and by when",
   "Where: country, city or site",
   "Scale: size, capacity or budget range, if you have one",
   "Documents you already have (plans, offers, bills, drafts)",
   "Anything that limits the project: regulations, deadlines, partners"
  ],
  "response_h2": "What happens next",
  "response_p": "You receive a confirmation with a reference number. A specialist from the right desk reads your request and replies with a first answer or with the questions we need to give you one. If the work needs a proposal, you receive it in writing with scope, timeline and price.",
  "confidentiality_p": "Your request is treated as confidential. We sign a non-disclosure agreement on request."
 },
 "privacy": {
  "desc": "How we collect, use and protect the personal data you send us through the request form.",
  "s0": ["What data we collect", "The data you enter in the request form: your name, email address, phone number, company, country, the description of your request, and the page and language you used. Requests are delivered to our support desk by email through Google services (Google Apps Script) and may be logged in a spreadsheet for follow-up."]
 },
 "desc_tail": {"from": ["Ask support by email.", "Write to support.", "Request a proposal."], "to": "Send your request."},
 "bp": {
  "name": "Business partnerships",
  "short": "We connect businesses with engineers, consultants, lawyers, suppliers and investors for joint projects.",
  "meta_title": "Business partnerships in Albania | AIEM",
  "meta_desc": "Find reliable business partners and specialist professionals in Albania: engineers, consultants, lawyers, suppliers and investors. Request an introduction.",
  "h1": "Business partnerships in Albania",
  "lead": "We connect your business with professionals and with other businesses: engineers, consultants, lawyers, accountants, suppliers and investors, for joint projects.",
  "includes": ["Partner profiles matched to skills and industry", "Filtered introductions, not unvetted contact lists", "Drafting the cooperation agreement and defining roles", "Follow-up during the first project phase"],
  "audience": "For businesses and investors that need an expert or a partner they do not have in-house, and want an introduction they can trust.",
  "deliver": ["A match profile with reasoning", "A direct introduction to interested parties", "A cooperation agreement with written terms"],
  "faqs": [
   ["Is a written agreement required?", "Yes. We agree the terms of cooperation in writing before every project, for both sides."],
   ["How do you choose the partners you introduce?", "We match on skills, experience and references, and we introduce only when there is a real project and a reason to believe the fit is right."]
  ],
  "note": ""
 },
 "how": {
  "title": "How it works | From request to proposal | AIEM",
  "desc": "How AIEM works: describe your request, get a specialist reply, review a written proposal with scope, timeline and price, then start. Clear and without pressure.",
  "h1": "How AIEM works: from your request to a written proposal",
  "lead": "You describe what you need. We route it to the right specialist desk and reply with a first answer or the questions we need. If the work calls for it, you receive a written proposal before anything starts. Four clear steps, no pressure.",
  "steps_h2": "The process, step by step",
  "steps": [
   {"t": "Describe your request",
    "d": "Choose the type of support and fill in the request form: your details and a description of what you need. A precise request gets a precise first answer, so it helps to be concrete.",
    "b": ["What you want to achieve and by when", "Where: country, city or site", "Scale and constraints, such as size, capacity or a budget range", "Documents or drawings you already have"]},
   {"t": "Your request reaches the right desk",
    "d": "Every service has its own dedicated desk. Your request goes straight to the specialists who handle that field, not to a general inbox. You receive an automatic confirmation with a reference number, in your language.",
    "b": ["A dedicated desk for each service", "Confirmation with a reference number", "Your data is treated as confidential"]},
   {"t": "A specialist replies",
    "d": "A specialist reads your request and replies, typically within minutes depending on volume. The reply contains either a first answer or the questions we need answered to give you a useful one.",
    "b": ["Reply in your language", "Clarifying questions, only if needed", "An early view on feasibility and realistic next steps"]},
   {"t": "Review a written proposal",
    "d": "If the work needs a paid engagement, you receive a written proposal: scope, deliverables, timeline, price and what is not included. The first exchange carries no obligation, and you decide at your own pace.",
    "b": ["Scope and exclusions in writing", "A timeline with milestones", "A fixed price or a clearly defined estimate"]},
   {"t": "Work, delivery and follow-up",
    "d": "Once you approve, a named lead coordinates the work with engineers, consultants and licensed partners wherever the law requires them. You receive deliverables you can use as they are, and we remain available for follow-up questions.",
    "b": ["One point of contact for you", "Licensed partners for legal, tax and medical matters", "Documents and files handed over in usable formats"]}
  ],
  "need_h2": "What makes a request easy to answer",
  "need_lead": "You do not need technical language or a finished brief. A few concrete facts are enough for a useful first reply:",
  "need": [
   "The goal, in plain words",
   "The location or site, and the country you are writing from",
   "The approximate scale: size, capacity, quantity or budget range",
   "Your deadline, if there is one",
   "What already exists: plans, offers, bills, drafts, previous work",
   "Anything that limits the project, such as regulations, partners or timing"
  ],
  "times_h2": "How fast do we reply?",
  "times_p": "The first reply typically arrives within minutes, depending on request volume. At busy times it can take longer, and the confirmation you receive lets you know your request has arrived. A written proposal takes longer than a first reply, because it has to be accurate. We tell you when to expect it.",
  "promise_h2": "What you can expect from us",
  "promise": [
   {"t": "Clear communication", "d": "Plain language, in your language, with a named contact and a reference number for every request."},
   {"t": "Written scope and price", "d": "Every proposal states what is included, what is not and what it costs, before any work begins."},
   {"t": "Confidentiality", "d": "Your idea and your data stay private. We sign a non-disclosure agreement on request."},
   {"t": "Honest limits", "d": "We say plainly what we can and cannot do, and we do not promise outcomes we cannot guarantee."}
  ],
  "models_h2": "Ways of working together",
  "models_lead": "The format depends on the service and on what you need. We agree it with you in the proposal.",
  "models": [
   {"t": "A single deliverable", "d": "A defined result for a defined price, such as a business plan, a design package or a company registration."},
   {"t": "A phased project", "d": "Larger work split into milestones, so you review and approve each phase before the next begins."},
   {"t": "Follow-up support", "d": "Continued help after delivery, such as questions during construction, registration steps or partner talks."}
  ],
  "limits_p": "AIEM is not a law firm, a tax advisor or a dental clinic. Legal, tax and medical matters are handled only by licensed partners, and we never guarantee outcomes outside our control, such as the approval of a loan or the return on an investment.",
  "faq_h2": "Frequently asked questions",
  "faq": [
   ["Is the first reply free?", "Yes. The first exchange is free of obligation. Before any paid work you receive a written proposal with scope, timeline and price."],
   ["How fast will I get an answer?", "The first reply typically arrives within minutes, depending on request volume. You receive a confirmation as soon as your request is sent."],
   ["Can I write in my own language?", "Yes. You can write in English, Albanian, Italian, German, French, Spanish, Turkish, Arabic, Russian or Chinese."],
   ["Do I need to know exactly what I need?", "No. Describe the problem or the goal as you see it. If something is missing, a specialist asks the questions needed to move forward."],
   ["How is the price set?", "By the scope of the work, which we confirm in the written proposal before you decide. We do not quote a price without understanding the request."],
   ["What happens to my data?", "It is used only to reply to your request and prepare a proposal. It is not sold. Details are in our privacy policy."]
  ],
  "cta_h2": "Ready to describe your request?",
  "cta_p": "It takes a few minutes. You receive a confirmation straight away, and a specialist replies with a first answer or the questions needed to give you one.",
  "cta_btn": "Send your request"
 },
 "about": {
  "title": "About AIEM | Engineering and business support in Albania",
  "desc": "Who we are, what we do and why clients choose us: engineers, business consultants and licensed partners working as one team for projects in Albania.",
  "h1": "About Albanian Industry Engineering and Management",
  "lead": "AIEM is an international support portal that connects businesses, investors and individuals with the right engineering, business and investment expertise in Albania.",
  "who_h2": "Who we are",
  "who": [
   "AIEM was created around a simple observation: people who want to build, do business or invest in Albania rarely lack ambition. What they lack is a reliable single point of contact who understands the local context and speaks their language. We are that point of contact.",
   "Our team combines engineers, business consultants and project coordinators with a network of licensed legal, tax, medical and real estate partners. You describe your project once, and we bring the right people together around it.",
   "We write to clients in ten languages, so that the conversation happens in the language you think in, and we explain Albanian procedures in terms an international client can act on."
  ],
  "mission_h2": "What we are here to do",
  "mission_p": "Our mission is to make decisions about projects in Albania easier and safer: technical and business analysis with visible assumptions, a written scope and price before any work, and specialists who are accountable for their part of the result.",
  "do_h2": "What we do",
  "do_lead": "Three areas of work, one point of contact.",
  "why_h2": "Why clients choose AIEM",
  "why": [
   {"t": "Engineering and business under one roof", "d": "Costs and feasibility come from technical analysis, not guesses. Business plans are built on real engineering figures."},
   {"t": "One point of contact", "d": "You do not coordinate five offices. One desk routes your request and one lead coordinates the work."},
   {"t": "Written scope and price", "d": "You know what is included, what is not and what it costs before you commit to anything."},
   {"t": "Licensed partners where the law requires", "d": "Legal, tax and medical matters are handled only by licensed professionals, never improvised."},
   {"t": "Local knowledge, international standard", "d": "We know how procedures work in Albania and present them with the clarity an international client expects."},
   {"t": "Your language", "d": "Write to us in any of ten languages and receive a clear, direct answer."}
  ],
  "clients_h2": "Who we work with",
  "clients": [
   "Companies and entrepreneurs entering the Albanian market",
   "Manufacturers and businesses building or upgrading facilities",
   "Investors in property and projects",
   "Individuals and the Albanian diaspora: company registration, property, dental treatment",
   "Businesses already in Albania that need engineering or planning support"
  ],
  "values_h2": "Our principles",
  "values": [
   {"t": "Honesty about limits", "d": "We say what we can do, what we cannot and what depends on others."},
   {"t": "Confidentiality", "d": "Your project and your data stay private, with a non-disclosure agreement on request."},
   {"t": "Transparent terms", "d": "Any fee or commission arrangement is agreed in writing in advance."},
   {"t": "Accountability", "d": "Every request has a reference number and a named contact until it is resolved."}
  ],
  "how_h2": "How we work",
  "how_p": "You describe your request, it reaches the dedicated desk for that service, a specialist replies, and, if the work calls for it, you receive a written proposal before anything starts. Every step is explained on one page.",
  "how_cta": "See how it works",
  "limits_h2": "Our boundaries",
  "limits_p": "We are not a law firm, a tax advisor or a dental clinic. Legal, tax and medical matters are handled only by licensed partners. We do not promise outcomes we cannot guarantee, such as the approval of a loan or the return on an investment. The decision always stays yours.",
  "cta_h2": "Tell us what you need.",
  "cta_btn": "Send your request"
 }
}
