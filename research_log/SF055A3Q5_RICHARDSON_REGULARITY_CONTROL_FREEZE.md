# SF055A3Q5 derivative-regularity control - prospective freeze

Date: 2026-09-16
Parent Q5 preregistration commit: `6a031dc34f67705ba355b40596513a91bfecd967`.
Status: implementation/numerical-analysis control inside Q5; not a new physical gate.

## Question
Does O(4) invariance plus the three canonical Bose-related shifted directions force the sharp-Litim projected scalar regularity class to be analytic in p^2 near p=0, so that the frozen Richardson cancellation can be assumed to have its smooth-even order? Or can an invariant |p|^3 term survive the symmetry average?

This question is frozen before executing the new symbolic/numerical control. It does not inspect Q5 full-tensor output, change the Q5 stencil, or authorize C3.

## Frozen counterexample class
Use the already-derived Q4 scalar denominator witness

`J_mu(p,u)=integral_{|q|<1} d^4q/(2pi)^4 / [max(1,|q+p u|^2)+mu]`,

with `mu=1/10` and unit vector u. The integration domain and measure are O(4)-invariant. Use the three canonical unit directions from Q4, all with equal magnitude p. No gravitational tensor numerator is imported.

Retain the prior small-p coefficients to be independently re-derived algebraically:

`J=J0+c2 p^2+c3 |p|^3+O(p^4)`.

Do not assume c3 vanishes. Determine it from the shell expansion.

## Tests
1. Derive c2 and c3 from explicit hemisphere moments; independently evaluate those moments symbolically.
2. Prove/verify that rotating u leaves J unchanged, so the equal-weight canonical three-shift Bose sum is exactly `3 J` in this counterexample class.
3. Therefore test whether its |p|^3 coefficient is zero or nonzero.
4. For a generic expansion `F=F0+a p^2+b |p|^3+c p^4+...`, derive the frozen estimator
   `R_h=[4(F(h)-F0)/h^2-(F(2h)-F0)/(2h)^2]/3`
   and its b-dependent leading bias.
5. Evaluate that bias for the scalar witness at frozen h=1/32; this is a numerical-analysis control only, not an estimate of the full gravitational bias.
6. Negative control: an explicitly chosen signed linear combination with weights summing to zero can cancel the rotated scalar witness. Record that such a cancellation is an additional coefficient relation, not a consequence of rotational/Bose symmetry alone.

## Pass / interpretation
PASS if a nonzero invariant |p|^3 coefficient survives the equal-weight three-direction sum and the frozen Richardson estimator has an O(h) bias for this allowed sharp-regulator witness.

Classification:
`BOSE_ROTATIONAL_SYMMETRY_DOES_NOT_IMPLY_P2_ANALYTICITY_SCOPED`.

A PASS does NOT establish a nonzero |p|^3 term in the full tensor flow. It establishes only that symmetry cannot be used as the theorem that removes it. Full tensor regularity/cancellation must be checked directly or included in an error bound.
