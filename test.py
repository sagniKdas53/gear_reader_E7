import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

print(pytesseract.image_to_string(r'final_pillow_crop_only_num.jpg'))