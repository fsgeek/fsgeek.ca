# Design project 1: primary/backup

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/design-project-1-primary-backup/

This project is based on DS Labs Primary/Backup replication. It is completion-graded, with formative feedback.

## Workflow

  1. **Design + peer review:** submit a design; review multiple peer designs using a structured rubric.
  2. **Implementation:** implement one selected design (not necessarily your own) using the DS Labs harness.
  3. **Reflection + peer review:** write a reflection on what implementation revealed; review multiple peer reflections.



## Failure-first prompts

  * What failures are in scope (crash, partition, delay, duplication), and what is explicitly out of scope?
  * What is the correctness model: what must always be true (safety), and what must eventually happen (liveness)?
  * What state is authoritative, and how is it recovered after failures?
