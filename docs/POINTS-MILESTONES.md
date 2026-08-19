# Points Rebuild — Milestone Batch (2026-08-19)

Batched run. Each milestone is GATED on the one before where it needs its output.
No check-in between milestones; report only when all four are complete.

- [ ] **M1 · Skills attachable to a model.**
      Gate: none. `Fighter` has no `skills` field, so a named skill cannot be
      costed onto a model. Tiers are already priced (20/35/55) and the vault
      already tier-tags its skills. Add the map, the field, the rank tier caps.

- [ ] **M2 · Rule the base gatherer rate.**
      Gate: none (independent of M1). Structures cost Materials, crews cost
      Credits, and no rate connects them. Ruled with a stated derivation and an
      OVERRIDE record; this is the parked decision, now taken rather than left.

- [ ] **M3 · Validate the priced catalogue in the sim.**
      Gate: **M1** — crews must be able to carry skills before a crew built from
      the catalogue means anything. Build equal-Crew-Rating lists from the real
      catalogue and check they play to ~50%. This is Phase 5 of the v2 directive
      and the closest honest proxy for table data: if equal-points crews are not
      equal-strength, the prices are wrong regardless of how they were derived.

- [ ] **M4 · Body-scale ruling.**
      Gate: **M3** — the fork (keep legacy bodies vs re-derive from the measured
      stat ladder) is decided on whether equal-points crews actually play even,
      not on the reference-data band alone.

Definition of done: all four checked, full suite green, consistency 0 FAIL,
committed and pushed.
