import random
import math as mt

generations = 1000
k = 5
pop_size = 70
d_size = 64
bounds = [-50,50]

elitism = True
# elitism = False

# 1 = Roullette, 2 = Tournament
# selection = 1
selection = 2

# Linear Scaling
linearScaling = True
# linearScaling = False

# 1 = Bits Alternados, 2 = Pares Alternados, 3 = sphere min , 4 = Radio, 5 = Graphic Pattern, 6 = N - Queens
# problem = 1
# problem = 2
# problem = 3
# problem = 4
# problem = 5
problem = 6

# 1 = onePoint; 2 = Uniform; 3 = BLX; 4 = Average; 5 = PMX
# cover = 1
# cover = 2
# cover = 3
# cover = 4
cover = 5

# 1 = bitFlip; 2 = randMutation; 3 = deltaMutation; 4 = gaussianMutation; 5 = swapPositions
# mutar = 1
# mutar = 2
# mutar = 3
# mutar = 4
mutar = 5


cod = 0
# cod = 0.0
# cod = False
