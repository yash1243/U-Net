# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 18:45:41 2019

@author: pyash
"""
import os 

path = next(os.walk('C:\\Users\\pyash\\Desktop\\dataset\\Testing'))[2]
print(path)

for f in path:
    os.makedirs(f[:-4])
    #os.makedirs(f + '_mask')
    
