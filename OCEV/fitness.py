import random
import math as mt
import variaveis as var
import string
import functools as ft

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
      fitness = fitness + (matriz[i][j]*matriz[i][j])
    gt.append(fitness)
    fitness = 0.0
  for i in range(pop):
    # print(gt)
    fit = 1.0-(gt[i]/max(gt))
    matriz[i].append(fit)
    matriz[i][d] = fit
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

# N - Queens
def nQueens(matriz,pop,d):
  fitness = 0.0
  collision = 0.0
  submat = []
  for i in range(pop):
    for j in range(d - 1):
      for k in range((j+1),d):
        if abs(matriz[i][j] - matriz[i][k]) == abs(k - j):
          collision += 1.0
    fitness = 1.0 - (collision/d)
    matriz[i].append(fitness)
    submat = []
    fitness = 0.0
    collision = 0.0
  return matriz

# DECEPTIVE FUNCTIONS
f3_size = 10
deceptiveN_size = 16
deceptiveN_nbits = 4

def evalF3(vet):
  if   vet==[0,0,0]:
    return 28
  elif vet==[0,0,1]:
    return 26
  elif vet==[0,1,0]:
    return 22
  elif vet==[1,0,0]:
    return 14
  elif vet==[1,1,1]:
    return 30
  else:
    return 0
  return 0

# F3
def f3(matriz,pop,d):
  for i in range(pop):
    fitness = 0.0
    gens = []
    gens = [j for j in matriz[i]]
    for k in range(f3_size):
      fitness += evalF3(gens[(k)*3:(k+1)*3])
    matriz[i].append(fitness)
    matriz[i][d] = fitness
  return matriz

# F3S
def f3s(matriz,pop,d):
  for i in range(pop):
    fitness = 0.0
    gens = []
    gens = [j for j in matriz[i]]
    for k in range(f3_size):
      fitness += evalF3([gens[k],gens[k+f3_size], gens[k+2*f3_size]])
    matriz[i].append(fitness)
    matriz[i][d] = fitness
  return matriz

# Deceptive N
def deceptiveN(matriz,pop,d):
  for i in range(pop):
    fitness = 0.0
    gens = []
    gens = [j for j in matriz[i]]
    for k in range(deceptiveN_size):
      v = sum(gens[(k)*deceptiveN_nbits:(k+1)*deceptiveN_nbits])
      if v == 0:
        fitness += deceptiveN_nbits+1
      else:
        fitness += v
    matriz[i].append(fitness)
    matriz[i][d] = fitness
  return matriz  