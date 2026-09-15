# SF035 — control-phase amplitude-dependence calibration — PREOUTCOME

Date: 2026-09-15
Inherited recovery commit: `e6684e775cd4cfe39809495ea3f694788a831b14`.

## PURPOSE

Test whether an explicit A-displacement amplitude ladder can separate the SF034 connected control-phase amplitude dependence from the **same known-gravity `C3` baseline**, without assuming `zeta1=0` and without adding or fitting any successor quantum-gravity residual.

## RETAINED PHYSICAL OBJECT

Keep the SF028B boundary-complete reduced-coherence protocol and the SF029–SF034 known-gravity/control interpretation.

At every amplitude setting preserve exact COM closure by scaling the A source displacement and its compensating D recoil displacement together.

No branch label, readout, R value, time definition, mass ratio or gravitational law is changed after this preregistration.

## FROZEN AMPLITUDE / GEOMETRY / TIME DESIGN

A-displacement amplitude:

`lambda_A in {0, 1/2, 1}`.

Apparatus distances:

`R/ell in {60,160,400}`.

Short-time values:

`tau in {0.05,0.10,0.20}`.

Total design: `3 x 3 x 3 = 27` science/control rows.

At `lambda_A=0`, the exact delete-A connected known-gravity basis must vanish.

At `lambda_A=1`, recover the existing SF029/SF030 coefficients.

## EXACT KNOWN-PHYSICS BASIS TO RECOMPUTE

For every `(lambda_A,R)` cell recompute from the original exact branch model:

`Delta3 V_N(lambda_A,R)`,

`Delta3 A_N(lambda_A,R)`,

`Delta3 V_static^1PN(lambda_A,R)`.

Do not interpolate the endpoints.

The phase-design columns are

`x_app = -Delta3 V_N(lambda_A,R) tau`,

`x_fb = [Delta3 A_N(lambda_A,R)/12] tau^3`,

`x_1PN = -Delta3 V_static^1PN(lambda_A,R) tau`.

For structural shape rank the nonzero `epsilon_PN` amplitude factor is omitted from `x_1PN`; it is a column scale, not a rank datum.

## FROZEN CONTROL-NUISANCE MODELS

### L1 — linear amplitude dependence

`zeta(lambda_A)=zeta0+zeta1 lambda_A`.

Add columns

`x_z0=tau`,

`x_z1=lambda_A tau`.

Full L1 design has five columns:

`[x_app,x_fb,x_1PN,x_z0,x_z1]`.

### Q2 — quadratic adversary

`zeta(lambda_A)=zeta0+zeta1 lambda_A+zeta2 lambda_A^2`.

Add

`x_z2=lambda_A^2 tau`.

Full Q2 design has six columns.

Q2 is a mandatory adversarial control; no post-result switch to a higher polynomial is allowed in SF035.

## FROZEN RANK / CONDITIONING PROCEDURE

Column-normalize every nonzero design column to unit Euclidean norm before singular-value rank/shape analysis.

Use numerical rank tolerance `1e-10 * s_max`.

Record singular values and normalized condition number.

### Classification

For each L1/Q2 model:

- `FULL_RANK_MODERATE` if full column rank and `kappa<=50`;
- `FULL_RANK_ILL_CONDITIONED` if full rank and `kappa>50`;
- `DEGENERATE` if rank deficient.

No scientific FAIL is inferred solely from a large condition number.

## MANDATORY ABLATIONS / FALSIFIERS

A1. Endpoint recovery: `lambda_A=0` gravity columns exact zero; `lambda_A=1` matches SF029 values.

A2. No-amplitude-lever negative control: restrict to `lambda_A=1`. Then `x_z0` and `x_z1` are exactly collinear, so L1 must be rank deficient. If not, implementation/rank logic is invalid.

A3. Delete-A + science only: restrict to `lambda_A in {0,1}` and record rank/conditioning. This tests whether the intermediate amplitude actually adds information.

A4. Single-R ablation: record rank at each fixed R with all lambda/tau values.

A5. Single-tau ablation: record rank at each fixed tau with all lambda/R values.

A6. Leave-middle-amplitude-out: compare `{0,1}` with `{0,1/2,1}` for L1 and Q2.

A7. Exact delete-one-label finite-difference controls remain zero when any source displacement amplitude is prospectively set to zero.

## DECISION RULE

### PASS L1

`LINEAR_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_SCOPED`

if L1 is full rank and the lambda=1 negative control is rank deficient as required.

### PASS Q2

`QUADRATIC_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_SCOPED`

if Q2 is also full rank on the full three-amplitude design.

### QUALIFIED

`AMPLITUDE_DEPENDENCE_IDENTIFIABLE_BUT_ILL_CONDITIONED_SCOPED`

if the relevant design is full rank but `kappa>50`.

### BLOCKED

`CONTROL_PHASE_AMPLITUDE_DEPENDENCE_DEGENERATE_WITH_KNOWN_GRAVITY_SCOPED`

if L1 is rank deficient on the full frozen design.

Q2 degeneracy does not revoke a valid L1 result; it limits the nuisance family that can be calibrated with this design.

### INVALID

Any post-result change to amplitude values, R/tau grid, nuisance polynomial degree, known-gravity basis, rank tolerance or observable requires a new preregistration.

## INTERPRETATION CEILING

A full-rank result establishes only structural calibration of the frozen effective nuisance family from the known-gravity protocol family.

It does not establish experimental phase precision, device stability, shot-noise requirements, actuator linearity outside the frozen model, a successor residual, a quantum matching coefficient, quantum `chi_ABC`, new physics or parent promotion.

Retain:

`AMPLITUDE_CALIBRATION != DEVICE_FEASIBILITY`.

Retain:

`KNOWN_PHYSICS_SUBTRACTION != QUANTUM_RESIDUAL_AUTHORITY`.
