# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 20:20:57 2019

@author: fahim
"""


from PIL import ImageTk, Image


from PIL import Image

def rotate_180(path,dest,mydir):
    output=mydir
    Input=output
    colorImage  = Image.open(Input)
    rotated     = colorImage.rotate(180)
    rotated.save(output)    
    print("Done 180")

def rotate_90(path,dest,mydir):
    output=mydir 
    Input=output    
    colorImage  = Image.open(Input)
    rotated     = colorImage.transpose(Image.ROTATE_270)
    rotated.save(output)
    print("Done 90")

def rotate_270(path,dest,mydir):
    output=mydir
    Input=output
    colorImage  = Image.open(Input)
    transposed  = colorImage.transpose(Image.ROTATE_90)
    transposed.save(output)
    print("Done 270")

#global path
#path='indicator.png'
#rotate_180()
#rotate_270()
#rotate_90()
