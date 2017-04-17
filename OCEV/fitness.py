import random
import math as mt
import variaveis as var

# PRINTAR MATRIZ POPULACIONAL
def printPopulacaoEFitness(matriz, pop,d):
  for i in range(pop):
    for j in range(d+1):
      print (matriz[i][j], end=" ")
    print()


# FUNCOES DE FITNESS
# BITS ALTERNADOS
def bitsAlternados(matriz, pop, d):
  fitness = 0
  for i in range(pop):
    for j in range(d-1):
      if(matriz[i][j] != matriz[i][j+1]):
        fitness = fitness + 1
    matriz[i].append(fitness)
    matriz[i][d] = fitness
    fitness = 0
  return matriz

# PARES ALTERNADOS
def paresAlternados(matriz, pop,d):
  fitness = 0
  for i in range(pop):
    for j in range(d-1):
      if((matriz[i][j] % 2) != (matriz[i][j+1] % 2)):
        fitness = fitness + 1
    matriz[i].append(fitness)
    fitness = 0
  return matriz

# FUNCAO ALGEBRICA X^2
def maxFuncAlg(matriz, pop, d):
  fitness = 0.0
  gt = []
  for i in range(pop):
    for j in range(d):
      fitness = fitness + (matriz[i][j]**2)
    gt.append(fitness)
    # matriz[i].append(fitness)
    # matriz[i][d] = fitness
    fitness = 0.0
  for i in range(pop):
    fit = gt[i]
    fit = fit/max(gt)
    newFt = (1.0 - fit)
    matriz[i].append(newFt)
    matriz[i][d] = newFt
  return matriz

def radio(matriz,pop,d):
  pass

def pattern(matriz,pop,d):
  pass
