import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


reddit_raw_link = resource_path("temp_data/reddit_raw_link.txt")
raw_view_file = resource_path("temp_data/raw_view_file.txt")


def write_lines_to_text_file(lines, file_path):
    try:
        with open(file_path, 'a') as file:  # Mở tệp ở chế độ ghi thêm ('a')
            file.writelines([line + '\n' for line in lines])  # Ghi danh sách các lít và thêm dấu xuống dòng
    except Exception as e:
        print("Có lỗi khi ghi các lít vào tệp:", str(e))

def get_link_reddit():
    url = "https://www.reddit.com/t/memes/"
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source
    raw_link = []
    raw_view = []
    if html:
        soup = BeautifulSoup(html, "html.parser")

        section_1 = soup.find_all("section", {"slot": "page-1"})


        for section in section_1:

            span_tag = section.find("span", class_="relative leading-[0] mr-sm")
            if span_tag:
                text = span_tag.get_text()
                raw_view.append(text)

            links = section.find_all("a", {"slot": "full-post-link"})
            for link in links:
                href = link.get("href")
                if href:
                    raw_link.append("https://www.reddit.com" + href)

        write_lines_to_text_file(raw_view, raw_view_file)
        write_lines_to_text_file(raw_link, reddit_raw_link)

    else:
        print("Yêu cầu không thành công. Mã trạng thái:")


get_link_reddit()
