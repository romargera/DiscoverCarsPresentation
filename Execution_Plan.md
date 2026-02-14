## Финальный план v10 — 16 слайдов

### Intro (слайды 1-2)
| # | Слайд | Содержание |
|---|---|---|
| 1 | Титульный слайд | Имя, позиция, дата |
| 2 | Agenda + Legend | Executive thesis — одно предложение-суть всей презентации. Навигация WHAT → WHY → HOW. Legend: как читать assumption markers в теле |

### WHAT (слайды 3-5)
| # | Слайд | Содержание |
|---|---|---|
| 3 | Customer Pain Points | Открываем с "Day in the Life" story — конкретный сценарий клиента (Maria в Malaga, pressured at desk). Затем insight framework: problem → frequency → severity → our solution fit. Сегментация: first-time renters vs experienced. Data: цитаты из Trustpilot/Google reviews, industry stats (Phocuswright/Statista), Reddit posts |
| 4 | Travel Protection Vision & Strategic Roadmap | Big picture: экосистема protection продуктов (3-4 направления), phasing на таймлайне, принципы sequencing, отметка "фокус презентации — Phase 1" |
| 5 | Chosen Concept: What, Why & Value Proposition | Что это, что покрывает, что получает клиент. Почему именно это первым (trade-off: почему не другие). Criteria выбора |

### WHY (слайды 6-9)
| # | Слайд | Содержание |
|---|---|---|
| 6 | Market Opportunity & Strategic Fit | TAM/SAM sizing с assumptions и ranges. Competitive landscape: конкретный gap analysis (RentalCover/Rentalcars/Booking — что делают, в чём слабы). Sincera advantage — почему in-house insurance company = unfair advantage: скорость итераций без external underwriter, data loop (claims → product → pricing), margin control. Cannibalization analysis — не отбираем ли revenue у suppliers at desk, как влияет на marketplace dynamics. Reference на текущий DiscoverCars booking flow |
| 7 | Customer Trust as Competitive Moat | Почему trust = higher attach rate + lower churn. Принципы прозрачности (plain language, no dark patterns, clear exclusions, instant claims). Дифференциация через trust vs конкуренты |
| 8 | Unit Economics & Commercial Viability | Сквозной numerical example: 1 booking → pricing → cost → margin. Cost structure (underwriting, claims, ops, tech). Scenario table: pessimistic / base / optimistic. Industry benchmark: excess insurance margins typically 50-70%. Sensitivity: что если attach rate ниже / claims выше. AI/ML пример: dynamic pricing based on destination risk, car category, booking lead time |
| 9 | WHY Summary: Stakeholder Value & Target Goals | Четыре блока — зачем каждому: Customer 🔵 (спокойствие → CSAT ≥4.2/5, complaint rate <2%), DiscoverCars 🟢 (revenue → attach rate 15-25%, revenue per booking +€5-10), Sincera 🟣 (portfolio → claims ratio <35%, margin 40-55%), Merchants 🟠 (меньше конфликтов → pickup complaint rate ↓30%) |

### HOW (слайды 10-15)
| # | Слайд | Содержание |
|---|---|---|
| 10 | Execution Roadmap, Timeline & Decision Gates | Overview фаз на таймлайне (Phase 0: weeks 1-4, Phase 1: weeks 5-14, Phase 2: weeks 15-28+). Decision points между фазами с criteria (go/pivot/kill). Learning loops встроены |
| 11 | Phase 0: Validation | Customer research (interviews, surveys), fake-door test на checkout, regulatory pre-assessment с Sincera, competitive teardown. 📊 Measure: fake-door CTR, willingness-to-pay, research signal strength. 🛡️ Guardrails: не обещаем что не можем deliver. 📝 Learn: реальный спрос, price sensitivity, regulatory blockers. Go/No-Go с thresholds |
| 12 | Phase 1: MVP Design, Build & Launch | Конкретный scope: список coverage items (tyres ✅, windscreen ✅, roof ✅, personal belongings ❌ — почему). Конкретный launch market с обоснованием (regulatory + volume). Checkout UX flow в 3-4 шага. Compliance requirements. Controlled rollout: 1-2 рынка. 📊 Measure: attach rate, conversion impact, claims frequency, CSAT. 🛡️ Guardrails: booking conversion не падает, complaint rate. 📝 Learn: реальная unit economics, claims patterns, UX friction, pricing elasticity |
| 13 | Phase 2: Initial Scale | Geo expansion (следующие рынки, regulatory readiness), pricing optimization (data-driven), channel expansion (email, in-app, post-booking), claims automation. 📊 Measure: attach rate по рынкам, revenue per booking, margin trend. 🛡️ Guardrails: claims ratio, CSAT, regulatory compliance. 📝 Learn: какие рынки лучше и почему, оптимальная цена, channel effectiveness |
| 14 | Dependencies & Risks | Pre-mortem framing: "It's 6 months later and this failed. Most likely reasons:" Риски по категориям: Regulatory (market-specific delays), Technical (integration complexity), Commercial (attach rate ниже, pricing pressure, cannibalization), Operational (claims capacity, fraud), Organizational (alignment Sincera vs DiscoverCars — разные incentives и risk appetite, влияние без formal authority, governance для конфликтов). Каждый риск: impact, probability, mitigation |
| 15 | Team & Partner Operating Model | RACI: DiscoverCars (distribution, UX, data) vs Sincera (underwriting, claims, regulatory). Cross-functional: engineering, design, legal, commercial. Governance: decision-making cadence, escalation path, joint review rituals |

### Wrap-up (слайд 16)
| # | Слайд | Содержание |
|---|---|---|
| 16 | Summary, Key Trade-offs & Assumptions | Recap ключевых решений и обоснований. Stakeholder value recap. Key Assumptions: сводка всех assumptions из презентации. What we don't know yet: явный список unknowns и подход к решениям при неполной информации |

---

## Development workflow

### Approach
- **Technology**: [Reveal.js](https://revealjs.com/) presentation framework
- Work **one slide at a time**: I draft slide content based on the plan → you review → you proactively request research if needed → finalize → move to next
- **Content first, design second**: all 16 slides get their content before we touch CSS/layout
- Presentation language: **English**. Working language between us: **Russian**

### Phase 0 — Project setup
| # | Step | What we do | Output |
|---|------|-----------|--------|
| 0.1 | Reveal.js setup | Initialize project: Reveal.js boilerplate, theme stub, basic slide scaffolding for 16 slides | Working `index.html` with empty slides |

> **Research on demand**: I draft each slide first using the plan description. You review and proactively ask me to do specific research (booking flow, competitors, reviews, market data, Sincera) when you see a slide needs it.

### Phase 1 — Slide content (one slide at a time)
Work through slides sequentially. For each slide:
1. I propose content structure/draft **or** you write your own text
2. We review and finalize the English text
3. Content goes into the presentation file
4. Move to next slide

| # | Slide | Depends on |
|---|-------|-----------|
| 1.1 | Slide 1 — Title | — |
| 1.2 | Slide 2 — Agenda + Legend | — |
| 1.3 | Slide 3 — Customer Pain Points | Research 0.1, 0.3— |
| 1.4 | Slide 4 — Travel Protection Vision & Strategic Roadmap | — |
| 1.5 | Slide 5 — Chosen Concept: What, Why & Value Prop | Research 0.1 |
| 1.6 | Slide 6 — Market Opportunity & Strategic Fit | Research 0.2, 0.4, 0.5 |
| 1.7 | Slide 7 — Customer Trust as Competitive Moat | — |
| 1.8 | Slide 8 — Unit Economics & Commercial Viability | Research 0.5 |
| 1.9 | Slide 9 — WHY Summary: Stakeholder Value & Target Goals | Slides 6-8 |
| 1.10 | Slide 10 — Execution Roadmap, Timeline & Decision Gates | — |
| 1.11 | Slide 11 — Phase 0: Validation | — |
| 1.12 | Slide 12 — Phase 1: MVP Design, Build & Launch | Research 0.1 |
| 1.13 | Slide 13 — Phase 2: Initial Scale | — |
| 1.14 | Slide 14 — Dependencies & Risks | — |
| 1.15 | Slide 15 — Team & Partner Operating Model | — |
| 1.16 | Slide 16 — Summary, Key Trade-offs & Assumptions | All slides |

### Phase 2 — Design & polish
| # | Step | What we do |
|---|------|-----------|
| 2.1 | Design system | Define color palette (stakeholder colors 🔵🟢🟣🟠), typography, layout grid, assumption marker style — all in CSS |
| 2.2 | Slide-by-slide styling | Apply design system to each slide, add icons/diagrams/visual elements |
| 2.3 | UX mockup | Create checkout page mockup for slides 5/12 |
| 2.4 | Competitive screenshots | Insert real screenshots with annotations for slide 6 |
| 2.5 | Responsive check | Verify everything fits within Reveal.js viewport (960×700, margin 15%) |

### Phase 3 — Final review (per checklist below)
| # | Step | What we do |
|---|------|-----------|
| 3.1 | Checklist pass | Go through every item in the checklist section below |
| 3.2 | Executive summary | Write STAR-format executive summary document |
| 3.3 | Read-through test | Open in browser, go slide by slide — does it tell a clear story without verbal explanation? |
| 3.4 | Export / share | Final file ready for submission |


## Чеклист (не забыть при выполнении)

### Визуал и дизайн
- [ ] UX mockup — схематичный скриншот checkout page с protection offer (слайд 5 или 12)
- [ ] Competitive teardown — скриншоты RentalCover/Rentalcars/Booking + их слабости + наш gap (слайд 6)
- [ ] Visual consistency — цвета по stakeholders через всю презентацию: Customer 🔵, DiscoverCars 🟢, Sincera 🟣, Merchants 🟠. Единый стиль assumption markers и trade-off boxes

### Research (до начала наполнения контентом)
- [ ] Реальные данные — Trustpilot/Google reviews цитаты, industry reports (Phocuswright/Statista), Reddit posts (слайд 3)
- [ ] Пройти реальный booking flow на DiscoverCars.com — сделать скриншоты текущего protection offer, заметить UX проблемы/возможности, reference конкретные элементы их UX в презентации (слайды 5, 6, 12)
- [ ] Изучить Sincera — что известно публично, как позиционируются, какие продукты уже есть (слайды 6, 8)

### Глубина контента при наполнении
- [ ] Customer insight synthesis — не просто цитаты, а insight framework: problem → frequency → severity → our solution fit. Сегментация: first-time renters vs experienced (слайд 3)
- [ ] MVP specificity — конкретный список coverage items (tyres ✅, windscreen ✅, personal belongings ❌ + почему), конкретный launch market с обоснованием, конкретный checkout UX flow в 3-4 шага (слайд 12)
- [ ] Financial model — сквозной numerical example: 1 booking → pricing → cost → margin. Scenario table: pessimistic / base / optimistic. Comparison с industry benchmarks (excess insurance margins typically 50-70%) (слайд 8)
- [ ] Sincera advantage — явно артикулировать почему in-house insurance company меняет всё: скорость итераций, data loop (claims → product → pricing), margin control vs external underwriter model (слайды 6, 8)