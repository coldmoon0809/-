# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 18:05:49 2020

@author: ACER
"""
from PIL import Image

string= 'cardback\\card_back2_2.jpg'
im = Image.open(string)
(x,y) = im.size 
x_s = 150 #更改照片大小
y_s = 150
out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
out.save(string)