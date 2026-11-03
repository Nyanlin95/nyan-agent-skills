---
name: dev-process-deterministic-core-and-replay
description: Implement deterministic core logic and recorded-input replay for reproducible bugs or verifiable simulation results. Use when exact replay is required; avoid imposing a simulation architecture on ordinary request recovery.
---

# Deterministic core and replay

1. Define the replay boundary and the state and outputs that must match.
2. Isolate external effects and inject time, randomness, and nondeterministic results.
3. Record the initial state, ordered inputs, seed, configuration, and compatible code or schema version needed for reconstruction.
4. Replay through the same core and report the first divergent state or output.
5. Retain a regression recording for the demonstrated failure.

Preserve event ordering and clock semantics; distinguish domain timestamps from elapsed processing time. Define floating-point and runtime compatibility limits before promising exact replay. Reject incomplete or incompatible recordings explicitly, and verify a valid replay plus a missing-input or version-mismatch failure. Keep recordings minimal and sanitized; replay external effects through isolated substitutes.

Validate input provenance and authoritative rules separately when checking a submitted score or result. Reproducing a claimed run alone does not prove the inputs were genuine.

Report the replay command, compatibility boundary, checks, and any nondeterminism left outside the model.

Adapted from the [tibo.dog development thread](https://x.com/poteto/status/2117043478140276847).
