from Lz77 import parsed

def lzBit(string):
  l = list()
  for i in string: 
    if i not in l:
      l.append(i)
  return len(bin(len(l)-1)[2:])

def lzLen(string):
  return len(string)*lzBit(string)

def keymaker(string):
  l = list()
  index  = 0
  for i in string:
    if i not in l:
      l.append(i)
      index += 1
    else: 
      aux = ""
      for j in string[index:]:
        if aux not in l and aux != "":
          l.append(aux)
          break
        else:
          aux+=j
          index += 1
          fi = aux
  l.append(fi)
  return l

def encodeLZ(string):
  l = keymaker(string)
  l1 = []
  l2 = []
  for i in l: 
    if i[0] not in l2: 
      l1.append((0,i))
    else:
      aux = i[0]
      for j in range(1,len(i)):
        prev = aux
        aux += i[j]
        if aux not in l2:
          l1.append((l.index(prev)+1, aux[len(aux)-1]))
          break
      else:
        l1.append((0, i[0]))
    l2.append(i)
  return l1

def decodeLZ(string):
  l = parsed(string)
  l1 = list()
  for i in l:
    aux = i.split(",")
    if aux[0] =="0":
      l1.append(aux[1])
    else:
      l1.append(l1[int(aux[0])-1]+aux[1])
  return "".join(("".join(l1)).split("'"))

def cadCompr(string, n=15):
  a = len(encodeLZ(string))
  return (lzBit(string)+len(bin(n-1)[2:]))*a

def comper(string):
  return cadCompr(string)/lzLen(string)

def percent(string):
  return (1-comper(string))*100