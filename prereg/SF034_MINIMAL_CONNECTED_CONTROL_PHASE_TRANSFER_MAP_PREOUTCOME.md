# SF034 — minimal connected control-phase transfer map — PREOUTCOME

Date: 2026-09-15
Inherited authoritative recovery head: `26b342cf51a3e67b7f57398111e3d1e98315510e`.

## PURPOSE

Supply the **minimum explicit operational model content** required by SF033 to decide whether the dominant `tau`-linear connected nuisance can be shared between the science configuration and the delete-A null-control configuration without post-hoc assumption.

This gate does not change the gravitational dynamics, branch geometry, `C3` readout, SF025/SF027 quantum-law fibre, or parent RQIRCG authority.

## INDEPENDENT MOTIVATION

The existing physical readout is the third Boolean/Mobius connected cumulant

`C3=Log K_111-Log K_110-Log K_101-Log K_011+Log K_100+Log K_010+Log K_001`.

Therefore any diagonal register/control phase polynomial of Boolean degree 0, 1 or 2 is annihilated exactly by `C3`. The lowest-degree diagonal register nuisance that can generate an additive connected `tau`-linear phase is cubic in the branch projectors.

This algebraic fact motivates the control model **before** evaluating its transferability consequence.

## RETAINED SCIENCE OBJECT

Keep the SF028B/SF029–SF033 motional/gravitational protocol unchanged:

`3 branch qubits + 4 motional bodies -> COM-closed branch-conditioned preparation -> free Newtonian/EIH evolution -> inverse recombination -> trace motion -> qubit tomography`.

The science setting uses the inherited A displacement amplitude.

The delete-A control changes only the A motional displacement amplitude to zero and updates the recoil-body displacement to preserve exact COM closure. The branch qubit A remains present in the same superposition and is not removed, projected, reset or relabelled.

## EXPLICIT EFFECTIVE CONTROL PARAMETER

Define `lambda_A` as the A-displacement control amplitude:

- science: `lambda_A=1`;
- delete-A null: `lambda_A=0`.

At the effective control level,

`U_prep(lambda_A)=sum_s |s><s| tensor T_s(lambda_A)`,

where only the A motional displacement and its compensating D displacement depend on `lambda_A`; B/C branch translations and the register basis are unchanged.

`U_read(lambda_A)=U_prep(lambda_A)^dagger`.

This is an implementation-level refinement of the already-authorized branch-conditioned translation map, not a new gravitational interaction.

## EXPLICIT REGISTER NUISANCE GENERATOR

During the free/readout phase allow the most general diagonal three-qubit control Hamiltonian through Boolean degree 3:

`H_reg/hbar = c0 + cA nA + cB nB + cC nC + cAB nA nB + cAC nA nC + cBC nB nC + zeta nA nB nC`,

with `nI=|1><1|_I`.

The coefficients are operational/control parameters, not gravitational couplings.

### Baseline control-separable model M0

Freeze the hypothesis

`partial H_reg / partial lambda_A = 0`.

Equivalently all `cS`, including `zeta`, are properties of the retained register/control phase evolution and are unchanged when only the motional displacement amplitude `lambda_A` is switched from 1 to 0.

This separability is **new prospective operational model content**. It is not inherited from SF028B and must not be described as experimentally established.

### Mandatory adversarial model M1

Also evaluate the smallest amplitude-dependent countermodel

`zeta(lambda_A)=zeta0+zeta1 lambda_A`,

with all lower-degree coefficients arbitrary.

M1 is a falsifier for perfect transferability: delete-A can measure `zeta0` but cannot by itself determine `zeta1`.

## REQUIRED ANALYTIC CHECKS

A1. Compute the exact third Boolean difference of every monomial `1`, `nI`, `nI nJ`, `nA nB nC`.

A2. Show whether the lower-degree register phases cancel from `C3` exactly.

A3. Derive the register contribution to `Theta3` under M0 for science and delete-A.

A4. Verify that the inherited delete-A **gravitational** connected terms remain zero while the retained register nuisance need not vanish.

A5. Derive the M1 science-minus-control residual and determine whether delete-A alone identifies it.

A6. State which variables are held fixed and which are changed between science and control.

## TRANSFER-MAP ELEMENTS TO SCORE

SF033 required six elements. SF034 may receive transfer-map credit only if it explicitly supplies:

1. nuisance-generating operation — `H_reg`;
2. action on science — `lambda_A=1` with full `H_reg`;
3. action on delete-A — `lambda_A=0` with the same register and `H_reg` under M0;
4. equality reason — the prospectively stated control-separability condition;
5. fixed-vs-changed variables — register Hamiltonian/readout/time fixed, only A/D motional transport changed;
6. falsification condition — nonzero `zeta1` or any measured/register-model dependence of the cubic connected phase on `lambda_A`.

## SOURCE / REALIZATION ROLE

External quantum-control literature may be used only to establish that state-dependent motional control and effective higher-order register interactions are physically realizable classes. No particular trapped-ion, superconducting, atomic, mechanical or other hardware implementation is imported as RQIRCGSF apparatus authority.

The scientific result of SF034 must follow from the frozen effective model above, not from analogy to another platform.

## DECISION RULE

### PASS WITH EXPLICIT MODEL SCOPE

`CONNECTED_CONTROL_PHASE_TRANSFER_MAP_DERIVED_UNDER_CONTROL_SEPARABILITY_SCOPED`

requires:

- exact Boolean cancellation of all diagonal degree <=2 register phases;
- exact survival of the cubic connected phase;
- equality of that cubic nuisance between science and delete-A under M0;
- exact inherited gravitational null for delete-A;
- all six SF033 transfer-map elements supplied;
- explicit retention of M1 as the transferability falsifier.

### BLOCKED

`BLOCKED_CONTROL_PHASE_MAP_NOT_CLOSED`

if the frozen effective model does not actually determine the connected nuisance in both configurations or cannot keep the gravitational null separate from the control phase.

### FAIL

`MINIMAL_CONTROL_SEPARABILITY_DOES_NOT_TRANSFER_CONNECTED_NUISANCE_SCOPED`

if even under M0 the frozen operations yield different connected register nuisance coefficients between science and delete-A.

### INVALID

Any post-result change to `C3`, the delete-A definition, the register basis, the degree-3 nuisance basis, the M0 separability statement, or the M1 falsifier requires a new preregistration.

## INTERPRETATION CEILING

A PASS would establish an **explicit effective implementation class** in which SF032 null-control calibration is physically mapped and exactly transferable at the model level.

It would not establish that a real laboratory device satisfies M0, that `zeta1=0` experimentally, that the required phase precision is achievable, or that the operational model is unique.

It would not authorize a successor quantum residual, quantum matching coefficient, quantum `chi_ABC`, new physics or parent RQIRCG promotion.

Retain:

`MODEL_LEVEL_TRANSFERABILITY != EXPERIMENTAL_TRANSFERABILITY`.

Retain:

`CONTROL_CALIBRATION != DEVICE_VALIDATION`.
