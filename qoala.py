from PIL import Image
import pytesseract

def ocr_core(filename):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    
    text = pytesseract.image_to_string(Image.open(filename))
    return text
    
a = ocr_core("C:\\Users\\adity\\Downloads\\thai_id.jpeg").lower().split("\n")

import re

def get_id(inputs):
    id = None
    for i in inputs:
        x = re.search(r"[0-9]\s[0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9]\s[0-9][0-9]\s[0-9]", i)
        if x is not None:
            id = x.group()

    return id


def get_name(inputs):
    for i in inputs:
        if "name " in i and not "lastname" in i:
            return i[i.index("name ")+5:]

def last_name(inputs):
    for i in inputs:
        if "lastname " in i:
            return i[i.index("lastname ")+9:]
        if "last name " in i:
            return i[i.index("lastname ")+10:]



print("id: ",get_id(a))
print("name: ",get_name(a))
print("last name: ",last_name(a))