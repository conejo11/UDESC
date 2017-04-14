import random
import math as mt
import variaveis as var

# PUPULACAO INICIAL
# INTEIRO
def randomPopINT(pop,d):
  randomPop = []
  items = []
  x = 1
  for i in range (d):
    items.append(x)
    x += 1
  for j in range(pop):
    random.shuffle(items)
    randomPop.append([items[i] for i in range(d)])
  return randomPop

# REAL
def randomPopFLOAT(pop,d,bound):
  randomPop = []
  for j in range(pop):
    randomPop.append([random.uniform(bound[0],bound[1]) for i in range(d)])
  return randomPop

# BINARIA
def randomPopBIN(pop,d):
  randomPop = []
  for j in range(d*pop):
    randomPop.append([random.choice([1,0]) for i in range(d)])
  return randomPop

def randomPopulation(cod,pop,d,bound):
  if type(cod) is bool:
    return randomPopBIN(pop,d)
  elif type(cod) is int:
    return randomPopINT(pop,d)
  elif type(cod) is float:
    return randomPopFLOAT(pop,d,bound)