import numpy as np
import sympy as sp

def creaDict(): 
  return {i:j for j, i in zip(list(range(0,26)),[chr(65+i) for i in range(0,26)])} 

def creaDict2(): 
  return {j:i for j, i in zip(list(range(0,26)),[chr(65+i) for i in range(0,26)])} 

def primero_segundo(palabra, entero, b): 
  s = ""
  d = creaDict()
  d2 = creaDict2()
  if b == 0: 
    for i in palabra: 
      aux = d[i] + entero
      if aux > 25: 
        aux = aux%26
      s += d2[aux]
  else: 
      for i in palabra: 
        aux = d[i] - entero
        if aux < 0: 
          aux = aux%26
        s += d2[aux]
  return s

def tercero(palabra1, palabra2):
  d = creaDict() 
  aux = d[palabra1[0]] - d[palabra2[0]]
  if aux < 0: 
    return aux + 26
  return aux

def cuarto(m, k):
  l = np.array([[creaDict()[j] for j in list(m[i:i+2])] for i in range(0, len(m), 2)])
  l2 = np.array([[creaDict()[j] for j in list(k[i:i+2])] for i in range(0, len(k), 2)])
  res = np.matmul(l,l2)
  return "".join([creaDict2()[item] for sublist in [[j % 26 for j in i] for i in res] for item in sublist ])

def quinto(c, k): 
  l = sp.Matrix([[creaDict()[j] for j in list(c[i:i+2])] for i in range(0, len(c), 2)])
  l2 =  sp.Matrix([[creaDict()[j] for j in list(k[i:i+2])] for i in range(0, len(k), 2)])
  x = l * l2.inv_mod(26)
  return "".join([creaDict2()[i % 26] for i in x])

def sexto(c,m):
  s = ""
  d2 = creaDict2()
  for i in range(0,26):
      for j in range(0,26):
          for k in range(0,26):
              for a in range(0,26):
                  s = d2[i] + d2[j] + d2[k] + d2[a]
                  if c == cuarto(m,s):
                      return s
