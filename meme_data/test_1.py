import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    url = "https://www.reddit.com"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source
    raw_link = []
    raw_view = []
    if html:
        soup = BeautifulSoup(html, "html.parser")
        div_outer = soup.find_all("div", class_="rpBJOHq2PR60pnwJlUyP0")

        for div_element in div_outer:
            div_inner = div_element.find("div", class_="_1NSbknF8ucHV2abfCZw2Z1")
            print("bbbb")
            if div_inner:
                a_elements = div_inner.find_all("a")
                print("ccc")
                for a_element in a_elements:
                    href = a_element.get("href")
                    raw_link.append("https://www.reddit.com" + href)

    # Save the extracted links to a file
    write_lines_to_text_file(raw_link, reddit_raw_link)

get_link_reddit()
