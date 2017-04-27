# Gabriel Guebarra Conejo e Rafael Rizzatti

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from matplotlib import cm
import time as tm
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
# -*- coding: cp1252 -*-
from PIL import Image

pil1=Image.open('low.jpg')
# pil1=Image.open('high.jpg')
(l,h)=pil1.size
print(l,h)

Iout=Image.new('RGB', (l,h))

n=pil1.histogram()

narray = np.asarray(n)
p=np.float32(narray)/(l*h)
print((l*h))
b2=plt.bar(range(256),p)

data = np.asarray(Iout)
plt.savefig("contrastHistogram.jpg")
