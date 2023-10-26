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

# Tạo một danh sách để lưu trữ các liên kết
all_links = []

# Lặp qua từng thẻ div và tìm các liên kết bên trong
for div in divs:
    links = div.find_all("a")
    for link in links:
        href = link.get("href")
        if href is not None:
            all_links.append(href)

# In danh sách các liên kết
for link in all_links:
    print(link)
