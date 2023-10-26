from selenium import webdriver
from bs4 import BeautifulSoup

# Khởi tạo trình duyệt (ở đây là Chrome)
driver = webdriver.Chrome()

# Mở trang web
url = "https://www.redbubble.com/shop/?query=quote%20sticker&ref=search_box"
driver.get(url)

# Lấy mã HTML của trang web
html = driver.page_source

# Đóng trình duyệt
driver.quit()

# Phân tích mã HTML bằng BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Tìm tất cả các thẻ div có class "styles__grid--23xRF"
divs = soup.find_all("div", class_="styles__grid--23xRF")

# Tạo một danh sách để lưu trữ văn bản từ các thẻ a
all_text = []

# Lặp qua từng thẻ div
for div in divs:
    # Tìm tất cả các thẻ a bên trong div
    links = div.find_all("a")
    for link in links:
        # Lấy văn bản từ thẻ a và thêm vào danh sách
        text = link.text
        all_text.append(text)

# In danh sách văn bản từ các thẻ a
for text in all_text:
    print(text)
