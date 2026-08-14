# The Algorithm

The production algorithm, in order, never skipped, never reordered. This is the operating system of GIGAHOUSE. If a design decision cannot point to which step it is on, it is analogical thinking and it is probably wrong.

## 1. Make the requirements less dumb

The requirement is usually the problem.

| Dumb requirement (v7, analogical) | Less-dumb requirement (physics) |
|---|---|
| Seven specialist desks like a real prop firm | Three factories. Policy heads are configs. |
| Agent PMs with careers | Employment-at-will. Public firing log. A-ladder as runtime state. |
| A terminal that feels like a morning meeting | One number. Everything else is a drill-down. |
| "v7-complete in 4.5–6 months" | Foundry compounding + Certainty paying rent. A state, not a date. |
| Agents find the best options | Deterministic Sensor finds. Cortex annotates and vetoes. Ledger scores. |
| Flow desk | Sensor feed. Feeds do not get P&L. |
| Satellite desk | Policy family on Surface. Competes. No building. |

**Test:** if we had never seen a prop firm's org chart, would we still build this part?

## 2. Delete the part or process

The best part is no part. The best process is no process.

Delete candidates (default yes):

- Any live-path branch that exists "for the agent"
- Any second journal, second Czar, or "temporary" side channel (H21)
- Any scanner that cannot name its mechanism as a physical claim
- Any UI that does not change a decision
- Any meeting that is not the weekly packet
- Any evergreen hypothesis (H20)
- Any live feature that does not delete more lines than it adds (H22)

If you are not deleting, you are not on step 2. You are decorating.

## 3. Simplify and optimize

Only after deletion.

- One Cortex, not seven brains
- One posterior service, one actuator, one Sensor SLA
- Sizing is one function: fractional Kelly on the conservative quantile
- Promotion is one door: frequentist floor ∧ Bayesian twin ∧ canary
- The Board is a rendering of the Sensor, not a product surface

Optimization without deletion is how you get a faster org chart.

## 4. Accelerate cycle time

The foundry's cycle time *is* the program's cycle time.

- Nightly replay is the minimum. Continuous shadow settlement is the target.
- A policy head that cannot be shadowed cannot be trusted — not because it is evil, because it is slow to falsify.
- Packet weekly. Firing continuous. Capital re-weight weekly. Sensor every minute.
- If a feedback loop is slower than the thing it claims to control, it is decoration.

## 5. Automate — last

Cortex is step 5. Starship is step 5. CUDA kernels are step 5.

Do not automate a process you have not deleted, simplified, and accelerated. An LLM on a dumb process is a very expensive way to do the wrong thing faster. An LLM in the live path is a drunk intern with a launch button.

**The Autopilot rule:** the neural net proposes; the safety computer disposes. If the safety computer is down, the car does not drive. If the Czar is down, the house does not trade.

## How to use this document

When a campaign prompt, PR, or agent proposal arrives, score it:

1. Which requirement did it make less dumb?
2. What did it delete?
3. What did it simplify *after* deleting?
4. Which loop got faster?
5. Why is automation allowed *now*?

If the answer to (2) is "nothing," the default is reject.
