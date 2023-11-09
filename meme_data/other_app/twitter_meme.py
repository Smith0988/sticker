import csv
import json
import os
import subprocess
import sys
import time

import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
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


def write_list_to_csv(list1, list2):
    try:
        with open("base_data.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            for item1, item2 in zip(list1, list2):
                writer.writerow([item1, item2])

        print(f"Đã ghi dữ liệu vào file CSV: ")
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")


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
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("@Smith53017960")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
    upload_button.click()
    pyautogui.sleep(1)
    pyautogui.write("Chung.241089")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                               "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    upload_button.click()

    pyautogui.sleep(180)

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
                    link = "https://twitter.com" + link_url
                    all_link.append(link)

    driver.quit()

    return all_link


def get_views():
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/meme_ki_diwani/status/1721074953179595030")

    pyautogui.sleep(60)
    # Lấy mã nguồn HTML của trang
    html_source = driver.page_source

    # Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(html_source, 'html.parser')

    # Tìm tất cả các phần tử <div> có class="css-1dbjc4n"
    div_elements = soup.find_all('div', class_='css-1dbjc4n r-1wbh5a2 r-1b7u577')

    # Lặp qua từng phần tử div có class='css-1dbjc4n'
    all_link = []
    for div_element in div_elements:
        # Tìm tất cả các phần tử con div trong div_element
        span_elements = div_element.find_all('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
        for span_element in span_elements:
            text = span_element.get_text()
            print(text)

    driver.quit()


def get_view_new():
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/search?q=memes&src=typed_query")

    # wait = WebDriverWait(driver, 200)
    # upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='text']")))
    # upload_button.click()
    # pyautogui.sleep(1)
    # pyautogui.write("utester.9001@gmail.com")

    # wait = WebDriverWait(driver, 200)
    # upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    # upload_button.click()
    # pyautogui.sleep(1)
    # pyautogui.write("@Smith53017960")

    # wait = WebDriverWait(driver, 200)
    # upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Next')]")))
    # upload_button.click()
    # pyautogui.sleep(1)
    # pyautogui.write("Chung.241089")

    # wait = WebDriverWait(driver, 60)
    # upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='button']//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0']")))
    # upload_button.click()

    # for i in range(10):
    # pyautogui.press('down')

    pyautogui.sleep(200)

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
                    link = "https://twitter.com" + link_url
                    all_link.append(link)
                    print(link)

                span_elements = link_element.find_all('span',
                                                      class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')
                for span_element in span_elements:
                    span_html = str(span_element)
                    print(span_html)

    driver.quit()

    return all_link


def get_memes_links_test():
    # driver = webdriver.Chrome()
    # driver.get("https://twitter.com/search?q=memes&src=typed_query")

    # pyautogui.sleep(5)

    # html_source = driver.page_source

    with open("ten_tep.html", "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
    html_source = html_content
    soup = BeautifulSoup(html_source, 'html.parser')
    div_elements = soup.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')

    all_link = []
    all_view = []
    for div_element in div_elements:
        inner_div_elements = div_element.find_all('div', class_='css-1dbjc4n r-13awgt0 r-18u37iz r-1h0z5md')
        for inner_div_element in inner_div_elements:
            link_elements = inner_div_element.find_all('a')
            i = 0
            for link_element in link_elements:
                text_content = link_element.get_text()
                href = link_element.get('href')
                all_view.append(text_content)
                all_link.append("https://twitter.com" + href)

    return all_link, all_view


def get_memes_links_view():
    def get_link_view(html_source):
        soup = BeautifulSoup(html_source, 'html.parser')
        div_elements = soup.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
        all_link = []
        all_view = []
        for div_element in div_elements:
            inner_div_elements = div_element.find_all('div', class_='css-1dbjc4n r-13awgt0 r-18u37iz r-1h0z5md')
            for inner_div_element in inner_div_elements:
                link_elements = inner_div_element.find_all('a')
                for link_element in link_elements:
                    text_content = link_element.get_text()
                    href = link_element.get('href')
                    all_view.append(text_content)
                    all_link.append("https://twitter.com" + href)

        write_list_to_csv(all_link, all_view)

    def get_for_loop():
        for i in range(100):
            pyautogui.press('down')
        html_source = driver.page_source
        get_link_view(html_source)

    driver = webdriver.Chrome()
    driver.get("https://twitter.com")

    with open("twitter_cookies.json", "r") as cookie_file:
        saved_cookies = json.load(cookie_file)
    for cookie in saved_cookies:
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.get("https://twitter.com/search?q=memes&src=typed_query")
    time.sleep(5)
    j = 0
    for i in range(100000):
        if j == 15:
            driver.get("https://twitter.com/search?q=memes&src=typed_query")
            time.sleep(5)
            j = 0
        get_for_loop()
        j = j + 1
    driver.quit()


get_memes_links_view()
