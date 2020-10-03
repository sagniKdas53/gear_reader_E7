import cv2 as cv
#import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('final_pillow_crop_only_num.jpg', 0)
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY, 11, 2)
plt.imshow(th3, 'gray')
plt.show()

