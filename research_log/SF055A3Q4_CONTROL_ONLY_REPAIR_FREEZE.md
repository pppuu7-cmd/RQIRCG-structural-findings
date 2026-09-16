# SF055A3Q4 — control-only repair freeze before retry

Date: 2026-09-16
Parent preregistration: `cd4176921f009761250fc4a25c3e1dfb9841ce1d`.

## FIRST LOCAL DRY-RUN STATUS

The first local checker execution completed the geometry/integration calculation but initially hit a JSON-only `numpy.bool_` serialization error. A serialization adapter changes no numerical or scientific result.

After serialization-only inspection, all prospectively frozen positive controls passed, but one required negative control did not fire:

`frozen_shifted_support_rejected = false`.

Diagnosis: the mutation used two hard-coded radial points (`r=0.96` and `r=0.995`) for `p=1/8,c=1`. Both lie on the same side of the exact shifted-shell root, so the purported mutation did not actually test freezing support across a moving shell.

This is an ineffective negative-control implementation, not evidence against the Q4 geometry. The first dry run is therefore treated as `INVALID_NEGATIVE_CONTROL_IMPLEMENTATION / NON_TERMINAL`, not as a scientific FAIL or PASS.

## FROZEN CONTROL-ONLY REPAIR

Before retry, replace only that mutation by an exact-root-straddling construction:

1. compute the already-preregistered exact positive root `r_b(p,c)`;
2. choose `r_in = r_b/2`;
3. choose `r_out = (r_b+1)/2`;
4. verify the true support bits at `r_in` and `r_out` differ;
5. define a frozen-support mutation as incorrectly reusing the `r_in` bit at `r_out`; require the checker to reject it.

This repair does not change:

- any geometry formula;
- any shifted line;
- any regulator;
- any momentum point;
- any positive control;
- any tolerance;
- the scalar shell control;
- the N sequence;
- the historical baseline classification;
- the interpretation ceiling.

The JSON serialization adapter and this root-straddling mutation are the only permitted changes before the exact retry.