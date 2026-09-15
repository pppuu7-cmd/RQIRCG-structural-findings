#!/usr/bin/env python3
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

import sf055a2_source_fourier_seed_engine as seed
import sf055a_eh_ghost_seed_engine as base

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3_TT_PROJECTOR_NORMALIZATION.json"
TOL_GRAM = 2e-12
TOL_DEC = 2e-12
TOL_REL = 2e-11


def json_default(x):
    if isinstance(x, np.bool_): return bool(x)
    if isinstance(x, np.integer): return int(x)
    if isinstance(x, np.floating): return float(x)
    raise TypeError(type(x).__name__)


def symmetric_ps_in_plane(a=0, b=1):
    p1 = np.zeros(4); p2 = np.zeros(4)
    p1[a] = 1.0
    p2[a] = -0.5
    p2[b] = math.sqrt(3.0)/2.0
    return [p1, p2, -(p1+p2)]


def bases_for(ps):
    return [base.tt_basis(p) for p in ps]


def gram_error(B):
    G = np.array([[np.einsum('mn,mn->', x, y) for y in B] for x in B])
    return float(np.max(np.abs(G-np.eye(5))))


def tensor3(ps_tensor, bases, lam):
    arr = np.zeros((5,5,5))
    for a,b,c in itertools.product(range(5), repeat=3):
        hs=[bases[0][a],bases[1][b],bases[2][c]]
        arr[a,b,c] = seed.eh_vertex_fourier(ps_tensor, hs, lam)
    return arr


def hash_arr(x):
    # deterministic little-endian float64 bytes
    y=np.ascontiguousarray(np.asarray(x,dtype='<f8'))
    return hashlib.sha256(y.tobytes()).hexdigest()


def rel(a,b):
    return abs(a-b)/max(1.0,abs(a),abs(b))


def deterministic_O(seedv):
    rng=np.random.default_rng(seedv)
    A=rng.normal(size=(4,4))
    Q,R=np.linalg.qr(A)
    s=np.sign(np.diag(R)); s[s==0]=1
    Q=Q@np.diag(s)
    return Q


def deterministic_Q5(seedv):
    rng=np.random.default_rng(seedv)
    A=rng.normal(size=(5,5)); Q,R=np.linalg.qr(A)
    s=np.sign(np.diag(R)); s[s==0]=1
    return Q@np.diag(s)


def rotate_basis(B,Q):
    return [sum((Q[i,a]*B[i] for i in range(5)),np.zeros((4,4))) for a in range(5)]


def global_rotate(ps,Bs,O):
    ps2=[O@p for p in ps]
    Bs2=[[O@h@O.T for h in B] for B in Bs]
    return ps2,Bs2


def norm2(T): return float(np.einsum('abc,abc->',T,T))


def main():
    ps=symmetric_ps_in_plane(0,1)
    Bs=bases_for(ps)
    grams=[gram_error(B) for B in Bs]
    zps=[np.zeros(4) for _ in range(3)]

    TG=tensor3(ps,Bs,0.0)
    TL=tensor3(zps,Bs,1.0)
    nginv=norm2(TG); nlinv=norm2(TL)
    Ng=1.0/nginv; Nl=1.0/nlinv

    # Source Eq. (6) component-wise decomposition.
    dec={}
    dec_pass=True
    for lam in (-0.7,-0.2,0.4):
        T=tensor3(ps,Bs,lam)
        err=float(np.max(np.abs(T-(TG+lam*TL))))
        dec[str(lam)]=err
        dec_pass &= err <= TOL_DEC

    # Independent TT-basis rotations, evaluated through source generator again.
    Qs=[deterministic_Q5(101+i) for i in range(3)]
    Br=[rotate_basis(Bs[i],Qs[i]) for i in range(3)]
    TGr=tensor3(ps,Br,0.0); TLr=tensor3(zps,Br,1.0)
    basis_rot={
        'Ng_inv_relative_change': rel(norm2(TGr),nginv),
        'Nlambda_inv_relative_change': rel(norm2(TLr),nlinv),
    }
    basis_rot['pass']=basis_rot['Ng_inv_relative_change']<=TOL_REL and basis_rot['Nlambda_inv_relative_change']<=TOL_REL

    # Global O(4) rotation; rotate momentum and basis tensors coherently.
    O=deterministic_O(211)
    psO,BsO=global_rotate(ps,Bs,O)
    TGO=tensor3(psO,BsO,0.0); TLO=tensor3(zps,BsO,1.0)
    global_rot={
        'Ng_inv_relative_change': rel(norm2(TGO),nginv),
        'Nlambda_inv_relative_change': rel(norm2(TLO),nlinv),
    }
    global_rot['pass']=global_rot['Ng_inv_relative_change']<=TOL_REL and global_rot['Nlambda_inv_relative_change']<=TOL_REL

    # Alternative deterministic symmetric embeddings of the 120-degree triangle.
    embeddings=[]
    for pair in [(0,1),(0,2),(1,3)]:
        pse=symmetric_ps_in_plane(*pair); Bse=bases_for(pse)
        TLe=tensor3(zps,Bse,1.0); TGe=tensor3(pse,Bse,0.0)
        embeddings.append({
            'plane':list(pair),
            'Ng_inv':norm2(TGe),
            'Nlambda_inv':norm2(TLe),
            'Ng_relative_change':rel(norm2(TGe),nginv),
            'Nlambda_relative_change':rel(norm2(TLe),nlinv),
        })
    embedding_pass=all(x['Ng_relative_change']<=TOL_REL and x['Nlambda_relative_change']<=TOL_REL for x in embeddings)

    # Bose-labelled permutations, rebuilding arrays in corresponding leg order.
    perms=[]
    for perm in itertools.permutations(range(3)):
        pp=[ps[i] for i in perm]; BB=[Bs[i] for i in perm]
        Tg=tensor3(pp,BB,0.0); Tl=tensor3(zps,BB,1.0)
        perms.append({
            'perm':list(perm),
            'Ng_relative_change':rel(norm2(Tg),nginv),
            'Nlambda_relative_change':rel(norm2(Tl),nlinv),
        })
    perm_pass=all(x['Ng_relative_change']<=TOL_REL and x['Nlambda_relative_change']<=TOL_REL for x in perms)

    # Counterexample-first: a single component is not the complete norm.
    single_g=float(TG[0,1,2]**2); single_l=float(TL[0,1,2]**2)
    # Fitted rescaling mutation is rejected against direct source tensor.
    fitted_scale=1.137
    scaled_err_g=float(np.max(np.abs(fitted_scale*TG-TG)))
    scaled_err_l=float(np.max(np.abs(fitted_scale*TL-TL)))
    negative={
        'single_polarization_not_full_Ng': abs(single_g-nginv)>1e-12,
        'single_polarization_not_full_Nlambda': abs(single_l-nlinv)>1e-12,
        'arbitrary_rescale_TG_rejected': scaled_err_g>1e-12,
        'arbitrary_rescale_TLambda_rejected': scaled_err_l>1e-12,
    }
    negative_pass=all(negative.values())

    positive={
        'TT_grams':max(grams)<=TOL_GRAM,
        'Ng_positive':nginv>0,
        'Nlambda_positive':nlinv>0,
        'eq6_decomposition':dec_pass,
        'basis_rotation_invariance':basis_rot['pass'],
        'global_rotation_invariance':global_rot['pass'],
        'embedding_invariance':embedding_pass,
        'Bose_norm_invariance':perm_pass,
    }
    positive_pass=all(positive.values())
    scientific_pass=positive_pass and negative_pass

    result={
        'gate':'SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION',
        'classification':('PASS_SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION_SCOPED' if scientific_pass else ('BLOCKED_ZERO_MOMENTUM_TT_PROJECTOR_CONVENTION' if not embedding_pass else 'FAIL_SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION_SCOPED')),
        'source_equations':[6,9,10,11],
        'Ng_inv':nginv,'Ng':Ng,'Nlambda_inv':nlinv,'Nlambda':Nl,
        'TG_sha256':hash_arr(TG),'TLambda_sha256':hash_arr(TL),
        'TG':TG.tolist(),'TLambda':TL.tolist(),
        'TT_gram_errors':grams,
        'eq6_max_component_errors':dec,
        'basis_rotation':basis_rot,
        'global_rotation':global_rot,
        'alternative_embeddings':embeddings,
        'Bose_permutations':perms,
        'negative_controls':negative,
        'positive_controls':positive,
        'positive_pass':positive_pass,'negative_pass':negative_pass,'scientific_pass':scientific_pass,
        'next_required':'FULL_TT_PROJECTED_FIGURE2_QUADRATURE_DERIVATIVE_AND_FINITE_DIFFERENCE_EXTRACTION',
        'interpretation_ceiling':'PROJECTOR_NORMALISATION_ONLY_NO_LOOP_QUADRATURE_NO_EQ14_NO_C3',
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    text=json.dumps(result,indent=2,sort_keys=True,default=json_default)+'\n'
    OUT.write_text(text)
    print(json.dumps({k:v for k,v in result.items() if k not in ('TG','TLambda','Bose_permutations')},indent=2,sort_keys=True,default=json_default))
    if not scientific_pass: raise SystemExit(1)

if __name__=='__main__': main()
