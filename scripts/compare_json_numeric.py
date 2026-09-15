import json, math, sys

if len(sys.argv) not in (3,4):
    raise SystemExit('usage: compare_json_numeric.py expected.json actual.json [tol]')
expected_path, actual_path = sys.argv[1], sys.argv[2]
tol=float(sys.argv[3]) if len(sys.argv)==4 else 1e-12
with open(expected_path,encoding='utf-8') as f: expected=json.load(f)
with open(actual_path,encoding='utf-8') as f: actual=json.load(f)

def cmp(a,b,path='$'):
    if isinstance(a,bool) or isinstance(b,bool):
        if type(a) is not type(b) or a!=b: raise AssertionError(f'{path}: {a!r} != {b!r}')
        return
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        if not (math.isfinite(float(a)) and math.isfinite(float(b))):
            if a!=b: raise AssertionError(f'{path}: nonfinite {a!r} != {b!r}')
            return
        if abs(float(a)-float(b)) > tol*(1+max(abs(float(a)),abs(float(b)))):
            raise AssertionError(f'{path}: {a!r} != {b!r} at tol {tol}')
        return
    if type(a) is not type(b): raise AssertionError(f'{path}: type {type(a).__name__} != {type(b).__name__}')
    if isinstance(a,dict):
        if set(a)!=set(b): raise AssertionError(f'{path}: keys differ {set(a)^set(b)}')
        for k in sorted(a): cmp(a[k],b[k],f'{path}.{k}')
    elif isinstance(a,list):
        if len(a)!=len(b): raise AssertionError(f'{path}: len {len(a)} != {len(b)}')
        for i,(x,y) in enumerate(zip(a,b)): cmp(x,y,f'{path}[{i}]')
    else:
        if a!=b: raise AssertionError(f'{path}: {a!r} != {b!r}')

cmp(expected,actual)
print(f'JSON_MATCH_WITH_NUMERIC_TOLERANCE={tol}')
