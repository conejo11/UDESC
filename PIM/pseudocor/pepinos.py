import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy.random import randn
from matplotlib import cm
# -*- coding: cp1252 -*-
from PIL import Image

#
# utilizando um mapa de cores do python (gist_ncar) e aplicando 
# sobre uma imagem
# 


pil1=Image.open('pepinos.jpg')#('lenaShort.jpg')#(vermelho.jpg')#('mandril.jpg')#('lena.pgm')
(l,h)=pil1.size
print(l,h)

Iout=Image.new('RGB', (l,h))


for j in range(0, h):
    for i in range(0, l):
        val=pil1.getpixel((i,j))
        temp= cm.nipy_spectral(val) # << utilizando o mapa de cores gist_ncar 
        temp =(np.uint8(255*(np.asarray(temp[0:3])))) # valores mapeados sao normalizados e convertidos para inteiros
        #print temp
        Iout.putpixel((i,j),(temp[0],temp[1],temp[2]))
               
        
Iout.save("Iout.jpg","JPEG")


data = np.asarray(Iout)
fig, ax = plt.subplots()
cax = ax.imshow(data, interpolation='nearest', cmap=cm.gist_ncar)
cbar = fig.colorbar(cax, ticks=[0, 128, 255])
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
plt.show()



