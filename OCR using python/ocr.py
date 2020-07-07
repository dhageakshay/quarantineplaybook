import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'
img=Image.open("C:/Users/Zeus/Documents/qurantineplaybook/OCR using python/OCR_Image.png")

text=pytesseract.image_to_string(img)
print(text)