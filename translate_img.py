import requests
from PIL import Image
import pytesseract
img_file = 'photo_1.jpg'

img = Image.open(img_file)

result = pytesseract.image_to_string(img, lang='ukr+eng')


url = "https://translate-plus.p.rapidapi.com/translate"

payload = {
	"text": f"{result}",
	"source": "uk",
	"target": "en"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "02fbd95b13msha8c91940307c8fap10f6d0jsnb7cc0aad5df9",
	"X-RapidAPI-Host": "translate-plus.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)
data = response.json()

text = data['translations']['translation']


print(text)