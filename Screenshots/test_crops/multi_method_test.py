import numpy as np
from pytesseract import Output,image_to_data
import cv2
#from matplotlib import pyplot as plt


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated


def pre_processing(file):
    d = image_to_data(file, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(file, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('img', file)
    cv2.waitKey(0)


img = cv2.imread('final_pillow_crop_only_num.jpg')
gs = remove_noise(get_grayscale(img))
pre_processing(gs)


'''titles = ['Original Image', 'Greyscale',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, gs, th2, th3]'''
