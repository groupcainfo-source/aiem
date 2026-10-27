# -*- coding: utf-8 -*-
# Përmbajtje e thellë (anglisht). Blloqe: h2, h3, p, ul, ol, note. Lidhje të brendshme: [[slug|tekst]].
DEEP = {
 "toc": "On this page",
 "services": {

  # ------------------------------------------------------------------ MECHANICAL
  "mechanical-engineering": {
   "blocks": [
    ["h2", "Signs your mechanical systems need engineering attention"],
    ["p", "Many factories and commercial buildings run on systems that were assembled piece by piece over the years: a new machine here, an extra fan there, a boiler replaced when it failed. Nothing is obviously wrong until the costs show up. If any of the following sounds familiar, a structured mechanical review will usually pay for itself."],
    ["ul", [
      "One production line stops several times a month for reasons nobody can fully explain.",
      "Energy bills keep rising while output stays the same.",
      "Ventilation cannot keep heat, dust, fumes or humidity within acceptable limits.",
      "New equipment was bought before anyone checked that power, compressed air, water or steam could support it.",
      "The drawings no longer match what is actually installed, so every repair starts with guesswork."]],
    ["h2", "How we run a mechanical project"],
    ["p", "We work in stages, so that decisions rest on evidence and can be reviewed before money is spent on equipment."],
    ["ol", [
      "Brief and site survey. We agree what must be produced, how much, and under which conditions. We measure the site and the existing equipment instead of assuming.",
      "Concept. Two or three layout options with utility needs and a rough cost range, so you can choose a direction early.",
      "Basic design. Heat loads, air flows, pipe and duct sizes, support structures and equipment specifications, all backed by calculations you can inspect.",
      "Supplier comparison. A technical table that compares offers on the same basis, not only on price.",
      "Detailed design. Drawings, schedules and instructions that a contractor can build from without guessing.",
      "Supervision and commissioning. We check the installation against the drawings, witness the tests and hand over complete documentation."]],
    ["h2", "Calculations that prevent expensive mistakes"],
    ["p", "Oversizing is one of the most common and least visible errors. A heating, ventilation or cooling system sized with a large safety margin costs more to buy, runs inefficiently at part load and often has control problems. Undersizing is just as costly, because the plant cannot hold the conditions the process needs. We size systems from calculated loads rather than from rules of thumb:"],
    ["ul", [
      "Heat gains and losses through the building envelope, equipment, lighting and people.",
      "Ventilation air for occupants and for process emissions such as dust, solvents or steam.",
      "Pressure drops in pipes and ducts, which decide the pumps and fans you actually need.",
      "Compressed-air demand, including a realistic allowance for leaks.",
      "Structural checks for equipment foundations, platforms and pipe supports."]],
    ["h2", "Choosing equipment: what we compare besides price"],
    ["p", "The cheapest offer is rarely the cheapest machine to own. When we compare suppliers we look at the whole picture:"],
    ["ul", [
      "Efficiency across the hours the equipment will really run, not only at its rated point.",
      "Availability of spare parts and qualified technicians in Albania or the region.",
      "Delivery time and installation conditions, including cranes, access and downtime.",
      "Noise, vibration, footprint and maintenance access.",
      "Warranty terms and what they exclude.",
      "Total cost over five to ten years, including energy and maintenance."]],
    ["h2", "Energy efficiency without a complete rebuild"],
    ["p", "Most plants can reduce energy use without replacing everything. Typical measures include repairing compressed-air leaks, insulating hot and cold pipes, fitting variable-speed drives to pumps and fans, recovering heat from exhaust air, and replacing only the equipment that is clearly oversized or at the end of its life. We start with an audit: we measure the consumption of the main systems over a representative period, rank the measures by payback and propose them in that order. The electrical side of the same project is covered by our [[electrical-engineering|electrical engineering]] service."],
    ["h2", "What we need from you to start"],
    ["ul", [
      "A short description of the product or process and the output you target.",
      "Building plans, or photos and key dimensions of the site.",
      "A list of existing equipment with nameplate data where available.",
      "Energy and utility bills for the last twelve months, if you have them.",
      "Your deadline and an approximate budget range."]],
    ["h2", "Mistakes we help you avoid"],
    ["ul", [
      "Buying equipment before a utilities study shows whether the site can supply it.",
      "Copying a design from another country without adapting it to local climate, power quality and available service.",
      "Forgetting maintenance access, so that every filter change needs scaffolding.",
      "Skipping commissioning tests, so that problems appear only after the contractor has left."]],
    ["p", "If the project is part of a larger investment, a [[business-plan|business plan]] built on realistic engineering costs will be far more convincing to a bank than one built on estimates."],
   ],
   "faqs": [
    ["Do you design heating, ventilation and cooling for buildings as well as for factories?", "Yes. We design HVAC for production halls, warehouses, offices, hotels and other commercial buildings, from load calculation to equipment selection and supervision."],
    ["Can you review a supplier's quotation before I sign?", "Yes. We check whether the offered equipment matches the calculated need, whether anything is missing from the scope, and how the offer compares with others on lifetime cost."],
    ["Which standards do you design to?", "We work to recognised European and international engineering standards and to the requirements that apply to your project in Albania. We confirm the applicable set with you at the start of each project."],
    ["Can you help if our drawings are missing?", "Yes. We survey the installation, produce as-built drawings and then use them as the basis for any upgrade."]
   ]
  },

  # ------------------------------------------------------------------ ELECTRICAL
  "electrical-engineering": {
   "blocks": [
    ["h2", "Why electrical design deserves its own engineering work"],
    ["p", "An electrical installation is the one system in a building that every other system depends on, and also the one most often improvised on site. A cable that is slightly too small, a breaker that is not coordinated with the one upstream, or an earthing system that was never measured can work for years and then fail at the worst moment. Designing the installation first is cheaper than correcting it later."],
    ["h2", "What a complete electrical project covers"],
    ["ul", [
      "Load calculation for every circuit and for the building as a whole, with allowance for growth.",
      "Cable sizing for current, voltage drop and fault conditions.",
      "Short-circuit levels and protection coordination, so that a fault trips the nearest breaker and not the whole site.",
      "Distribution switchboards with clear single-line diagrams and labelling.",
      "Earthing and equipotential bonding, and lightning protection where the building requires it.",
      "Lighting design that meets the task and keeps energy use low.",
      "Automation and control, including PLC systems for machinery and building services."]],
    ["h2", "Power factor, harmonics and the bill you actually pay"],
    ["p", "Many industrial customers pay more than necessary because of poor power factor or because electronic loads distort the supply. Motors, welders and drives can draw reactive power that the utility may charge for. Variable-speed drives and rectifiers create harmonics that heat cables and transformers and disturb sensitive equipment. We measure these effects, size power-factor correction where it makes sense and check whether filters are needed, before recommending any expensive equipment."],
    ["h2", "Solar photovoltaic systems: sizing for self-consumption"],
    ["p", "A photovoltaic system is worth the most when it supplies electricity that you would otherwise buy during the day. We therefore start from your consumption profile, not from the roof size. The study compares system sizes, shows how much of the production you would use yourself, estimates payback under clearly stated assumptions and checks the roof structure, shading, cable routes and the point of connection. Grid connection follows the procedures of the distribution operator, and we prepare the technical documentation that the process requires. We do not promise a specific saving, because it depends on tariffs, consumption and the rules in force at the time."],
    ["h2", "Automation that operators can actually maintain"],
    ["p", "Good automation is simple enough for your own technicians to diagnose. We specify controllers, sensors and drives that are available in the region, document the logic in plain language and design the control panels with accessible test points. If a supplier will program the machinery, we write a clear functional specification so that the result matches what the process needs."],
    ["h2", "Measurements and tests before commissioning"],
    ["p", "Before an installation goes live, it should be tested and the results recorded. Depending on the project this includes insulation resistance, continuity, earth-loop impedance, earth-electrode resistance, residual-current device trip times and correct phase sequence. For existing sites we can also use thermal imaging on switchboards to find loose connections before they fail. You receive the protocols, which are also what an insurer or inspector will ask to see."],
    ["h2", "What we need from you to start"],
    ["ul", [
      "Building plans or a description of the site and its main loads.",
      "Recent electricity bills and, if available, the load profile.",
      "A list of machinery with power ratings and nameplate data.",
      "Existing electrical drawings, even if they are outdated.",
      "Any plans for expansion in the next three to five years."]],
    ["h2", "Common problems we correct"],
    ["ul", [
      "Switchboards that are full, unlabelled and impossible to extend.",
      "Cables loaded beyond their rating after several machines were added.",
      "No selectivity, so one short circuit blacks out a whole building.",
      "Earthing that was installed but never measured.",
      "Photovoltaic systems sized for the roof instead of for the load."]],
    ["p", "Electrical design usually goes hand in hand with [[mechanical-engineering|mechanical design]], because motors, heating and cooling are the largest electrical loads, and the investment case for a plant or a solar system can be written into a [[business-plan|business plan]]. For a new building, we coordinate both disciplines so that the cable routes and the plant rooms do not collide."],
    ["note", "We design to recognised international and European installation standards and to the requirements of the Albanian authorities and the grid operator that apply to your project. Final approvals remain with the competent authorities."],
   ],
   "faqs": [
    ["Can you design the installation for a new factory from scratch?", "Yes. We start from the process and the machinery list, calculate the loads, design the distribution and produce the drawings and specifications for tender and construction."],
    ["Do you test existing installations?", "Yes. We measure and inspect existing installations, report the findings in order of risk and propose corrections with an estimated cost."],
    ["How do I know whether solar panels make sense for my business?", "We compare your hourly or daily consumption with the expected production of different system sizes, then show how much you would consume yourself and what the payback is under stated assumptions."],
    ["Can you help reduce my electricity bill?", "Often yes. We look at tariff structure, power factor, peak demand and wasted consumption, and rank the measures by payback."]
   ]
  },

  # ------------------------------------------------------------------ BUSINESS PLAN
  "business-plan": {
   "blocks": [
    ["h2", "What a business plan is really for"],
    ["p", "A business plan has two readers. The first is the person who will decide whether to lend, invest or partner, and who wants to see that you understand the market and that the numbers hold together. The second is you: the process of writing it forces you to test every assumption on paper, which is far cheaper than testing it with your own money. A plan built only to satisfy a form tends to fail both readers."],
    ["h2", "What we put in a plan that a bank or investor will read"],
    ["ol", [
      "Executive summary. One page that states the opportunity, the amount you need and what it will be used for.",
      "Market analysis. Who the customers are, how large and how fast-growing the demand is, who competes for it and how you differ.",
      "Offer and pricing. What you sell, why customers will choose it and how the price relates to cost and to competitors.",
      "Sales and marketing plan. How customers will actually hear about you and buy, with realistic conversion assumptions.",
      "Operations plan. Location, equipment, suppliers, staffing and capacity, with timelines for each step.",
      "Management and organisation. Who does what, and where the plan depends on specific people.",
      "Financial model. Revenue, costs, cash flow, financing and returns, built from the assumptions above.",
      "Risks and scenarios. What can go wrong, how likely it is and what you would do about it."]],
    ["h2", "Assumptions are where plans win or lose"],
    ["p", "Every number in a financial model rests on an assumption: price, volume, cost, payment terms, the time to reach full capacity. A reader will look hardest at the assumptions that move the result most. We list them in one place, give each a source or a reasoned basis, and show how the outcome changes when they move. A plan that says openly which five assumptions matter most is more credible than one that presents a smooth curve."],
    ["h2", "The financial model: what it contains"],
    ["ul", [
      "Revenue by product or segment, month by month in the first year and yearly afterwards.",
      "Fixed and variable costs, separated, so that the break-even point is clear.",
      "Investment in equipment, premises and working capital, with timing.",
      "Cash flow including taxes, loan repayments and the delay between selling and being paid.",
      "Debt service coverage, which lenders check first, and the return for investors.",
      "Three scenarios, base, optimistic and pessimistic, with a short explanation of each."]],
    ["p", "The model is delivered in Excel with open formulas, so that you can change a price or a volume and see the result without calling us."],
    ["h2", "Where engineering makes the plan stronger"],
    ["p", "Many plans fail on costs that nobody checked: the real price of the equipment, the utilities a plant needs, the time construction takes. Because our team includes engineers, a production or property project can be costed from a technical basis. Equipment and installation costs come from [[mechanical-engineering|mechanical]] and [[electrical-engineering|electrical]] specifications, not from a guess. That makes the plan easier to defend in front of a lender."],
    ["h2", "Entering a market with a plan"],
    ["p", "If the plan is for entering the Albanian market from abroad, it also covers how to reach customers, whether to work through a distributor or a local company, and what the legal structure will be. Those questions are linked to [[market-entry-partnerships|market entry and partnerships]] and to [[company-formation-albania|company formation]], and we can handle them together so that the plan and the practical steps agree."],
    ["h2", "What we need from you to start"],
    ["ul", [
      "A description of the business idea or project, even if it is rough.",
      "Any numbers you already have: quotes, prices, past sales, costs.",
      "The purpose of the plan: bank loan, investor, grant, partner or your own decision.",
      "The amount of financing you are looking for, if known.",
      "The language the plan must be written in."]],
    ["h2", "Mistakes we help you avoid"],
    ["ul", [
      "Treating a hoped-for result as a forecast.",
      "Forgetting working capital, so that a profitable business runs out of cash.",
      "Using one scenario only.",
      "Ignoring the time between starting and reaching full capacity.",
      "Writing for the bank when the real decision-maker is a partner, or the reverse."]],
    ["note", "No consultant can guarantee that a loan, grant or investment will be approved. We build the plan so that it meets the criteria lenders and investors commonly apply and so that every assumption can be defended."],
   ],
   "faqs": [
    ["What is the difference between a business plan and a feasibility study?", "A feasibility study asks whether an idea is worth pursuing. A business plan assumes you will go ahead and sets out how. We often start with a short feasibility check when the idea is still uncertain."],
    ["How many scenarios do you include?", "At least three: a base case, an optimistic case and a pessimistic case, with the main assumptions that change between them."],
    ["Can the plan be used for a grant application?", "Often yes, but grant programmes have their own formats and criteria. Tell us which programme you have in mind and we adapt the structure."],
    ["Will I be able to update the financial model myself?", "Yes. The model is delivered in Excel with open formulas, and we include a short walkthrough so that you can change inputs and read the results."]
   ]
  },

  # ------------------------------------------------------------------ MARKET ENTRY
  "market-entry-partnerships": {
   "blocks": [
    ["h2", "Why most market entries are really partner decisions"],
    ["p", "A company entering a new country rarely fails because the product is bad. It fails because the first local partner was chosen quickly, on the basis of a good meeting and a friendly introduction. In a smaller market the effect is larger, because there are fewer partners to choose from and a bad fit is harder to replace. Our work is to make that choice deliberate."],
    ["h2", "The routes into the Albanian market"],
    ["p", "Before looking for a partner, it helps to decide which route you want. Each has a different cost, a different level of control and a different risk."],
    ["ul", [
      "Distributor. A local company buys from you and resells. Fast and inexpensive to start, but you have less control over price and brand.",
      "Sales agent. A local person or company finds customers and earns a commission, while you invoice directly. More control, but you carry the stock and the credit risk.",
      "Joint venture. You and a local company set up a shared business. Combines your product with their knowledge and relationships, and needs a carefully drafted agreement.",
      "Own subsidiary or branch. Maximum control, with the full cost of setting up and running it. Often a later step once demand is proven.",
      "Contract manufacturing or local assembly. Used when transport costs, tariffs or lead times make local production attractive."]],
    ["h2", "How we find and screen partners"],
    ["ol", [
      "Brief. Your product, your target customers, the volumes you hope for and what you want from a partner.",
      "Market study. Who buys, through which channels, and who already sells similar products.",
      "Long list. Companies that appear to fit, from our network and from open sources.",
      "Screening. We check what the company really does, its customers, its financial standing as far as it can be verified and its reputation with suppliers and buyers.",
      "Short list and meetings. We prepare the introductions, interpret between business cultures where needed and take notes.",
      "Terms. We help you structure the relationship and prepare the points for the contract."]],
    ["h2", "What a good partnership agreement covers"],
    ["ul", [
      "Territory and whether it is exclusive, and what happens if the partner misses its targets.",
      "Minimum purchase or sales commitments, and how they are reviewed.",
      "Pricing, discounts, payment terms and who carries the credit risk.",
      "Use of your brand, trademarks and marketing material.",
      "Service, warranty and spare-parts responsibilities.",
      "Duration, renewal and clear termination rules, including stock and customer handover.",
      "Confidentiality and protection of your know-how."]],
    ["p", "Contracts are drafted and reviewed by licensed lawyers. We prepare the commercial points and work with partner lawyers so that the agreement matches what was agreed in the room."],
    ["h2", "Culture and communication"],
    ["p", "Business in Albania often moves through personal relationships and direct conversation. Foreign companies used to formal procedures can read that as disorder, while local partners can read formality as distrust. Having someone who understands both sides, and who can translate not only words but expectations, saves time and avoids misunderstandings that later look like disputes."],
    ["h2", "Signs of a good partner, and of a bad one"],
    ["ul", [
      "Good: it already sells to the customers you want, and can show it.",
      "Good: it is willing to commit to targets and to put them in the contract.",
      "Good: its own suppliers and customers speak well of it.",
      "Bad: it wants exclusivity for the whole country without any commitment to sell.",
      "Bad: it asks for large advance payments or for credit that you cannot control.",
      "Bad: it cannot explain how it would reach your customers."]],
    ["h2", "What we need from you to start"],
    ["ul", [
      "Product or service description, with catalogues or specifications.",
      "Your target customers and the volumes or turnover you hope to reach.",
      "The route you are considering, or the question of which route to choose.",
      "Any contacts or past attempts in the market.",
      "Your timeline and the budget for the exploration phase."]],
    ["h2", "Related support"],
    ["p", "Entering a market usually needs more than a partner. A [[business-plan|business plan]] sets out the numbers, [[company-formation-albania|company formation]] covers a local entity if you need one, and our [[business-partnerships|professional network]] gives access to engineers, lawyers and consultants who can support the project."],
   ],
   "faqs": [
    ["Do you act as my agent or distributor in Albania?", "No. We help you find, check and meet suitable partners and structure the relationship. The partner becomes your counterparty, not us."],
    ["Can you help a company that already has a partner but is unhappy?", "Yes. We can review the relationship, identify what is not working and help you renegotiate or look for an alternative."],
    ["How long does it take to find a suitable partner?", "It depends on the industry and the requirements. A first short list is usually possible after the market study, and meetings follow. We give you a written timeline at the start."],
    ["Is the service only for foreign companies?", "No. Albanian companies also use it to find foreign suppliers, technology partners and distributors."]
   ]
  },

  # ------------------------------------------------------------------ COMPANY FORMATION
  "company-formation-albania": {
   "blocks": [
    ["h2", "Choosing the right legal form"],
    ["p", "The legal form decides who is liable, how the company can raise money and how much administration it carries. For most small and medium businesses the choice is between a limited liability company (SH.P.K.) and, for larger or more complex projects, a joint stock company (SH.A.). Other options include an individual business and a branch of a foreign company. A branch is part of its parent and does not limit the parent's liability, which is why many investors prefer a separate local company."],
    ["ul", [
      "SH.P.K. A common choice for owners who want limited liability and a simple structure.",
      "SH.A. Suited to projects with many shareholders, or plans to raise capital by issuing shares.",
      "Individual business. Simple, but the owner is personally responsible for the business.",
      "Branch of a foreign company. Useful when the parent wants to operate directly, with the liability consequences described above."]],
    ["h2", "The registration process step by step"],
    ["ol", [
      "Decide the form, the name, the object of activity and the share structure.",
      "Prepare the founding documents: the statute and the founding act, with the details of owners and administrators.",
      "Provide identification of the owners and administrators. For foreigners, documents issued abroad usually need an apostille or legalisation and a certified translation.",
      "Register with the National Business Centre (QKB). On registration the company receives its business identification number (NUIS).",
      "Open a bank account for the company and deposit the share capital, if required for the chosen form.",
      "Complete registration for taxes and, if the company will employ people, for employer obligations and social insurance.",
      "Set up accounting and a calendar of recurring filings and payments."]],
    ["h2", "Questions to settle before you register"],
    ["ul", [
      "Object of activity. It must match what you will really do, because some activities need a licence or permit before you start.",
      "Registered address. The company needs a seat in Albania, and the address should be one you can use to receive official letters.",
      "Owners and control. Albanian rules require the real beneficial owners to be identified, so the structure must be transparent from the beginning.",
      "Administrator. Who will manage the company, and whether that person needs to live in Albania.",
      "Taxes. Whether and when the company must register for value added tax depends on its activity and expected turnover, and should be confirmed with an accountant."]],
    ["h2", "Registering from abroad"],
    ["p", "Many foreign founders ask whether they must travel to Albania. In some cases the process can be completed with a power of attorney given to a representative. This requires the document to be prepared properly, signed in front of the right authority and legalised, which takes time if it is not planned. We tell you at the start what is possible in your case and which documents you will need to prepare in your country."],
    ["h2", "After registration: the obligations people forget"],
    ["ul", [
      "Regular tax filings and payments, which have fixed dates.",
      "Annual financial statements.",
      "Keeping the company register up to date when owners, addresses or administrators change.",
      "Employment contracts and social insurance for staff.",
      "Licences and permits linked to the activity, which may need renewal."]],
    ["p", "A good accountant who knows your activity pays for themselves by avoiding late filings and penalties. We can introduce partner accountants, and we connect company formation with the [[business-plan|business plan]] and, where relevant, with [[real-estate-investment-albania|property purchase]] so that the legal structure fits the investment."],
    ["h2", "A realistic timeline"],
    ["p", "Once the documents are complete, the registration step itself can be quick. The delays usually come from elsewhere: documents issued abroad that need an apostille and a certified translation, the bank's onboarding and compliance checks for a new company, and licences for regulated activities. We give you a calendar at the start that separates the steps you control from the ones you do not, so that a launch date is based on the slowest step, not the fastest."],
    ["h2", "What we need from you to start"],
    ["ul", [
      "What the company will do, in two or three sentences.",
      "The names, nationalities and ownership shares of the owners.",
      "Who will administer the company.",
      "Whether you will be present in Albania or need to act through a representative.",
      "Your expected start date."]],
    ["note", "This service does not replace legal or tax advice. Legal and tax matters are handled with partner lawyers and accountants, and rules change, so everything is verified against current requirements before you sign."],
   ],
   "faqs": [
    ["What is the difference between SH.P.K. and SH.A.?", "An SH.P.K. is the usual form for small and medium companies with a small number of owners. An SH.A. is designed for larger structures and for raising capital through shares. We recommend a form after learning about your plans."],
    ["Can I keep my ownership private?", "Albanian rules require beneficial owners to be identified and registered, so the structure must be transparent. We explain what information becomes available and to whom."],
    ["Do I need an accountant?", "In practice yes. Even a small company has recurring filings and payments, and mistakes lead to penalties. We can introduce partner accountants."],
    ["Can you help after the company is registered?", "Yes. We can support with the bank account, the first contracts, partners and the business plan, and put you in touch with accountants and lawyers."]
   ]
  },

  # ------------------------------------------------------------------ PARTNERSHIPS
  "business-partnerships": {
   "blocks": [
    ["h2", "Why a network works better than a directory"],
    ["p", "A directory gives you a list of names. A network gives you someone who knows what each of them is good at, who has seen them work and who can tell you honestly whether they suit your project. We build our network by profile and reference, and we introduce people only when there is a real project and a reason to believe they fit."],
    ["h2", "How a match is made"],
    ["ol", [
      "You describe what you need: a skill, a partner or a supplier, and the project it is for.",
      "We translate that into a profile: the skills, the experience, the size and the languages that matter.",
      "We select from the network and, where needed, from outside it, and check references.",
      "We introduce two or three suitable candidates, with the reasons we chose them.",
      "You meet them. We can attend the first meeting, take notes and help clarify scope.",
      "If you decide to proceed, we help you put the cooperation terms in writing."]],
    ["h2", "Who is in the network"],
    ["ul", [
      "Mechanical and electrical engineers and technical specialists.",
      "Business, financial and management consultants.",
      "Lawyers, notaries and accountants.",
      "Suppliers, manufacturers and distributors.",
      "Real estate professionals and clinics.",
      "Investors looking for projects."]],
    ["p", "Each member is reviewed on profile and references. We keep the network focused on a limited number of fields, so that an introduction is always relevant to the project and never a mass mailing to everyone on a list."],
    ["h2", "For clients: what a good introduction saves you"],
    ["p", "Finding a reliable subcontractor or adviser on your own costs time, and the cost of choosing wrongly appears later. A short, reasoned list of candidates saves you the search, and a written agreement from the start saves you from the disputes that come from unclear roles. If your question is mainly about reaching customers or suppliers in a new market, see [[market-entry-partnerships|market entry and partnerships]]."],
    ["h2", "For professionals: how to apply"],
    ["p", "Independent professionals and small companies often have the skills for larger projects but not the visibility. If that describes you, apply by email with a short description of your expertise, the type of projects you want and one or two references we can contact. We review every application. Joining is not a purchase and does not guarantee work. We introduce you when a request fits your profile."],
    ["h2", "What a cooperation agreement should say"],
    ["ul", [
      "The scope of work and who is responsible for each part.",
      "How the price is set and when it is paid, including how changes are handled.",
      "Deadlines, acceptance criteria and what happens if they are missed.",
      "Ownership of the results, drawings and documents produced.",
      "Confidentiality, and what happens to client contacts.",
      "How either side can end the cooperation."]],
    ["p", "Working with other professionals can be as simple as a technical second opinion or as large as a joint bid. For technical work see [[mechanical-engineering|mechanical engineering]] and [[electrical-engineering|electrical engineering]]; for projects that need financing, a [[business-plan|business plan]] is usually the first step."],
    ["h2", "Typical situations where we connect people"],
    ["ul", [
      "A manufacturer needs a licensed electrician or mechanical contractor for an installation, and wants a reasoned shortlist instead of a phone book.",
      "A foreign company wants a local accountant and a lawyer who can work together, in a language it understands.",
      "An investor with capital is looking for a project with a competent local operator.",
      "A small engineering firm wants to join a larger tender and needs a prime contractor to introduce it.",
      "A clinic, hotel or property agent wants a reliable partner who sends international clients and handles the coordination."]],
    ["h2", "Red flags when choosing a partner"],
    ["p", "Whether you find a partner through us or on your own, a few warning signs are worth taking seriously:"],
    ["ul", [
      "Promises that sound too good, with no references you can call.",
      "Reluctance to put terms, prices or responsibilities in writing.",
      "A company that does everything and cannot show recent work in your field.",
      "Pressure to pay a large advance before any work is defined.",
      "Contacts that cannot be verified, or that change when you ask questions."]],
    ["h2", "How we protect both sides"],
    ["ul", [
      "We introduce only when there is a real need and a reasoned fit.",
      "Terms are agreed in writing before work starts.",
      "We sign confidentiality agreements on request.",
      "We do not guarantee outcomes, and we say so before you decide."]],
   ],
   "faqs": [
    ["Does it cost anything to join the network?", "Applying is free. If we introduce you to a client, the terms of any commission or fee are agreed in writing beforehand."],
    ["Do you guarantee that members will receive projects?", "No. We introduce members when a request fits their profile, but we cannot guarantee work."],
    ["Can I use the network to find a supplier?", "Yes. Describe what you need and we propose suitable candidates, within or outside the network."],
    ["How do you check professionals?", "We review their profile, their experience and their references. For regulated professions we expect valid licences."]
   ]
  },

  # ------------------------------------------------------------------ DENTAL TOURISM
  "dental-tourism-albania": {
   "blocks": [
    ["h2", "What dental tourism really involves"],
    ["p", "Travelling for dental treatment combines a medical decision with a trip. The medical part belongs entirely to the dentist. Our part is everything around it: finding clinics that can be checked, getting a written quote, arranging travel and accommodation, interpreting during visits and keeping the clinic and you coordinated. A well-organised trip lets you concentrate on the treatment instead of on logistics."],
    ["h2", "How the process works"],
    ["ol", [
      "You send us a short description of your situation and, if you have them, X-rays or earlier treatment records.",
      "We ask partner clinics to review them and to propose a treatment plan and a written quote.",
      "You compare the offers: what is included, how many visits are needed, what the clinic guarantees and what extra costs may arise.",
      "After you choose, we plan the trip: flights, hotel, airport transfers and the visit schedule.",
      "In Albania we can accompany you and interpret at appointments if you wish.",
      "After treatment we stay in contact and help you reach the clinic for follow-up questions."]],
    ["h2", "How to compare clinics without being a dentist"],
    ["p", "You cannot judge clinical quality from a brochure, but you can check things that tell you how a clinic works:"],
    ["ul", [
      "Whether the dentists and the clinic are licensed, and whether they will tell you who will treat you.",
      "Whether the quote is written and itemised, and states what is not included.",
      "What imaging and diagnosis come before the plan, rather than a price given by telephone.",
      "Which materials and brands are used, and whether you receive the details in writing.",
      "What the warranty covers, for how long and what you must do to keep it valid.",
      "How the clinic handles complications and whether you can reach it after you return home."]],
    ["h2", "Planning the trip realistically"],
    ["p", "Some treatments need only one visit. Others need several, with healing time in between. For example, when implants are involved, the dentist decides how long to wait between stages, and in many cases that interval is measured in months, which may mean two trips. Ask the clinic for a realistic schedule at the start, and book more days than seem necessary, so that you do not shorten treatment to catch a flight."],
    ["h2", "Questions to ask before you decide"],
    ["ul", [
      "Who will perform each stage of the treatment, and will it be the same dentist throughout?",
      "Are there cheaper or less invasive alternatives, and why is this one recommended?",
      "What are the risks, and what happens if the result is not as planned?",
      "How many visits are needed and how long is each?",
      "What does the warranty exclude?",
      "Who do I contact after I return, and how quickly?"]],
    ["h2", "Who uses this service"],
    ["p", "Most of our clients are people living abroad who want treatment in Albania, including members of the Albanian diaspora who combine treatment with a visit home. We also help assistance companies and travel organisers who need a reliable local coordinator. If your trip includes a wider stay in Albania, our team can also support related needs such as [[real-estate-investment-albania|property viewing and investment]]."],
    ["h2", "Aftercare and follow-up"],
    ["p", "Good treatment includes what happens after you leave the chair. Before you travel, make sure you know the aftercare instructions, the symptoms that need a call to the clinic and how quickly someone will answer. Keep copies of your treatment records, X-rays and the materials used, so that any dentist at home can continue your care. Clinics, hotels and assistance companies that would like to work with international patients can apply to our [[business-partnerships|professional network]]."],
    ["ul", [
      "Ask for written aftercare instructions in your language.",
      "Agree who you contact, and by which channel, if something feels wrong.",
      "Plan a check-up with your own dentist after you return."]],
    ["h2", "What we need from you to start"],
    ["ul", [
      "Your country, preferred travel dates and how long you can stay.",
      "What treatment you are considering or what problem you want solved.",
      "Any X-rays, scans or treatment records you already have.",
      "Whether you travel alone or with companions.",
      "Your language for communication."]],
    ["note", "We are not a dental clinic and do not give medical advice. Diagnosis, treatment plans and prices are decided by the dentist. Please discuss any treatment with your own dentist or doctor as well."],
   ],
   "faqs": [
    ["Is dental treatment abroad safe?", "Safety depends on the clinic and the dentist, not on the country. That is why we help you check licensing, written quotes, materials, warranty and follow-up arrangements before you travel."],
    ["How many days should I plan to stay?", "It depends on the treatment. The clinic should give you a realistic schedule, and we advise adding spare days so that nothing is rushed."],
    ["Can you arrange hotel and transport?", "Yes. We arrange hotel, airport transfers and local transport, and can accompany you and interpret during visits."],
    ["What if I have a problem after returning home?", "We ask the clinic about warranty and follow-up before you decide, so that you know what to expect, and we help you contact the clinic if you need it."]
   ]
  },

  # ------------------------------------------------------------------ REAL ESTATE
  "real-estate-investment-albania": {
   "blocks": [
    ["h2", "Why checks before the advance payment matter"],
    ["p", "Property is usually the largest purchase a person or company makes, and in Albania the history of a property can be more complicated than the listing suggests. Decades of changes in ownership rules, informal construction, restitution and compensation claims and incomplete records mean that two apparently identical apartments can carry very different risks. Checks made before you pay cost very little compared with the problems they prevent."],
    ["h2", "The legal checks we organise with a partner lawyer"],
    ["ul", [
      "Ownership. That the seller is the registered owner and has the right to sell, and that the registered details match the property that is shown.",
      "Encumbrances. Mortgages, seizures, easements, lease rights and any claims or disputes registered against the property.",
      "Cadastral data. That the area, boundaries and registration of the property in the cadastre match reality.",
      "Construction legality. The building permit and, where relevant, the documents for use of the building. Properties with informal construction history need special attention.",
      "Land and ownership claims. For land in particular, whether there are competing claims from earlier processes.",
      "Who may buy. Rules for foreign buyers can differ by type of property, for example between buildings and agricultural land, and are verified before you commit."]],
    ["h2", "The technical inspection"],
    ["p", "A property can be legally perfect and technically poor. Our engineers inspect what a viewing does not show, and give you a report with approximate renovation costs, so that you can negotiate the price with real figures."],
    ["ul", [
      "Structure: cracks, settlement, damp and the condition of floors, roofs and facades.",
      "Electrical installation: panel, wiring, earthing and capacity for the intended use.",
      "Plumbing, heating, cooling and ventilation.",
      "Insulation, windows and likely energy costs.",
      "For commercial and industrial buildings: floor loads, access, utilities and suitability for the planned operation."]],
    ["h2", "Return analysis with visible assumptions"],
    ["p", "A purchase is also an investment decision. We build a simple model of the expected costs and income: the price, taxes and fees, renovation, furnishing if needed, and then rent, occupancy and operating costs. The assumptions are written down so that you can change them. We show the result under more than one scenario, and we do not promise a return. For larger or more complex projects the same analysis can be extended into a full [[business-plan|business plan]]."],
    ["h2", "Choosing by purpose"],
    ["ul", [
      "Own use. Location, access, services, building quality and the cost of running the property.",
      "Long-term rental. Demand in the area, rent levels, tenant profile and management effort.",
      "Tourism. Seasonality, regulations for short-term letting and operating cost.",
      "Development. Land use rules, permits, utilities, access and construction cost, where engineering input is essential."]],
    ["h2", "Costs beyond the price"],
    ["p", "The advertised price is rarely the full cost of owning a property. Budget for all of the following before you decide:"],
    ["ul", [
      "Transfer taxes, notary fees and registration costs.",
      "Legal checks and the technical inspection.",
      "Renovation, furnishing and any repairs the inspection finds.",
      "Property taxes and building maintenance charges.",
      "Management, insurance and vacancy periods if you plan to rent the property out."]],
    ["h2", "Buying through a company"],
    ["p", "Some investors buy through a company, for tax, liability or business reasons. That decision should be taken before the purchase, because moving a property into a company afterwards can add cost and complexity. If it is relevant to you, we can combine this service with [[company-formation-albania|company formation]]."],
    ["h2", "What we need from you to start"],
    ["ul", [
      "Your purpose: living, renting, tourism, development or business use.",
      "Your budget, including how much you plan to spend on renovation.",
      "Preferred cities or areas.",
      "Whether you will be in Albania for viewings or need help from abroad.",
      "Whether you intend to buy as an individual or through a company."]],
    ["h2", "The steps from viewing to signing"],
    ["ol", [
      "Define purpose and budget, then select and view properties.",
      "Request documents for the shortlisted properties.",
      "Complete legal checks and technical inspection before any payment.",
      "Negotiate the price using the findings.",
      "Agree the contract terms, with the lawyer, and sign in the form required by law.",
      "Complete the registration of the new owner and handover."]],
    ["note", "This service does not replace legal or financial advice. Property law and taxes change, and the decision to invest remains yours. We recommend that no advance payment is made until the legal checks are complete."],
   ],
   "faqs": [
    ["Can foreigners buy property in Albania?", "Rules depend on the type of property and the buyer. In particular, the position on land differs from the position on buildings. We verify the current rules with a lawyer before you pay anything."],
    ["Do you sell properties?", "No. We help you find, check and evaluate properties. We do not hold property to sell, which keeps our advice independent."],
    ["Do you guarantee a return on investment?", "No. We prepare an analysis with visible assumptions and several scenarios, not a promise of return."],
    ["Can you help me renovate after I buy?", "Yes. Our engineers can prepare the renovation specification, estimate costs and supervise the works."]
   ]
  },
 }
}
