import pyperclip
text = pyperclip.paste().replace('- \n', ' ').replace('-\n', ' ').replace('\n', ' ')
pyperclip.copy(text)
print(text)