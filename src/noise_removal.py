# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:28:58 2019

@author: fahim
"""

def color_gaussian(path,dest,mydir):  
    import cv2 as cv
    from matplotlib import pyplot as plt
    output=mydir 
    Input=output
    
    img = cv.imread(Input)
    #img = cv.cvtColor(img, cv.COLOR_BGR2HSV) # convert to HSV
    figure_size = 3 # the dimension of the x and y axis of the kernal.
    dst = cv.fastNlMeansDenoisingColored(img,None,10,10,1,21)

#    
    from PIL import Image
    im = Image.fromarray(dst)
    im.save(output)
 # the dimension of the x and y axis of the kernal.
def gray_gaussian(path,dest,mydir):  
    import cv2 as cv
    from matplotlib import pyplot as plt
    output=mydir
    Input=output

    img = cv.imread(Input)
    dst = cv.fastNlMeansDenoising(img,None,10,1,21)
#    plt.subplot(121),plt.imshow(img)
#    plt.subplot(122),plt.imshow(dst)
#    
#    plt.show()
    
    from PIL import Image
    im = Image.fromarray(dst)
    im.save(output)
    
def colorgray_salt(path,dest,mydir):
    import cv2
    from matplotlib import pyplot as plt
    from PIL import Image
    #%matplotlib inline
    output=mydir
    Input=output

    image = cv2.imread(Input) # reads the image
    #image2= cv2.imread('result.PNG')
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # convert to HSV
    figure_size = 3
    new_image = cv2.medianBlur(image, figure_size)
    im = Image.fromarray(new_image)
    im.save(output)