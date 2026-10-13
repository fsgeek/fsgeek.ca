# Using GenAI in this course without Goodharting it

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/genai-without-goodharting/

Generative AI use is required in this course. The goal is not to “produce answers faster”. The goal is to use GenAI to accelerate **iteration** and **clarify thinking** while keeping the work grounded in **evidence**.

## The failure mode (Goodhart’s ceiling)

When a metric becomes a target, it stops being a good metric. In this course, the risky metric is “polished artifacts” (clean prose, perfect diagrams, plausible designs) that are not supported by a trace of reasoning and testing. GenAI makes this failure mode cheap.

The countermeasure is simple:

  * **Artifacts are not sufficient.** Every significant claim needs an evidence trail.
  * **Evidence is not performative.** It is the minimal trace needed to support a claim and enable feedback.



## What counts as evidence here

  * **Signed git history:** commits/PRs/issues that show incremental construction.
  * **AI interaction log:** what you asked, what mattered in the answer, what you changed, and what you rejected.
  * **Protocol evidence:** invariants/safety claims, liveness assumptions, and the reasoning that connects failures to mechanisms.
  * **Execution evidence:** scripts, experiments, failure injections, logs/metrics/traces that support claims.
  * **Model evidence:** TLA+/PlusCal (preferred) or another formal/spec artifact that ruled something out or clarified an assumption.



## What does not count (and will be treated as low-signal)

  * One-shot “final answers” without intermediate commits/experiments.
  * Beautiful designs with no failure model, invariants, or evaluation plan.
  * AI transcript dumps with no decisions, deltas, or attribution.
  * Claims like “it works” without a reproduction recipe and failure cases.



## The operating procedure

  1. **State the failure:** write down the failure model and what “recovery” means.
  2. **State the guarantees:** list at least one safety invariant and one liveness assumption (if applicable).
  3. **Ask GenAI targeted questions:** “what mechanism enforces this invariant?”, “what failure breaks this design?”, “what evidence would distinguish two hypotheses?”.
  4. **Record the decision:** what you accepted, what you rejected, and why.
  5. **Change the artifact:** update the design/spec/code/tests.
  6. **Commit with a trace:** signed commit that references the log entry.
  7. **Validate under failure:** test at least one adverse scenario and capture evidence.



## AI interaction log: minimal schema

Keep the log lightweight. The point is traceability, not volume.

  * **Goal:** what you were trying to decide/build.
  * **Prompt summary:** what you asked (no need to paste everything).
  * **Key output:** the one idea/claim that mattered.
  * **Decision:** what you adopted/rejected and why.
  * **Evidence link:** commit/PR/issue/experiment that resulted.
  * **Unknowns:** what remains uncertain and how you plan to test it.



## How to use GenAI for TLA+/PlusCal (and not fool yourself)

  * **Use it to learn syntax and patterns** , then verify with the model checker.
  * **Ask for invariants and counterexamples** , then restate them in your own words.
  * **Do not trust plausibility.** Only trust properties you checked or can justify.



More detail: [TLA+ / PlusCal track (lightweight)](/teaching/cpsc-416-winter-2025-term-2/tla-pluscal-track/).

## Peer review expectations

Peer review is about helping a design become correct under its failure model. When reviewing:

  * Look for missing assumptions and untested liveness claims.
  * Ask for evidence: “what would you log to diagnose this?”, “what failure would falsify this?”.
  * Reward clarity and falsifiability, not polish.



## Integrity and privacy

  * Disclose GenAI use and keep an AI log.
  * Do not paste secrets/tokens into prompts.
  * Do not include personal data in logs beyond what is required for course work.
