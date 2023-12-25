import pytesseract
import re
import cv2 as cv
import os

# load tesseract to process the image
def ocr_core(image_data):
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    text = pytesseract.image_to_string(image_data)
    return text
    

# function to extract the id from the array of values
def get_id(inputs):
    id = None
    for i in inputs:
        x = re.search(r"[0-9]\s[0-9][0-9][0-9][0-9]\s[0-9][0-9][0-9][0-9][0-9]\s[0-9][0-9]\s[0-9]", i)
        if x is not None:
            id = x.group()

    return id

# function to extract the name from the array of values
def get_name(inputs):
    for i in inputs:
        if "name " in i and not "lastname" in i:
            return i[i.index("name ")+5:]

# function to extract the last name from the array of values
def last_name(inputs):
    for i in inputs:
        if "lastname " in i:
            return i[i.index("lastname ")+9:]
        if "last name " in i:
            return i[i.index("last name ")+10:]
        
# function to extract the dates from the array of values
def dates(inputs):
    dats = []
    regex_statement = r"[0-9][0-9]\s[a-z][a-z][a-z]\,\s[0-9][0-9][0-9][0-9]|[0-9][0-9]\s[a-z][a-z][a-z]\.\s[0-9][0-9][0-9][0-9]"
    for i in inputs:
        for m in re.finditer(regex_statement,i):
            # print(m.start(), m.end())
            dats.append(i[int(m.start()): int(m.end())+1].replace(",","").replace(".",""))
    return dats



def process_image(image_data):
    
    status = False
    image_path = os.getcwd()+"\\ocr_images\\"+str(image_data)

    # load image to open to to make it binary with the set threshold
    img = cv.imread(image_path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray, 115, 255, cv.THRESH_BINARY)

    cv.imwrite(image_path, thresh) #save image to the same name and location 
    
    # extract text from tesseract
    ocr_text = ocr_core(image_path).lower().split("\n")

    # error handling of the resulting data
    try:
        id_number = get_id(ocr_text)
    except:
        return "Error"
    try:
        name = get_name(ocr_text)
        for i in ["miss","mr","mrs","ms"]:
            if i in name: 
                name.replace(i,i+".")
    except:
        name = "Unknown"
    try:
        last_name_value = last_name(ocr_text)
    except:
        last_name_value = "Unknown"
    try:
        dats = dates(ocr_text)
        if len(dats) == 3:
            status = True
        elif len(dats) == 2:
            dats.append("-")
        elif len(dats)>3:
            dats = dats[1:]
            status = True
        elif len(dats) == 1:
            dats.append("-")
            dats.append("-")
        else:
            dats = ["-","-","-"]
    except:
            dats = ["-","-","-"]
        
    result = {
        'id': id_number,
        'name': name,
        'last_name': last_name_value,
        'date-of-birth' : dats[0],
        'date-of-issue': dats[1],
        'date-of-expiry': dats[2],
        "status":status
    }

    return result, " ".join(ocr_text)