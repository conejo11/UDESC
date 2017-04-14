import random
import math as mt
import variaveis as var

# PROBABILIDADE CROSSOVER
def cross():
  x = 1.0
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
  for i in range(d):
    matriz[dad][i] = submatDad[i]
    matriz[mom][i] = submatMom[i]
  # print (submatDad)
  # print (submatMom)
  # print()
  # printPopulacaoEFitness(matriz,pop,d)
  return matriz

def onePointCrossover(matriz,pop,d,dad,mom):
  submatDad = []
  submatMom = []
  for i in range(d):
    submatDad.append(matriz[dad][i])
    submatMom.append(matriz[mom][i])
  cut = random.randint(0,(d-1))
  # print(cut)
  for i in range(d):
    if i >= cut:
      b = submatDad[i]
      c = submatMom[i]
      submatDad[i] = c
      submatMom[i] = b
  for i in range(d):
    matriz[dad][i] = submatDad[i]
    matriz[mom][i] = submatMom[i]
  # print (submatDad)
  # print (submatMom)
  # print()
  # printPopulacaoEFitness(matriz,pop,d)
  return matriz

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
  for i in range(d):
    matriz[dad][i] = submatDad[i]
    matriz[mom][i] = submatMom[i]
  # print (submatDad)
  # print (submatMom)
  return matriz

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
  for i in range(d):
    matriz[dad][i] = submatDad[i]
    matriz[mom][i] = submatMom[i]
  # print (submatDad)
  # print (submatMom)
  return matriz   

# CROSSOVER PERMUTACAO
def pmxPerm(matriz,pop,d,dad,mom):
  submatDad = []
  submatMom = []
  for i in range(d):
    submatDad.append(matriz[dad][i])
    submatMom.append(matriz[mom][i]) 
  cut1 = random.randint(0,(d-1))
  cut2 = random.randint(0,(d-1))
  pass