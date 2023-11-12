
# Chuyển ảnh sang ảnh đen trắng
import cv2
import pytesseract

# Đặt đường dẫn tới tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Cong Dinh\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Đường dẫn tới tệp ảnh
image_path = 'bottom_left_part.jpg'

# Đọc ảnh với OpenCV
img = cv2.imread(image_path)

# Chuyển ảnh sang ảnh đen trắng
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Trích xuất văn bản với pytesseract
text = pytesseract.image_to_string(gray)

# In kết quả
print(text)
