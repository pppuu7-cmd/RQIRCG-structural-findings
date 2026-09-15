# SF055A3 baseline derivative convergence audit - prospective diagnostic freeze

Date: 2026-09-16
Main authority read: 7898ae6aea08feaf2488f2b3c742f7a46d386fd4.
Executed branch: 1828aeb994265cb78691493a21bdd4f120a30d58; PR 16.
Run: 35019599951; aggregate job: 104590644553.
Aggregate artifact: 10421617496; ZIP SHA256: 85f0a9dd92d067ada9bbcccba8fbb3059d7545e4e039865cd26ff7b30ad10952.

## Provenance and scope
The run and its aggregate have already been inspected. All required input records are present; its result is BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED despite target_pass=true. This is NOT a pre-outcome re-registration of that run. It freezes only a post-run diagnostic analysis and new mathematical controls before their quantitative evaluation. Retain the failed convergence result. Do not rerun the expensive matrix, change its thresholds, choose a different derivative stencil from its observed target agreement, or enable C3.

The selected iteration asks: are the two unstable beta outputs independent problems, or propagated consequences of one inadequately resolved momentum derivative? What information is needed to repair its numerical validation without changing the physical model?

## Frozen inputs
Use the unchanged aggregate JSON, original reducer at the executed branch, source N_g and N_lambda, lambda_3=-7/10, and the same Gauss orders N=8,12,16,24. Read the preregistered source contract and programme hard-stop plan. An agreement-to-target test is NOT a convergence proof. Adjacent quadrature differences are diagnostics, not rigorous absolute error bounds.

## Analytic targets
1. Recompute D(h)=(F(h)-F(0))/h^2 and R(h)=[4 D(h)-D(2h)]/3 at h=1/32 from archived input values. In this notation F(p)=Flow_G(p^2). Recover the exact linear stencil weights.
2. Propagate deterministic perturbations of the three F values into R, beta_g and beta_lambda3. Derive a sufficient worst-case pointwise error budget conditional on certified input error bounds. Do not reinterpret N16-N24 differences as certified bounds.
3. Derive the Jacobian of (beta_g,beta_lambda3) with respect to (R,Flow_Lambda(0)). Identify the derivative-insensitive linear combination and verify it against the archived outputs. This is a diagnostic coordinate transformation, not a new selector or independent successful target.
4. Reproduce all original classifications without fitted factors. Keep finite-difference p=1 control separate from the derivative-at-zero benchmark.

## Boundary/regularity control, not a gravity model
Use the same denominator regularity class as the optimized regulator:
J_mu(p)=integral_{|q|<1} d^4q/(2*pi)^4 / [max(1,|q+p e1|^2)+mu], with mu=1/10.
Derive its leading small-p coefficient by an explicit shell calculation and independent split-domain integration. Compare to differentiating a finite set of interior quadrature nodes at p=0. Test whether finite-N differentiation and N->infinity commute. This scalar witness cannot by itself establish the exact size or sole cause of the full graviton-flow error.
Use p=1/8,1/16,1/32 and halved values as diagnostic controls only. No gravity derivative stencil will be changed. Derive any regulator-surface split geometrically from |q+p e1|=1, not from target fitting. Declare every used boundary convention. No claim of a new C3 result.

## Controls
- Stencil annihilates constants and p^4, reproduces the coefficient of p^2, and has the derived p^6 bias.
- Synthetic errors bounded by a common epsilon attain/satisfy the analytic worst-case amplification bound.
- The beta combination removes derivative perturbations exactly.
- Independent scalar shell quadrature agrees with the analytical leading coefficient as p decreases; p=0 normalization is known from the 4-ball volume.
- Finite-N interior differentiation is checked separately from the integrated derivative.
- Original raw file hash and run IDs are preserved; all new outputs are identified as locally executed diagnostics.

## Outcomes and locks
DIAGNOSTIC_PASS requires the mathematical identities and independent controls to pass, not the historical physics gate. Any failed numerical control is retained and bounded rather than silently tuned.
Historical Lane A/SF055 remain BLOCKED unless the ORIGINAL full criteria pass in an independently authorized, unchanged-scope implementation. This audit cannot grant that PASS. The programme verdict follows the frozen plan: MISSING_OBJECT_OR_CONTROL_BLOCKER_SCOPED when the indispensable baseline is not stabilized.
Any prospective replacement integration method requires explicit equivalence and same-threshold validation. Keep RHPI classical selection, SF025 physical matching freedom, state-vs-law distinction, independence firewall, and quantum chi_ABC embargo unchanged.
