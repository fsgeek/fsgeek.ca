# Readings

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/readings/

Readings are short, targeted, and chosen to support the **failure-first** protocol development we do in lecture and the **design-first** work you do in DP1/DP2 and the capstone.

**Baseline:** this mapping is adapted from the previous offering’s reading list (Winter 2023 Term 1 syllabus) and aligned to the current lecture spine.

**Where PDFs live:** Canvas Files → Readings.

## Core sources

  * **Petrov:** Alex Petrov, _Database Internals_ (O’Reilly; selected chapters)
  * **Kleppmann:** Martin Kleppmann, _Designing Data-Intensive Applications_ (O’Reilly; selected chapters)
  * **Primary papers:** Lamport (Paxos; Byzantine), Castro & Liskov (PBFT), Chandy-Lamport (snapshots)



**Textbook access:** both core books are O’Reilly titles and are available electronically to UBC students at no additional charge (via the UBC Library’s O’Reilly platform): [UBC Library — O’Reilly for Higher Education (log in)](https://techserv.library.ubc.ca/2020/10/13/oreilly-for-higher-education-safari-new-log-in/).

**Accessibility:** O’Reilly often provides audio versions for some titles/chapters. Audio can be helpful for commuting and for students whose first language is not English.

## Week 01 (Jan 6 / Jan 8)

  * **Tue (Jan 6) — Required:** Start Here
  * **Tue (Jan 6) — Required:** [Assessment & evidence chain](/teaching/cpsc-416-winter-2025-term-2/assessment-and-evidence/)
  * **Tue (Jan 6) — Required:** [Using GenAI in this course without Goodharting it](/teaching/cpsc-416-winter-2025-term-2/genai-without-goodharting/)
  * **Thu (Jan 8) — Required:** Petrov, Chapters 1–2
  * **Thu (Jan 8) — Required:** DS Labs framework (how we use it)



## Week 02 (Jan 13 / Jan 15)

  * **Tue (Jan 13) — Required:** Petrov, Chapters 3–4
  * **Thu (Jan 15) — Required:** Petrov, Chapter 5 and Chapter 7
  * **Week 02 — Required:** DS Labs Client/Server lab handout (Gradescope)
  * **Recommended background:** “Distributed Systems for Fun and Profit” (partial failure, retries/timeouts): <https://book.mixu.net/distsys/>



## Week 03 (Jan 20 / Jan 22)

  * **Tue (Jan 20) — Required:** Kleppmann, Chapter 7 (Transactions)
  * **Thu (Jan 22) — Required:** Petrov, Chapter 13 (Distributed Transactions)
  * **Thu (Jan 22) — Required:** Introduction to formal verification (guest lecture slot): modeling + TLA+/PlusCal background
  * **Tool intro:** Learn TLA+ (PlusCal optional): <https://learntla.com/>



## Week 04 (Jan 27 / Jan 29)

  * **Tue (Jan 27) — Required:** Petrov, Chapter 8 (through Two Generals’ Problem)
  * **Thu (Jan 29) — Required:** Petrov, Chapter 8 (from FLP Impossibility to end)
  * **Week 04 — Required:** DP1 prompt: [Design Project 1 — Primary/Backup replication](/teaching/cpsc-416-winter-2025-term-2/design-project-1-primary-backup/)



## Week 05 (Feb 3 / Feb 5)

  * **Tue (Feb 3) — Required:** Petrov, Chapter 11 (Replication & Consistency)
  * **Thu (Feb 5) — Required:** Kleppmann, Chapter 5 (Replication)



## Week 06 (Feb 10 / Feb 12)

  * **Tue (Feb 10) — Required:** Petrov, Chapter 10 (Leader Election)
  * **Thu (Feb 12) — Required:** Petrov, Chapter 14 (Consensus)
  * **Week 06 — Required:** Lamport’s bakery algorithm (mutual exclusion as “ballots before Paxos”): bakery.pdf
  * **Week 06 — Required:** Viewstamped Replication (primary/backup with view change as a “Raft 25 years earlier” lens): 1988 Viewstamped Replication (Oki-Liskov).pdf
  * **Week 06 — Required:** DP1 peer review + implementation instructions (Canvas assignments)



## Week 07 (Feb 24 / Feb 26)

  * **Tue (Feb 24) — Required:** Lamport, “Paxos Made Simple”: paxos-simple-Copy.pdf
  * **Thu (Feb 26) — Required:** Petrov, Chapter 14 (Consensus) — continue/discuss
  * **Week 07 — Recommended:** Lamport, “The Part-Time Parliament” (for the underlying ballot/acceptor story): 1998 The Part-Time Parliament (Lamport).pdf
  * **Week 07 — Required:** DP2 prompt: [Design Project 2 — Paxos](/teaching/cpsc-416-winter-2025-term-2/design-project-2-paxos/)



## Week 08 (Mar 3 / Mar 5)

  * **Tue (Mar 3) — Required:** Altinbuken & van Renesse, “Paxos Made Moderately Complex”: PaxosMMCAltinbukenVanRenesse.pdf
  * **Thu (Mar 5) — Required:** Kleppmann, Chapter 6 (Partitioning)
  * **Week 08 — Recommended:** Ongaro & Ousterhout, “In Search of an Understandable Consensus Algorithm (Raft)”: 2014 In Search of an Understandable Consensus Algorithm (Raft).pdf
  * **Week 08 — Recommended:** “Viewstamped Replication Revisited” (modernized write-up of the VR protocol): 2012 Viewstamped Replication Revisited.pdf
  * **Tool refresher:** Learn TLA+ (model-checking safety properties): <https://learntla.com/>



## Week 09 (Mar 10 / Mar 12)

  * **Tue (Mar 10) — Required:** Chandy & Lamport, “Distributed Snapshots”: 1985 Distributed Snapshots Determining Global States of Distributed Systems.pdf
  * **Thu (Mar 12) — Required:** Mid-course “Goodhart revisit” notes (posted in Week 09 module)



## Week 10 (Mar 17 / Mar 19)

  * **Tue (Mar 17) — Required:** Lamport et al., “The Byzantine Generals Problem”: 1982 The Byzantine Generals Problem OCR.pdf
  * **Thu (Mar 19) — Required:** Castro & Liskov, “Practical Byzantine Fault Tolerance”: 1999 Practical Byzantine Fault Tolerance.pdf



## Week 11 (Mar 24 / Mar 26)

  * **Tue (Mar 24) — Required:** “Making Reads in BFT SMR Fast, Linearizable and Live” (2021): 2021 Making Reads in BFT State Machine Replication Fast Linearizable and Live.pdf
  * **Thu (Mar 26) — Required:** Bitcoin whitepaper (ledger incentives): <https://bitcoin.org/bitcoin.pdf>



## Week 12 (Mar 31 / Apr 2)

  * **Tue (Mar 31) — Required:** Petrov, Chapter 12 (Anti-Entropy & Dissemination)
  * **Thu (Apr 2) — Required:** “A comprehensive study of Convergent and Commutative Replicated Data Types” (CRDT overview): <https://hal.inria.fr/inria-00555588/document>



## Week 13 (Apr 7 / Apr 9)

  * **Low-risk week:** project reviews, demos, and capstone clinics (no required reading).
