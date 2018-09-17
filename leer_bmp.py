#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 06:52:07 2018

@author: eddy
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
data_byte = np.fromfile('imagen1.bmp', dtype='uint8')

print (len(data_byte))
data_Header=data_byte[0:14]
data_InfoHeader=data_byte[14:54] #14 - 14+40bytes

   
HeaderSize= int.from_bytes(data_byte[14:18], byteorder='little') 
BitmapWidth= int.from_bytes(data_byte[18:22], byteorder='little')
BitmapHeight= int.from_bytes(data_byte[22:26], byteorder='little')
Planos= int.from_bytes(data_byte[26:28], byteorder='little') 
BitCount= int.from_bytes(data_byte[28:30], byteorder='little')
Compression= int.from_bytes(data_byte[30:34], byteorder='little')
ImageSize= int.from_bytes(data_byte[34:38], byteorder='little')

print ("+++ Lector de Imagenes BMP +++")
print ("Width: ", BitmapWidth, "pix")
print ("Height: ", BitmapHeight, "pix")
array = np.array(list(data_byte[14+HeaderSize:]))
#array =  np.diag(array)

#red=np.array(list(data_byte[a:a+b]))
#red=red.reshape(BitmapHeight, BitmapWidth)
#red=np.flipud(red)
Imagen = array.reshape(BitmapHeight, BitmapWidth, 3)
red=Imagen[:,:,0]
red=np.flipud(red)
green=Imagen[:,:,1]
green=np.flipud(green)
blue=Imagen[:,:,2]
blue=np.flipud(blue)

Imagen[:,:,0]=red
Imagen[:,:,1]=green
Imagen[:,:,2]=blue
plt.imshow(Imagen)
im=Image.fromarray(Imagen)
im.show()

