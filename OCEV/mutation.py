import random
import math as mt
import variaveis as var

#PROBABILIDADE MUTACAP
def mut():
  x = 0.05
  y = random.random()
  if x > y:
    return True
  else:
    return False

# MUTACAO
# BINARIO
def bitFlip(valorMat):
  if valorMat == 1:
    valorMat = 0
  elif valorMat == 0:
    valorMat = 1
  return valorMat

# INTEIRO
def randMutation(valorMat,d):
  ran = random.randint(1,d)
  valorMat = ran
  return valorMat


# REAL
def deltaMutation(valorMat):
  prob = random.choice([0,1])
  if prob == 0:
    u = valorMat + (random.uniform(var.bounds[0],var.bounds[1])/10)
    valorMat = u
  if prob == 1:
    u = valorMat - (random.uniform(var.bounds[0],var.bounds[1])/10)
    valorMat = u
  return valorMat

def gaussianMutation(valorMat):
  x1 = random.random()
  x2 = random.random()
  if x1 == 0:
    x1 = 1
  if x2 == 0:
    x2 = 1
  y1 = mt.sqrt(-2.0 * mt.log(x1)) * mt.cos(2.0 * mt.pi * x2)
  final = y1 * 0.1 + valorMat
  valorMat = final


  return valorMat

# PERMUTACAO
def swapPositions(matriz,posI,posJ,d):
  change = random.randint(0,(d-1))
  aux = matriz[posI][posJ]
  aux2 = matriz[posI][change]
  matriz[posI][posJ] = aux2
  matriz[posI][change] = aux
  return matriz
  

