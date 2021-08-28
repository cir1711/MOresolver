def creaProbs(string):
  d = dict()
  leng = len(string)
  l = list(string)
  for i in sorted(l): 
    if i not in d: 
      d[i] = 1/leng
    else:
      d[i] += 1/leng
  return d
  
def creaTupla(string):
  d = creaProbs(string)
  l = list()
  anterior = 0
  probs = 0
  keys = list(d.keys())
  for i in keys:
    probs += d[i]
    l.append((anterior, probs))
    anterior = probs
  numero = 0
  for i in keys:
    d[i] = l[numero]
    numero += 1
  return d 

def encodeAri(string):
  d = creaTupla(string)
  alt = 1
  baix = 0
  for i in string: 
    rang = alt - baix
    alt  = baix + rang * d[i][1]
    baix = baix + rang * d[i][0]
  return (baix,alt)

def creaTupla2(l):
  newL = list()
  anterior = 0
  prob = 0
  for i in l:
    prob += i
    newL.append((anterior,prob))
    anterior = prob
  return newL

def decodeAri(integer, s, l, n):
  while integer > 1:
    integer = integer/10
  aux = ''
  valor = integer
  alt = 1
  baix = 0 
  newL = creaTupla2(l)
  for i in range(0,n):
    valor = (valor - baix)/(alt - baix)
    for j in range(0,len(s)):
      if newL[j][0] <= valor and valor < newL[j][1]:
        aux += s[j]
        alt = newL[j][1]
        baix = newL[j][0]
        break
  return aux