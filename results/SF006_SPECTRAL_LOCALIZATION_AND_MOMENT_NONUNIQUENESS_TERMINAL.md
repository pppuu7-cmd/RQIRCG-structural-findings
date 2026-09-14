# SF006 — spectral localization and moment-nonuniqueness gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / structural mathematical witness / no `chi_ABC` evaluation**

## Outcome lock

`chi_ABC` remained embargoed throughout SF006.

The gate was preregistered before evaluation in `prereg/SF006_SPECTRAL_LOCALIZATION_AND_MOMENT_NONUNIQUENESS_GATE.md`.

## Lane A — exact positive-moment witness

Freeze the two positive normalized measures from the preregistration:

`mu_A = delta(x-1)`

and

`mu_B = (1/2) delta(x-1/2) + (1/2) delta(x-3/2)`.

For both measures,

`m_0 = Integral dmu = 1`.

Their first moments are also identical:

`m_1(A) = 1`,

`m_1(B) = (1/2)(1/2) + (1/2)(3/2) = 1`.

The preregistered decisive second moment differs:

`m_2(A) = 1`,

`m_2(B) = (1/2)(1/2)^2 + (1/2)(3/2)^2 = 1/8 + 9/8 = 5/4`.

Hence two positive spectral measures can agree exactly on normalization and the first calibrated moment while disagreeing on the next matching datum.

Lane classification:

`EXACT_POSITIVE_MEASURES_SHARE_LOWER_MOMENTS_AND_DIFFER_AT_HIGHER_MOMENT`.

## Lane B — relation to EFT/dispersive matching

The witness is deliberately abstract. It does not assert that every gravitational Wilson coefficient is literally a moment of the one-variable measure above.

Its role is narrower: whenever low-energy coefficients are represented by positive/dispersive spectral integrals or sums over massive states, finite low-energy information constrains moments or weighted integrals of microscopic spectral data. Different positive spectra can share those lower weighted integrals while differing in higher ones.

This is structurally consistent with gravitational dispersive analyses in which higher-curvature coefficients are bounded in terms of a mass gap and other Wilson/spectral data rather than uniquely fixed by the massless graviton normalization alone.

Representative comparator:

- Z. Bern, D. Kosmopoulos, A. Zhiboedov, *Gravitational Effective Field Theory Islands, Low-Spin Dominance, and the Four-Graviton Amplitude*, arXiv:2103.12728.

Lane classification:

`FINITE_IR_MATCHING_CONSTRAINS_WEIGHTED_SPECTRAL_DATA_NOT_FULL_MICROSCOPIC_MEASURE`.

## Lane C — finite information versus complete spectral information

The exact witness is a truncated moment problem. Positivity does not convert finitely many moments into a unique positive measure.

The two-measure construction already proves nonuniqueness for the frozen `m_0,m_1` calibration. More generally, a finite collection of low-energy observables/bounds cannot be silently identified with specification of a complete spectral density, UV S-matrix, microscopic Hamiltonian, or state-generating rule.

A unique microscopic reconstruction would require additional information such as:

- enough moments/analytic data to solve a determinate moment problem in the relevant class;
- a microscopic spectrum and couplings;
- a state-counting/generating law;
- a boundary/fixed-point principle that determines the spectral density;
- or another independently motivated rule of equivalent information content.

Lane classification:

`FINITE_POSITIVE_MOMENT_DATA_ARE_NOT_COMPLETE_GENERATING_DATA`.

## Lane D — RQIR-facing localization

SF001-SF005 progressively moved the missing selector from an arbitrary connected channel to a nonlinear generator, then to its homogeneous invariant sector, then to UV/Wilson matching data.

SF006 sharpens this once more:

`consistency + finite IR calibration + positivity`

is not enough to reconstruct

`microscopic spectral measure / equivalent generating data`.

Therefore the next RQIR audit must search for an actual rule that fixes physical state/spectral content, not another inequality, positivity requirement, covariance condition, or finite collection of low-energy calibration identities.

The missing object may be represented schematically as

`S_micro = {spectrum, couplings, state/boundary rule}`

or any mathematically equivalent complete generating datum from which the relevant Wilson coefficients follow.

Lane classification:

`MISSING_OBJECT_LOCALIZED_TO_MICROSCOPIC_SPECTRAL_OR_EQUIVALENT_GENERATING_DATA`.

## Terminal decision

The preregistered falsifier is exactly satisfied:

`FINITE_IR_MOMENTS_DO_NOT_SELECT_MICROSCOPIC_SPECTRAL_MEASURE`.

This is a scoped mathematical structural result. It is not a theorem that all quantum-gravity UV data can be represented by a positive one-dimensional moment measure.

## New scientific fact for this programme

The nonlinear-selection problem cannot be solved merely by repeatedly strengthening finite low-energy consistency gates if each new gate only fixes or bounds another finite set of moments of an otherwise free microscopic completion.

A successful principle must either:

1. determine the microscopic generating data themselves, or
2. prove that all nonlinear observables of interest are independent of those data.

The second possibility has already been disfavored structurally by SF003-SF005 because genuine higher-order invariant/on-shell amplitude directions survive and alter nonlinear dynamics.

## Exact next admissible gate

Audit the frozen RQIR requirements for a **latent microscopic selector**.

The audit must distinguish:

- operational/relational observability requirements;
- consistency and positivity conditions;
- finite low-energy calibration/holdout requirements;

from a genuinely stronger rule specifying the physical spectrum, microscopic state space, measure, boundary condition, fixed-point data, or equivalent generating principle.

If no such rule exists in frozen RQIR, the structural-findings branch should record that fact before proposing any new microscopic axiom.
