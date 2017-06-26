import random
import math as mt
import numpy as np
import variaveis as var

def getGap(matriz, percent,pop,d):
  x = []
  for i in range(percent):
    x.append([matriz[i][j] for j in range(d)])
  return x

def sharing(matriz,pop,d):
  alpha = 2.0
  sigma = 1.5
  mini = 99999
  maxi = -1
  for i in range(pop):
    if matriz[i][d] < mini:
      mini = matriz[i][d]
    if matriz[i][d] > maxi:
      maxi = matriz[i][d]
  for i in range(pop):
    som = 0.0
    dist = 0.0
    for j in range(pop):
      dist += (float(mt.fabs(matriz[i][d] - matriz[j][d]/float((maxi-mini)*d))))
    som += (1.0-((dist/sigma)**alpha))
    cru = matriz[i][d]
    matriz[i][d] = cru/som

def crowding():
  select = 5
  newM = []
  pass