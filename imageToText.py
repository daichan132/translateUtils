from PIL import ImageGrab
import pyocr
import pyperclip

img = ImageGrab.grabclipboard()
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
tools = pyocr.get_available_tools()
tool = tools[0]
text = tool.image_to_string(img, lang="eng", builder=builder)
text = text.replace('- \n', ' ').replace('-\n', ' ').replace('\n', ' ')
pyperclip.copy(text)
print(text)