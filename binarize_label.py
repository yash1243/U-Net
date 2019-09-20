'''
This code resizes, converts and saves the bolus label images from ImageJ to binary format.
'''

from PIL import Image
import os
import numpy as np
import glob


# Change the directories according to your dataset.


listdir = ['C:\\Users\\Handenur Caliskan\\Desktop\\reliability\\Labels - ns104a (from 1-4) and ns104c/*.png']

for m in range(0, len(listdir)):
    filelist = glob.glob(listdir[m])  
    for i in range(0, len(filelist)):
            img = Image.open(filelist[i])
            img_name = os.path.splitext(os.path.basename(filelist[i]))[0]
            
            #uncomment to binarize the label---------------

            thresh = 200
            fn = lambda x : 255 if x > thresh else 0
            r = img.convert('L').point(fn, mode='1')
            #r.save(img_name + '.png')
            
            #uncomment to resize the label or the frame-------------

            r = r.resize((512,512))
            r.save(img_name +'_resized_512.png')




