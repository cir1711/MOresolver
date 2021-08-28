def parsed(string):
  l = []
  bolean = True
  x = 1
  for i in string:     
    if bolean == True and x != 1:
      l.append(i)
    if i == "(":
      bolean = True
    if i == ")": 
      bolean = False
    x+=1
  l = "".join(l).split(")")
  l.pop()
  return l
  
def encodeLZ(string):
  l = []
  s = ""
  index = 0
  while len(s) < len(string):
    actual = searcher(string[index], s, string[index:])
    if actual != -1:
      aux = 0
      for i in range(index, len(string)):
        n = len(s)-actual
        if string[i] != s[n]:
          break
        aux+=1
        s += string[i]
      index = index + aux + 1
      try:
        l.append((actual, aux, string[index-1])) 
      except:
        print(index, actual, aux)
        l.append((0,0,string[len(string)-1]))
        break
      s += string[index-1] 
    else:
      l.append((0,0,string[index]))
      s += string[index]
      index += 1
  return l


def searcher(a,string, string2):
  m = -1
  aux = 1
  aux2 = -1
  if len(string) <= 15:
    for i in range(len(string)-1, -1, -1):
      s = a
      if a == string[i]:
        for j in range(1, len(string2)):
          s+=string2[j]
          if string.find(s) != -1: 
            aux2 = len(string) - string.find(s)
          else:
            break
        m = aux
      aux+=1
  else: 
    off = len(string) - 15
    for i in range(len(string)-1, -1+off, -1):
      if a == string[i]:
        s = a
        for j in range(1, len(string2)):
          s+=string2[j]
          if string.find(s) != -1: 
            aux2 = (len(string) - off) - string.find(s)
          else:
            break
        m = aux
      aux+=1
  if aux2 > 0:
    return min(m, aux2)
  return m

def decodeLZ(string):
  l = parsed(string)
  l1 = []
  for i in l:
    aux = i.split(",")
    if aux[0] == 0 and aux[1]== 0:
        l1.append(aux[2])
    else:
      length = len(l1)
      for j in range(0, int(aux[1]),1):
        if j < int(aux[1]):
            l1.append(l1[length-int(aux[0])+j])
        else: 
          break
      l1.append(aux[2])
  return "".join(l1)

def LZlen(string):
  l = parsed(string)
  l1 = []
  for i in l:
    aux = i.split(",")
    if aux[2] not in l1:
      l1.append(aux[2])
  return len(bin(len(l1)-1)[2:])

def cadlen(string):
  s = decodeLZ(string)
  return len(s)*LZlen(string)

def cadLzlen(string):
  count = 0
  for i in string:
    if i == ")":
      count+=1
  return count

def btlz(sb, lab, string):
  return cadLzlen(string)*(len(bin(sb)[2:])+LZlen(string)+len(bin(lab)[2:]))

def compresstax(string):
  return btlz(15,7,string)/cadlen(string)

def compress_pert(string):
  return (1 - compresstax(string))*100