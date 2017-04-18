import random
import math as mt

generations = 100
k = 2
pop_size = 50
d_size = 36
bounds = [-50,50]

elitism = True
# elitism = False

# 1 = Roullette, 2 = Tournament
# selection = 1
selection = 2

# 1 = bitsAlternados, 2 = Pares Alternados, 3 = max x^2, 4 = Radio, 5 = padrao grafico
# problem = 1
# problem = 2
# problem = 3
# problem = 4
problem = 5

# 1 = onePoint; 2 = Uniform; 3 = BLX; 4 = Average; 5 = PLX
cover = 1
# cover = 2
# cover = 3
# cover = 4
# cover = 5

# 1 = bitFlip; 2 = randMutation; 3 = deltaMutation; 4 = gaussianMutation; 5 = swapPositions
mutar = 1
# mutar = 2
# mutar = 3
# mutar = 4
# mutar = 5


# cod = 0
# cod = 0.0
cod = False
