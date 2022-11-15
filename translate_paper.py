import fitz
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
pdf_file_path = "./pdf/11533719_21.pdf"
output_file_path = "./md/11533719_21.md"
page_num = 1
with fitz.open(pdf_file_path) as pdf_in:

    text = ""
    for page in pdf_in:
        page1 = page.get_text()

        data = {
            "auth_key": os.environ['API_KEY'],
            "text": page1.replace("-\n", "").replace("\n", ""),
            "target_lang": "JA",
        }

        response = requests.post("https://api-free.deepl.com/v2/translate", data=data)
        d = json.loads(response.text)
        _text = f"""### Page{page_num}\n{d['translations'][0]['text']}\n"""
        text = text + _text
        page_num += 1

with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(text)
