import random
import math as mt
import variaveis as var

# SELECAO NATURAL
# Selecao Roleta
def selectRoulette(matriz, pop, d):
  submat = []
  submat2 = []
  summ = 0
  for i in range(pop):
    submat.append(matriz[i][d])
  for i in range(pop):
    summ = summ + submat[i]
  for i in range(pop):
    submat2.append(submat[i]/summ)
  y = random.random()
  i = 0
  while True:
    if y<submat2[i]:
      return i
    else:
      y = y-submat2[i]
      i = i+1

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
  #print(best)
  #print(j)
  return(j)