# Gabriel Guebarra Conejo e Rafael Rizzatti

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from matplotlib import cm
import time as tm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from matplotlib import cm
import time as tm
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
import operator
import functools
# -*- coding: cp1252 -*-
from PIL import Image

def equalize(h):
  l = []
  for i in range(0, len(h), 256):
    step = functools.reduce(operator.add, h[i:i+256])/255
    n = 0
    for j in range(256):
      l.append(n/step)
      n = n+h[j+i]
  return l

def linearf(x):
  x = x/256
  return int((1.3*x)*256)

x = sys.argv[1]

if x == "rins":
  final = Image.open('rins1.jpg')
elif x == "aorta":
  final = Image.open('aorta1.jpg')

l = equalize(final.histogram())
final = final.point(l)
final.save("equalizedImage.jpg")

final2 = Image.open("equalizedImage.jpg")
(l,h)= final2.size
Iout=Image.new(final2.mode, (l,h))

for j in range(0, h):
    for i in range(0, l):
        val=linearf(final2.getpixel((i,j))[0])
        if x == "rins":
          temp = cm.RdGy(val)
        elif x == "aorta":
          temp= cm.RdGy_r(val) 
        temp =(np.uint8(255*(np.asarray(temp[0:3])))) 
        Iout.putpixel((i,j),(temp[0],temp[1],temp[2]))

Iout.save("realced","JPEG")