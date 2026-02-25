import re

notes_data = """
Slide 1 — Title (0:00 – 0:40)
[Hold title slide, make eye contact, then begin]
Good morning/afternoon.
My name is Roman Babunts, and I'm here to walk you through my solution to the take-home task — how I'd define, validate, and bring a new Travel Protection product to market at DiscoverCars.
The scope: one week of work. I'll cover the full loop — customer problem, commercial rationale, how I'd build and measure it, and where the real risks sit. Let's go.

Slide 2 — Agenda (0:40 – 1:30)
Three sections. WHAT — the problem and the chosen direction. WHY — the market opportunity and unit economics. HOW — execution, measurement, risks, compliance, and team alignment.
One note on data: you'll see the letter "A" throughout the deck — those are my assumptions. I'll always tell you the logic behind each one, and flag exactly which internal data points would sharpen or invalidate them. We can go deep on the math in Q&A.

Slide 3 — WHAT: Customer Pain Points (1:30 – 3:30)
I started from first principles — what does the customer actually suffer through when renting a car?
I did qualitative research across 62 data points — Reddit, TripAdvisor, travel blogs, competitor teardowns. All public signal; with your internal data this gets much stronger.
I mapped 14 pain points across the journey — pre-booking, pickup, and post-trip. Prioritized by LTV impact and Contribution Margin potential.
Decision: We focus on PRE-BOOKING.
Why: Tackling friction before purchase sets expectations correctly and prevents downstream disputes — highest CM potential.
The wedge: Look at Pain #4. A flight gets delayed. The rental desk closes. The customer is hit with a no-show fee, forced to rebook at double the price. Total loss: €350+ through no fault of theirs. That's our entry point.

Slide 4 — WHAT: Strategic Directions (3:30 – 5:00)
I evaluated 10 strategic directions against a scoring model: CM potential × inverse effort × confidence. Max score: 9.
Decision: We prioritize Trip Disruption Protection.
Why: It matches the highest commercial score with a massive competitive gap. Enterprise, Hertz, Avis — none offer explicit car-rental cost protection for flight disruptions. RentalCars covers flights and accommodation via Booking, but not the car rental cost itself. That's the gap.
Impact: A blue-ocean ancillary product that no direct competitor is solving today.
One honest note: Packaging & Monetization scored the same (7/9), but it's an optimization play. Trip Disruption is a new product with a higher ceiling. I'd want to validate the scoring against your internal booking mix and Sincera's underwriting capacity before committing.

Slide 5 — WHAT: Chosen Direction (5:00 – 6:30)
Let me make the problem concrete with a real scenario.
"You booked a car at Malaga Airport three weeks ago. Your flight is delayed six hours. You land at 23:40. The rental desk is closed. The car has been released. €120 no-show fee. Next car is twice the price. Your prepaid booking? Non-refundable. Total out-of-pocket: €350-plus — through no fault of yours."
[Pause]
This happens thousands of times a year. Every one of those customers is a DiscoverCars customer.
The Rule: If a flight delay forces a missed pickup, we reimburse the no-show fee or the non-refundable cancellation penalty.
Scope: Car rental costs only. Not flights, not hotels. This keeps the product clean, claimable, and compliant from day one.
Job To Be Done: "Protect my rental money when the airline messes up."

Slide 6 — WHY: Market Opportunity (6:30 – 8:30)
Let me walk you through the numbers — I'll show my logic so you can challenge any assumption.
TAM (Total Addressable Market): 113M fly-and-drive bookings globally × €7.50 average premium = €850M. The 113M filters ~270M global online rentals for airport/fly-and-drive (~60%) and target segment (~70%).
SAM (Serviceable Available Market): Cross-validated two ways — top-down ($28B travel insurance market → car-rental share → DC share) and bottom-up (unit economics). Both converge at ~€11.6M SAM.
SOM (Serviceable Obtainable Market) — what we can realistically capture:
* Year 1: €594K — 990K eligible × 10% attach × €6.00
* Year 2: €1.87M — 17% attach, pricing scales
* Year 3: €3.5–3.9M — 23% attach at €7.80
Assumptions to validate: Your actual airport vs. non-airport booking mix, and Sincera's baseline underwriting capacity for European markets.
Competitive gap: No current player offers explicit trip disruption coverage for car rental costs. That's a first-mover opportunity.

Slide 7 — WHY: Unit Economy (8:30 – 10:30)
Here's how a single policy breaks down.
Line	Amount
Price (Revenue)	€7.50
Risk Cost (45% loss ratio)	−€3.38
Ops & Tech	−€0.62
Net Margin	€3.50 (47%)
Why 45% loss ratio? It's the sweet spot for a parametric product — tight enough for healthy margin, generous enough to pay valid claims and build trust. The actual number comes from Sincera's actuarial model and real flight disruption frequency data.
Key efficiency driver: If the trigger is flight delay data (fully automatable), ops cost per claim goes down as volume goes up. That's the unit economics flywheel.
Assumptions to validate: We need Sincera's actuaries to model true volume of 4+ hour flight delays on top routes and confirm the 45% LR holds at scale.
I have a detailed scenario model — bear, base, bull — in the linked spreadsheet. Happy to walk through it in Q&A.

Slide 8 — WHY: Summary & Goals (10:30 – 12:00)
Here's the combined view for all stakeholders.
Why Trip Disruption first?
* High CM potential with low expected claims frequency
* Zero competitors offering this product explicitly
* 48h parametric payout drives retention — trust compounds
* Every claim = training point for dynamic pricing → margin improves YoY
Who benefits:
* Customer: No-show fee covered, rebooking difference covered, prepaid penalty reimbursed. CSAT target 4.2+; complaint rate under 2%.
* DiscoverCars: €250K CM Year 1 → €2.5M+ by Year 3. Attach rate 15% → 25%.
* Sincera: 45% loss ratio target, 15% ops cost ratio — sustainable underwriting.
* Rental Suppliers: Fewer no-show disputes, lower chargeback rate.

Slide 9 — HOW: Execution Roadmap (12:00 – 14:00)
Decision: We don't big-bang launch. We run a UK-only MVP, followed by a Canary A/B test.
Why: Insurance has an 8-week claims lag. You book today, travel next month, claim two weeks later. You don't know your true loss ratio on Day 1. We bake this data maturation phase into the timeline deliberately.
Impact: We don't scale to EU or US until the Phase 1 cohort proves unit economics hold. Patient scaling prevents expensive rollbacks.
Phase 0 (Weeks 1–4): PRD, concept validation, stakeholder alignment including Sincera kick-off, design mockups, regulatory checklist. Key output: go/no-go before a single line of production code.
Phase 1 (Weeks 5–8): Usability testing, MVP build (UK pilot), Sincera API integration, claims flow E2E test.
Canary (Weeks 9–10): Internal launch, live claims test, Go/No-Go decision.
Data Maturation (Weeks 11–18): The most underestimated phase in most PM plans. 8-week claim lag. We build this into the timeline deliberately, not as a buffer.
Full Rollout (Week 19+): 100% UK, then EU and US expansion, Dynamic Pricing V1.
The UK-first pilot is a deliberate constraint — single regulatory jurisdiction, English-language copy, known consumer behavior. Simplest possible learning environment.

Slide 10 — HOW: MVP Solution Draft (14:00 – 15:30)
The MVP is scoped extremely narrow.
Scope: UK residents, airport bookings, verified flight disruptions only.
Product tests: Two versions to A/B test — standalone "Trip Disruption" add-on, and a bundle inside "Full Coverage Plus". We want to learn if customers prefer dedicated coverage or a comprehensive package.
Ops model: Because flight delays are public data, we can verify triggers via API. This drastically reduces Sincera's manual claims review load and keeps ops costs flat as volume scales.
Coverage rules: Explicit trigger (flight delay ≥ 4h or cancellation), clear payout caps, required proof (flight status API + receipts). Exclusions shown before purchase, not buried in T&Cs.
Launch: Canary rollout → ramp to 100% UK after positive signals.
Learning gate: Wait for the 8-week claim cohort before scaling. I will not recommend scaling before we've validated the loss ratio in real conditions.

Slide 11 — HOW: Measurement & Learning (15:30 – 17:00)
North Star metrics: Two. New incremental revenue per booking, and Attach Rate.
Guardrails — six metrics that protect us from bad outcomes. Most critical: zero-harm to core booking conversion, and loss ratio target band 35–55%. If loss ratio exceeds 55%, we reprice or tighten triggers. Plus: Time-to-Pay (P50/P90), dispute/chargeback rate, complaint rate.
How we learn: A/B tests on copy, placement, pricing — short sprints. Qualitative: heatmaps, customer feedback, custdev. Claims analytics: cohort by booking→trip→claim, denial reasons, fraud flags.
Pivot signals: Pivot if attach rate stays below 5% after optimization, or support tickets exceed 2% of bookings. Persevere if contribution margin is positive and trending. The discipline: don't over-index on week-1 data. The meaningful cohort arrives at week 11.

Slide 12 — HOW: Risks & Mitigation (17:00 – 19:00)
Nine risks in the model. Two require immediate executive focus.
Risk #1 — Failed by Misalignment (Score 9/9).
This is a virtual cross-functional team: DC engineers, designers, legal, Sincera underwriters, claims ops. Misalignment is the top risk.
Mitigation: One virtual team, shared OKRs, unified dashboard. Sincera isn't a vendor — they're our internal capability. We move as one unit from sprint zero.
Risk #2 — Exclusions Destroying Trust (Score 9/9).
A customer files a claim, gets denied on a technicality they didn't know about, posts it everywhere. That's the insurance trust-killer.
Mitigation: Radical transparency. Exclusions rendered clearly pre-purchase. If a customer doesn't know what they're buying, an eventual denial will churn them forever.
Other risks flagged: regulatory delays (Sincera leads checklist from Phase 0, not week 8), claims ops scalability, anti-fraud maturity, and cannibalization of Full Coverage — tracked via Net Basket Value.

Slide 13 — HOW: Trust & Compliance (19:00 – 20:30)
Trust and compliance are not obstacles — they are the product.
Decision: Eliminate legalese. Automate payouts. Build compliance in from Day 0.
Why: Regulatory delays kill momentum. Grey products get fined. Compliant products create moats competitors cannot easily knock down.
Three dimensions:
Clarity over Confusion. Exclusions flagged before purchase, policy language at a set readability target. No jargon requiring a law degree.
Certainty over Anxiety. For verified flight delays — data-driven trigger — we target 48-hour parametric payout. Plus a real-time claim status tracker. That one feature alone reduces inbound support load materially.
Legitimacy over Exposure. Sincera is our built-in underwriting and compliance partner — not an external vendor. The regulatory checklist is a parallel workstream from Phase 0, not a legal review at the end. T&Cs auto-adapt to local law as we expand.
Trust is not a soft goal — it flows directly to Contribution Margin through higher retention, higher attach on repeat bookings, and lower chargeback rate.

Slide 14 — HOW: Team & Partner Alignment (20:30 – 22:00)
This requires horizontal leadership.
My role: I don't manage Sincera; I align them. It's about clarity and speed, without breaking compliance.
Team structure: Virtual team format. Joint squads including Sincera from day one. Dedicated channels per project and per functional area. Real-time unblocking is the design.
Legal/Finance sandbox: Pre-agreed guidelines for rapid copy and pricing iteration. Not every word change goes to a 3-week legal review. We agree on guardrails at the start, then iterate within them.
Rituals: Weekly syncs for cross-functional alignment, sprint planning for engineering, retros for improvement. Regular 1:1s with tech lead, designer, analytics, and Sincera counterpart.
One note on Sincera: they're not a vendor — they're our built-in insurance expertise. Underwriting, claims ops, regulatory licensing — that capability sits inside the group. The PM's job is to align incentives and create the conditions for them to operate at their best.

Slide 15 — Next Steps (22:00 – 23:00)
If we agree to proceed, four concrete next steps:
1. Team kick-off — align on goals, roles, working rhythm.
2. Phase 0 — 4-week validation sprint. PM + Designer, working with real users and stakeholders. Output: refined PRD and go/no-go recommendation.
3. Data sync — pull real airport booking mix and local flight delay frequencies to sharpen the business case.
4. Sincera sync — lock in regulatory checklist for UK, align on 45% loss ratio target and underwriting appetite.
"""

# Extract individual notes
raw_notes = notes_data.split("Slide ")[1:]
notes_list = []
for n in raw_notes:
    # Remove the first line (the slide title like "1 - Title ...")
    parts = n.split("\n", 1)
    # the actual content
    content = parts[1].strip()
    notes_list.append(content)

with open("slides.md", "r", encoding="utf-8") as f:
    slides_md = f.read()

# Separate by exactly "---"
parts = re.split(r'\n---\n', slides_md)

# First part has notes for Slide 1
# Second part has notes for Slide 2
# ... there are 15 parts, plus maybe a trailing empty one.
# Reconstruct with notes added.

for i in range(len(notes_list)):
    if i < len(parts):
        # check if notes already exist to avoid duplication
        if "Notes:" not in parts[i]:
            parts[i] = parts[i] + "\n\nNotes:\n" + notes_list[i] + "\n\n"

# Join back
new_slides = "\n---\n".join(parts)

with open("slides.md", "w", encoding="utf-8") as f:
    f.write(new_slides)

print("Notes injected successfully!")
