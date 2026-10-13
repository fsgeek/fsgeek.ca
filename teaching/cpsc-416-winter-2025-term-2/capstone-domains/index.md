# Capstone domains

2026-10-08 · https://fsgeek.ca/teaching/cpsc-416-winter-2025-term-2/capstone-domains/

The course will suggest 4–6 capstone domains. Students can also propose a different domain; it will be approved if it meaningfully exercises distributed systems reasoning (failures, invariants, coordination, consistency, and observability).

## Suggested domains (draft)

  1. **Distributed key-value store:** sharding + replication + reconfiguration; explicit consistency model; failure recovery.
  2. **Coordination service (etcd/ZooKeeper-like):** consensus-backed configuration, leader election, locks/leases, and watches.
  3. **Real-time collaboration:** CRDT-based shared document/state with offline edits and merge semantics.
  4. **Secure messaging / decentralized relay:** end-to-end encryption plus distributed delivery, replay protection, and metadata-aware tradeoffs.
  5. **Distributed compute / serverless mini-platform:** scheduling, retries, idempotency, and failure isolation across workers.
  6. **Transactional system across shards:** 2PC-based transactions or ledger/banking-style transfers with clear atomicity guarantees.



Alternative domains are welcome via nomination; the goal is not a specific application, but that the project forces protocol-level reasoning under failure.

## Nomination criteria

  * Clear failure model (crash, partition, byzantine is optional, slow nodes, message loss/duplication).
  * Concrete invariants or safety/liveness statements.
  * Protocol-level design (not just “use X library”).
  * Evaluation plan that includes failure injection or adversarial scenarios.
