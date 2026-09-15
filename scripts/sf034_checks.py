#!/usr/bin/env python3
from itertools import product
import json, hashlib

BITS=list(product([0,1], repeat=3))

def d3(vals):
    return (vals[(1,1,1)]-vals[(1,1,0)]-vals[(1,0,1)]-vals[(0,1,1)]
            +vals[(1,0,0)]+vals[(0,1,0)]+vals[(0,0,1)]-vals[(0,0,0)])

mons={
    '1':lambda a,b,c:1,
    'nA':lambda a,b,c:a,
    'nB':lambda a,b,c:b,
    'nC':lambda a,b,c:c,
    'nAnB':lambda a,b,c:a*b,
    'nAnC':lambda a,b,c:a*c,
    'nBnC':lambda a,b,c:b*c,
    'nAnBnC':lambda a,b,c:a*b*c,
}
boolean={name:d3({x:f(*x) for x in BITS}) for name,f in mons.items()}

results={
  'prereg_commit':'45a121c99f41e285b4f007984ffe55763831f343',
  'boolean_third_difference':boolean,
  'M0':{
      'science_lambda_A':1,
      'control_lambda_A':0,
      'theta3_register_science':'-zeta*T',
      'theta3_register_deleteA':'-zeta*T',
      'science_minus_control_register':'0',
      'transferability':'EXACT_WITHIN_M0'
  },
  'M1':{
      'zeta_lambda':'zeta0+zeta1*lambda_A',
      'theta3_register_science':'-(zeta0+zeta1)*T',
      'theta3_register_deleteA':'-zeta0*T',
      'science_minus_control_register':'-zeta1*T',
      'deleteA_alone_identifies_zeta1':False,
      'transferability':'FAILS_UNLESS_ZETA1_ZERO_OR_INDEPENDENTLY_CALIBRATED'
  },
  'sf033_transfer_elements':{
      'nuisance_generator':True,
      'science_action':True,
      'deleteA_action':True,
      'equality_reason_M0':True,
      'fixed_vs_changed_variables':True,
      'falsification_condition':True,
      'count_present_M0':6
  },
  'classification':'CONNECTED_CONTROL_PHASE_TRANSFER_MAP_DERIVED_UNDER_CONTROL_SEPARABILITY_SCOPED',
  'qualification':'MODEL_LEVEL_TRANSFERABILITY_NOT_DEVICE_VALIDATION'
}
raw=json.dumps(results,indent=2,sort_keys=True)
print(raw)
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
