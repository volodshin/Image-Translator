from config import headers, url
import requests
from PIL import Image
import pytesseract
import PySimpleGUI as sg
import io, os


#Path to tesseract(Only for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

sg.theme('dark grey 9')

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

#Interface loyout
layout = [
	[sg.Text("Choose your image")],
    [sg.Input(key='-file-'), sg.FileBrowse(file_types=file_types)],
    [sg.OptionMenu(values=['en', 'uk', 'pl', 'fr', 'de'], default_value = 'en', key='-TEXT_LANG-'), sg.Push(),
    sg.OptionMenu(values=['en', 'uk', 'pl', 'fr', 'de'], default_value = 'en', key='-TRANSLATE_LANG-')],
    [sg.Multiline(size=(60, 15), key="-IMGTXT-"), sg.Multiline(size=(60, 15), key='-OUTPUT-')],
    [sg.Button('Translate'), sg.Push(), sg.Button('Quit')]]

# Create the window
window = sg.Window('Tanslate', layout, size=(900, 400))



# Display and interact with the Window using an Event Loop
while True:
	event, values = window.read()
	if event == sg.WINDOW_CLOSED or event == 'Quit':
		break

	img_path = values['-file-']
	img_file = f'{img_path}'

	img = Image.open(img_file)

	text_lang = values['-TEXT_LANG-']
	translate_lang = values['-TRANSLATE_LANG-']

	#Convert image text to str
	result = pytesseract.image_to_string(img, lang=f'{text_lang}')

	#API translate
	payload = {
	"text": f"{result}",
	"source": f"{text_lang}",
	"target": f"{translate_lang}"
	}

	#Get translation from json
	response = requests.request("POST", url, json=payload, headers=headers)
	data = response.json()
	text = data['translations']['translation']

	#Upload text on the screen
	window['-IMGTXT-'].update(f'{result}')
	window['-OUTPUT-'].update(f'{text}')


window.close()