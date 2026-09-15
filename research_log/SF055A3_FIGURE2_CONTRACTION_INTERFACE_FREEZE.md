# SF055A3 — Figure-2 tensor-contraction interface — PROSPECTIVE FREEZE

Date: 2026-09-15
Parent gate: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION`.
Inherited PASS authorities:

- `PASS_A3_1_LANDAU_TRANSVERSE_INTERNAL_PROPAGATOR_CALIBRATION_SCOPED`;
- `PASS_A3_2_FIGURE2_ROUTING_PREFLIGHT_SCOPED`;
- `PASS_SOURCE_FOURIER_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED`;
- `PASS_IMPLEMENTED_THREE_POINT_FLOW_C3_INSERTION_MANIFEST_SCOPED`.

Status at this commit: prospective freeze before any Figure-2 tensor-contraction output is inspected.

## PURPOSE

Freeze the exact tensor-index and single-scale-line interface needed to assemble the baseline Figure-2 EH/ghost three-point flow at fixed loop momenta, with C3 disabled, before quadrature.

This substep validates contraction assembly only. It does not yet integrate the loop and cannot pass Lane A or SF055.

## INTERNAL GRAVITON EDGE OBJECT

For each nonzero oriented internal momentum `ell`, construct one orthonormal six-dimensional basis `B_ell={E_a(ell)}` of the Landau-transverse subspace

`K(ell)=ker F(ell)`.

Because `K(-ell)=K(ell)`, the **same stored tensor basis** `B_ell` is used at both endpoints of an edge carrying `ell` and `-ell`. Independently recomputing an SVD basis at the opposite endpoint is forbidden because an arbitrary basis rotation/sign would otherwise be mistaken for physics.

Restrict the source-Fourier EH two-point Hessian to this basis:

`H_ab(ell;lambda_2)=Gamma_EH^(2)[E_a(ell),E_b(ell)]`.

At k=1 define

`H0_ab(ell)=H_ab(ell;0)`,

`r(x)=(1-x)/x theta(1-x)`, `x=ell^2`,

`R_ab(ell)=H0_ab(ell) r(ell^2)`,

`G(ell)=[H(ell;lambda_2)+R(ell)]^{-1}`.

For eta_h=0 the frozen differentiated regulator is

`dotR(ell)=2 H0(ell)/ell^2` for `0<ell^2<1`,

and zero for `ell^2>1`.

The differentiated internal edge is represented by the single-scale bilinear

`S(ell)=G(ell) dotR(ell) G(ell)`.

The canonical q edge frozen in the routing preflight is the differentiated edge in every baseline topology. All other internal edges carry ordinary `G`.

## GRAVITON VERTEX ARRAYS

With external TT tensors fixed, construct vertex arrays directly from the already-passed source-Fourier EH generator.

### Tadpole T5

For external `(p1,h1),(p2,h2),(p3,h3)` and q-edge basis `E_a(q)`, define

`V5_ab = Gamma_EH^(5)[h1,h2,h3,E_a(q),E_b(q)]`

with incoming momenta `[p1,p2,p3,q,-q]`.

Canonical fixed-q contraction:

`I_T5 = (-1/2) sum_ab V5_ab S_ba(q)`.

### Bubble B43

For the frozen canonical `(p1,p2 | p3)` routing, let

`ell=q+p1+p2=q-p3`.

Use one stored basis for q and one for ell. Define

`V4_ab = Gamma_EH^(4)[h1,h2,E_a(q),E_b(ell)]`

at incoming `[p1,p2,q,-ell]`, and

`V3_cd = Gamma_EH^(3)[h3,E_c(q),E_d(ell)]`

at incoming `[p3,-q,ell]`.

The same edge basis is used across opposite endpoints. Canonical contraction:

`I_B43 = (+3) sum_abcd V4_ab S_ac(q) V3_cd G_db(ell)`.

Equivalent transpose/index placements are allowed only if demonstrated algebraically/numerically to give the same scalar under the stored endpoint convention; no post-output transpose choice is permitted.

### Graviton triangle T333

With frozen edges

`e12=q`, `e23=q-p2`, `e31=q+p1`,

construct one basis for each edge. Define

`V1_ac = Gamma_EH^(3)[h1,E_a(e12),E_c(e31)]`,

`V2_bd = Gamma_EH^(3)[h2,E_b(e12),E_d(e23)]`,

`V3_ef = Gamma_EH^(3)[h3,E_e(e23),E_f(e31)]`,

with signs of the incoming edge momenta exactly as frozen in the routing gate; endpoint tensors themselves use the common stored basis of the unoriented edge.

Canonical contraction:

`I_T333 = (-3) sum_abcdef V1_ac S_ab(e12) V2_bd G_de(e23) V3_ef G_fc(e31)`.

## GHOST EDGE / ARROW CONVENTION

For a ghost edge with oriented ghost momentum `ell`, use vector basis `e_i` and source-Fourier two-point matrix

`M_ij(ell)=Gamma_FP^(2)[c=e_j,bar c=e_i] = -ell^2 delta_ij`.

Define

`R_c(ell)=M0(ell) r(ell^2)`,

`G_c(ell)=[M(ell)+R_c(ell)]^{-1}`,

`dotR_c(ell)=2 M0(ell)/ell^2 = -2 I` for `0<ell^2<1`, zero above cutoff,

`S_c(ell)=G_c dotR_c G_c`.

Freeze the ghost-arrow orientation around the canonical triangle as

`e12: V1 -> V2`,

`e23: V2 -> V3`,

`e31: V3 -> V1`.

At each vertex the source `fp_h_vertex_fourier(ph,h,pc,c,barc)` is called with `pc` equal to the incoming momentum of the `c` leg at that vertex. With the routing note's incoming momenta this gives

- V1: `c` on incoming `q`, `bar c` on incoming `-(q+p1)`;
- V2: `c` on incoming `q-p2`, `bar c` on incoming `-q`;
- V3: `c` on incoming `q+p1`, `bar c` on incoming `-(q-p2)`.

The corresponding vertex matrices are stored with row = bar-c index and column = c index. The canonical ghost contraction is

`I_ghost = (+6) Tr[V1 S_c(e12) V2 G_c(e23) V3 G_c(e31)]`

using the frozen matrix orientation. Reversing the whole closed ghost loop is permitted only as an explicit equality control; it is not a second topology and does not change the +6 coefficient.

## EXTERNAL SYMMETRISATION

For every topology compute all six labelled permutations of the external `(p_i,h_i)` pairs by regenerating the frozen routing mechanically. The baseline topology contribution used later for projection/integration is the arithmetic average over those six labelled contractions unless the source projection convention requires an explicitly equivalent summed normalization; the choice `average vs source-normalized sum` must be resolved and frozen from the source before Eq. (14) comparison.

This pre-quadrature gate only requires that all six contractions are generated and their permutation relation is deterministic. It does not yet authorize selecting a normalization by matching Eq. (14).

## FIXED-Q POSITIVE CONTROLS

Use deterministic loop controls away from singular/cutoff boundaries:

- `qA=(0.23,-0.31,0.17,0.29)`;
- `qB=(0.41,0.12,-0.27,0.19)`.

Use the frozen unit symmetric external point and deterministic external TT polarizations `(0,1,2)` from the existing TT basis construction.

For each topology and q control require:

1. every source vertex call satisfies momentum conservation;
2. all required `G` and `S` matrices are finite;
3. all propagator inverse residuals are <= `1e-10`;
4. contraction scalar is finite;
5. contraction is invariant within `1e-9*(1+|I|)` under simultaneous orthogonal basis rotations applied consistently at both endpoints of each internal graviton edge;
6. recomputing an opposite endpoint with an independently rotated basis **without** transport must be caught by the negative-control harness rather than silently accepted;
7. for the ghost triangle, full-loop arrow reversal gives the same scalar within `1e-9*(1+|I|)` after consistent transposition/reversal of all ghost matrices.

No nonzero requirement is imposed topology-by-topology: a symmetry-allowed exact or accidental zero at one frozen control is not by itself failure. At least one of the two q controls must yield a nonzero finite value `>|1e-12|` for each topology before that topology is considered numerically exercised.

## NEGATIVE CONTROLS

The checker must reject at least:

- TT-only 5D graviton internal basis;
- independently recomputed/oppositely rotated endpoint basis with no transport;
- replacing `S=G dotR G` by `G dotR`;
- placing the single-scale insertion on a noncanonical edge while leaving the routing/regulator bookkeeping unchanged;
- omitting one ordinary propagator in bubble or triangle;
- wrong transpose/order in the ghost matrix chain;
- wrong ghost-arrow `pc` assignment at one vertex;
- wrong inherited topology coefficient;
- using a scalar identity graviton regulator instead of `H0 r`.

## PASS

`PASS_A3_2_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_SCOPED`

only if all fixed-q positive controls and the frozen negative-control harness pass before quadrature output is inspected.

## FAIL

`FAIL_A3_2_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_SCOPED`

if the source-closed object is constructible but one or more frozen contraction controls fail after implementation bugs are excluded without changing the frozen physical object.

## BLOCKED

`BLOCKED_A3_2_TENSOR_CONTRACTION_OBJECT`

if a required source-defined index/arrow object cannot be instantiated without an additional unsupported convention.

## INTERPRETATION CEILING

Passing this gate validates fixed-q tensor contraction assembly only. It does not validate quadrature, Eq. (14), Lane A, SF055, any C3 beta function, fixed point, or physical matching selector.
