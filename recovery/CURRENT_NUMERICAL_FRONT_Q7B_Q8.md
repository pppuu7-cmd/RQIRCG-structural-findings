# RQIRCGSF current numerical front — Q7B/Q8 addendum

Updated: 2026-09-16.

This file is a narrow addendum to `recovery/CURRENT_FRONT.md`; it does not replace parent/governance authority or rewrite any earlier terminal verdict.

## Newly terminal Q7B

Classification:

`PASS_Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_CONSTRUCTED_SCOPED`.

Prospective freeze: `7f4dec270e50d2c63427e3187daf06497c562b55`.

Executable diagnostic: `a2c837bedb481fd15b4d6e2930f3faab31e89786`.

Independent GitHub Actions verification:

- run `35145658603`;
- conclusion `success`;
- artifact `10466641953`;
- digest `sha256:cc5af23db1f340258944e9ba68163a9c589418c9642eb70ce1a3eb7cc6e0ad83`.

Terminal result:

`results/SF055A3Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_TERMINAL.md`.

Exact retained numerical facts:

- `|d beta_g/dF32| = 5164428.3780624345`;
- historical 0.2% beta criterion at the authoritative Q6 N24 scale corresponds locally to `|Delta Flow_G(p=1/32)| <= 2.9396080381477514e-09` if that primitive alone changes;
- observed Q6 N16->N24 p=1/32 primitive drift was `8.056166134691499e-07`, or `274.05579349849967` times that local budget;
- inherited p=0 N16->N24 drift propagates to only `0.00014474589698914965` absolute beta_g, about `0.9534426536%` of the historical allowed beta change.

Retain:

`P32_PRIMITIVE_STABILITY_REQUIRED_AT_FEW_TIMES_1E-9_FLOW_G_SCALE_SCOPED`.

`Q7B_DIAGNOSTIC_PASS != Q8_CONVERGENCE_PASS`.

## Active prospectively frozen Q8

Gate:

`SF055A3Q8_P32_HIGH_RESOLUTION_DERIVATIVE_CONVERGENCE_AND_ERROR_BUDGET`.

Preregistration: `47121c499fc036a6e0723f6c52266cae1c809207`.

Workflow head: `912d9dc3cb813a8b0f77e27ebf2a6b7048bbacf8`.

Workflow run: `35140467914`.

Only `p=1/32` is newly evaluated at N=32,40,48 with frozen shard counts 4,5,8 and unchanged Q6 integrand/executor. No C3 physics is enabled.

Latest authorized status in this addendum:

- all four N32 shard jobs have completed and archived artifacts;
- N40/N48 shard jobs remain nonterminal;
- no partial shard numerical value has been consumed for a scientific verdict;
- no Q8 PASS/BLOCKED classification exists yet.

Q8 remains the active numerical successor. Do not open a competing p=1/32 science verdict while run `35140467914` is nonterminal.

## Parent separation retained

Historical parent remains on

`WAIT_FOR_EXPLICIT_PROGRAMME_DISPOSITION_DECLARATION`.

No D1/D2/D3 disposition is selected. `chi_ABC` remains unauthorized/not computed. No Q7B/Q8 result automatically becomes historical RCG-002 authority or SF055 terminal PASS.
