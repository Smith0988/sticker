from selenium import webdriver

url = "https://www.reddit.com/r/memes/comments/17scon0/please_be_kind/"

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang web
driver.get(url)

# Chụp ảnh màn hình và lưu vào file
driver.save_screenshot("screenshot.png")

# Đóng trình duyệt
driver.quit()