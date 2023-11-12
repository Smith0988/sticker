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


def get_memes_links_test():
    """
    driver = webdriver.Edge()
    driver.get("https://www.instagram.com/")

    pyautogui.sleep(120)

    html_source = driver.page_source
    with open('ten_tep.html', 'w', encoding='utf-8') as file:
        file.write(html_source)

    # Đóng trình duyệt
    driver.quit()
    """


    with open("ten_tep.html", "r", encoding="utf-8") as html_file:
        html_content = html_file.read()
    html_source = html_content
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
                text = int(''.join(filter(str.isdigit, text_content)))
                href = link_element.get('href')
                base_link = href.split("liked_by/")[0]
                all_view.append(text)
                all_link.append("https://www.instagram.com" + base_link)
    print(all_view)
    print(all_link)



get_memes_links_test()