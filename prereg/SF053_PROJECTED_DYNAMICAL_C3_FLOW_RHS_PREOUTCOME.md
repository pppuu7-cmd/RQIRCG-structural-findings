# SF053 — projected dynamical C3 flow RHS availability — PREOUTCOME

Date: 2026-09-15
Inherited authority: SF052 `PASS_COMPLETE_SIX_DERIVATIVE_TT_QUOTIENT_SCOPED`.

## HYPOTHESIS

Existing dynamical graviton-vertex FRG machinery may or may not retain enough tensor/momentum information to evaluate the completed SF052 essential C3 projector on an actual three-graviton flow RHS. The gate tests availability and object identity; it does not infer a C3 flow from lower-derivative dressings.

## EXACT TARGET OBJECT

Frozen projector:

`P_E_6d`, defined by the SF052 essentialized TT tensor at the real Euclidean symmetric point.

Target flow object:

`F_3 = [partial_t Gamma_k^(3)]_TT`

for the dynamical graviton three-point function, before any projection that removes the local p6 tensor direction.

Desired scalar extraction:

`B_C3(k) = P_E_6d[F_3]`

up to separately declared wave-function/coupling normalization conventions.

## FROZEN SOURCE QUESTIONS

A. Does the published dynamical three-graviton FRG construction define the full TT tensor-valued flow or only one/few scalar dressings after contraction with preselected classical tensors?

B. Is the momentum dependence retained richly enough to separate a local p6 C3 structure from lower-derivative structures at the symmetric point?

C. Is the C3 tensor/coupling itself included in the fluctuation truncation, or would its contribution to propagators/vertices/RHS be omitted?

D. Are the raw/unprojected flow tensor or sufficient tensor components published or reconstructible from explicit equations/code?

E. Can the SF052 projector be applied without assuming equality between a background essential coupling and a fluctuation coupling?

## PRIMARY SOURCES TO AUDIT

- Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016.
- Denz, Pawlowski, Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, arXiv:1612.07315.
- later fluctuation-vertex / momentum-dependent graviton work if it materially changes A–E.

## PASS

`PROJECTED_DYNAMICAL_C3_FLOW_RHS_AVAILABLE_SCOPED` only if an explicit source object supplies enough tensor/momentum information to evaluate `P_E_6d[F_3]` without reconstructing discarded tensor directions or importing a background C3 flow as a substitute.

## PARTIAL / BLOCKED

`BLOCKED_P6_FLOW_TENSOR_DATA_DISCARDED_BY_EXISTING_PROJECTION_SCOPED` if existing calculations formulate a full functional flow in principle but publish/execute only lower-dimensional projected dressings that do not retain the C3 direction.

`BLOCKED_C3_FLUCTUATION_TRUNCATION_NOT_INCLUDED_SCOPED` if tensor data would be adequate in principle but the C3 fluctuation vertex/coupling is absent from the truncation needed for a closed RHS.

`BLOCKED_TARGET_FLOW_OBJECT_NOT_RECONSTRUCTIBLE_SCOPED` if both limitations apply or no source-faithful reconstruction is possible.

## FAIL

No scientific FAIL is authorized merely from missing published data. FAIL would require an explicit target flow calculation showing the completed C3 projector vanishes or is inconsistent in the frozen domain.

## CONTROLS

- lower-derivative Einstein-Hilbert tensor dressings must not be relabeled C3 data;
- a formal Wetterich/vertex equation is not by itself an executed p6 tensor flow;
- background essential `G_C3` is not substituted for a fluctuation C3 coupling;
- green CI / numerical convergence is irrelevant unless it is for the target tensor object.

## INTERPRETATION CEILING

A PASS would provide a projected fluctuation-flow object, not regulator-independent physical matching. A BLOCKED verdict localizes missing data/machinery and is not a no-go for asymptotic safety or C3 running. No physical SF025 `b`, Lorentzian observable, quantum `chi_ABC`, historical RCG-002 authority, full-QG or new-physics claim is authorized.
