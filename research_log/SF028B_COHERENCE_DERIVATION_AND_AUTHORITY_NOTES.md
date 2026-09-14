# SF028B — coherence derivation and authority notes

Date: 2026-09-15
Preregistration: `521ee723d66ff289f447c5474f7715b3fdd16dc3`.
Executed coefficient script: `scripts/sf028b_checks.py`, commit `46a6743f7f718b07e4fa452f53ebb61b31f8e9ae`.
Raw canonical output: `results/raw/SF028B_CHECKS.json`, commit `16cffa02797e9616c856d580445d994e836bd90a`.

## 1. Physical reduced-coherence object

After the frozen controlled translation, free evolution and exact inverse translation, the branch-conditioned motional state is

`|phi_s^X(T)> = T_s^dag U_X(T) T_s |psi_ref>`.

The normalized internal coherence relative to branch `000` is therefore exactly

`K_s^X(T)=<phi_000^X(T)|phi_s^X(T)>`

because all branch populations remain `1/8` under branch-diagonal free evolution and unitary readout.

Thus the promoted object is a Loschmidt/fidelity amplitude between two **complete physical branch evolutions**, reconstructed by tomography on the retained three-qubit register. It is not an open action.

The connected cumulant frozen in the preregistration is the Boolean/Mobius combination of the continuously chosen logarithms of these coherences.

## 2. Short-time linear-force derivation

Translate each branch center back to the common reference coordinate. At leading narrow-packet order write the branch Hamiltonian as

`H_s = K + V_s + g_s . x + higher spatial derivatives`,

where

`V_s=V(q_s)` and `g_s=grad V(q_s)`.

Use the kinetic interaction picture. Since

`x_I(t)=x_I+M_I^{-1}p_I t`,

one has

`H_I,s(t)=V_s+g_s.x+g_s.M^{-1}p t`.

The commutator at two times is a c-number:

`[H_I,s(t1),H_I,s(t2)] = i hbar (t2-t1) A_s`,

with

`A_s=g_s^T M^{-1} g_s`.

Therefore the Magnus expansion terminates at second order for the frozen linear-force problem:

`Omega_s = -(i/hbar)[V_s T + g_s.x T + g_s.M^{-1}p T^2/2] + (i/hbar) A_s T^3/12`.

For two branches `s` and `0`, the two Weyl generators have proportional position/momentum coefficients, so their mutual symplectic c-number phase cancels exactly. For a centered real isotropic Gaussian the expectation of the residual Weyl displacement is real and positive.

Hence, at leading semiclassical/narrow-packet order,

`arg K_s = -(V_s-V_0)T/hbar + (A_s-A_0)T^3/(12 hbar) + higher orders`.

Taking the frozen third Boolean combination gives

`Theta3^N(T)=-(T/hbar) Delta3 V_N + (T^3/(12 hbar)) Delta3 A_N + ...`.

This coefficient is intentionally different from the SF026 open released-action coefficient `1/3`. The two objects have different boundary/readout definitions. SF028B therefore supplies a direct example of why open action and measured/reduced coherence may not be conflated.

## 3. Leading connected visibility cumulant

For isotropic per-coordinate variance `sigma^2`, the centered Gaussian expectation of the Weyl displacement gives

`-Re Log K_s = (sigma^2 T^2/(2 hbar^2)) |g_s-g_0|^2 + O(T^4)`

at the retained leading width order.

Therefore

`Gamma3^N(T)=(sigma^2 T^2/(2hbar^2)) Delta3 Q + O(T^4)`

where

`Q_s=sum_I |g_{I,s}-g_{I,000}|^2`.

`Gamma3` is a connected logarithmic visibility cumulant and is not required to be positive term-by-term.

## 4. 3D domain audit

The SF028 defect is removed in three dimensions.

Near a pair coincidence, the Newtonian singularity has local radial measure

`r^2 dr / r = r dr`,

which is integrable.

Repeated-label 1PN static terms contain `1/r^2`; locally

`r^2 dr / r^2 = dr`,

also integrable.

For a distinct triple product `1/(r_AB r_AC)`, use two independent 3D relative coordinates near simultaneous coincidence. The local six-dimensional measure gives

`r_AB^2 dr_AB r_AC^2 dr_AC /(r_AB r_AC)`

which is locally integrable.

The frozen smooth Gaussian packets therefore do not reproduce the one-dimensional logarithmic object defect.

## 5. EIH power counting

The standard conservative 1PN N-body EIH Lagrangian contains:

- `v^4/c^2` terms;
- `G v^2/(r c^2)` velocity-dependent pair terms;
- the static `G^2/(r r c^2)` ordered triple sector used by SF022.

All branch mean velocities are zero at preparation.

Newtonian evolution gives

`v_N=O(G T)`

at fixed initial geometry.

Consequently the velocity-dependent 1PN action terms scale after time integration as

`G v_N^2 T/c^2 = O(G^3 T^3/c^2)`.

The `v^4` term is still higher,

`O(G^4 T^5/c^2)`.

The Newtonian displacement is `delta q_N=O(GT^2)`. Pulling the static `O(G^2/c^2)` EIH potential along that displacement changes it by `O(G^3T^2/c^2)`, hence contributes to the phase only at `O(G^3T^3/c^2)`.

Likewise an `O(G^2/c^2)` correction to the trajectory inserted into `L_N` first affects the on-shell semiclassical phase at `O(G^3T^3/c^2)` in this initial-rest counting.

Therefore the **only** term needed for the frozen same-protocol comparator through

`O(G^2 T/(hbar c^2))`

is the initial static EIH potential:

`Delta_1PN Theta3(T)=-(T/hbar) Delta3 V_static^(1PN) + O(G^3T^3/(hbar c^2),c^-4,eta^2 epsilon_PN)`.

No velocity term was removed because of its sign or numerical value; the omission follows the preregistered power counting.

## 6. Exact finite-R coefficients

All coefficients below were recomputed after the SF028B preregistration with exact rational arithmetic.

For the frozen `M_D=5m`, `R=100 ell` protocol:

`Delta3 V_N = -3.441209917267863e-7 * G m^2/ell`.

This is a finite-R **Newtonian apparatus/COM connected baseline**. It is not a new Newtonian three-body vertex.

`Delta3 A_N = -1.3308528151997442e-4 * G^2 m^3/ell^4`.

Thus the self-consistent force contribution to `Theta3^N` is

`-1.1090440126664535e-5 * G^2 m^3 T^3/(hbar ell^4)`.

The full all-body static EIH coefficient is

`Delta3 V_static^(1PN) = +0.002070114091375611 * G^2 m^3/(c^2 ell^2)`.

Hence

`Delta_1PN Theta3 = -0.002070114091375611 * G^2 m^3 T/(hbar c^2 ell^2) + higher orders`.

For the leading connected visibility cumulant,

`Delta3 Q = -1.3308490057392498e-4 * (G^2 m^4/ell^4)`

when the dimensional force scale is restored. Therefore

`Gamma3^N = -6.654245028696249e-5 * sigma^2 G^2 m^4 T^2/(hbar^2 ell^4) + O(T^4)`.

With the frozen `sigma=ell/100`, this becomes

`Gamma3^N = -6.654245028696249e-9 * G^2 m^4 T^2/(hbar^2 ell^2) + ...`.

Again, this connected cumulant is not a positive decoherence rate.

## 7. Source-only / apparatus-decoupling control

For the same SF026 source geometry with the apparatus formally removed to infinity:

`Delta3 V_N -> 0`,

`Delta3 A_N -> -82/616005 * G^2 m^3/ell^4`,

and

`Delta3 V_static^(1PN) -> (2/945) G^2 m^3/(c^2 ell^2)`.

The exact rational `-82/616005` reproduces the SF026 source-only force-pullback authority.

The 1PN source coefficient `2/945` is the correct SF026-geometry analog of SF022's `13/2520`, which used a different frozen branch geometry.

The finite-R ladder `R/ell=50,100,200,1000` approaches these source-only values monotonically in the executed control.

At `R=100 ell` the force-pullback coefficient differs from the source-only value by only about `2.29e-4` fractionally, while the static 1PN coefficient differs by about `2.19e-2`. This is why finite-R apparatus terms must be included rather than inferred negligible from the Newtonian force control alone.

## 8. Delete-one-bit controls

Prospectively setting any one of the three source displacement amplitudes to zero makes every executed connected coefficient vanish exactly:

`Delta3 V_N=Delta3 A=Delta3 V_static^(1PN)=Delta3 Q=0`.

Thus the reported connected terms depend on all three labels and are not produced by the finite-difference implementation itself.

## 9. Known-physics baseline hierarchy

The raw Newtonian finite-R phase contains an `O(GT)` apparatus contribution. The same-protocol EIH-minus-N comparator cancels the shared Newtonian dynamics and isolates the 1PN correction in theory.

Using

`epsilon_PN=Gm/(c^2 ell)`,

the ratio of the frozen direct Newtonian apparatus `O(T)` coefficient to the frozen 1PN `O(T)` coefficient is

`|Delta3 V_N|/(epsilon_PN Delta3 W1) = 1.6623286279748693e-4 / epsilon_PN`.

Thus in sufficiently weak fields the raw connected phase can be dominated by ordinary Newtonian apparatus closure even though the theory-difference comparator remains well defined. This is an interpretation/calibration warning, not a feasibility verdict.

The Newtonian force-pullback/1PN ratio is

`0.005357405262284278 * tau^2/epsilon_PN`.

So finite-time source motion is also a mandatory known-physics comparator; it cannot be labeled a nonlinear-gravity discovery.

## 10. Finite-size authority

The point-particle result remains the authoritative computed object.

For extended-body applicability, the following primary/review authorities support the standard 1PN effacement logic for nonspinning monopole bodies:

1. W. D. Goldberger and I. Z. Rothstein, *An Effective Field Theory of Gravity for Extended Objects*, arXiv:hep-th/0409156. Their EFT power counting finds spinless short-distance/finite-size information absent through low PN orders; the first curvature-squared tidal finite-size operators enter at order `v^10`, far beyond 1PN.
2. G. Schäfer and P. Jaranowski, *Hamiltonian formulation of general relativity and post-Newtonian dynamics of compact binaries*, arXiv:1805.07240. The review records the historical EIH/fluid-ball derivations and the effacing-principle context.

This authority is sufficient for a **1PN monopole/point-particle applicability statement** for nonspinning spherical bodies within the stated weak-field PN model.

It is not an engineering model of material deformation, branch-generation stresses, pulse hardware, or finite-time control implementation. Those remain outside the SF028B claim ceiling.

## 11. Boundary/readout sanity authority

S. Dimopoulos, P. W. Graham, J. M. Hogan and M. A. Kasevich, *General Relativistic Effects in Atom Interferometry*, arXiv:0802.4098, explicitly treats observable interferometer phases as combinations of propagation, interaction/control and separation/readout contributions. SF028B does not import their apparatus. It uses the paper only as an external sanity check for the principle that an open propagation action is not by itself the instrument observable.

## 12. Interpretation firewall

The result is a known-physics operational baseline.

Retain exactly:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

The finite-R Newtonian term is apparatus/COM closure; the `T^3` Newtonian term is force/trajectory/coherence pullback; the 1PN term is the ordinary GR/EIH nonlinear correction. None is new physics.

No quantum-gravity matching contribution was included.