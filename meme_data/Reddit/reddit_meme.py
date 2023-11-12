import os
import sys
import time

import pyautogui
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_links_to_file(links):
    file_path =  "base_data.txt"
    with open(file_path, "a") as file:
        for link in links:
            file.write(link + "\n")

def get_link_reddit():

    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/r/memes/")
    time.sleep(2)

    for i in range(5000):
        pyautogui.press('down')


    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    div_elements = soup.find_all('main', class_='main block col-span-4 xs:col-span-12 s:col-span-8 m:col-span-6 l:col-span-9 xl:col-span-9')
    all_link = []
    for div_element in div_elements:
        inner_div_elements = div_element.find_all('shreddit-post', class_='block relative cursor-pointer bg-neutral-background focus-within:bg-neutral-background-hover hover:bg-neutral-background-hover xs:rounded-[16px] p-md my-2xs nd:visible')
        for inner_div_element in inner_div_elements:
            link_elements = inner_div_element.find_all('div', class_='relative overflow-hidden pointer-cursor mb-xs isolate bg-neutral-background rounded-[16px]')
            for link_element in link_elements:
                text_contents = link_element.find_all('a')
                for text in text_contents:
                    if text:
                        href = text.get('href')
                        all_link.append("https://www.reddit.com" + href)

    driver.quit()
    write_links_to_file(all_link)
    return all_link



def get_view(url):
    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/r/memes/")
    time.sleep(2)

    #for i in range(1000):
        #pyautogui.press('down')

    html_source = driver.page_source


    soup = BeautifulSoup(html_source, 'html.parser')
    desired_div = soup.find_all('div', class_='block xs:mt-xs xs:-mx-xs xs:px-xs xs:rounded-[16px] pt-xs nd:pt-xs bg-[color:var(--shreddit-content-background)] box-border mb-xs nd:visible nd:pb-2xl')
    print(desired_div)




url = "https://www.reddit.com/r/memes/comments/17sk5u1/this_is_the_reality_we_live_in/"




get_link_reddit()
