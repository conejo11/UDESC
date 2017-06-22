import random
import math as mt
import numpy as np
import variaveis as var

def getGap(matriz, percent,pop,d):
  x = []
  for i in range(percent):
    x.append([matriz[i][j] for j in range(d)])
  return x

# def sharing(matriz,pop,d): ARRUMARRRRRRRRR
#   alpha = 1.05
#   sigma = 0.255

#   dists = [[0 for i in range(pop)] for j in range(pop)]
#   sd = [[0 for i in range(pop)] for j in range(pop)]

#   for i in range(1,pop):
#     for j in range(1,pop):
#       if j>i:
#         continue
#       else:
#         dists[j][i] = dists[i][j] = abs(matriz[i][d] - matriz[j][d])

#   maxi = max(dists)
#   dists = dists ./ maxi

#   for i in range(1,pop):
#     for j in range(1,pop):
#       if j>i:
#         continue
#       else:
#         if dists[i][j] > sigma:
#           sd[i][j] = 0.0
#           sd[j][i] = 0.0
#         else:
#           sd[i][j] = 1.0 - ((dists[i][j]/sigma)**alpha)
#           sd[j][i] = 1.0 - ((dists[i][j]/sigma)**alpha)

#   for i in range(pop):
#     matriz[i][d] = matriz[i][d]/sum([(sd[i][j]) for j in range(pop)])

def crowding():
  pass