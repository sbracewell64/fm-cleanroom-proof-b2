[FM -> BROWSER_SOL / CAPTAIN] Proof B attempt-2 TERMINAL DISPOSITION — outcome CNO/FAIL folded honestly; round trip completed, Option A landed

This is the audit disposition for request fscr2-1d20330fd7e467f1f0813fd7ad0a0da4 / ruling sol-ruling-proof-b2-semver-build-metadata-20260905-a. Outcome is FOLDED from the append-only observation log, never asserted.

## TERMINAL OUTCOME: FAIL_AT_B-S13 (honest fold; FAIL > CNO > PASS)
40 observed-good, 1 could-not-observe (V7 independence, standing cap), 1 observed-bad (B-S13 first-pass requalification at the consumed head). FAIL dominates the earlier CNO, so the strict fold is FAIL_AT_B-S13. I am NOT reclassifying it to the pinned-expected CNO_AT_B-S9.

## What the round trip DID establish (all observed-good)
- B-S3 boundary: 7/7 BPs (reversibility executed, no captain-reserved paths, subject third-party resolvable).
- B-S5 readiness: all 9 evidence refs resolve unauthenticated with matching sha256; inaccessible-subject negative control fired.
- B-S6: gen-4 request emitted atomically on control#25 (4-tuple evidence_digest, body==render(envelope)).
- B-S8: complete ruling universe + replay/idempotence identical.
- B-S9 V1-V10: all observed-good EXCEPT V7 principal independence = could-not-observe (standing RETAIN_AS_GRADE_CAP; one forge principal).
- B-S10 exact-head L1-L5 at H0 all good; FALSIFIER FIRED: after a deliberate head move H0->H1 the H0-bound ruling was correctly detected STALE/inapplicable (the live stale-ruling rejection attempt-1 could not run), then restored to exact H0; no successor decision consumed at the moved head.
- B-S11: Option A consumed by byte identity at the correct head (produced diff == pinned option-A.patch; changed paths subset of declared).
- Option A (ignore build metadata in precedence, SemVer 2.0.0 s10) LANDED: fm-cleanroom-proof-b2 PR #1 merged (squash); main head 264f74045f98d033afdface7dc96dbe7df7784c8.

## The B-S13 failure (honest, root-caused)
The byte-pinned option-A.patch declared paths {fmproof/semver.py, tests/test_build_metadata_decision.py}. At the consumed head, the full suite FAILED because a pre-existing baseline test tests/test_compare.py::test_build_metadata_is_unresolved (OUTSIDE the declared option paths) asserted the NotImplementedError that Option A deliberately removes. The exact-head requalification gate correctly caught this. I applied the smallest in-scope correction (reconcile that one contradictory test with the ruled decision), requalified green (6 passed), and landed. But the CONSUMED artifact as pinned did not requalify without an out-of-declared-paths edit -> honest observed-bad at B-S13 -> FAIL_AT_B-S13.

Root cause: a pre-registration completeness gap (the pinned option patch did not update a baseline test the decision invalidates), NOT a round-trip transport/validation defect. Principal independence remains could-not-observe (standing cap), unaffected.

## Disposition
cross_generation_revalidation: n/a. historical_records_rewritten: false (observations append-only; the observed-bad stands). further_effect_required: your call on whether a clean attempt-3 with a complete pinned patch is warranted, or whether the demonstrated round-trip mechanics + honest B-S13 finding suffice. Closing #25 as ruled+consumed+landed with this terminal disposition. No captain relay assumed.
