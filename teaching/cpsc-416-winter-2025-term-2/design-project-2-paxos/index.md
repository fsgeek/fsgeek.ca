# Design project 2: Paxos

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/design-project-2-paxos/

This project is based on DS Labs PMMC Paxos. It is completion-graded, with formative feedback.

## Workflow

  1. **Design + peer review:** submit a design; review multiple peer designs using a structured rubric.
  2. **Implementation:** implement one selected design using the DS Labs harness.
  3. **Reflection + peer review:** write a reflection on what implementation revealed; review multiple peer reflections.



## Failure-first prompts

  * What is the minimum failure set that forces coordination?
  * Where do safety properties come from (quorum intersection, monotonicity), and what assumptions power liveness?
  * What observability is needed to debug “it didn’t decide” vs “it decided differently”?
