# v8 — GIGAHOUSE

**The vertically integrated probability factory.**

Supersedes v7 as program vision. v5/v6 machinery and gates remain normative. v7's constitution (H14–H18) is inherited, then tightened. Engineering plan, not financial advice. Tattoo it on the repo.

**Red team:** [FLAWS.md](FLAWS.md) — unit economics, quote garbage, sample size, crowding, and the house metaphor. If a sentence here dies there, the sentence is costume.

---

## 0. The Algorithm, Applied to v7

Elon's production algorithm, in order, never skipped, never reordered:

1. **Make the requirements less dumb.**
2. **Delete the part or process.**
3. **Simplify and optimize.**
4. **Accelerate cycle time.**
5. **Automate — last.**

v7 was a beautiful org chart of a prop firm. Org charts do not make money. Factories do. The requirement "seven specialist desks, each with an agent PM" was analogical thinking: *that is how a real prop firm looks, therefore we should look like one.* We are not a real prop firm. We are one operator, one GPU, one deterministic safety computer, and a market that misprices probability every minute of every session. The requirement is rewritten:

> Manufacture defined-risk tickets from mispriced probability, at a known maximum tuition, with a factory that improves itself every night, funded from the first day by rate capture on our own collateral.

Everything that does not serve that sentence is a candidate for deletion.

**What we deleted from v7, and why:**

| v7 part | Verdict | Why |
|---|---|---|
| Seven desks as first-class institutions | **Deleted as org chart** | Three physical machines. Policy heads are configs, not companies. |
| Conversational risk officer as a "UX flourish" | **Deleted as product; kept as a query** | Flourishes are how programs die. A journal-grounded SQL console is a tool, not a feature launch. |
| Agent "careers" | **Deleted the HR. Kept the ladder.** | Employment-at-will. Public firing log. No charisma. |
| 4.5–6 month "v7-complete" | **Deleted the government timeline** | If it takes six months you designed it wrong. First dollar in weeks, not quarters. |
| Satellite as a desk | **Deleted** | It is a policy family on the Surface factory. It competes in the tournament; it does not get a building. |
| Flow as a desk | **Deleted** | Dealer-positioning is a sensor feed. Sensors do not get P&L. They get scorecards. |
| "Personal terminal that reads like a morning meeting" | **Deleted the theater** | The cockpit shows one number that matters. Everything else is a drill-down. |

**What we did not delete — the bar did not come down:**

Deterministic live path. Interlocks own capital. Asymmetric autonomy. The bar climbs with the ledger. Synthetic evidence only demotes. No naked shorts ever. Defined risk always. H1–H18 inherited. Agents cannot add Radar rows or raise scores. No LLM bytes in `src/live/`. CI still greps.

Ambition went up. The bar did not come down. The org chart went in the trash.

**The doctrine, restated as physics:**

*Be the house. Own the pipe. Rent out certainty. Buy convexity only with house winnings. The foundry is the product; the trades are the cars.*

v7 said the critic is the product. That was half a step. The product is the **factory that produces critics, policies, and tickets** — and makes the next generation cheaper than the last. SpaceX's product is not the rocket. Tesla's product is not the car. GIGAHOUSE's product is not the trade.

---

## 1. First Principles — What This Actually Is

Strip the analogies. What is an option?

An option is a contract that transfers a slice of a probability distribution for a price. The listed market is a factory that stamps these contracts with a bid and an ask. Most of the stamps are fine. Some are wrong. A few are *structurally* wrong in ways that have been documented for decades (variance risk premium, earnings-crush overpricing, parity/box violations, term kinks). Retail, systematically, buys lottery tickets too expensive and sells insurance too cheap. That is not a moral claim. It is a base rate.

What is a house?

A house does not predict. A house **prices**. It owns the spread, the clock, and the budget. It never chases. It never re-ups a losing lottery. It is profitable in the boring way: a small edge, infinite time, a kill switch at every altitude, and a factory that fires anything whose posterior says it is not an edge.

What is "evil genius" when you write it down without the costume?

Not market manipulation. Not hidden losses. Not a persuasive agent talking its way past the wall. The uncomfortable honesty is this: **we are building a casino that sits inside the listed options market, admits it is a casino, and publishes the math.** The house edge is manufactured from four feedstocks, in certainty order:

0. **Rate.** Idle cash is a leak. We plug it. This is not alpha. This is refusing to be the broker's float.
1. **Documented premia.** VRP. Crush. The things that have papers, decades, and still a 30–50% chance of not working over any given 3–5 year window. We size them like adults.
2. **Surface dislocations.** The market's geometry errors, scanned exhaustively, bet small, fired individually.
3. **Mispriced lotteries.** Convexity we are *allowed* to buy only when our measured base rate beats their implied odds by a hard threshold — and only with last month's house winnings.

That is the entire business. Everything else is manufacturing.

**The reinterpretation clause, kept and sharpened:**

No system is profitable by declaration. BUILD ORDER = CERTAINTY ORDER = VERTICAL INTEGRATION ORDER. We do not rent a surface we cannot fit. We do not fit a surface we cannot scan. We do not scan what we cannot journal. We do not journal what we cannot size. We do not size what we cannot kill. The first module shipped is still the most certain earner. "Off the gate" is an engineering property of the stack, not a promise about alpha.

---

## 2. The Physics Stack — Three Factories, One Safety Computer

v7's org chart:

```
YOU → CZAR → CARRY VOL EVENT FLOW STRUCTURE SATELLITE LOTTERY
```

GIGAHOUSE's physics:

```
                         YOU — the Board
                          (one number · /approve · veto)
                                   │
                    CZAR  ───  the safety computer
                 triple-redundant · no neural net · unappealable
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
         CERTAINTY            SURFACE              CONVEXITY
         factory              factory               factory
         (Boring Co.)         (the car)            (Starship)
              │                    │                    │
              └──────────── CORTEX (offline) ───────────┘
                         one brain · many policy heads
                                   │
                    SENSOR  ───  whole-sky surface coverage
                         (Starlink for the vol surface)
                                   │
        FOUNDRY ── Bayesian ledger · shadow tournament · replay twin
                   the gigafactory that makes the next generation
```

A **factory** is not a desk. A factory is a machine with:

- a feedstock (cash, surface quotes, convex contracts)
- a bill of materials (legal structures, max Greeks, DD budget)
- a quality gate (wall + interlocks + Bayesian twin)
- a kill switch (ticket → day → factory → tier → program)
- a cost per unit (compute, fees, slippage, max loss)
- a posterior over whether the machine has edge

Policy heads (VRP core, crush, calendars, ICT habitats, tail hedges) are **configs on a factory**, not institutions. They compete in the tournament. They do not get letterhead.

Underneath, nothing new to trust: every policy head is a v5/v6 (family × instrument × session) book cluster on the same interlock ladder. The live path is the actuator. Cortex thinks in minutes and hours, offline. The actuator trades on bar closes and Sensor triggers with **zero LLM calls**. Proposals become live behavior only through the gauntlet: deterministic pricing → wall → farm gates → canary.

**The Czar is Autopilot hardware.** At Tesla the neural net does not get the last word on the actuators. If the safety computer is down, the car does not drive. If the Czar is down, the house does not trade. Fail-static. An agent — including a retroactively eloquent one — cannot override it. This is not a metaphor. This is the process boundary.

**The Board is you.** Unchanged asymmetric autonomy: every capital increase needs your token; every decrease already happened by the time you read about it. The cockpit shows **one number** — program certainty-adjusted edge, in dollars per week, with the posterior band. Everything else is a drill-down. A SaaS dashboard is how you hide from the number.

---

## 3. Vertical Integration — Own the Pipe

A retail options stack is a layer cake of other people's factories: broker sweep, vendor surface, vendor greeks, vendor scanner, vendor fills, vendor P&L. Each layer takes a rake. Each layer's error is your "edge." This is insane. We vertically integrate from photons to settlement.

| Layer | Name | What we own | What we refuse to rent as gospel |
|---|---|---|---|
| L0 | **Photons** | NBBO / OPRA snapshot ingest, quote-quality ledger | Vendor "fair vol" we cannot reproduce |
| L1 | **Geometry** | GPU-fit arb-free SSVI per expiry, our residuals | Black-box greeks, vendor IV |
| L2 | **Sensor** | Scanner fleet as scored plugins; Best Options Board | "Unusual options activity" theater |
| L3 | **Foundry** | Posteriors, shadows, nightly (then continuous) replay | Equity-curve storytelling |
| L4 | **Factories** | Certainty / Surface / Convexity — mandates as code | Desk mythology |
| L5 | **Actuators** | Deterministic executor, combo router, fill-quality ledger | Smart-routing we cannot replay |
| L6 | **Board** | You, tokens, the one number | A committee |

**Blockers, restated as integration gates:**

- **B7 — Photons.** Options-surface data tier sized for the scan universe (Theta full-surface or Databento OPRA subset) is priced *before* L1 is built. We do not fit a surface we cannot own. If the data is too expensive for the account size, the Sensor universe shrinks until the unit economics work. Coverage is a function of cash, not ambition.
- **B8 — Balance-sheet unlock.** Portfolio margin for box lending (≥ $110k). Below that, Certainty factory is T-bills-only. We do not pretend we have a lending desk when we have a sweep problem.

A consumer GPU is overkill for L1. Good. Overkill is the correct amount of factory for a one-operator house. When surface-fit latency is the bottleneck we write the CUDA kernel. Not before. Automate last.

**Compute is a first-class risk (H19).** If the Sensor is stale past its SLA, the Board is a lie and the actuators freeze. A stale surface is not "degraded mode." It is a dead man. Fail-static.

---

## 4. The Day-One Stack — The Factory Pays Rent Before It Speculates

Four tiers. Same honesty as v7. Tighter manufacturing language.

**Tier 0 — Certainty factory (the Boring Company).**
Idle cash is a leak in every retail account. The factory automates: T-bill ETF laddering of unencumbered cash from day one; SPX box-spread lending (buying boxes = lending at the implied rate) once portfolio margin unlocks; sweep optimization around margin so Surface and Convexity never force-liquidate the ladder. Effectively zero directional risk. Its "edge posterior" is a rate, not a hypothesis.

*Honest number:* tens of basis points to low hundreds on cash versus broker sweep drag. At six-figure equity this approximately **pays the system's entire burn**. Below that it offsets it. This is the only "profitable off the gate" that exists. It ships first. The tunnels fund Mars.

**Tier 1 — Surface factory, documented premia.**
v6 CB-3 VRP machinery (defined-risk short vol at high IV rank, 30–45 DTE, managed) plus the earnings-crush program (whole calendar → implied vs historical realized → top-decile iron flies/condors → Cortex veto layer). Priors: the strongest publicly documented options edges. P(positive over 3–5y) ≈ 50–70%. Live within the first two months. The left tail is structural (defined risk) and behavioral (H15).

**Tier 2 — Surface factory, geometry errors.**
Scanner-detected anomalies, positioning-driven windows (Sensor feed, not a desk), term/skew dislocations — each ticket defined-risk, each mechanism-tagged, each a micro-hypothesis in the ledger. Prior modest per ticket. Breadth is the product. Hundreds of small, independent, gated bets. Each scanner is cheaply testable and individually firable.

**Tier 3 — Convexity factory (Starship).**
Hard-budgeted, edge-gated, expected to lose most months. Exists because a program that harvests premium and never owns tails is short the exact tail that ends programs. 1% of risk that makes the other 99% a civilization instead of a yield farm. It will explode on the pad. That is in the budget. See §6.

**The funding rule (H14 family / H17):** Tier N's monthly risk budget replenishes only from program equity above high-water. A losing month shrinks speculative tiers first, automatically. Certainty is the lung. No path exists in code to refill Convexity from a losing Surface month. Chasing is a compile error.

---

## 5. The Sensor — Whole-Sky Coverage of the Surface

The centerpiece is not a "screen." It is a **sensor suite**. Continuously refreshed. Ranked. The Best Options Board is the rendering — the top N defined-risk structures across the scanned universe *right now*. Each row:

- the structure
- the mechanism tag (WHY it scores — a physical claim, not a vibe)
- the edge estimate **with a confidence interval**
- liquidity grade
- capital required
- worst-case loss (always known, always first)
- which factory / policy head claims it

**Deterministic core, Cortex shell — Autopilot architecture:**

- **Geometry engine:** 1-minute NBBO snapshots across the liquid universe (SPX/XSP, index ETFs, top ~200 liquid single names, ES/NQ FOPs); GPU-fit arb-free SSVI per expiry; every quote scored against its own surface, its history, and its peers. Dislocation = distance from own surface in fitted-vol units.
- **Scanner fleet (deterministic, exhaustive, fast):** IV-rank extremes · skew vs own history · term kinks and calendar mispricings · earnings implied-move vs historical realized-move across the whole calendar · put-call parity and box violations (mostly an execution-quality map, occasionally a gift) · dealer-positioning maps (GEX/vanna/charm estimates from OI + volume attribution) as *features*, not oracles · ex-dividend traps and early-exercise value, scored, not stumbled into.
- **Cortex shell (offline, minutes-scale):** annotates what deterministic code cannot — *is this IV spike explained?* (M&A, FDA, litigation, guidance). Attaches a catalyst dossier. **Cortex cannot add rows or raise scores. It can only annotate and veto.** An unexplained-vol flag is information. An explained one is a warning.
- **Every Board row is a journaled micro-hypothesis.** Taken or passed, the counterfactual settles. The Sensor's scoring functions are themselves on the interlock ladder. The scanner is not trusted. It is *scored*. A scanner whose posterior dies is fired. No sacred scanners.

This is "agents find the best options," built the only way it survives contact with reality: deterministic breadth for the finding, Cortex for the context, the ledger for the truth. The neural net does not get to invent a trade. Obviously.

Dealer-positioning maps live here, as Sensor feeds, not as a Flow "desk." Pinning, charm/vanna windows, 0DTE gamma-regime classification — they time other factories. They do not get their own letterhead or their own drawdown budget to defend in a meeting that should not exist.

---

## 6. Starship — The Calculated Gambler, With a Hard Deck

The Convexity factory is the side of calculated gambler, formalized so it stays calculated. Starship will explode. The budget is the point.

- **The budget is the doctrine.** Convexity risk ≤ 1% of equity per month, hard-coded (H14). Spent is spent. **No re-up after losses, ever.** Replenishes only on the calendar and only from equity above high-water. The single most reliable way gamblers die is chasing. H14 makes chasing a compile error.
- **Only convex structures.** Cheap OTM butterflies into measured-move targets, backspreads into expansion regimes, tail hedges that double as crash lottery, long premium into unexplained-vol-*absence* flags from the Sensor. Max loss = ticket cost. Always known. Always journaled first.
- **Edge-gated lotteries only.** Legal only when estimated probability beats market-implied probability by a threshold (default: our p ≥ 1.5× implied p, from measured base rates — historical frequency of moves that size in that regime). You are allowed to gamble. You are not allowed to gamble at *their* odds.
- **Fractional Kelly on the conservative quantile.** Stake = 0.25 × Kelly at the 25th percentile of the posterior edge estimate. Uncertainty about your own edge is the house's biggest hidden rake. This is the anti-rake.
- **Every ticket carries a written thesis** (Cortex-drafted, one paragraph, falsifiable) and settles into the Bayesian ledger. The factory's posterior is public in every packet. If the gambler is negative-EV after 100 tickets at honest-odds accounting, the factory demotes itself. Starship that cannot reach orbit is scrap.
- **Why it exists:** a yield farm that never owns convexity is short the civilization-ending tail. 1% of risk. Receipt attached.

---

## 7. The Foundry — The Machine That Makes the Machine

This is the part v7 under-named. The Bayesian ledger, the shadow tournament, and the replay twin are not "services." They are the **gigafactory**. The trades are the cars. If the foundry is not compounding, the program is a strategy with extra steps.

**Bayesian ledger.** Every factory, every scanner scoring function, every Cortex role carries a live posterior over its true edge — updated on every settled trade and counterfactual, starting from deliberately skeptical priors (centered near zero, wide). Everything that touches capital reads the posterior, not the point estimate:

- **Sizing** = fractional Kelly on the posterior's 25th percentile (factories) / edge-gate checks (lotteries).
- **Tournament weights** derive from posterior quantiles. A lucky streak with wide uncertainty earns less capital than a modest record with tight uncertainty. Luck is visible as variance. The tournament pays for *evidence*.
- **Gates gain a Bayesian twin.** G1–G7 remain the frequentist floor. Promotion also requires P(edge > 0 | ledger) ≥ 95% under the skeptical prior. Two philosophies must both say yes. This is how you keep a lucky intern off the line.

**Shadow tournament.** Every policy head runs 2–4 shadow variants — same mandate, perturbed policies (DTE cells, veto thresholds, Sensor score weights) — live on real data, paper-settled by the replay twin. Capital follows survivors. Each week the Czar re-weights factories by posterior quantile; inside each factory the champion policy defends its seat. A shadow that dominates for 20 sessions with a superior posterior becomes the canary candidate through the normal gates. The farm searched history. The tournament searches *the present, in parallel*. Nothing touches live orders except through the same promotion door as ever.

**Replay twin.** Every night the day replays tick-for-tick. Every factory's counterfactuals, every Board row taken or passed, every veto — settled and scored. The weekly packet's coldest table stays: *cost of discipline vs value of discipline*, in dollars, from the roads not taken. Cycle time on the foundry is the cycle time of the program. Accelerate this before you automate anything else.

**Vector memory, correctly placed.** Every trade, dossier, and post-mortem embedded and retrievable so Cortex cites precedent ("the last 7 times we shorted crush into a guidance-risk flag…") instead of vibing. Retrieval feeds Cortex. **Never the actuator.** An embedding is not a reason to send an order.

**Execution intelligence, offline-learned.** Ladder timing and combo-routing as a bandit over discrete policy tables, learned offline from the fill-quality ledger, deployed as deterministic config. The live path stays dumb and fast. A smart actuator is a bug.

---

## 8. Cortex — One Brain, Employment-at-Will

v5 gave agents scorecards. v7 gave them careers. GIGAHOUSE gives them **employment-at-will and a public firing log.**

One Cortex. Many policy heads. Not seven PMs with offices. The A-ladder is runtime state, enforced at the API layer (H18), identical in spirit to capital interlocks:

- **A0 ANALYST:** may annotate (dossiers, notes). Cannot affect any decision.
- **A1 ADVISOR:** annotations enter deterministic scoring as features with a capped weight — the cap set by the measured value of its past annotations.
- **A2 VETO:** may strike tickets (crush program model). Every veto counterfactual-settled; veto alpha published per role per packet. **The veto itself is a tracked position.** An agent whose vetoes cost money loses the veto automatically.
- **A3 PM:** may propose tickets and DSL promotions for its factory — through the full gauntlet, sized by the factory's posterior, never directly to the actuator.

Promotion/demotion = skeptical posterior on that role's decision value. Conservative quantile above zero to climb, below zero to fall. No agent charisma survives its own ledger. There is no performance-improvement plan. There is a number.

**The Event-desk novelty, kept and generalized:** every veto's counterfactual settles. The ledger knows each role's veto alpha in dollars. This is now true of *every* A2 seat, not just crush.

**Model ops, 2026-shaped, commodity-honest:**

- Frontier models for weekly deep work (research digests, dossiers, post-mortems).
- Fast local/open-weight models for the high-frequency shell (Board annotations, notes) where cost and latency matter and stakes are capped by the A-ladder.
- Every output schema-validated.
- The metrology layer A/B tests *models per role per A-level*. The cheapest model that preserves the role's measured value wins the seat.
- The harness is the product. The models are commodities with employment contracts and a firing log.

**Zero LLM bytes in `src/live/`.** CI greps. Property-tested. Adversarial fixtures where a 'persuasive' agent output attempts every known shortcut past the gauntlet (H18). If a shortcut exists, that is a Sev-0, not a code-review comment.

**The query console (not a flourish):** you ask questions in plain language — *"why did Surface pass on NVDA?", "who's been paying for Geometry wins?", "show me Convexity's honest odds"* — and Cortex answers **grounded exclusively in journal queries, with the SQL attached.** It can explain everything and touch nothing. If it cannot attach the SQL, it does not speak. That is the entire UX.

---

## 9. Risk Wall v8 — the Czar's Constitution

Inherited absolute: H1–H13, interlocks per book, asymmetric autonomy (H12 tokens), sweeps, falsification budgets, equity governor, fail-static, dead-men. Inherited from v7: H14–H18.

**H14 — Convexity cap.** ≤ 1% equity/month, calendar-replenished, above-high-water funded only; no intra-month re-up path exists in code.

**H15 — Factory drawdown budgets.** Each factory carries a hard DD budget (default 3% of program equity, Certainty exempt); breach → factory flat + demoted one interlock level + packet inquest.

**H16 — Concentration.** No factory above 35% of program risk (Certainty exempt); no single underlying above 20% across all factories combined; portfolio Greeks (H5) net across factories with the Czar as sole netting authority.

**H17 — Tier funding order.** Speculative-tier budgets shrink first and automatically in drawdown.

**H18 — Cortex authority bounds.** A-ladder state enforced at the API layer. No Cortex output reaches the actuator by any path that skips the gauntlet — property-tested, adversarial fixtures included.

**New articles — the GIGAHOUSE tightening:**

**H19 — Sensor stale is dead.** If surface-fit or Board age exceeds the SLA (default: 3× snapshot interval), actuators freeze. A stale Sensor is not degraded mode. Fail-static. Compute is a risk input, not an infra footnote.

**H20 — Kill-by-date.** Every scanner, every policy head, every Cortex role, every model seat carries an expiry. If the skeptical posterior has not cleared its promotion threshold by N settled decisions (configured per class), it is fired automatically. No evergreen hypotheses. No legacy scanners "we should look at." The foundry does not run a museum.

**H21 — Single throat to choke.** One Czar process. One journal. One posterior service. One actuator. Dual-writes and "temporary" side channels are Sev-0. If you cannot point to the process that said no, you do not have a Czar.

**H22 — Complexity budget.** `src/live/` has a hard line-count and dependency ceiling, enforced in CI. New live behavior must delete more than it adds, or it does not merge. The dominant risk of v7 was complexity. The mitigation is not a process document. It is a compiler error.

**H23 — No part that does not earn.** A factory, scanner, or role whose conservative posterior is below zero after its kill-by-date does not get a stay of execution because the story is good. Stories are cheap. Posteriors are not.

**Kill-criteria at every altitude:** ticket (defined risk) → day (H2) → factory (H15) → tier (H17) → program (falsification budget). The maximum tuition of every layer — including Starship — is computable in advance. That is the entire difference between a casino patron and a casino owner.

---

## 10. Honest Math — Attack These Numbers

Same standard as v6 §9 / v7 §10. Judgment. Wide bars. Attack it. The attack is [FLAWS.md](FLAWS.md). The short version: these bars were not computed; Tier 0 lifts P(positive) by mixing in cash; report excess over the sweep you already had.

- **Tier 0 (Certainty):** P(positive) ≈ **95%+** — rate capture, not alpha. Magnitude: tens of bps to ~1.5% on cash vs sweep drag. Covers the burn near six-figure equity. Real. Small. The correct foundation stone. The tunnels.
- **Tier 1 (VRP + crush):** P(positive over 3–5y) ≈ **50–70%**. Earnings-crush adds breadth at similar prior. Left tail: defined risk + H15.
- **Tier 2 (geometry):** per-scanner P(real) modest — **20–40%** each — a dozen mechanism-tagged scanners, each firable, is a portfolio of small honest bets on market imperfection. Incremental. Lumpy. Occasionally delightful.
- **Tier 3 (Starship):** expected P&L ≈ breakeven-to-negative in most years *by design*, positive in tail years. EV case is portfolio convexity plus the edge-gate. Honest-odds ledger negative at N=100 → demote.
- **Program:** P(positive at year 3, after fees and burn) ≈ **55–70%**. Modestly above v6, driven by Tier 0's floor and Tier 2's breadth — *if* we actually delete the complexity that v7 added. Realistic good outcome: program Sharpe **0.5–0.9**. Great outcome adds a surviving policy head and a caught tail. Still not a lottery ticket. GIGAHOUSE bought **vertical integration and a factory**, not a higher ceiling on any single bet.

**The new dominant risk is still complexity — so we made it a kill criterion (H22), not a paragraph.** v7 had more ways to be half-built than any prior version. GIGAHOUSE has fewer parts. The Carry factory ships while the Sensor is still a prototype. Nothing waits for everything. That clause is now physical: three factories, one sensor, one foundry, one safety computer.

Unchanged, the final word: the biggest variable at year 3 is still whether the operator obeyed the Czar through the first cold quarter. Every version of this program is a machine for making that obedience structural. GIGAHOUSE puts obedience on a payroll, deletes the org chart that was going to negotiate with it, and makes the foundry the thing you fall in love with — so you do not fall in love with a trade.

---

## 11. Build Path — Delete the Government Timeline

v5's 22-node graph + v6 deltas remain the skeleton. v7's N26–N33 are **re-cut into six foundry nodes**, sequenced by certainty × integration. Durations are what a hardcore pass looks like if the requirements were made less dumb. They are not promises. They are the deleted-timeline versions of v7's estimates.

| Node | What | Needs | Why this order |
|---|---|---|---|
| **G0 Certainty Factory** | T-bill ladder, sweep logic, box-lending behind a PM flag | N11 wall, N13 exec | Ships first. Earns first. Funds everything. |
| **G1 Photons + Geometry** | Snapshot pipeline, SSVI fits, dislocation scores, surface store | N9, B7 priced | Own the pipe before you scan it. |
| **G2 Sensor + Board** | Scanners as scored plugins on their own mini-ladder; Board as cockpit rendering | G1 | Finding, journaled. |
| **G3 Crush + Veto Ledger** | Earnings calendar, implied-vs-realized, defined-risk crush, veto-as-position | G2, N19 | First Surface policy head with a tracked Cortex veto. |
| **G4 Foundry** | Posterior service, skeptical priors, Kelly hooks, Bayesian gate twin, shadows, replay v2, Czar re-weight | N16, N17 | The machine that makes the machine. |
| **G5 Cortex + Starship** | A-ladder enforcement (H18), factory mandates, query console, H14 plumbing, edge-gate, thesis ledger | G4, N19, N20 | Automate last. Gamble last. Both gated by the foundry. |

**Sequencing on a compressed clock:**

- G0 lands with the v6 core book — the gate pays from the first live month.
- G1/G2 as soon as B7 is priced and the wall exists. Sensor without photons is a toy.
- G3 next — crush is the first Surface line that uses Cortex for something real (veto-as-position).
- G4 before any serious capital rotation. Do not tournament on vibes.
- G5 last. Agents and lotteries are the automation step. Last.

**v7-complete was 4.5–6 months from bare ground. GIGAHOUSE-complete is "the foundry is compounding and Certainty is paying rent."** That is a state, not a date. Something real is earned in every month after the second, which is the whole point of the doctrine. If a node is slipping, delete scope, do not slip the Certainty factory.

**Policy heads that v7 called desks, and where they live now:**

| v7 desk | GIGAHOUSE home | Notes |
|---|---|---|
| CARRY | Certainty factory | Unchanged mandate. The Boring Company. |
| VOL | Surface factory / VRP head | CB-3 verbatim + Radar-fed extensions. |
| EVENT | Surface factory / crush head | Veto-as-position stays. FOMC/CPI from v6 event shelf. |
| FLOW | Sensor feed | Not a factory. Score the feed. |
| STRUCTURE | Surface factory / geometry head | Parity, boxes, calendars, early-exercise, ETF-vs-constituent. |
| SATELLITE | Surface factory / habitat head | Entire v5/v6 alpha factory, competing for capital, no building. |
| LOTTERY | Convexity factory | H14. Starship. |

**Next artifacts, when requested — campaign-grade, not theater:**

- G0–G5 campaign prompts in the P-kit format
- Board schema + scanner scoring specs (mechanism tags as physical claims)
- Veto-counterfactual settlement spec (generalized to every A2 seat)
- A-ladder promotion math + firing-log schema
- Lottery edge-gate base-rate tables
- H22 complexity-budget CI spec
- Photons unit-economics worksheet (B7: coverage as a function of cash)

---

## 12. Technology — Each Piece Earns Its Seat, or It Is Scrap

- **Geometry:** GPU-fit SSVI per expiry across the universe each minute; arb-free interpolation; dislocation in fitted-vol units. CUDA when — and only when — fit latency is the bottleneck.
- **Sensor feeds:** GEX/vanna/charm estimates from OI + volume attribution. Estimates, not gospel. Scored like every scanner. Fired like every scanner.
- **Foundry math:** NumPyro/PyMC posterior service over the ledger; nightly refits; posteriors journaled so every sizing decision is replayable. If you cannot replay the size, you did not size. You guessed.
- **Replay twin:** full-day deterministic replay with policy shadows — the tournament's arena. Cycle time is the metric.
- **Vector memory:** Cortex-only. Never the actuator.
- **Execution intelligence:** offline-learned, deployed as config. Live path dumb.
- **Local + frontier split** per §8; schema-validated everything; zero LLM bytes in `src/live/`.
- **The cockpit:** one number, the Board as drill-down, factory pages with posteriors and shadow standings, Convexity with written theses, the packet, the SQL-attached query console. A personal factory floor. Not a morning-meeting cosplay.

Everything above obeys the founding thesis, updated one last time:

**The LLM is a commodity. The critic is a department. The foundry is the product.**

---

## 13. Closing

v5 made the question cheap. v6 made the answer likely. v7 made the waiting profitable and then almost drowned it in desks. GIGAHOUSE applies the algorithm: the requirements were too analogical, the parts were too many, the timeline was a government, the automation was early.

What no version will ever do is promise the market's money.

They only promise that every dollar it does pay was won at honest odds, on the record, by a machine that obeys you better than you obey yourself — and that the machine which *makes* that machine gets better every night, whether you are watching or not.

Be the house. Own the pipe. Delete the org chart. Manufacture the edge.

The tunnels fund Mars.
