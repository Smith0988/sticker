import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def upload_image_to_postimage(link_image):
    driver = webdriver.Edge()
    driver.get("https://postimages.org/")

    wait = WebDriverWait(driver, 60)

    upload_button  = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='uploadFile']")))
    upload_button .click()
    pyautogui.sleep(2)

    pyautogui.write(link_image)
    pyautogui.sleep(2)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 60)
    copy_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-clipboard-target='#code_html']")))
    copy_button.click()
    pyautogui.sleep(2)

    copied_text = pyperclip.paste()
    pyautogui.sleep(2)
    driver.quit()

    return copied_text

if __name__ == "__main__":
    link = "D:\\1.Github\sticker\\temp_data\\logo.png"
    result = upload_image_to_postimage(link)
    print(result)
