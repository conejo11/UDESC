import random
import math as mt
import variaveis as var
import functools

# SELECAO NATURAL
# Selecao Roleta
def selectRouletteLinearScaling(matriz,pop,d,ce):
  matfit=[]
  newFit=[]
  relativeFit=[]
  for i in range(pop):
    matfit.append(matriz[i][d])
  minFit=99999
  maxFit=0
  avgFit=0
  fitsom=0
  for i in range(pop):
    if(matfit[i]>maxFit):
      maxFit=matfit[i]
    if(matfit[i]<minFit):
      minFit=matfit[i]
    fitsom=fitsom+matfit[i]
  avgFit=fitsom/pop
  alpha=0
  beta=0
  if(minFit>(ce*avgFit-maxFit/(ce-1))):
    alpha=(avgFit*(ce-1))/(maxFit-avgFit)
    beta=(avgFit*(maxFit-ce*avgFit))/(maxFit-avgFit)
  else:
    alpha=avgFit/(avgFit-minFit)
    beta=(-minFit*avgFit)/(avgFit-minFit)
  for i in range(pop):
    meufit=matfit[i]
    novofit=meufit*alpha+beta
    newFit.append(novofit)
    if(i>=1):
      relativeFit.append((novofit/fitsom)+relativeFit[i-1])
    else:
      relativeFit.append(novofit/fitsom)
  num = random.random()
  for i in range(pop):
    if(relativeFit[i]>num):
      return i

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
      # print(best) 
      index = i
  for i in range(d):
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