# SF055 -> programme-level verdict execution plan — FROZEN

Date: 2026-09-15
Repository: `pppuu7-cmd/RQIRCG-structural-findings`
Parent authority: SF055 projected FRG implementation contract and all already-terminal scoped SF055 Lane-B/Lane-C and Lane-A calibration results.

## Purpose

Replace open-ended micro-iteration with one short dependency chain. This plan does not relax any previously frozen physics object, source convention, normalization, regulator, projector, convergence sequence, or PASS threshold. It only fixes the order and hard-stop logic for the remaining programme.

## Major Step 1 — close Lane A baseline calibration

### 1A. SF055A3Q1 exact projector regrouping

Execute the already-preregistered exact identity

`sum_abc T_abc F(E1_a,E2_b,E3_c) = sum_ab F(E1_a,E2_b,sum_c T_abc E3_c)`

for both source projectors `T_G` and `T_Lambda` and all frozen controls.

Allowed result:

- PASS: use grouped projector in quadrature.
- FAIL: do not alter the physics object or fit Eq. (14); fall back to brute-force complete TT contraction if computationally feasible. A regrouping implementation FAIL alone is not a physics FAIL.

### 1B. Frozen Figure-2 quadrature and Eq. (14) baseline reproduction

Using only the already-frozen source objects and source-normalized external symmetrisation,

- `Sym_3 = (1/6) sum_{S3}`;
- loop measure `d^4q/(2 pi)^4`;
- topology coefficients `(-1/2,+3,-3,+6)`;
- full 6D Landau-transverse graviton internal sector;
- source-Fourier EH/FP vertices;
- canonical `G dotR G` single-scale insertion;
- complete TT source projectors and their source-derived `N_g`, `N_lambda`;
- C3 disabled;

execute the already-frozen deterministic convergence sequence `N = 8, 12, 16, 24`.

Reproduce through the same diagram code path all three prospectively frozen Eq. (14) three-point baseline targets. No target-dependent rescaling, fitted overall factor, changed symmetrisation convention, altered measure, or hard-coded Eq. (14) value is permitted.

A separate two-point `beta_mu` object remains separate from Figure-2 and is not to be silently substituted into the three-point check.

### 1C. Lane-A / SF055 terminalization

If the frozen baseline converges and reproduces all required baseline targets under the pre-existing tolerance, terminalize Lane A.

Because Lane B and Lane C are already terminal scoped PASS, Lane-A PASS authorizes SF055 terminal PASS.

If the baseline does not reproduce after implementation-bug corrections that leave the frozen science contract unchanged, classify Lane A/SF055 as FAIL or BLOCKED according to the pre-registered failure mode and STOP. Do not inspect or compute a substantive C3 projected flow after a baseline failure.

## Major Step 2 — projected dynamical C3 flow, conditional on SF055 PASS only

Only if SF055 terminalizes PASS:

- enable the one common covariant `g_C3^fluc` deformation;
- use the already-terminal common-origin correlated `Gamma_C3^(3,4,5)` generator;
- use exactly the already-terminal implemented one-C3 insertion manifest;
- compute the first-order projected dynamical C3 flow with the complete essential `P_E_6d` projector;
- execute the same deterministic integration/convergence discipline used by the calibrated baseline;
- report stability, topology decomposition, insertion-order decomposition and projector controls.

No background coupling may substitute for the fluctuation coupling.

If the projected dynamical C3 object is missing, non-convergent, numerically unstable, or projector-inconsistent, terminalize the corresponding missing-object/instability blocker and STOP before downstream physical matching.

## Conditional Step 3 — background/fluctuation + Nielsen/split control

Only if the dynamical C3 flow exists and is stable:

- test the background/fluctuation relation rather than assume equality;
- implement the relevant Nielsen/split-Ward control within the same truncation scope;
- quantify any residual split dependence needed to interpret the C3 flow.

Failure or non-closure here is a programme-level control blocker and prevents promotion to a physical selector.

## Conditional Step 4 — Lorentzian on-shell matching

Only if the split/background control is adequate:

- continue/map the Euclidean fluctuation result to the already-constructed Lorentzian on-shell C3 helicity/matching coordinate;
- preserve the previously identified global-sign convention uncertainty unless independently closed;
- do not call an off-shell Euclidean coefficient a physical observable without this bridge.

## Final programme-level verdict

After the last reached gate, issue exactly one evidence-based programme-level classification from the following families:

1. `PHYSICALLY_CONTENTFUL_SELECTOR_FOUND_SCOPED` — only if baseline calibration, dynamical C3 flow, split/background control and Lorentzian matching all close sufficiently to yield a physical matching selector within the declared scope.
2. `NONUNIQUENESS_OR_NO_GO_RETAINED_SCOPED` — if the completed chain shows that the proposed quantum/gravity structure still does not select the finite physical matching datum.
3. `MISSING_OBJECT_OR_CONTROL_BLOCKER_SCOPED` — if an indispensable baseline, dynamical, split/Nielsen, or Lorentzian object cannot be reconstructed or stabilized.

No stronger theory-establishment claim follows from any outcome.

## Hard-stop / anti-proliferation rule

The remaining work is treated as approximately three mandatory major steps (Q1/baseline; SF055 terminalization; projected C3 flow) plus at most two or three conditional downstream scientific gates. New subchecks may be introduced only as implementation controls inside one of these major steps; they must not silently become a new open-ended scientific programme or alter the frozen success criteria after outcomes are visible.
