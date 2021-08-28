import numpy as np

def huffman(p):
    assert(sum(p.values()) < 1.0 + 1e-10 or sum(p.values()) < 1.0 - 1e-10) # Ensure 

    if(len(p) == 2):
        a1, a2 = lowest_prob_pair(p)
        return dict(zip([a1, a2], ['0', '1']))

    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

def lowest_prob_pair(p):
    assert(len(p) >= 2) 

    sorted_p = sorted(p.items(), key=lambda pz: pz[1])
    return sorted_p[0][0], sorted_p[1][0]

def mk_dct(string):
  d = dict()
  total = len(string)
  for i in string:
    if i not in d:
      d[i] = 1/total
    else:
      d[i] += 1/total
  return d

def Entropy(probabilities):
  return sum([i*np.log2((i**-1)) for i in probabilities])

def av_cwlen(dct1, dct2):
  return sum([len(dct1[i])*dct2[i] for i in dct1.keys()])

def efficiency(string):
  d=mk_dct(string)
  return Entropy(d.values())/av_cwlen(huffman(d),d)

def Slen(string):
  return len(bin(len(string)-1)[2:])