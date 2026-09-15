# SF045 — Lorentzian C3 matching bridge authority audit

Date: 2026-09-15
Preregistration: `d24f67663ee48d15e15c221f94c56717c86371ab`.

## Primary sources audited

1. Baldazzi, Falls, Kluth, Knorr, `Robustness of the derivative expansion in Asymptotic Safety`, arXiv:2312.03831 (current arXiv version inspected 2026-09-15).
2. Pawlowski, Reichert, Wessely, `Self-consistent graviton spectral function in Lorentzian quantum gravity`, arXiv:2507.22169.
3. Assant, Litim, Reichert, `Spectral Functions of Lorentzian Quantum Gravity`, arXiv:2606.19321.
4. Knorr, Ripken, Saueressig, `Form Factors in Asymptotically Safe Quantum Gravity`, arXiv:2210.16072.
5. Bern, Kosmopoulos, Zhiboedov, `Gravitational Effective Field Theory Islands, Low-Spin Dominance, and the Four-Graviton Amplitude`, arXiv:2103.12728.
6. Bern, Chi, Dixon, Edison, `Two-Loop Renormalization of Quantum Gravity Simplified`, arXiv:1701.02422.
7. Dunbar, Godwin, Jehu, Perkins, `Loop Amplitudes in an Extended Gravity Theory`, arXiv:1711.05526.

## Target-element audit

### T1 Lorentzian physical observable

PASS in a broad sense.

arXiv:2507.22169 supplies a self-consistent graviton spectral function in a physical mass-shell renormalization scheme, with a massless graviton peak and continuum, and explicitly motivates scattering applications.

arXiv:2606.19321 computes Lorentzian graviton spectral functions and a quantum effective action through quadratic order in curvature.

Thus Lorentzian, on-shell-oriented asymptotic-safety observables now exist.

### T2 Cubic-curvature / Goroff-Sagnotti observable

NOT CLOSED.

The 2026 Lorentzian effective action is explicitly reported only through quadratic curvature. No audited source computes the pure-gravity Lorentzian `C^3` form factor, its three-graviton all-equal-helicity vertex, or the induced four-graviton amplitude from the UV-safe essential trajectory.

### T3 UV-safe trajectory to target observable

NOT CLOSED.

Baldazzi et al. give the essential action coordinate

`Gamma_k superset G_C3(k) int sqrt(g) C^3`

and define `g_C3=k^2 G_C3`. Their unique UV-safe separatrix predicts the infrared integration constant in the displayed truncation.

But the Lorentzian spectral-function calculations do not ingest that same `G_C3(k)` trajectory into a cubic-curvature on-shell observable.

### T4 Low-energy physical EFT matching

PARTIAL AS TWO HALVES, NOT A CLOSED CHAIN.

Amplitude/EFT literature independently establishes that the parity-even `R^3` operator changes physical graviton amplitudes. SF025 records a nonzero four-graviton insertion in an explicit convention.

Therefore the low-energy target coordinate is physical and observable.

What is missing is the first-principles asymptotic-safety computation connecting its UV-safe essential trajectory to that amplitude coefficient.

### T5 Regulator/scheme independence

NOT CLOSED.

Baldazzi et al. explicitly investigate regulator dependence. Their representative `A=-3.988e-6` belongs to a finite derivative expansion and a technical regulator choice. More importantly, the same paper finds that its low-energy quantum coefficient does not reproduce the known perturbative two-loop coefficient and states that an infinite derivative expansion may be required.

The physical Lorentzian spectral program improves the observable framework but has not yet demonstrated regulator cancellation for the cubic-curvature target.

## Current-literature check through 2026-09-15

Targeted current searches for Lorentzian/asymptotic-safety `C^3`, `Riemann^3`, Goroff-Sagnotti and four-graviton amplitude calculations found no primary work closing the target bridge beyond the sources above.

The newest directly relevant Lorentzian source located, arXiv:2606.19321, stops at quadratic curvature.

## Structural conclusion

Two independently real half-bridges exist:

`UV-safe essential trajectory -> truncation-level G_C3(k)`

and

`physical R^3 coefficient -> nonzero on-shell graviton amplitude`.

But the composition map

`G_C3^AS(k) -> regulator-independent Lorentzian physical R^3 amplitude coefficient`

has not been computed in the audited literature.

Therefore the target is not a missing generic principle. It is a missing explicit vertex/amplitude calculation plus regulator/truncation closure.

## Important normalization observation for next gate

The Baldazzi action convention is explicit:

`Gamma_k superset G_C3 C^{rho sigma}_{ mu nu} C^{mu nu}_{ alpha beta} C^{alpha beta}_{ rho sigma}`.

SF025 uses

`delta Gamma = epsilon^2 delta b kappa^2 I3`,

`I3=int sqrt(-g) R_ab^{ cd} R_cd^{ ef} R_ef^{ ab}`,

with `kappa^2=32 pi G`.

On flat-space vacuum external graviton states, Ricci curvature vanishes and Weyl equals Riemann, so the operator directions coincide on shell. This suggests a separately auditable action-coordinate normalization map between `G_C3` and `b`; it does not establish regulator independence of the asymptotic-safety prediction.
