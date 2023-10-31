import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt Microsoft Edge
driver = webdriver.Edge()

# Mở trang web Postimage
driver.get("https://postimages.org/")

# Sử dụng XPath để tìm nút "Choose Images"
upload_button = driver.find_element(By.XPATH, "//nav[@class='mainmenu']//a[normalize-space()='Upload by URL']")

# Nhấp vào nút "Choose Images"
upload_button.click()

# Tải lên tệp ảnh
# Chờ cho hộp thoại mở ra để chọn tệp ảnh
pyautogui.sleep(2)  # Chờ 2 giây

# Nhấp vào ô nhập tệp
pyautogui.click(x, y)  # Thay (x, y) bằng tọa độ của ô nhập tệp

# Đợi cho việc tải lên hoàn thành (có thể sử dụng explicit wait)
# Sau khi tải lên, bạn có thể lấy URL của ảnh được tải lên.

# Đóng trình duyệt
driver.quit()
