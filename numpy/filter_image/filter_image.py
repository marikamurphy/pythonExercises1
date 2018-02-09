"""
Filter Image
------------

Read in the "dc_metro" image and use an averaging filter
to "smooth" the image.  Use a "5 point stencil" where
you average the current pixel with its neighboring pixels::

              0 0 0 0 0 0 0
              0 0 0 x 0 0 0
              0 0 x x x 0 0
              0 0 0 x 0 0 0
              0 0 0 0 0 0 0

Plot the image, the smoothed image, and the difference between the
two.

Bonus
~~~~~

Re-filter the image by passing the result image through the filter again. Do
this 50 times and plot the resulting image.

See :ref:`filter-image-solution`.
"""

import matplotlib.pyplot as plt
import os
import numpy as np


def filterImage(img):
    img=np.array(img)
    
    img=(img[:-1,:-1]+img[1:,:-1]+img[:-1,1:]+img[1:,1:])/4   
    
    return img

def reFilterImage(img, numTimes):
    newImage=img
    for i in range(50):
        newImage=filterImage(newImage)
    return newImage
    
def findDifference(img1,img2):
    return img1[1:,1:]-img2
        

image=os.path.dirname(__file__)+'/dc_metro.png'
img = np.array(plt.imread(image))
'''
test=[[i for i in range(10)] for i in range(10)]
print(filterImage(test))
'''
plt.subplot(2,2,1)
plt.imshow(img, cmap=plt.cm.hot)
plt.title("Original image")

plt.subplot(2,2,2)
newImg=filterImage(img)
plt.imshow(newImg, cmap=plt.cm.hot)
plt.title("Filtered Image")

plt.subplot(2,2,3)
plt.imshow(findDifference(img,newImg), cmap=plt.cm.hot)
plt.title("Difference Between Images") #????????????

plt.subplot(2,2,4)

plt.imshow(reFilterImage(img,50), cmap=plt.cm.hot)
plt.title("Filtered 50x Image")

plt.show()
