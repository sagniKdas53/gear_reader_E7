import cv2 as cv
import numpy as np


def img_box(inp_i, inp_t1, inp_t2, op_tmp):
    img_rgb = cv.imread(inp_i)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    templatel = cv.imread(inp_t1, 0)
    templater = cv.imread(inp_t2, 0)
    wl, hl = templatel.shape[::-1]
    wr, hr = templater.shape[::-1]
    resl = cv.matchTemplate(img_gray, templatel, cv.TM_CCOEFF_NORMED)
    resr = cv.matchTemplate(img_gray, templater, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc_l = np.where(resl >= threshold)
    loc_r = np.where(resr >= threshold)
    #print(loc_l, '\n', loc_r)
    for pt in zip(*loc_r[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + wr, pt[1] + hr), (0, 0, 255), 2)
    for pt in zip(*loc_l[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + wl, pt[1] + hl), (0, 0, 255), 2)
    #print(loc_l[0][0], '\n', loc_r[0][0])
    cv.imwrite(op_tmp, img_rgb)


#img_box('Screenshots/left_visible,init_stat,some_other_false.jpg','Screenshots/top_left.jpg',
#        'Screenshots/top_right.jpg','Screenshots/MetCr1.jpg')
#img_box('Screenshots/left_visible,init_stat,some_other_false.jpg','Screenshots/res.jpg',
#        'Screenshots/top_right.jpg','Screenshots/MetCr2.jpg')
#img_box('Screenshots/left_visible,increase_stat,some_other_false.jpg','Screenshots/res.jpg',
#        'Screenshots/top_right.jpg','Screenshots/MetCr3.jpg')
#img_box('Screenshots/left_hidden,decrease_stat,some_other_true.jpg','Screenshots/res.jpg',
#        'Screenshots/top_right.jpg','Screenshots/MetCr4.jpg')
