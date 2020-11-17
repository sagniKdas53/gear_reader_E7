from PIL import Image

im = Image.open('Screenshots/Screenshot_.jpg')

im.crop((185, 605, 590, 935)).save('initial_pillow_crop.jpg', quality=95)

im.crop((450, 605, 590, 935)).save('initial_pillow_crop_only_num.jpg', quality=95)

im.crop((715, 605, 1020, 935)).save('final_pillow_crop.jpg', quality=95)

im.crop((715, 605, 835, 935)).save('final_pillow_crop_only_num.jpg', quality=95)
