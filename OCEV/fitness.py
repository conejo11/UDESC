import random
import math as mt
import variaveis as var
import string

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

# FUNCAO ALGEBRICA X^2 -- SPHERE
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
  cut = 5
  submat1 = []
  submat2 = []
  submat3 = []
  for i in range(pop):
    for j in range(d):
      submat1.append(matriz[i][j])
  for i in range(pop):
      submat2.append(submat1[:cut])
      submat3.append(submat1[cut:])
      str1 = ''.join(str(e) for e in submat2)
      str2 = ''.join(str(e) for e in submat3)
      convst = int(str1,2)
      convlx = int(str2,2)
  pass


def pattern(matriz,pop,d):
  pass
