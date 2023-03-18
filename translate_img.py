import requests
from PIL import Image
import pytesseract
img_file = 'photo_2.jpg'

img = Image.open(img_file)

custom_config = r'-l ukr+eng'
result = pytesseract.image_to_string(img, config=custom_config)

url = "https://long-translator.p.rapidapi.com/translate"

payload = "source_language=auto&target_language=us&text={}".format(result)
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "ff2c859cf0msh6ab4cd32f934a2dp1a52a8jsn039fdc4a2f6a",
	"X-RapidAPI-Host": "long-translator.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
data = response.json()

translation = data["translatedText"]

print(translation)