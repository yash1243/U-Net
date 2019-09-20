# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:38:39 2019

@author: pyash
"""

import os 

path = r'C:\\Users\\pyash\\Desktop\\dataset\\train\\'
list = os.listdir(path)
for i in list:
    mask_path = r'C:\\Users\\pyash\\Desktop\\dataset\\train\\' + i + '\\\\' + i + '_mask\\\\' + i + '.png'
    os.remove(mask_path)
