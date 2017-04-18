import random
import math as mt
import copy

m_nmdf = 0.00000000

def getBest(matriz,pop,d):
  submat = []
  best = -1
  for i in range(pop):
    submat.append(matriz[i][d])
  for i in range(d):
    if submat[i] > best:
      best = submat[i]
  return best

def averageInd(matriz,pop,d):
  submat = []
  som = 0
  for i in range(pop):
    submat.append(matriz[i][d])
  for i in range (d):
    som = som + submat[i]
  som = som/d
  return som

def bestInd(matriz,pop,d):
  submat = []
  individual = []
  best = -1
  j = -1
  for i in range(pop):
    submat.append(matriz[i][d])
  for i in range(d):
    if submat[i] > best:
      best = submat[i]
      j = i
  for i in range(d):
    individual.append(matriz[j][i])
  return individual

def diversityHam(matriz,pop,d):
  diversity = 0
  n = 1
  for i in range(pop):
    for j in range(i+1,pop,1):
      aux = 0
      for k in range(d):
        aux += mt.fabs(matriz[i][k] - matriz[j][k])
        diversity += float(aux/(pop-n))
    n +=1
  return diversity

def diversityMeasure(matriz,pop,d):
  diversity = 0.00000000
  aux1 = 0.00000000
  aux2 = 0.00000000
  global m_nmdf
  for a in range(0,pop,1):
    for b in range(a+1,pop,1):
      aux1 = 0.0
      for c in range(0,d,1):
        aux1 += mt.fabs(matriz[a][c] - matriz[b][c])**2
      aux1 = copy.copy(mt.sqrt(aux1))
    #   print(d)
      aux1 = copy.copy(aux1/d)
      if (b == (a+1) or aux2 > aux1):
        aux2 = copy.copy(aux1)
    diversity += mt.log1p(aux2)
  if m_nmdf < diversity:
    m_nmdf = diversity
  return diversity/m_nmdf
