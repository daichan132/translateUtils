from PIL import ImageGrab
import pyocr
import pyperclip
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
img = ImageGrab.grabclipboard()
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
tools = pyocr.get_available_tools()
tool = tools[0]
text = tool.image_to_string(img, lang="eng", builder=builder)
text = text.replace('- \n', ' ').replace('-\n', ' ').replace('\n', ' ')
data = {
    "auth_key": os.environ['API_KEY'],
    "text": text,
    "target_lang": "JA",
}
response = requests.post("https://api-free.deepl.com/v2/translate", data=data)
translatedText = json.loads(response.text)['translations'][0]['text']

pyperclip.copy(text+"\n"+translatedText)
print(text)
print("================")
print(translatedText)

