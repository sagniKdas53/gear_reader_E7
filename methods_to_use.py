import cv2
import pytesseract

img = cv2.imread('final_pillow_crop_only_num.jpg')

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
# cv2.waitKey(0)


'''https://www.youtube.com/watch?v=Bbc4RzTTLec
https://www.google.com/search?client=ubuntu&hs=Eb5&channel=fs&sxsrf=ALeKk033-IovQ28slbCdMxnSb_b4onHC1g:1601651743733&q=tesseract+read+text+from+image&spell=1&sa=X&ved=2ahUKEwigvPTZmZbsAhWTUn0KHb6LDtEQBSgAegQIGRAq&biw=1360&bih=576
https://pypi.org/project/pytesseract/
https://nanonets.com/blog/ocr-with-tesseract/
https://tesseract-ocr.github.io/tessdoc/ImproveQuality#binarisation
https://www.flameeyes.com/projects/unpaper
'''