# SF053 — projected dynamical C3 flow RHS availability — AUTHORITY AUDIT

Date: 2026-09-15
Preregistration: `d924354f54f777b33105bae14db8554cc3ca18e0`.

## Target

Evaluate whether the completed SF052 projector `P_E_6d` can be applied to an actually published dynamical graviton three-point FRG flow object

`F_3=[partial_t Gamma_k^(3)]_TT`

without reconstructing tensor directions that were discarded by the executed truncation/projection.

## Source A — Christiansen et al., Local Quantum Gravity

Primary source: arXiv:1506.07016.

The fluctuation three-point machinery is genuine: the functional flow of the three-point correlator is obtained by field differentiating the FRG equation, and in principle the RHS generates tensor structures allowed by the symmetries.

However the executed vertex ansatz takes the tensor structures from the classical gauge-fixed Einstein-Hilbert action. Coupling flows are extracted after contracting the tensorial flow with selected TT Einstein-Hilbert projectors. The reported channels separate a momentum-independent part and the p^2 Einstein-Hilbert/Newton part.

Therefore the published scalar `Flow_Lambda` / `Flow_G` objects are not an unprojected tensor record from which an orthogonal local p6 C3 coefficient can later be reconstructed.

Verdict on A/B/D:

`P6_TENSOR_INFORMATION_NOT_RETAINED_IN_REPORTED_THREE_POINT_COUPLING_FLOW`.

## Source B — Denz, Pawlowski, Reichert

Primary source: arXiv:1612.07315.

The systematic vertex expansion is extended to the four-graviton function, but the vertex ansatz continues to use Einstein-Hilbert tensor structures, with momentum-dependent scalar dressings. The source explicitly explains that all tensor structures can be generated in principle, while the vertex functions are restricted to the chosen classical tensor structures.

The paper constructs an orthogonal R^2 test and explicitly states that back-feeding a second tensor structure would require a two-tensor approximation of the three- and four-graviton vertices, deferred to future work.

This is direct evidence that orthogonal tensor information not included in the ansatz is not recoverable merely from the scalar momentum dressing.

For the C3 target the problem is stronger: the frozen projector isolates a p6 tensor direction rather than an R/R^2 dressing of the Einstein-Hilbert tensor.

Verdict:

`EXISTING_VERTEX_EXPANSION_IS_NOT_A_P6_C3_TENSOR_TRUNCATION`.

## Source C — Pawlowski and Traenkle effective-action reconstruction

Primary source: arXiv:2309.17043 / Phys. Rev. D 110, 086011 (2024).

This later work uses fully momentum-dependent three- and four-graviton scattering couplings and reconstructs the effective action through quadratic-curvature form factors.

The paper explicitly notes that p6 contributions corresponding to R^3-type operators can be present, but states that they are subdominant in the cited previous studies and are not considered in the reconstruction.

Thus the later momentum-dependent data pipeline does not close the SF053 target either.

Verdict:

`P6_R3_C3_SECTOR_EXPLICITLY_EXCLUDED_FROM_RECONSTRUCTION`.

## Frozen questions A-E

A. Full tensor-valued flow retained in published executed result?

`NO_FOR_TARGET_EXTRACTION`.

The formal functional RHS is tensor-valued, but the published coupling flows are contracted onto a small preselected tensor basis.

B. Momentum information sufficient to separate local p6 C3?

`NO`.

A scalar dressing multiplying an Einstein-Hilbert tensor cannot reconstruct an orthogonal tensor structure that the ansatz/projection discarded. Later reconstruction explicitly stops below p6/R3.

C. C3 fluctuation coupling included self-consistently in the truncation?

`NO`.

No audited target calculation includes a dynamical fluctuation C3 tensor/coupling with its correlated higher vertices in the closed RHS.

D. Raw/unprojected RHS published or reconstructible from explicit source equations/code at the required tensor resolution?

`NOT CLOSED`.

The formal diagrams/equations define a flow, but the source-faithful numerical/output object needed for `P_E_6d[F_3]` is not supplied.

E. Can the missing fluctuation object be replaced by the background essential G_C3 trajectory?

`NO`.

Background and fluctuation sectors are distinct in the FRG setup; their relation requires split/Nielsen identity control. SF043 background-essential selection cannot be substituted for the missing fluctuation tensor flow.

## Core distinction

`FORMAL TENSOR-VALUED FRG EQUATION != PUBLISHED PROJECTOR-READY P6 FLOW DATA`.

and

`FULL MOMENTUM DEPENDENCE OF ONE CHOSEN TENSOR DRESSING != FULL TENSOR BASIS`.

## Classification basis

The frozen PASS rule is not met because no audited source supplies enough retained tensor information to evaluate `P_E_6d[F_3]`.

Both frozen blockers are active:

1. p6/C3 tensor information is discarded/not represented by the executed projections;
2. the dynamical C3 fluctuation truncation is not included self-consistently.

Therefore the most accurate primary terminal is

`BLOCKED_TARGET_FLOW_OBJECT_NOT_RECONSTRUCTIBLE_SCOPED`.

This is a missing-object result, not evidence that the true projected C3 beta function vanishes.
