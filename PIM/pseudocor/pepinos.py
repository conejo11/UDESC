# Gabriel Guebarra Conejo e Rafael Rizzatti

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from matplotlib import cm
# -*- coding: cp1252 -*-
from PIL import Image


pil1=Image.open('pepinos.jpg')
(l,h)=pil1.size
print(l,h)

Iout=Image.new('RGB', (l,h))


for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        temp= cm.nipy_spectral(val)
        temp =(np.uint8(255*(np.asarray(temp[0:3])))) 
        Iout.putpixel((i,j),(temp[0],temp[1],temp[2]))
               
        
Iout.save("Iout.jpg","JPEG")


data = np.asarray(Iout)
fig, ax = plt.subplots()
cax = ax.imshow(data, interpolation='nearest', cmap=cm.nipy_spectral)
cbar = fig.colorbar(cax, ticks=[0, 128, 255])
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])
plt.show()



