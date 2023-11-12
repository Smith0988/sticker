import csv
from datetime import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import time

import numpy as np
import pandas as pd
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
        with open("base_data_instagram.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            for item1, item2 in zip(list1, list2):
                writer.writerow([item1, item2])

        print(f"Đã ghi dữ liệu vào file CSV: ")
    except Exception as e:
        print(f"Có lỗi xảy ra: {str(e)}")

def create_sku_code_instagram():
    now = datetime.now()
    day = now.day
    formatted_day = f"{day:02}"
    month = now.month
    formatted_month = f"{month:02}"
    year = now.year
    hour = now.hour
    formatted_hour = f"{hour:02}"
    minute = now.minute
    formatted_minute = f"{minute:02}"
    second = now.second
    formatted_second = f"{second:02}"

    sku = "ST" + str(
        year) + formatted_month + formatted_day + "_" + formatted_hour + formatted_minute + formatted_second
    return sku

def move_base_data_instagram():

    csv_path = 'base_data_instagram.csv'
    df = pd.read_csv(csv_path, header=None, names=['Link', 'Views'])
    df['Timestamp'] = datetime.now()
    total_file_path = 'total_data_instagram.csv'
    df.to_csv(total_file_path, mode='a', header=False, index=False)


def get_memes_links_view_instagram():

    def get_link_view(html_source):
        soup = BeautifulSoup(html_source, 'html.parser')
        div_elements = soup.find_all('div', class_='x78zum5 xdt5ytf x5yr21d xa1mljc xh8yej3 x1bs97v6 x1q0q8m5 xso031l x11aubdm xnc8uc2')
        all_link = []
        all_view = []
        for div_element in div_elements:
            inner_div_elements = div_element.find_all('div', class_='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xr1yuqi xkrivgy x4ii5y1 x1gryazu x1n2onr6 x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf x1a02dak xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1')
            for inner_div_element in inner_div_elements:
                link_elements = inner_div_element.find_all('a')
                for link_element in link_elements:
                    text_content = link_element.get_text()
                    href = link_element.get('href')
                    base_link = href.split("liked_by/")[0]
                    cleaned_text = ''.join(filter(str.isdigit, text_content))
                    if cleaned_text:
                        number_of_likes = int(cleaned_text)
                        all_view.append(number_of_likes)
                        all_link.append("https://www.instagram.com" + base_link)

        write_list_to_csv(all_link, all_view)

    def get_for_loop():
        for i in range(100):
            pyautogui.press('down')
        html_source = driver.page_source
        get_link_view(html_source)

    driver = webdriver.Edge()
    driver.get("https://www.instagram.com/")

    time.sleep(90)
    j = 0
    for i in range(5):
        if j == 15:
            driver.get("https://www.instagram.com/")
            time.sleep(5)
            j = 0
        get_for_loop()
        j = j + 1
    driver.quit()


def convert_views_instagram(views):
    if isinstance(views, str):
        # Nếu views là một chuỗi, thực hiện chuyển đổi
        return int(views.replace(',', ''))
    elif isinstance(views, int):
        # Nếu views đã là số nguyên, không cần thay đổi
        return views
    else:
        # Trong trường hợp khác, trả về NaN để sau này có thể loại bỏ
        return None


def sorted_by_view_instagram():
    input_file = 'base_data_instagram.csv'
    output_file = 'output_sorted_by_view.csv'

    # Đọc CSV và đặt tên cột
    df = pd.read_csv(input_file, names=['Link', 'Views'])

    # Chuyển đổi số view sang kiểu số nguyên
    df['Views'] = df['Views'].apply(convert_views_instagram)

    # Loại bỏ các giá trị không hợp lệ
    df = df.dropna(subset=['Views'])

    # Sắp xếp theo số lượt xem giảm dần
    df_sorted = df.sort_values(by='Views', ascending=False)

    # Ghi vào tệp CSV mới
    df_sorted.to_csv(output_file, header=False, index=False)


def sort_by_repeat_instagram():

    input_file = 'output_sorted_by_view.csv'
    output_file = 'output_sorted_by_repeat.csv'

    # Đọc tệp CSV đã sắp xếp, sử dụng trị số cột 0 và 1
    df = pd.read_csv(input_file, header=None)

    # Tạo một Series chứa số lần xuất hiện của từng phần tử trong cột 0 (Link)
    link_counts = df[0].value_counts()

    # Thêm một cột mới là số lần duplicate (dup)
    df['Dup'] = df[0].map(link_counts) - 1  # Trừ 1 để loại bỏ một lần xuất hiện ban đầu

    # Sắp xếp theo thứ tự giảm dần của số lần duplicate
    df_sorted = df.sort_values(by='Dup', ascending=False)

    # Lấy danh sách các phần tử đã sắp xếp
    sorted_links = df_sorted[0]

    # Ghi danh sách đã sắp xếp và số lần duplicate vào tệp
    df_sorted.to_csv(output_file, index=False)



def remove_duplicate_instagram():

    df = pd.read_csv('output_sorted_by_repeat.csv', header=None, names=['Link', 'Value1', 'Value2'])
    df_deduplicated = df.drop_duplicates(subset=['Link', 'Value2'])
    df_deduplicated.to_csv('output_deduplicated.csv', index=False)


def get_top_list_instagram():

    df_deduplicated = pd.read_csv('output_deduplicated.csv')
    df_deduplicated = df_deduplicated.iloc[2:]
    first_10_deduplicated = df_deduplicated.head(10)
    df_sorted = pd.read_csv('output_sorted_by_view.csv')
    first_10_sorted = df_sorted.head(10)
    with open('top_list_instagram.csv', 'a') as outfile:
        first_10_deduplicated.to_csv(outfile, index=False, header=False, mode='a')
        first_10_sorted.to_csv(outfile, index=False, header=False, mode='a')

    files_to_delete = ['output_deduplicated.csv', 'output_sorted_by_repeat.csv', 'output_sorted_by_view.csv', 'base_data_instagram.csv']
    for file_name in files_to_delete:
        if os.path.exists(file_name):
            os.remove(file_name)



#get_memes_links_view_instagram()
#time.sleep(1)
#move_base_data_instagram()
#time.sleep(1)
#sorted_by_view_instagram()
#time.sleep(1)
#sort_by_repeat_instagram()
#time.sleep(1)
#remove_duplicate_instagram()
#time.sleep(1)
#get_top_list_instagram()
#time.sleep(1)
