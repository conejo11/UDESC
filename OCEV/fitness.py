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
def sphere(matriz, pop, d):
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

# Radio Factory
def radio(matriz,pop,d):
  cut = 5
  submat1 = []
  submat2 = []
  submat3 = []
  for i in range(pop):
    for j in range(d):
      submat1.append(matriz[i][j])
    submat2 = submat1[:cut]
    submat3 = submat1[cut:]
    str1 = ''.join(str(e) for e in submat2)
    str2 = ''.join(str(e) for e in submat3)
    new = int(str2,2)
    new2 = int(str1,2)
    max_bit = 2 ** 5 - 1
    convst = (0.0+(24.0 / max_bit)) * new2 #
    convlx = (0.0+(16.0 / max_bit)) * new
    fit = ((30.0*convst + 40.0*convlx)/1360.0) - max(0.0,(convst + 2.0 * convlx - 40.0)/16.0)
    matriz[i].append(fit)
    submat1 = []
    submat2 = []
    submat3 = []
    fit = 0.0
  return matriz


# Graphic Pattern
def pattern(matriz,pop,d):
  fitness = 0
  compare = [1,0,1,1,1,1,
  			 1,0,1,0,0,1,
  			 1,0,1,0,1,1,
  			 1,1,1,1,0,1,
  			 1,0,0,0,1,1,
  			 1,1,1,1,0,1]
  for i in range(pop):
    for j in range(d):
      if matriz[i][j] == compare[j]:
        fitness += 1
    matriz[i].append(fitness)
    matriz[i][d] = fitness
    fitness = 0
  return matriz
