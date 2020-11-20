import cv2 as cv
import numpy as np
from PIL import Image

img_rgb = cv.imread('Screenshots/left_hidden,decrease_stat,some_other_true.jpg', 0)
img_rg = cv.imread('Screenshots/left_hidden,decrease_stat,some_other_true.jpg')
img_gray = cv.cvtColor(img_rg, cv.COLOR_BGR2GRAY)
templatel = cv.imread('Screenshots/top_left.jpg', 0)
templater = cv.imread('Screenshots/top_right.jpg', 0)
wi, hi = img_rgb.shape[::-1]
wl, hl = templatel.shape[::-1]
wr, hr = templater.shape[::-1]
resl = cv.matchTemplate(img_gray, templatel, cv.TM_CCOEFF_NORMED)
resr = cv.matchTemplate(img_gray, templater, cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc_l = np.where(resl >= threshold)
loc_r = np.where(resr >= threshold)

im = Image.open('Screenshots/left_hidden,decrease_stat,some_other_true.jpg')
im.crop((loc_l[0][0], loc_r[0][0], hi, hi)).save('cropped.jpg', quality=95)


def make_rect():
    for pt in zip(*loc_r[::-1]):
        cv.rectangle(img_rg, pt, (pt[0] + wr, pt[1] + hr), (0, 0, 255), 2)
        cv.rectangle(img_rg, pt, (pt[0] + wr + hi, pt[1] + hr + hi), (0, 0, 255), 2)
    for pt in zip(*loc_l[::-1]):
        cv.rectangle(img_rg, pt, (pt[0] + wl, pt[1] + hl), (0, 0, 255), 2)
        cv.rectangle(img_rg, pt, (pt[0] + wl + hi, pt[1] + hl + hi), (0, 0, 255), 2)
    cv.imwrite('squared_output.png',img_rg)


def verbose():
    print(loc_l, '\n', loc_r)
    print(loc_l[0][0], '\n', loc_r[0][0], '\n', hi, '\n', hi)