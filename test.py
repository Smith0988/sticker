import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt Microsoft Edge
driver = webdriver.Edge()

# Mở trang web Postimage
driver.get("https://postimages.org/")

# Sử dụng XPath để tìm nút "Choose Images"
#upload_button = driver.find_element(By.XPATH, "//span[@id='uploadFile']")

# Nhấp vào nút "Choose Images"
#upload_button.click()

wait = WebDriverWait(driver, 60)

# Tạo điều kiện đợi: Đợi cho phần tử được tìm thấy bằng XPath
upload_button  = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='uploadFile']")))
upload_button .click()


# Tải lên tệp ảnh
# Chờ cho hộp thoại mở ra để chọn tệp ảnh
pyautogui.sleep(2)  # Chờ 2 giây

# Ghi đường dẫn tệp cần tải lên
pyautogui.write("D:\\1.Github\sticker\\temp_data\\logo.png")

pyautogui.sleep(2)

# Nhấp Enter để mở tệp
pyautogui.press("enter")

# Tạo một đối tượng WebDriverWait với thời gian tối đa 30 giây
wait = WebDriverWait(driver, 60)

# Tạo điều kiện đợi: Đợi cho phần tử được tìm thấy bằng XPath
copy_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-clipboard-target='#code_html']")))
copy_button.click()

# Lấy văn bản (text) của phần tử
pyautogui.sleep(2)

copied_text = pyperclip.paste()
pyautogui.sleep(2)

print(copied_text)

# Đóng trình duyệt
driver.quit()
