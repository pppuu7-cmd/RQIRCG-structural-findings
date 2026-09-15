# SF055 Lane C — implemented three-point flow C3 insertion manifest — TERMINAL

Date: 2026-09-15
Parent preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
Lane-C prospective freeze: `749be3e1bbc7ac147c8141771308b6c848d3053b`.

## RESULT / CLASSIFICATION

`PASS_IMPLEMENTED_THREE_POINT_FLOW_C3_INSERTION_MANIFEST_SCOPED`.

SF055 overall status remains **NON-TERMINAL**.

`SF055_TERMINAL_PASS = FALSE`.

Lane A baseline EH/ghost flow reproduction remains separately required. No substantive projected C3 beta value is authorized for inspection or interpretation.

## SOURCE AUTHORITY

Primary source:

N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2.

Frozen source objects:

- Eq. (1): bosonic graviton and Faddeev-Popov ghost Wetterich traces;
- Figure 2: source coefficient/topology sequence `-1/2 + 3 - 3 + 6`, with external-momentum symmetrization;
- Eq. (7): the three-graviton flow depends on dressed graviton vertex orders `n in {3,4,5}`.

Inherited SF054/SF055 authority supplies one common covariant `C^3` fluctuation coupling with `Gamma_C3^(2)=0` on flat background and correlated `Gamma_C3^(3,4,5)`.

## FROZEN IMPLEMENTED MANIFEST

The prospectively frozen machine-readable source topology classes are exactly:

1. `T5_GRAV`: coefficient `-1/2`, vertex order `[5]`;
2. `B43_GRAV`: coefficient `+3`, vertex orders `[4,3]`;
3. `T333_GRAV`: coefficient `-3`, vertex orders `[3,3,3]`;
4. `T333_GHOST`: coefficient `+6`, ghost sector.

The coefficient reconstruction is exactly:

- graviton tadpole: `(1/2)*(-1) = -1/2`;
- graviton 4/3 bubble: `(1/2)*(+6) = +3`;
- graviton triangle: `(1/2)*(-6) = -3`;
- ghost triangle: `(-1)*(-6) = +6`.

All source topologies carry the frozen external-symmetrization flag.

## FIRST-ORDER COMMON-C3 INSERTION COMPLETENESS

At `O(g_C3^fluc)` the implemented manifest contains exactly six pure-graviton one-C3 insertion slots before symmetry reduction:

- `T5_GRAV`: one `Gamma_C3^(5)` slot;
- `B43_GRAV`: one `Gamma_C3^(4)` slot and one `Gamma_C3^(3)` slot;
- `T333_GRAV`: three ordered `Gamma_C3^(3)` slots;
- `T333_GHOST`: zero C3 slots.

Executed insertion histogram:

`{3:4, 4:1, 5:1}`.

The union of required dressed graviton orders is exactly `{3,4,5}`.

Every permitted insertion uses the same common coupling identifier `g_C3_fluc` and has `c3_power=1`.

## NEGATIVE CONTROLS

All prospectively frozen counterexample mutations were rejected by the executed checker:

- deleting the n=5 tadpole insertion;
- deleting one 4/3-bubble insertion;
- deleting one ordered triangle insertion;
- adding a C3 two-point/propagator insertion;
- adding a C3 ghost insertion;
- changing one insertion to `c3_power=2`;
- altering a source coefficient;
- adding an extra source topology;
- assigning an independent n=4 C3 coupling.

Thus a green result is not merely a positive-template match: the checker demonstrably detects the declared failure modes.

## REPRODUCIBILITY / PROVENANCE

GitHub Actions:

- run: `34995935520`;
- job: `104472035930` (`topology-manifest`);
- conclusion: `success`;
- head: `83fc6165e15a2eef07335e30fc5c6ff696062195`;
- artifact id: `10407288690`;
- artifact name: `sf055c-topology-manifest`;
- artifact digest: `sha256:879f6860559205acf526eb1cf65386b17eeb3914a7a278b05e9e7fe9beb28502`.

The workflow output reports:

- `positive_pass = true`;
- `negative_pass = true`;
- `scientific_pass = true`;
- `source_coefficient_derivation_pass = true`;
- classification `PASS_IMPLEMENTED_THREE_POINT_FLOW_C3_INSERTION_MANIFEST_SCOPED`.

Durable files:

- `prereg/SF055C_IMPLEMENTED_THREE_POINT_FLOW_TOPOLOGY_MANIFEST_PREOUTCOME.md`;
- `results/raw/SF055C_THREE_POINT_FLOW_TOPOLOGY_MANIFEST.json`;
- `scripts/sf055c_topology_manifest_check.py`;
- `results/raw/SF055C_THREE_POINT_FLOW_TOPOLOGY_CHECK.json`;
- `.github/workflows/sf055c-topology-manifest.yml`.

## NEW SCIENTIFIC / IMPLEMENTATION FACT

Within the frozen SF055 flat-Euclidean fluctuation architecture, the three-graviton Wetterich source topology can be represented with a source-faithful finite manifest in which the one common covariant C3 deformation supplies all and only the required first-order n=3,4,5 pure-graviton insertions while producing no n=2 or ghost-C3 insertion.

This closes the **topology/insertion-bookkeeping** part of Lane C.

## INTERPRETATION CEILING

This PASS does not validate:

- loop integrands or symmetry factors beyond the frozen source topology coefficients;
- propagator or regulator implementation;
- momentum integration;
- the published EH/ghost baseline numerical flow;
- an actual unprojected tensor loop RHS;
- the projector-flow contraction on such a loop RHS;
- a C3 beta function, fixed point, regulator independence, background/fluctuation equality, Lorentzian matching, or successor selector.

## REMAINING SF055 DEPENDENCY

Highest-priority remaining calibration dependency:

`LANE_A_BASELINE_EH_GHOST_THREE_POINT_FLOW_REPRODUCTION`.

Only after Lane A terminalizes under the already-frozen source conventions may the substantive unprojected TT loop RHS be assembled and inspected for `P_E_6d` C3 projection.
