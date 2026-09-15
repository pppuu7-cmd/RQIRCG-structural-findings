# SF055A3Q3 — independent two-point beta_mu projector cross-check

Date: 2026-09-16
Status: outcome-independent source cross-check written while the Q3 workflow is queued.

## PRIMARY / INDEPENDENT SOURCES

Parent source:

N. Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016v2.

Independent detailed derivation:

D. Denz, J. M. Pawlowski, M. Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, Eur. Phys. J. C 78, 336 (2018), Appendix E.

Public full text:

`https://pmc.ncbi.nlm.nih.gov/articles/PMC6438657/`

## CROSS-CHECK

Appendix E states for the transverse-traceless graviton two-point flow at `p^2=0`:

`partial_t mu = (eta_h(0)-2) mu + (32 pi / 5) Flow_TT^(hh)(0)`.

The frozen SF055A3Q3 projector is

`Flow_TT_mass(0) = (1/5) sum_(a=0)^4 Flow^(2)(0)[E_a,E_a]`

with source two-point normalisation

`K_EH = 1/(32 pi)`.

Therefore at `eta_h=0`

`Flow_TT_mass/K_EH - 2 mu`

`= (32 pi / 5) sum_a Flow^(2)[E_a,E_a] - 2 mu`,

which matches the independently published TT mass-flow normalisation once `Flow_TT^(hh)` is identified with the complete TT projector trace.

Thus the Q3 factor `1/5` and `1/K_EH=32 pi` are independently source-supported and were not inferred from the frozen Eq. (14) numeric beta_mu target.

## INTERPRETATION CEILING

This is a normalization cross-check only. It does not establish the Q3 terminal result, perform loop quadrature, reproduce the Eq. (14) number, terminalize Lane A/SF055, or authorize C3 output.