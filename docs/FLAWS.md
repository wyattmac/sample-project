# Where this whole thing is flawed

A red team of GIGAHOUSE / v7 / v6. The vision asked to attack the numbers. This is that attack. If a sentence in `VISION.md` cannot survive this file, the sentence is costume.

Engineering plan, still not financial advice. The flaws are worse than the advice disclaimer.

---

## 0. The one-line autopsy

This is a **multi-year, institutional-grade infrastructure program** pointed at a **retail account**, trying to harvest **crowded, low-Sharpe premia** and **quote residuals that are mostly garbage**, while paying **institutional data prices** and **one human's full-time attention**, then wrapping the remainder in **Bayesian theater that will not have statistical power this decade**.

The constitution is good. The metaphors are better than the economics. The factory is sized for a firm. The balance sheet is sized for a person.

---

## 1. You are not the house

This is the load-bearing lie.

The house in listed options is the market maker: Citadel, Susquehanna, IMC, Jane Street, Wolverine. They own the pipe for real — colocation, OPRA at the source, internalization, customer flow, inventory, board of a hundred names they are *obligated* to bid. They get paid the spread. You pay the spread.

GIGAHOUSE sits in a retail (or at best, small-prime) account and says "be the house." What it can actually do is:

- take the *other* side of some retail behavior (buy expensive lotteries, sell cheap insurance), **while still being adverse-selected by actual dealers**
- collect a bit of cash yield the broker was already mostly paying
- run defined-risk short-vol that every vol ETF, every "wheel" blog, and half of Twitter already runs

That is not a casino. That is a customer with a very expensive dashboard. The dealers see your orders. You do not see theirs. A 1-minute NBBO snapshot of a single-name wing is not a pricing engine. It is a postcard from a market that moved.

**Parity, boxes, calendar kinks, ETF-vs-constituent surface errors** — these are lunch. By the time a one-minute snapshot flags them, the size is one contract at a stub quote, or they are gone. Structure-factory "occasionally wonderful" is a true sentence about *someone*. It is almost never a true sentence about a retail fill at the mid.

**GEX / vanna / charm from open interest** is a cottage industry. OI is lagged, weakly signed, and not "dealer positioning." Treat it as a Twitter indicator with a scorecard, which the plan already says — then notice that a Sensor feed you do not trust is still 30% of the architecture diagram.

---

## 2. The Certainty factory does not pay for this machine

v7/v8's foundational claim: T-bill ladder + sweep + (later) box lending "pays the system's entire burn" at six-figure equity.

Do the arithmetic without the slogan.

**What Certainty actually captures.** At a competent broker (IBKR and peers), idle cash already sweeps to something near the policy rate minus a small rake. The gap versus `SGOV` / `BIL` / a T-bill ladder is often **tens of basis points, not hundreds**, and sometimes less than the bid-ask and tax lot pain of the ladder. You can do the honest version of Certainty in an afternoon: buy `SGOV`, turn on the broker's best sweep, stop. That is not a factory. It is a settings page.

**Box lending is not free money.** It needs portfolio margin (the plan says ≥ $110k — the real number moves, and PM approval is not a flag you flip), SPX/box permissions, assignment/exercise ops, and a rate that, after commissions and the box's own bid-ask, is often *close to T-bills*. You are not "becoming a lender." You are doing a more fragile T-bill.

**The burn is the data, not the compute.** B7 is the actual business model. Full-surface snapshots across SPX/XSP, index ETFs, ~200 names, ES/NQ FOPs, stored so the replay twin can settle tick-for-tick, refreshed every minute — that is not a retail data bill. Theta / Databento OPRA-class feeds are **hundreds to thousands of dollars a month** once you want history *and* live *and* enough depth that SSVI is not a fit to noise. Add a GPU box if you want, but the GPU is not the line item.

On a $100k account:

| Item | Rough yearly |
|---|---|
| Extra yield vs a decent sweep, 30–80 bps on *unencumbered* cash (not the whole $100k — options tie cash up) | **$150–$600** |
| Serious surface data + history for replay | **$3k–$30k+** |
| Commissions, fees, assignment mess | real |
| Operator time, even at a cheap internal rate | **dominates everything** |

Certainty does not pay the rent. Certainty pays for a money-market ETF. The Radar, the Foundry, and the replay twin are a **negative-carry research lab** subsidized by the operator's salary or savings. "Build order = certainty order" is honest sequencing. It is not a funding strategy. Calling T-bill yield "the only profitable-off-the-gate that exists" is true — and it is also an accounting trick: **you counted the risk-free rate as program P&L.** Of course P(positive) goes up if half the book is T-bills. That is not a trading system starting to earn. That is duration.

Until the account is large enough that data is a rounding error (high six / seven figures) *and* the operator's time is already committed, the unit economics of GIGAHOUSE are upside down. The plan's own blocker B7 says "coverage is a function of cash." It does not then delete the Sensor. It should.

---

## 3. The Sensor will mostly find garbage

SSVI-every-minute across the liquid universe sounds like owning the pipe. The input is the problem.

Retail (and most non-colo) option NBBO is **wide, stale, locked, crossed, and stubbed**, especially:

- far OTM (exactly where Convexity wants to hunt)
- far DTE
- single names outside the top 20
- the first minutes after a print or a halt
- anything you would call a "dislocation"

A fit of an arbitrage-free surface to that NBBO will light up **model residuals that are quote artifacts**. Distance-from-surface in fitted-vol units is not edge. It is "the wing quote is 0.05 / 0.25 and the interpolator is unhappy." Liquidity grade is supposed to filter this. After you filter, what remains is **liquid, and therefore closer to efficiently priced.** The Board's interesting rows and the Board's tradeable rows are different sets. The plan journals both as micro-hypotheses. The journal will fill with passed garbage and the scoring functions will learn the shape of bad quotes.

**You do not get the mid.** Edge estimates that assume a mid fill are fiction. The short-vol ticket that is +0.8 vol "cheap" versus your surface is often −0.5 vol after the ask, and worse if you are lifting a combo. Structure trades are "mostly execution-bound" — the plan says this and then still builds a factory around them. Execution-bound at retail size means **negative EV after friction**, not "occasionally wonderful."

**Tick-for-tick replay** has the same disease. Historical NBBO for options at this universe is the expensive half of B7, forever. Counterfactual fills ("we would have sold the mid, the shadow won") are how shadows get promoted. Twenty sessions of shadow dominance (the plan's number) is one expiration cycle of noise plus a fill model. That is not a tournament. That is a fitting exercise on your own assumptions.

---

## 4. The documented premia are real — and you are last in line

VRP and earnings-crush have papers. That is the opposite of a secret. It means:

- the premium has been harvested by vol funds, market makers, and every "sell 30–45 DTE iron condor at high IV rank" retail system since 2012
- crowding shows up as **worse entry, faster mean-reversion of IV rank, and a fatter left tail when the regime breaks**
- 2018 volmageddon, 2020, 2022, and whatever the next one is do not care that your ticket is defined-risk. Defined risk caps the *ticket*. The *book* still clusters: many condors lose in the same month, the factory hits H15, you go flat, and you spent the year collecting nickels for that privilege

The plan's own number is the tell: **P(positive over 3–5y) ≈ 50–70%.** That is a coin with a slight weight, path-dependent, with a left tail that is "structural" only per ticket. A personal operator who lives through the 30–50% failure window does not get a second 5-year sample. They get a ruined year and a system they now distrust. The plan says the biggest variable is obedience in the first cold quarter. Correct. The unstated corollary: **a 50–70% 5-year edge is not something a human with a day job and a Git repo will obey.**

Earnings crush: implied-vs-realized is taught in every options 201. The names where the ratio looks fattest are the names everyone is short. The agent veto ("guidance risk, M&A, litigation") is the same narrative layer every desk already uses. It is not a novelty. It is a blog post with an API.

**Defined risk is not "no short options."** An iron fly has short options. Early assignment, dividends, hard-to-borrow, and weekend gaps can make the long legs fail to offset the way the diagram promised. "No naked shorts ever" is a good constraint. It is not a complete ops model. The tuition you can compute in advance is the *thesis* tuition, not the assignment tuition.

---

## 5. The Bayesian foundry will starve

This is the intellectual center of v8 and it does not have the sample size it pretends to.

A personal book of defined-risk options produces **tens to low hundreds of settled tickets a year**, highly overlapping (same DTE cell, same regime, same index beta), fat-tailed, non-stationary. You want, simultaneously:

- a skeptical prior centered at zero
- P(edge > 0 | ledger) ≥ 95% to promote
- G1–G7 frequentist floor
- 0.25 × Kelly at the **25th percentile** of the posterior
- per-scanner, per-policy-head, per-Cortex-role posteriors
- veto alpha in dollars
- kill-by-date if the posterior has not cleared

Those constraints, taken seriously, imply: **almost nothing promotes, and almost everything that might have an edge is sized at noise.** That is philosophically admirable. It is also how you build a $20k/year research stack that trades `SGOV` and three condors.

Specific breaks:

- **Likelihood misspecification.** If the update assumes anything like i.i.d. trade returns, the posterior gets sharp and wrong. Options P&L is clustered, overlapping, and regime-switching. A "tight" posterior after a quiet year of VRP is the exact setup for the year that matters.
- **Kelly on a mis-estimated edge is how you blow up slowly.** The 25th-percentile haircut is a gesture at this. It does not fix a wrong model. Conservative Kelly of a fantasy edge is still a fantasy.
- **Veto alpha will not resolve.** One name, one quarter, one path. The counterfactual ("if we had not vetoed NVDA…") is not a statistic. You will not know if the Event veto is +EV this decade. Firing A2 on that number is firing a coin.
- **Multiple comparison.** Dozen scanners × 2–4 shadows × several policy heads = a foundry that is *designed* to discover luck. The Bayesian twin is the fix only if the likelihood and the dependence structure are honest. They will not be, not at this N.
- **20-session shadow promotion** contradicts the 95% skeptical posterior. One of these rules will be ignored. The ignored one will be the conservative one, because otherwise the tournament never moves. That is how constitutions die.

The foundry-is-the-product line is the most Elon sentence in the repo. It is also how you fall in love with the lab and never notice the lab is unfunded.

---

## 6. Complexity was not deleted. It was renamed.

v7 said the dominant risk is complexity, then added eight nodes. v8 said delete the org chart, then specified:

GPU SSVI, snapshot pipeline, scanner plugins, Board, crush calendar, veto ledger, NumPyro/PyMC posteriors, nightly tick replay, policy shadows, Czar re-weight, A-ladder API enforcement, adversarial gauntlet tests, vector memory, offline bandit router, local+frontier model split, cockpit UI, H22 line-count CI.

H22 caps `src/live/`. That pushes risk into **offline → config → canary → live**, which is exactly where a half-built system ships a bad DSL promotion at 3:55 p.m. The live path being "dumb" does not make the promotion path dumb. The promotion path is the product, and it is not small.

**One operator cannot run this.** Not as a weekend project. Not as a 12-week hardcore sprint. The hidden systems are: broker sync, margin, corporate actions, dividends, early exercise, expirations, rolls, PDT, tax lots, wash sales, clock drift, data outages, OPRA corrections, symbol changes, halted names, contract adjustments. Real prop firms have people whose *entire job* is that list. GIGAHOUSE assigns it to "N13 exec" and a fail-static slogan.

The Elon compression ("if it takes six months you designed it wrong") is motivational. It is also how you ship G0, start G1, discover B7 costs more than Certainty earns, and now you have a repo, a data bill, and no off switch for the identity you built around the factory.

Curiosity will violate build-order = certainty-order. The GPU fitter is more fun than `SGOV`. Everyone who writes a document like this already knows which node they will build first. It will not be G0.

---

## 7. The constitution cannot bind the person who can `git push`

Asymmetric autonomy is the right design for software. It is not a design for the owner.

You hold the Board token. You hold the repo. You hold the broker password. H14 "no re-up path exists in code" exists until the week Convexity is stopped out and you add a path. H22 exists until you raise the ceiling. The Czar is unappealable by agents. It is fully appealable by you. The plan admits the cold-quarter problem and then talks as if articles are compiler errors. **Compiler errors are for the LLM. You are the compiler.**

This is not cynical. It is the same reason diet apps do not make people thin. The machine for obedience is still a document plus a person who can edit the document. The only binding Czar is a separately controlled account you cannot refill, with a data bill you prepay, and a strategy so small that overriding it feels stupid. That system is called "buy `SGOV` and a boring vol allocation, and do not build GIGAHOUSE."

---

## 8. The honest math is still a vibe

Program P(positive at year 3) ≈ 55–70%, Sharpe 0.5–0.9. The plan says "judgment, wide bars, attack it." Attack:

- Those numbers are **not computed from anything**. They are a mood about T-bills plus crowded VRP plus "breadth."
- Adding Tier 0 mechanically lifts P(positive) by mixing in cash. Report excess return over the sweep you already had, or you are lying with the risk-free rate.
- Sharpe 0.5–0.9 **after fees, data, and burn** is optimistic for a retail-executed, defined-risk, short-vol-heavy book. Many real vol funds do not clear that after costs in the last decade. You have worse execution than they do.
- "Modestly above v6 because Tier 0 and Tier 2 breadth" — Tier 2's per-scanner P(real) is 20–40% and the tradeable subset is smaller. Breadth of *scanners* is not breadth of *independent bets*. One vol regime hits all of them.

The most honest sentence in the vision is still true: no version promises the market's money. The second most honest sentence should have been: **most versions of this, built by one person, will spend more than they capture and never get a clean read on whether the rest would have worked.**

---

## 9. What is *not* flawed

Say this plainly so the red team is not a tantrum.

- **No LLM in the live path.** Correct. Non-negotiable. Keep it.
- **Defined risk, kill switches at ticket/day/book/program.** Correct shape. Incomplete on assignment/ops, but the shape is right.
- **Synthetic evidence only demotes.** Correct. Do not let backtests promote.
- **Skeptical priors, two doors (frequentist ∧ Bayesian).** Correct instinct. It will starve the book. That is a feature until you quietly disable it.
- **Agents cannot add Board rows or raise scores.** Correct. The only safe LLM job here is annotation and veto, and even veto is statistically weak.
- **Naming complexity and obedience as the real risks.** Correct. This file is those two risks with numbers.
- **Do not pretend a personal account is Jane Street.** v8 deleted the seven-desk letterhead. It did not delete the seven-desk *workload*. Delete the workload next.

---

## 10. If you still want to build, build the small thing

The algorithm's step 2 was not finished.

A realistic personal system that keeps the doctrine and throws away the costume:

1. **Certainty in a day:** `SGOV` (or the broker's best cash vehicle) + margin-aware sweep. No box desk until PM is real and the rate after friction beats `SGOV` on a spreadsheet, not a manifesto.
2. **One Surface policy, not a fleet:** v6 CB-3 *or* crush, not both, not plus ICT, not plus geometry. Paper for a year or size so small that H15 cannot matter. If you cannot write the edge in one paragraph without "and also," you are collecting scanners.
3. **No whole-sky Sensor until B7 is a rounding error.** If data costs more than expected excess over `SGOV`, you do not have a Sensor. You have a hobby with a vendor.
4. **No foundry until you have N that can move a posterior.** Journal trades in a CSV. A NumPyro service over 40 overlapping condors is a shrine.
5. **No Convexity book until the above is boring.** 1% lotteries are how the interesting part of the brain stays in the project. That is the failure mode, not the feature.
6. **Measure excess over the cash you would have held anyway.** If that number is not clearly positive after data and fees, the factory is a consumer of your life, not a producer of edge.

That list is smaller than G0–G5. It is also the only version that does not require you to be a prop firm, a data vendor, and a Bayesian shop before you have a fill.

---

## 11. Closing, without the tattoo

v5 made the question cheap. v6 made the answer sound likely. v7 made the waiting sound profitable. v8 made the org chart sound deleted.

The market did not agree to any of that.

The flaws are not that the writing is unserious. The writing is too serious. It spent its seriousness on institutions, posteriors, and cockpits, and under-spent on **fills, data invoices, sample size, crowding, assignment, and the fact that the Czar is you.**

Be the customer who knows they are the customer. Own a boring cash vehicle. Do not own a pipe you cannot afford. Do not manufacture an edge the mid does not pay. Do not build a foundry for a sample that will not arrive.

If something in this file is wrong, it will be wrong in a journal of *fills and invoices*, not in a better metaphor.
