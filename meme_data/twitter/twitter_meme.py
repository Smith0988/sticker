import os
import sys
import time

import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
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

def get_memes_links():

    driver = webdriver.Chrome()
    driver.get("https://twitter.com/search?q=memes&src=typed_query")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("utester.9001@gmail.com")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("@Smith53017960")


    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("Chung.241089")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    upload_button.click()

    for i in range(1000):
        pyautogui.press('down')

    pyautogui.sleep(5)

    # Lấy mã nguồn HTML của trang
    html_source = driver.page_source

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(html_source, 'html.parser')

    # Tìm tất cả các phần tử <div> có class="css-1dbjc4n"
    div_elements = soup.find_all('div', class_='css-1dbjc4n')

    # Lặp qua từng phần tử div có class='css-1dbjc4n'
    all_link = []
    for div_element in div_elements:
        # Tìm tất cả các phần tử con div trong div_element
        inner_div_elements = div_element.find_all('div', class_='css-1dbjc4n r-16y2uox r-1pi2tsx r-13qz1uu')

        # Lặp qua từng phần tử div con để lấy các liên kết
        for inner_div_element in inner_div_elements:
            # Tìm tất cả các liên kết (thẻ <a>) bên trong phần tử div con
            link_elements = inner_div_element.find_all('a')

            # Lấy các liên kết và in ra màn hình
            for link_element in link_elements:
                link_url = link_element.get('href')
                if link_url:
                    link = "https://twitter.com"+link_url
                    all_link.append(link)

    driver.quit()

    return all_link


def get_views():

    driver = webdriver.Chrome()
    driver.get("https://twitter.com/CenturiiC/status/1721103763682034145")

    pyautogui.sleep(1000)

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'30.1K')]")))
    text = element.text
    print(text)

    driver.quit()


get_views()



"""
links = get_memes_links()
file_name = "links.txt"
with open(file_name, "w") as file:
    for link in links:
        file.write(link + "\n")
"""