# SF029 — robustness derivation and authority notes

Date: 2026-09-15
Preregistration: `ee392560debda35c0fbe51ca65112d1939fb3cfb`.
Executed script: `scripts/sf029_checks.py`, commit `2373f6baca6a77d169553b09fd6ed89f1d7e1170`.
Canonical raw projection: `results/raw/SF029_CHECKS.json`, commit `fc11740ea476253b6755d2af90a0cd763ee6ee36`.
Local executed script SHA-256: `6dd62123bc8c523fa8731a596ce2e59447d67a6f13936851bf46e48c75bc7b94`.

## 1. Object identity

SF029 does not alter the SF028B physical readout.

The object remains the reduced three-qubit connected coherence after one common COM-closed branch preparation, all-body free evolution, exact inverse preparation/recombination, trace over motion, and qubit tomography.

The retained leading formulas are

`Theta3^N = -(T/hbar) Delta3[V_N] + (T^3/(12hbar)) Delta3[A_N] + ...`,

`Gamma3^N = (sigma^2 T^2/(2hbar^2)) Delta3[Q] + ...`,

`Delta_1PN Theta3 = -(T/hbar) Delta3[V_static^1PN] + ...`.

No open action is used as the output object.

## 2. Frozen new nuisance grid

New finite-R cells:

`R/ell = {30,40,60,80,120,160,250,400,800}`.

Packet widths:

`sigma/ell = {1/200,1/100,1/50,1/25,1/20}`.

Dimensionless times:

`tau = T/sqrt(ell^3/(Gm)) = {1/100,1/50,1/20,1/10,1/5}`.

Spherical-radius applicability values:

`rho/ell = {0,1/200,1/100,1/50,1/20}`.

The inherited branch geometry, `M_D=5m`, COM closure and readout were unchanged.

## 3. Exact controls

For every new R cell, deleting any one branch displacement (`A`, `B`, or `C`) gives exact rational zero for

- `Delta3 V_N`;
- `Delta3 A_N`;
- `Delta3 V_static^1PN`;
- `Delta3 Q`.

All delete-one-label controls therefore pass exactly.

The signs over the full new R grid are stable:

- `Delta3 A_N < 0` in every cell;
- `Delta3 Q < 0` in every cell;
- `Delta3 V_static^1PN > 0` in every cell.

No sign-crossing nuisance cell was found.

## 4. Finite-R hierarchy

The exact source-only limits inherited from SF028B are

`Delta3 A_N(infinity) = -82/616005 = -1.3311580263147214e-4`,

`Delta3 V_static^1PN(infinity) = 2/945 = 2.1164021164021165e-3`

in the corresponding dimensionless coefficient units.

Decision-relevant finite-R values are:

| R/ell | Delta3 V_N | Delta3 A_N | Delta3 V_static^1PN | frac A error | frac 1PN error | epsilon_app |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | -1.2410122806e-4 | -1.2576576828e-4 | 1.6088098132e-3 | 5.52e-2 | 2.398e-1 | 7.71385e-2 |
| 40 | -2.4436077329e-5 | -1.3148777371e-4 | 1.8003903731e-3 | 1.223e-2 | 1.493e-1 | 1.35727e-2 |
| 60 | -3.3555877206e-6 | -1.3284856606e-4 | 1.9807147976e-3 | 2.008e-3 | 6.411e-2 | 1.69413e-3 |
| 80 | -9.1269578525e-7 | -1.3303771928e-4 | 2.0425049356e-3 | 5.866e-4 | 3.492e-2 | 4.46851e-4 |
| 120 | -1.5750132275e-7 | -1.3310153369e-4 | 2.0847328088e-3 | 1.072e-4 | 1.496e-2 | 7.55499e-5 |
| 160 | -4.6825312028e-8 | -1.3311145960e-4 | 2.0989242159e-3 | 3.263e-5 | 8.258e-3 | 2.23092e-5 |
| 250 | -7.3709687541e-9 | -1.3311510394e-4 | 2.1093914438e-3 | 5.249e-6 | 3.313e-3 | 3.49436e-6 |
| 400 | -1.0799848261e-9 | -1.3311569897e-4 | 2.1137018589e-3 | 7.787e-7 | 1.276e-3 | 5.10945e-7 |
| 800 | -6.5325326219e-11 | -1.3311579630e-4 | 2.1157349544e-3 | 4.754e-8 | 3.152e-4 | 3.08759e-8 |

Here

`epsilon_app(R)=|Delta3 V_N|/|Delta3 V_static^1PN|`.

For a physical weak-field parameter

`epsilon_PN = Gm/(c^2 ell)`,

the finite-R Newtonian apparatus `O(T)` term is larger than the 1PN `O(T)` term whenever

`epsilon_PN < epsilon_app(R)`.

This is a crossover relation, not a chosen experimental parameter.

The frozen grid shows that large R can make the Newtonian apparatus term arbitrarily small while the ordinary 1PN source term approaches a nonzero source-only limit. However the R needed for a requested systematic fraction depends on the intended precision and cannot be selected post hoc as a new scientific gate result.

Descriptively, on this frozen grid the 1PN apparatus correction first falls below:

- 10% at `R=60 ell`;
- 5% at `R=80 ell`;
- 2% at `R=120 ell`;
- 1% at `R=160 ell`;
- 0.5% at `R=250 ell`;
- 0.2% at `R=400 ell`.

These are geometry-specific calibration landmarks, not universal design requirements.

## 5. Large-R diagnostic slopes

The preregistration allowed asymptotic slopes only as diagnostics, not as theorem replacements.

Using successive large-R intervals gives effective powers:

### Newtonian apparatus connected coefficient `|Delta3 V_N|`

- `160 -> 250`: `p = 4.143`;
- `250 -> 400`: `p = 4.086`;
- `400 -> 800`: `p = 4.047`.

### Apparatus correction to Newtonian feedback `|Delta3 A_N - Delta3 A_N(infinity)|`

- `160 -> 250`: `p = 4.094`;
- `250 -> 400`: `p = 4.060`;
- `400 -> 800`: `p = 4.034`.

### Apparatus correction to static 1PN coefficient `|Delta3 V_1PN(R)-Delta3 V_1PN(infinity)|`

- `160 -> 250`: `p = 2.047`;
- `250 -> 400`: `p = 2.030`;
- `400 -> 800`: `p = 2.017`.

This is numerically consistent with the analytic SF024 multipole hierarchy:

- connected Newtonian apparatus contamination `O(R^-4)`;
- mixed source-source-apparatus 1PN contamination `O(R^-2)`.

The finite grid does not replace that analytic derivation.

## 6. Short-time validity lane

For each branch and R cell, the executed script computes:

`eta_disp = [max leading displacement]/d_min`,

`eta_H = tau^2 lambda_H`,

where `lambda_H` is the largest absolute eigenvalue of the symmetric mass-normalized Newtonian Hessian.

The preregistered control thresholds were

`eta_disp <= 0.02`,

`eta_H <= 0.05`.

Every `tau <= 0.1` cell passes, as required for preregistered PASS.

In fact every frozen `tau=0.2` cell also passes. The worst observed values at `tau=0.2` are approximately

`eta_disp = 8.63e-4`,

`eta_H = 6.20e-3`,

both well inside the prospectively fixed control region.

This extends the internally controlled short-time window over the full tested grid, but does not prove exact all-time validity.

The feedback crossover is

`epsilon_fb(R,tau)=|Delta3 A_N| tau^2/(12 |Delta3 V_static^1PN|)`.

At `tau=0.1`, it ranges from `6.51e-5` at `R=30` to `5.24e-5` at `R=800`. Thus ordinary self-consistent Newtonian feedback is larger than the 1PN comparator whenever `epsilon_PN` lies below this crossover. Again this is baseline hierarchy, not new physics.

## 7. Packet-width lane

At inherited `R=100 ell`, the frozen width grid has

`eta_sigma = sigma/d_min` from `1.67e-3` to `1.67e-2`.

The executed leading formula gives the identical value

`Gamma3/(sigma^2 T^2/hbar^2) = -6.654245028696249e-5`

for every width cell.

Thus `Gamma3` follows the prospectively frozen `sigma^2` scaling exactly at this order. The connected cumulant sign remains negative; this is not a negative probability or a negative decoherence rate.

No width was selected for making the cumulant small.

## 8. Finite-size applicability lane

The largest frozen spherical support radius is

`rho=ell/20`.

The minimum branch-center separation on the full grid is `3 ell`, leaving a center-level nonoverlap margin `d_min-2rho >= 2.9 ell`.

No finite-size coefficient was fitted or invented.

The scope is supported by standard PN/EFT authorities:

1. W. D. Goldberger and I. Z. Rothstein, *An Effective Field Theory of Gravity for Extended Objects*, arXiv:hep-th/0409156. Their EFT power counting shows decoupling of spinless internal structure through low PN orders and places leading conservative tidal finite-size operators at order `v^10` in the compact-object counting.
2. G. Schäfer and P. Jaranowski, *Hamiltonian formulation of general relativity and post-Newtonian dynamics of compact binaries*, arXiv:1805.07240. The review explicitly uses point-mass dynamics through high PN orders and treats tidal interactions as separate higher-order structure.

These authorities support the inherited **1PN monopole applicability ceiling**. They do not model laboratory material stresses, branch-generation hardware, exact rigid-body Gaussian tails, or tidal deformation of a specific apparatus.

Therefore the finite-size lane passes only in the declared leading-semiclassical nonspinning spherical/monopole scope. A full extended-body quantum protocol remains a separate model, not hidden inside this gate.

## 9. Result against frozen decision rule

All preregistered exact negative controls pass.

No sign reversal occurs in `Delta3 A_N`, `Delta3 Q`, or `Delta3 V_static^1PN` on the full new R grid.

The preregistered `tau<=0.1` validity condition passes for every R cell; the full `tau<=0.2` grid also remains inside the fixed bounds.

The frozen spherical-radius family remains inside the declared center-level nonoverlap/1PN monopole applicability scope.

Therefore the preregistered terminal classification is

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`.

## 10. Structural conclusion

The important robustness result is not merely that coefficients preserve their sign.

The known-physics baseline has **parametrically different nuisance scalings**:

`Newtonian finite-R apparatus O(T) ~ R^-4`  (asymptotic diagnostic consistent with SF024),

`Newtonian feedback O(T^3) -> nonzero source-only limit, apparatus correction ~ R^-4`,

`1PN O(T) -> nonzero source-only limit, apparatus correction ~ R^-2`,

`visibility connected cumulant ~ sigma^2 T^2` at the retained order.

This creates explicit crossover surfaces rather than a single nuisance amplitude.

A nonzero raw connected coherence is therefore not itself a discriminator. The same-protocol baseline must be modeled or independently calibrated across its distinct R/T/sigma scalings.

## Claim ceiling

No laboratory feasibility, exact all-time channel, exact extended-body quantum dynamics, new quantum law, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC`, or new physics is established.