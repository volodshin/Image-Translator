   ## Image Translator
   **Installation**
 1. Clone my repository:
 

    git clone https://github.com/volodshin/Image-Translator.git

 2. Download requirement libraries:


 

    `pip install -r requirements.txt`
  3. Install Tesseract-OCR on your OS: https://tesseract-ocr.github.io/tessdoc/Installation.html

****
**Add new language**

 If you want to add new language, download from here: https://github.com/tesseract-ocr/tessdata,
 and place in /Tesseract-OCR/tessdata
 
**⛔Importantly⛔**

Rename your all language file from ISO 639-2 to ISO 639-1 **(eng.traineddata to en.traineddata)**, because API does not accept ISO 639-2 languages code.

Also you need add to the window interface new language. 
To do this add to list your language in ISO 639-1 code:

    sg.OptionMenu(values=['en', 'uk', 'pl', '<your language>'])
   *****
  **API**

I use free API from rapidapi.com. 
Link: https://rapidapi.com/sohailglt/api/translate-plus.

But if you want use another API, change url and headers in config.py file. 

Enjoy!