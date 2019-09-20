# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:13:38 2019

@author: pyash
"""

import os

path = r'C:\\Users\\pyash\\Desktop\\Labels - ns104a (from 1-4) and ns104c'
list = os.listdir(path)
for name in list:
  os.rename(path + '\\' + name, name[:-4] + '_resized_512.png')
