from PIL import Image
import pytesseract

img_file = 'photo_1.jpg'

img = Image.open(img_file)

custom_config = r'-l ukr+eng'
result = pytesseract.image_to_string(img, config=custom_config)

print(result)