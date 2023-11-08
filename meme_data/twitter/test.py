import time

from selenium import webdriver

# Đường dẫn đến tệp thực thi của GeckoDriver
chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# Khai báo trình duyệt Firefox sử dụng GeckoDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.example.com")

# Thực hiện các tác vụ trên trang web, ví dụ: tương tác với trang, lấy dữ liệu, và nhiều tác vụ khác
time.sleep(100)
# Đóng trình duyệt khi hoàn thành
driver.quit()
