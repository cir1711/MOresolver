def mcd(n):
  l = []
  for divisor in range(1,n+1):
    if (n % divisor) == 0:
      l.append(divisor)
  return l

def inverse_mod(e, n):
  for x in range(1, n):
    if (((e%n) * (x%n)) % n == 1):
      return x   
  return None

def pregunta_1(e,n):
  if e % 2 == 0: 
    return "NO"
  l, l2 = mcd(e), mcd(n)
  for i in l2: 
    if i != 1 and i in l: 
        return "NO"
  return "SI"

def pregunta_2(e,n):
  l = mcd(n)
  n_phi = (l[1] - 1)*(l[2] - 1)
  return inverse_mod(e, n_phi)

def pregunta_3(e, m, n):
  return (m**e) % n

def pregunta_4(d,m,n):
  return (m**d) % n

def pregunta_5(d, c, e):
  return (c**d) % e