# SF055 — C3 projected fluctuation-FRG implementation contract — PREOUTCOME

Date: 2026-09-15
Inherited authority: SF052 completed `P_E_6d`; SF053 localized the missing executed p6 flow object; SF054 proved that a covariant C3 flow requires correlated 3/4/5-point C3 vertices.

## PURPOSE

Freeze the exact implementation conventions BEFORE any numerical C3 flow coefficient is inspected. This gate is an implementation/calibration contract, not yet a claim about the C3 beta function.

## FROZEN BASELINE REALIZATION

Inherit the published fluctuation setup of Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016, unless a later explicit successor gate prospectively replaces it:

- D=4 flat Euclidean background;
- linear split `g=bar g+h`;
- De-Donder-type linear gauge in the Landau limit;
- graviton plus Faddeev-Popov ghost fluctuation sectors;
- regulator of the source form `R_phi(x)=Gamma_k^(phi phi)|_{mu=0}(x) r(x)` with `x r(x)=(1-x) theta(1-x)`;
- symmetric external three-point kinematics `|p1|=|p2|=p`, angle `2 pi/3`; target C3 evaluation at `p=k`, equivalent after rescaling to the SF052 unit symmetric point;
- source wave-function/canonical normalization conventions tracked explicitly.

## FROZEN C3 EXTENSION

One and only one fluctuation C3 coupling:

`G_C3^fluc(k) int sqrt(g) C^3`.

Dimensionless coordinate:

`g_C3^fluc(k)=k^2 G_C3^fluc(k)`.

Generate from this same covariant operator the correlated pure-graviton vertices

`Gamma_C3^(3)`, `Gamma_C3^(4)`, `Gamma_C3^(5)`.

No independent 3/4/5 C3 coefficients are permitted in this gate.

`Gamma_C3^(2)=0` around flat space is a mandatory negative control.

## TARGET RHS

Compute the TT three-graviton flow before an Einstein-Hilbert-only tensor contraction:

`F3_TT = [partial_t Gamma_k^(3)]_TT`.

At first order in `g_C3^fluc`, retain:

1. baseline graviton and ghost diagrams;
2. all one-C3-insertion graviton contributions generated through `Gamma_C3^(3,4,5)`;
3. the source regulator prescription and baseline propagators;
4. no background-C3 substitution.

Final target extraction:

`B_C3(k)=P_E_6d[F3_TT(p_i^2=k^2,p_i.p_j=-k^2/2)]`.

## CALIBRATION LANES

### Lane A — source baseline

Before trusting any C3 output, reproduce a published source baseline using the same diagram generator / propagator / gauge / regulator conventions. At minimum reproduce the structure of the published projected three-point flow; a numerical benchmark must be prospectively fixed before use as a PASS threshold.

### Lane B — tensor controls

- reproduce `Gamma_C3^(2)=0`;
- reproduce the SF052 three-point C3 tensor/projector response at the symmetric point;
- verify Bose symmetry of generated `Gamma_C3^(3,4,5)`;
- verify no independently tuned higher-vertex C3 coefficients.

### Lane C — flow completeness

Show diagrammatically/code-wise that all graviton topologies in the three-point Wetterich flow receive every permitted one-C3 insertion among n=3,4,5, while ghost diagrams remain baseline-only because the C3 action has no ghost fields.

## PASS

`C3_PROJECTED_FRG_IMPLEMENTATION_VALIDATED_FOR_EXECUTION_SCOPED` only if all calibration lanes pass before the substantive C3 beta output is interpreted.

## BLOCKED

`BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED` if the correlated mixed-momentum C3 3/4/5 vertices cannot be generated source-faithfully.

`BLOCKED_BASELINE_FRG_REPRODUCTION` if the implementation cannot reproduce its prospectively specified baseline control.

`BLOCKED_PROJECTOR_FLOW_INTERFACE` if the unprojected TT flow cannot be contracted with `P_E_6d` without losing the required tensor information.

## INVALID

Changing gauge, regulator, split, external kinematics, C3 vertex closure, or projector after inspecting a substantive C3 flow result requires a new preregistered gate.

## INTERPRETATION CEILING

Passing SF055 would authorize execution of a scoped fluctuation C3 flow calculation. It would not itself establish a beta function value, UV fixed point, background/fluctuation equality, regulator independence, Lorentzian physical matching, SF025 `b`, quantum `chi_ABC`, historical RCG-002 authority, full quantum gravity, or new physics.
