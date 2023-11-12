import pytesseract
from PIL import Image

# Mở ảnh
img = Image.open('bottom_left_part.jpg')

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Cong Dinh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(img)


# In kết quả
print(text)
