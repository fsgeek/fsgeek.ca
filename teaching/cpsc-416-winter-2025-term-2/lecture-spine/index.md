# Lecture spine

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/lecture-spine/

This is a topic roadmap for the term. The **assignment schedule** and **milestones** are stable; the exact ordering of topics can shift (e.g., for a guest lecture) without changing what is assessed.

**Readings:** see [Readings](/teaching/cpsc-416-winter-2025-term-2/readings/) for the week-by-week mapping.

**Modeling:** see [TLA+ / PlusCal track (lightweight)](/teaching/cpsc-416-winter-2025-term-2/tla-pluscal-track/) for how formal specs fit into the course.

## Three arcs

  1. **Universal agreement:** transactions and atomic commit (2PC/3PC) — what breaks under failure, and what assumptions are needed to recover.
  2. **Partial agreement:** quorums (set quorum first), view changes, and crash-fault consensus (Viewstamped Replication / Paxos).
  3. **Adversarial agreement:** Byzantine consensus (pBFT) and incentive-driven ledger systems.



## Two recurring lenses

  * **Failure-first:** start from the failure, then derive the protocol mechanism that prevents or recovers from it.
  * **Optimization & Goodhart:** metrics are projections; optimizing one property can erase other properties. We use this lens both for distributed systems (e.g., incentives, availability vs correctness) and for GenAI-assisted work (polish vs evidence).



## Week-by-week sketch (W01–W12)

Reading week sits between W06 and W07. The final week of class meetings (W13) is reserved for low-risk activities (reviews/demos).

  * **W01:** Course framing (failure-first, evidence chain) + GenAI/Goodhart + DS Labs scaffold
  * **W02:** Communication semantics (timeouts/retries, at-most-once) and why “exactly-once” is hard
  * **W03:** Transactions under failure: 2PC (blocking) + invariants; introduce TLA+/PlusCal as a tool
  * **W03 (slot):** Guest lecture on modeling and formal verification (TLA+/PlusCal)
  * **W04:** 3PC and synchrony assumptions; failure detectors; DP1 design due by start of week
  * **W05:** Replication: primary/backup + view change; set quorum intuition; DP1 peer review
  * **W06:** Leader election & “ballots before Paxos”: Lamport’s bakery algorithm as a warm-up; then partial consensus (viewstamped → Paxos safety); DP1 implementation + reflection setup
  * **W07:** Paxos mechanics and Multi-Paxos; DP1 reflection; DP2 design (leveraging DP1 lessons)
  * **W08:** Paxos in systems: reconfiguration, performance, observability; optional follow-up on TLA+ modeling
  * **W09:** Mid-course Goodhart revisit: measurement, incentives, fault injection, and “evidence vs polish”
  * **W10:** Byzantine failures: pBFT and quorum intersection under adversarial behavior
  * **W11:** Ledgers: Nakamoto-style consensus and incentive design; optimization tradeoffs (sourdough analogy)
  * **W12:** Avoiding consensus: CRDTs/eventual consistency; capstone evaluation clinic (failure plans)
