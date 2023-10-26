from selenium import webdriver
from bs4 import BeautifulSoup

import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()  # Cài đặt ChromeDriver

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Tiếp tục với mã Selenium của bạn



def get_sticker_text(url):
    driver.get(url)

    # Lấy mã HTML của trang web
    html = driver.page_source

    # Đóng trình duyệt
    driver.quit()

    # Phân tích mã HTML bằng BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Tìm tất cả các thẻ div có class "styles__grid--23xRF"
    divs = soup.find_all("div", class_="styles__grid--23xRF")

    # Tạo một danh sách để lưu trữ văn bản từ các thẻ span
    all_text = []

    # Lặp qua từng thẻ div
    for div in divs:
        # Tìm tất cả các thẻ a bên trong div
        links = div.find_all("a")
        for link in links:
            # Tìm tất cả các thẻ div bên trong thẻ a
            divs_inside_a = link.find_all("div", class_="styles__box--2Ufmy styles__display-flex--2Ww2j")
            for div_inside_a in divs_inside_a:
                # Tìm tất cả các thẻ span bên trong thẻ div
                spans = div_inside_a.find_all("span", class_="styles__box--2Ufmy styles__text--23E5U styles__display6--3wsBG styles__nowrap--33UtL styles__display-block--3kWC4")
                for span in spans:
                    # Lấy văn bản từ thẻ span và thêm vào danh sách
                    text = span.text
                    all_text.append(text)

    # Ghi văn bản vào tệp "sticker_data.txt" với chế độ "a"
    with open("sticker_data.txt", "a", encoding="utf-8") as file:
        for text in all_text:
            file.write(text + "\n")

# Mở trang web
for page in range(1, 101):
    url = f"https://www.redbubble.com/shop/?page={page}&query=quote%20sticker"
    get_sticker_text(url)
