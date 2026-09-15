# SF055B — independent verification of the common C3 vertex generator — PREOUTCOME

Date: 2026-09-15
Parent: active SF055 implementation contract.
Status: criteria frozen before the independent implementation is executed.

## WHY THIS CHECK EXISTS

The first prospectively frozen Lane-B implementation test produced:

- n=2 negative control PASS;
- all 125 n=3 SF052 components PASS with the frozen global factor 6;
- n=5 control PASS;
- the single frozen n=4 positive-control component exactly zero.

A post-outcome diagnostic at the same n=4 momenta found other TT components nonzero, so the original B2 positive control is classified as an accidental component null and remains INVALID. It is not changed or rescued.

SF055B does **not** retroactively convert that invalid control into a PASS. Its purpose is to test the common generator by a computationally independent extraction method before deciding whether the generator itself is trustworthy enough for later SF055 work.

## INDEPENDENT METHOD

Do not use the square-free/nilpotent polynomial algebra to compute the verification values.

For ordinary real amplitudes `epsilon_i`, evaluate directly at x=0 the metric jet

`g_mn = delta_mn + sum_i epsilon_i h_i,mn`,

`partial_a g_mn = sum_i epsilon_i p_i,a h_i,mn`,

`partial_a partial_b g_mn = sum_i epsilon_i p_i,a p_i,b h_i,mn`.

Using ordinary dense numerical linear algebra:

1. invert the numeric metric;
2. compute `sqrt(det g)`;
3. construct Christoffels;
4. compute `partial Gamma` using `partial g^{-1} = -g^{-1}(partial g)g^{-1}` and the analytic second metric derivatives;
5. construct Riemann, Ricci, scalar curvature and D=4 Weyl;
6. form the numeric scalar density `L(epsilon)=sqrt(g) Tr(C^3)`.

Extract the fully mixed n-leg derivative with the n-dimensional central sign sum

`D_n(h) = (2h)^(-n) sum_{s_i=+-1} (prod_i s_i) L(h s_1,...,h s_n)`.

Use frozen steps

`h1 = 0.04`, `h2 = 0.02`

and Richardson estimate

`D_R = (4 D_n(h2) - D_n(h1))/3`.

No nilpotent coefficient tables may enter the direct geometry calculation.

## FROZEN CONFIGURATIONS

### V2

Use the existing B0 two-leg momenta/polarizations from `scripts/sf055_c3_vertex_generator.py`.

Expected exact common-action coefficient from the first implementation: `0`.

PASS_V2: `|D_R| <= 1e-6`.

### V3

Use the SF052 unit symmetric momenta and TT polarization indices `(1,3,3)`.

Compare the independent `D_R` against the committed common-action generator value for this component.

PASS_V3: mixed relative/absolute error <= `5e-5 * (1+|target|)`.

### V4

Use the frozen B2 four-point momenta but TT polarization indices `(1,1,1,1)`. This is explicitly a post-outcome audit component, not a replacement for the invalid original B2 positive control.

PASS_V4: independent `D_R` agrees with the committed common-action generator value within `5e-5 * (1+|target|)`.

### V5

Use the original B3 five-point momenta and TT polarization indices `(0,1,2,3,4)`.

PASS_V5: independent `D_R` agrees with the committed common-action generator value within `2e-4 * (1+|target|)`.

The looser V5 tolerance is frozen because a 32-corner fifth mixed derivative has substantially stronger floating cancellation than V3/V4.

## GEOMETRIC CONTROLS

At every direct-evaluation corner require:

- `det(g) > 0`;
- finite inverse metric and density;
- Weyl trace `g^{ac} C_abcd` max norm <= `1e-9`;
- first-pair and second-pair Weyl antisymmetry max error <= `1e-9`.

Any violated geometric control is `INVALID_DIRECT_VERIFIER`, not evidence for or against the nilpotent generator.

## CLASSIFICATION

If V2–V5 and geometric controls pass:

`INDEPENDENT_DIRECT_GEOMETRY_VERIFIES_COMMON_C3_GENERATOR_SCOPED`.

If direct geometry is valid but one or more comparisons fail:

`COMMON_C3_GENERATOR_CROSS_IMPLEMENTATION_MISMATCH_SCOPED`.

If direct geometry controls fail:

`INVALID_DIRECT_C3_GENERATOR_VERIFIER_SCOPED`.

## INTERPRETATION CEILING

Even a PASS does not retroactively PASS the invalid B2 frozen positive control and does not by itself terminalize all SF055 calibration lanes. It would establish that the square-free generator's n=2/3/4/5 contracted outputs are independently reproducible by ordinary metric geometry plus finite-difference extraction at the stated configurations.
