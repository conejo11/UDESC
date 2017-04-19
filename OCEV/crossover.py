import random
import math as mt
import variaveis as var
import copy
import functools
# PROBABILIDADE CROSSOVER
def cross():
  x = 0.94
  y = random.random()
  if x > y:
    return True
  else:
    return False

# CROSSOVER BINARIO/INTEIRO
def uniformCrossover(matriz,pop,d,dad,mom):
  submatDad = []
  submatMom = []
  for i in range(d):
    submatDad.append(matriz[dad][i])
    submatMom.append(matriz[mom][i])
  for i in range(d):
    prob = random.random()
    if prob < 0.5:
      a = submatDad[i]
      b = submatMom[i]
      submatDad[i] = b
      submatMom[i] = a
  return submatDad,submatMom

def onePointCrossover(matriz,pop,d,dad,mom):
  cut = random.randint(0,pop-1)
  cut = random.randint(1,pop-1)
  head1 = matriz[dad][:cut]
  head2 = matriz[mom][:cut]
  tail1 = matriz[dad][cut:]
  tail2 = matriz[mom][cut:]
  son1 = head1+tail2
  son2 = head2+tail1
  return son1,son2

# CROSSOVER REAL
def blxReal(matriz,pop,d,dad,mom):
  a = 0.5
  submatDad = []
  submatMom = []
  for i in range(d):
    submatDad.append(matriz[dad][i])
    submatMom.append(matriz[mom][i])
  for i in range(d):
    e = mt.fabs(submatDad[i] - submatMom[i])
    u = random.uniform((min(submatDad[i],submatMom[i])-(a*e)),(max(submatDad[i],submatMom[i])+(a*e)))
    submatDad[i] = u
    o = random.uniform((min(submatDad[i],submatMom[i])-(a*e)),(max(submatDad[i],submatMom[i])+(a*e)))
    submatMom[i] = o
  return submatDad,submatMom

def uniformAverageReal(matriz,pop,d,dad,mom):
  submatDad = []
  submatMom = []
  for i in range(d):
    submatDad.append(matriz[dad][i])
    submatMom.append(matriz[mom][i])
  for i in range(d):
    average = (submatDad[i]+submatMom[i])/2
    number = random.choice([1,0])
    if number == 0:
      submatDad[i] = average
    elif number == 1:
      submatMom[i] = average
  return submatDad,submatMom

# CROSSOVER PERMUTACAO
def pmxPerm(matriz,pop,d,dad,mom):
  submatDad = []
  submatMom = []
  for i in range(d):
    submatDad.append(matriz[dad][i])
    submatMom.append(matriz[mom][i]) 
  size = len(submatMom)
  points = random.sample(range(size), 2)
  x,y = min(points), max(points)
  bro = copy.copy(submatDad)
  bro[x:y+1] = submatMom[x:y+1]
  sis = copy.copy(submatMom)
  sis[x:y+1] = submatDad[x:y+1]
  for parent,child in zip([submatDad,submatMom], [bro,sis]):
    for i in range(x,y+1):
      if parent[i] not in child[x:y+1]:
        spot = i
        while x<=spot<=y:
          spot = parent.index(child[spot])
        child[spot] = parent[i]
  return bro,sis
