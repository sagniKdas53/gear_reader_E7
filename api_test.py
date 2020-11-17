import requests
from api_key import give_key
import re


def ocr_space_file(filename, overlay=False, api_key=give_key(), language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


file = ocr_space_file(filename='initial_pillow_crop_only_num.jpg', language='eng')
print(file)
t = re.search(r'\"ParsedText\":\"([0-9\\r\\n.%]*)\"', file)
print(t)
