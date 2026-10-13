# TLA+ / PlusCal track

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/tla-pluscal-track/

This course is design-first and failure-first. TLA+ (and optionally PlusCal) is a tool for making assumptions explicit and checking whether a protocol sketch actually enforces the properties you claim.

**Goal:** use a small model to rule out bad designs early and to produce evidence-bearing artifacts for peer feedback and capstone risk reduction.

## What this is (and is not)

  * **Is:** a structured way to practice “invariants first” and to get concrete counterexamples (TLC traces) when an idea is wrong.
  * **Is not:** a formal methods course; we keep models intentionally small and focused on one safety property at a time.



## Where it appears in the term

  * **Week 03:** first tiny model (atomic commit / coordination) + how to read a counterexample trace.
  * **Week 07–08:** optional extension tied to DP2 (Paxos safety in a deliberately small model).
  * **Capstone:** optional modeling milestone to de-risk assumptions and sharpen the failure evaluation plan.



## Minimum expected artifacts

  * **One-page spec:** state the failure model, the safety invariant(s), and the liveness assumption(s) you rely on.
  * **Model:** a small TLA+ or PlusCal spec that captures just enough structure to check the invariant.
  * **Evidence:** a TLC run (or equivalent) and either (a) “passes with invariant X” or (b) a counterexample trace plus your fix.
  * **Reflection:** a short note explaining what the model changed about your design thinking.



## How to use GenAI with TLA+ without fooling yourself

  * **Use GenAI for syntax and patterns** (operators, state variables, typical spec structure).
  * **Use TLC as the judge** : treat the model checker’s trace as the ground truth, not plausibility.
  * **Log decisions** : record what you asked, what you adopted, and the TLC evidence that resulted.
  * **Explain in your own words** : restate invariants and traces without copying tool output verbatim.



## Recommended learning resource

  * <https://learntla.com/> (TLA+ fundamentals; PlusCal optional)
