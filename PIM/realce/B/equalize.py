# Gabriel Guebarra Conejo e Rafael Rizzatti

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from matplotlib import cm
import time as tm
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import operator
# -*- coding: cp1252 -*-
from PIL import Image

pil1=Image.open('baixoContraste.jpg')
# pil1=Image.open('figuraCinza.jpg')
# pil1=Image.open('figuraEscura.jpg')
(l,h)=pil1.size
Iout=Image.new(pil1.mode, (l,h))

histogram=pil1.histogram()
narray = np.asarray(histogram)
p=np.float32(narray)/(l*h)
b2=plt.bar(range(len(p)), p)
data = np.asarray(Iout)
plt.savefig("oldHistogram.jpg")

def equalize(h):
  l = []
  for i in range(0, len(h), 256):
    step = reduce(operator.add, h[i:i+256])/255
    n = 0
    for j in range(256):
      l.append(n/step)
      n = n+h[j+i]
  return l

final = Image.open('baixoContraste.jpg')
# final = Image.open('figuraCinza.jpg')
# final = Image.open('figuraEscura.jpg')
l = equalize(final.histogram())
final = final.point(l)
final.save("equalizedImage.jpg")

(l,h)= final.size
hist = final.histogram()
narray = np.asarray(hist)
p=np.float32(narray)/(l*h)
b2=plt.bar(range(len(p)), p)
data = np.asarray(Iout)
plt.savefig("equalizedHistogram.jpg")
