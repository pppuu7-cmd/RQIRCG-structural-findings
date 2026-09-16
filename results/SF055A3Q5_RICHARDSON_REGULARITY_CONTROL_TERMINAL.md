# SF055A3Q5 derivative-regularity control - TERMINAL

Date: 2026-09-16
Freeze: `2a95bbfd78c651ff89435f71090ce42cb9ed8efd`.
Repository checker: `scripts/sf055a3q5_richardson_regularity_control.py`, latest implementation commit `0eddbd0e724f68d73ae3f5b286db8c4445f6c73d`.
Local raw: `results/raw/SF055A3Q5_RICHARDSON_REGULARITY_CONTROL_LOCAL.json`, commit `9311133edbc072afc0069645c1d0beb4c3ac98f7`.

## Classification

`BOSE_ROTATIONAL_SYMMETRY_DOES_NOT_IMPLY_P2_ANALYTICITY_SCOPED`.

This is a Q5 numerical-analysis control. It does not change the Q5 full-tensor science gate, its frozen stencil, or the original SF055A3 blocked baseline.

## Exact counterexample class

Use the already-authorized sharp-regulator scalar witness

`J_mu(p,u)=int_{|q|<1} d^4q/(2pi)^4 [max(1,|q+p u|^2)+mu]^-1`.

The ball, measure and integrand class are O(4)-covariant. For any unit u, rotations map the integral to the same scalar J_mu(|p|). Therefore the equal-weight sum over the three canonical Q4 shift directions is exactly three copies of the same invariant function. Group averaging cannot remove an invariant nonanalytic term merely by changing its direction.

## Shell coefficients

With `a=1+mu`, exact S^3 hemisphere moments are

`I1=int_hemi u dOmega_3=4pi/3`,

`I2=int_hemi u^2 dOmega_3=pi^2/4`,

`I3=int_hemi u^3 dOmega_3=8pi/15`.

The Q4 shell expansion gives

`J_mu(p)=J_mu(0)+c2 p^2+c3 |p|^3+O(p^4)`,

`c2=-1/[64 pi^2 a^2]`,

`c3=(8-5a)/[180 pi^3 a^3]`.

At mu=0.1:

`c2=-0.0013083830532326676`,

`c3=+0.0003365424329368007`.

For the equal-weight three-direction sum the cubic coefficient is

`3 c3=(8-5a)/[60 pi^3 a^3]`,

which is nonzero at the frozen mu. Thus complete rotational covariance and equal-weight treatment of the three canonical directions do **not** imply analyticity in p^2.

## Frozen Richardson consequence

For the generic positive-p expansion

`F(p)=F0+A p^2+B p^3+C p^4+...`,

the frozen estimator

`D(h)=[F(h)-F0]/h^2`,

`R_h=[4D(h)-D(2h)]/3`

gives exactly through this order

`R_h=A+(2/3)B h`.

The p^4 term cancels, but the `|p|^3` term leaves an O(h) bias. Therefore an O(h^4) truncation claim requires an additional regularity/cancellation theorem for the *full tensor projected flow*; it is not supplied by Bose/O(4) symmetry alone.

At the scalar control values and frozen h=1/32 the corresponding bias is

`7.011300686183349e-06`,

or about `0.535875%` of |c2|. This number is **not** an estimate of the gravitational baseline bias; it only shows that the allowed sharp-regulator regularity class can produce an effect larger than the 0.2% N-convergence threshold.

## Negative control

A signed combination with weights `(1,1,-2)` cancels the three identical rotated copies because its weights sum to zero. This demonstrates what cancellation would require: an additional coefficient relation. It is not a consequence of rotational or Bose symmetry itself.

## Executed checks

All 10 symbolic checks passed: exact hemisphere moments, c2/c3 formulae, nonzero c3 at mu=0.1, survival under equal-weight three-shift sum, exact Richardson formula, p4 cancellation, and the signed zero-sum negative control.

The local synchronous symbolic mirror produced raw SHA256 `2f07f6ee3afd22a2fc14241525abe952bc5db85588cc8a7b9a211905e965cce7`. It is a reproducibility control, not a GitHub Actions premise.

## New structural fact

`ROTATIONAL/Bose SYMMETRY` constrains the dependence to an invariant function of |p|, but `INVARIANT FUNCTION OF |p|` does not imply `ANALYTIC FUNCTION OF p^2` for a sharp moving-support regulator. The missing regularity information is dynamical/integrand-specific.

## Claim ceiling / next dependency

No claim is made that the full graviton sum has a nonzero |p|^3 coefficient. It may cancel after the actual tensor numerators/topology sum. Q5 must either demonstrate that cancellation directly or carry a truncation uncertainty that allows it. The full piecewise baseline run remains the active science calculation and C3 remains disabled.
