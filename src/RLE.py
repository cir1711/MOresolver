import re

def RLE(string):
  l = list(map(int, string.split(",")))
  return len(bin(l[0])[2:])*len(l)

def RLE_2(string):
  l = list(map(int, string.split(",")))
  l2 = []
  contador = 0
  for i in l:
    if sum(l2)==l[0]:
      l2 = []
      contador += 1
    l2.append(i)
  return contador

#no es eficiente pero funciona
def RLE_3(string):
  l = list(map(int, string.split(",")))
  l2 = list()
  l3 = list()
  for i in l[1:]:
    l2.append(i)
    if sum(l2) == l[0]:
      l3.append(l2)
      l2 = []
  par = 1
  l4 = []
  l5 = []
  for i in l3: 
    for j in i:
      if j!=0:
        if par%2==0:
          l4.append(j*"x")
        else:
          l4.append(j*"0")
      par += 1
    l5.append(l4)
    l4 = []
    par = 1
  counter = 0
  for i in l5:
    for j in i:
      counter += j.count("0")
  return counter

def RLE_4(l):
  return len(l)*len(l[0])+len(bin(len(l[0]))[2:])

def rle_string(string):
  ones = list(map(len, re.findall("X+", string)))
  zeros = list(map(len, re.findall("0+", string)))
  
  if string[0] != '0':
    zeros = [0] + zeros

  ret = []

  for i in range(len(zeros)+len(ones)):
    try:
        if i % 2 == 0:
            ret.append(zeros[i//2])
        else:
            ret.append(ones[i//2])
    except:
        break

  return ret
  
def rle_encode(data):
    ret = [len(data[0])]
    for i in data:
      ret += rle_string(i)

    return ret