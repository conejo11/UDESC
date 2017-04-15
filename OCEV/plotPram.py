import random
import math as mt

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
