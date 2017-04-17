import random
import math as mt
import variaveis as var

# SELECAO NATURAL
# Selecao Roleta

def selectRoulette(matriz, pop, d):
  submat = []
  submat2 = []
  soma = 0
  somaProb = 0
  j = -1
  for i in range(pop):
    submat.append(matriz[i][d])  
  for i in range(pop):
    soma += submat[i]
  compare = random.uniform(0,soma)
  current = 0
  j = -1
  for i in range(pop):
    current += submat[i]
    if current > compare:
      return i 

# selecao torneio
def selectTournament(matriz,pop,d,k):
  best = -1
  submat = []
  j = -1
  for z in range(pop):
    submat.append(matriz[z][d])
  for i in range(k):
    z = random.randint(0,d-1)
    if submat[z]>best:
       best = submat[z]
       j = z
  return(j)

def elit(matriz,pop,d):
  submat = []
  best = -1
  submat2 = []
  index = -1
  for i in range(d):
    submat.append(matriz[i][d])
  for i in range(d):
    if submat[i] > best:
      best = submat[i]
      index = i
  for i in range(d+1):
    submat2.append(matriz[index][i])
  return submat2

def getWorst(matriz,pop,d):
  submat = []
  best = 90000
  j = -1
  for i in range(pop):
    submat.append(matriz[i][d])
  for i in range(d):
    if submat[i] < best:
      best = submat[i]
      j = i
  return j