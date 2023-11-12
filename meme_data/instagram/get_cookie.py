from selenium import webdriver
import time
import json

# Khai báo trình duyệt Chrome
driver = webdriver.Chrome()

# Truy cập trang Twitter và đăng nhập bình thường
driver.get("https://twitter.com")
# Thực hiện đăng nhập và các tác vụ khác tại đây

# Đợi một chút để trang hoàn thành đăng nhập
time.sleep(80)

# Lấy danh sách cookie hiện tại
current_cookies = driver.get_cookies()

# Lưu cookie vào tệp hoặc cơ sở dữ liệu
with open("twitter_cookies.json", "w") as cookie_file:
    json.dump(current_cookies, cookie_file)

# Đóng trình duyệt
driver.quit()

# Lần chạy sau
# Khai báo trình duyệt Chrome
driver = webdriver.Chrome()

# Truy cập trang Twitter
driver.get("https://twitter.com")

# Đọc danh sách cookie từ tệp
with open("twitter_cookies.json", "r") as cookie_file:
    saved_cookies = json.load(cookie_file)

# Thêm cookie đã lưu vào trình duyệt
for cookie in saved_cookies:
    driver.add_cookie(cookie)

# Truy cập lại trang Twitter đã xác thực
driver.get("https://twitter.com")

# Bây giờ bạn đã đăng nhập bằng cookie và có thể thực hiện các tác vụ trên trang
