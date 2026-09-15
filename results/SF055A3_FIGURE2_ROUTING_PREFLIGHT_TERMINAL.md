# SF055A3 — Figure-2 loop routing preflight — TERMINAL

Date: 2026-09-15
Parent SF055A3 freeze: `prereg/SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME.md`.
Prospective routing freeze: `a54ac458248b72071f05a6f1eeccdaa5bf85ec79`.

## CLASSIFICATION

`PASS_A3_2_FIGURE2_ROUTING_PREFLIGHT_SCOPED`.

This closes graph-level routing bookkeeping only. It does not terminalize SF055A3 Lane A or SF055.

## EXECUTED RESULT

The canonical incoming-momentum routings for the inherited Figure-2 topology classes

- `T5_GRAV` coefficient `-1/2`,
- `B43_GRAV` coefficient `+3`,
- `T333_GRAV` coefficient `-3`,
- `T333_GHOST` coefficient `+6`

were checked under five prospectively frozen affine diagnostic loop-coordinate shifts and all six external-leg permutations.

For every executed routing:

- each vertex conserved momentum;
- each internal edge appeared at its two incident vertices with opposite momentum;
- inherited topology coefficients remained unchanged;
- no diagnostic q-shift generated a new graph topology;
- six labelled external permutations were generated before any later symmetry reduction.

The largest observed vertex-conservation residual was `5.551115123125783e-17`; internal-edge opposition errors were zero at floating precision.

## COUNTEREXAMPLE-FIRST CONTROLS

All frozen routing mutations were rejected:

- wrong bubble V3 shifted-momentum sign;
- triangle internal endpoint sign flip;
- loss of an external permutation;
- treating a duplicate permutation as a new topology;
- mutation of an inherited source coefficient;
- moving propagator routing while holding the differentiated regulator line fixed.

Retain:

`LOOP_ROUTING_EQUIVALENCE != HOLD_REGULATOR_ARGUMENT_FIXED_WHILE_SHIFTING_OTHER_LINES`.

## REPRODUCIBILITY REPAIR

The first run `35000421090`, job `104487155775`, completed the calculation but failed while serializing `numpy.bool_` diagnostics. Commit `1340cd7e8bf72afedd7c3afc28d97571b1717b2f` changed only JSON serialization; no routing, coefficient, threshold, topology, or physics criterion changed.

Successful run:

- Actions run: `35000570266`;
- job: `104487655005`;
- executed head: `1340cd7e8bf72afedd7c3afc28d97571b1717b2f`;
- artifact: `10409661837`, `sf055a3-figure2-routing`;
- artifact digest: `sha256:4f20ca865dfc1987937a3689de7106bd38923331d9b6c666b01eace0e8ba7d5f`.

## NEW IMPLEMENTATION FACT

The frozen source-Fourier Figure-2 baseline topology set admits a deterministic, conservation-exact graph routing interface compatible with mechanical external symmetrisation and with coherent transformation of the differentiated regulator line under diagnostic loop-coordinate reparameterisation.

## INTERPRETATION CEILING

No EH/ghost loop tensor contraction has yet been evaluated. No quadrature, Eq. (14) reproduction, Lane-A terminal PASS, C3 projected flow, fixed point, or physical matching claim is authorized by this result.

## NEXT REQUIRED DEPENDENCY

`FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_WITH_FULL_KQ_PROPAGATORS`.

The contraction engine must use the A3.1 six-dimensional `K(q)` internal graviton propagators/regulators, the SF055A2 source-Fourier EH/FP seed vertices, the inherited Lane-C source coefficients, and the routing frozen here, with C3 disabled.
