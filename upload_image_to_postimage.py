import csv
from datetime import datetime
import pyautogui
import pyperclip
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from write_data_to_excel import *


def upload_image_to_postimage_folder():
    driver = webdriver.Chrome()
    driver.get("https://postimages.org")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='expire']")))
    upload_button.click()
    pyautogui.sleep(1)

    pyautogui.press('up')
    pyautogui.sleep(1)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='uploadFile']")))
    upload_button.click()
    pyautogui.sleep(2)

    pyautogui.hotkey('ctrl', 'v')

    # pyautogui.write(link_image)
    pyautogui.sleep(5)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 90000)
    copy_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@data-clipboard-target='#code_gallery']//i[@class='fa fa-clipboard']")))
    copy_button.click()
    pyautogui.sleep(1)

    copied_text = pyperclip.paste()
    pyautogui.sleep(2)
    driver.quit()

    return copied_text


def sort_urls_by_number(urls):
    # Hàm tự tạo để trích xuất số từ phần đầu tiên của URL
    def extract_number(url):
        parts = url.split("-")
        if len(parts) > 1:
            first_part = parts[1]
            try:
                number = int(first_part)
                return number
            except ValueError:
                return 0
        return 0

    # Sắp xếp danh sách các URL theo số tăng dần
    sorted_urls = sorted(urls, key=extract_number)

    return sorted_urls


def get_image_link_folder(url):
    links = []
    driver = webdriver.Chrome()
    driver.get(url)
    for i in range(200):
        pyautogui.press('down')

    pyautogui.sleep(5)
    html_source = driver.page_source
    if html_source:
        soup = BeautifulSoup(html_source, "html.parser")
        a_tags = soup.find_all("a", class_="img")

        for a_tag in a_tags:
            style = a_tag["style"]
            url = style.split("(")[1].split(")")[0]
            cleaned_link = url[1:-1]
            links.append(cleaned_link)
        sort_links = sort_urls_by_number(links)

        return sort_links
    else:
        print("Không thể truy cập trang web.")


def upload_process_folder():
    sku_list = read_csv_file_folder()
    main_link = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\2. Main\\"
    url1_link = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\3. ULR1\\"
    url2_link = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\4. ULR2\\"

    for sku in sku_list:
        main_link = main_link + f'"{sku} copy.jpg"' + " "
        url1_link = url1_link + f'"{sku} copy.jpg"' + " "
        url2_link = url2_link + f'"{sku} copy.jpg"' + " "

    pyperclip.copy(main_link)
    #link_1 = upload_image_to_postimage_folder()
    link_1 = "https://postimg.cc/gallery/X4Ssq9d"
    link_main = get_image_link_folder(link_1)
    print("link 1\n" + link_1)
    print( link_main)

    pyperclip.copy(url1_link)
    #link_2 = upload_image_to_postimage_folder()
    link_2 = "https://postimg.cc/gallery/VtysM1x"
    link_url1 = get_image_link_folder(link_2)
    print("link 2\n" + link_2)
    print( link_url1 )

    pyperclip.copy(url2_link)
    #link_3 = upload_image_to_postimage_folder()
    link_3 = "https://postimg.cc/gallery/S4shybf"
    link_url2 = get_image_link_folder(link_3)

    print("link 3\n" + link_3)
    print(link_url2 )

    for i in range(len(sku_list)):
        data_to_write = [sku_list[i], link_main[i], link_url1[i], link_url2[i]]
        write_to_excel(data_to_write)

    move_temp_excel_form()
    create_folder_and_copy_data()
    delete_folder_data()




def create_sku_code_1():
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

    sku = "FD_" + str(
        year) + formatted_month + formatted_day + "_" + formatted_hour + formatted_minute + formatted_second
    return sku


def create_folder_and_copy_data():
    fd_name = create_sku_code_1()
    base_directory = r"E:\0.Sticker\image_base"
    new_folder_name = fd_name

    new_folder_path = os.path.join(base_directory, new_folder_name)
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)

    source_directory = r"C:\Users\Cong Dinh\Desktop\Sticker Image"

    destination_directory = f"E:\\0.Sticker\\image_base\\{fd_name}"
    folders_to_copy = ["1. PSD", "2. Main", "3. ULR1", "4. ULR2", "5. PNG", "temp_data"]

    for folder in folders_to_copy:
        source_path = os.path.join(source_directory, folder)
        destination_path = os.path.join(destination_directory, folder)
        if os.path.exists(source_path):
            shutil.copytree(source_path, destination_path)


def delete_folder_data():
    source_directory = r"C:\Users\Cong Dinh\Desktop\Sticker Image"
    folders_to_clear = ["1. PSD", "2. Main", "3. ULR1", "4. ULR2", "5. PNG", "temp_data"]
    for folder in folders_to_clear:
        folder_path = os.path.join(source_directory, folder)

        if os.path.exists(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)  # Xóa tất cả tệp

                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    shutil.rmtree(dir_path)  # Xóa tất cả thư mục con

            print(f"Xóa dữ liệu trong thư mục {folder} thành công.")
        else:
            print(f"Thư mục {folder} không tồn tại, không thể xóa dữ liệu.")


def read_csv_file(file_name):
    csv_file = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\temp_data\\{file_name}"
    list_1 = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list_1.append(row[0])
    if list_1:
        list_1 = list_1[1:]  # Tạo danh sách mới bằng cách bỏ qua phần tử đầu tiên
    return list_1


def read_csv_file_folder(file_name):
    csv_file = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\temp_data\\{file_name}"
    list_1 = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            list_1.append(row[0])
    if list_1:
        list_1 = list_1[1:]  # Tạo danh sách mới bằng cách bỏ qua phần tử đầu tiên
    return list_1


def upload_image_to_postimage(sku_name, type):
    if type == "main":
        link_image = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\2. Main\\{sku_name} copy.jpg"
    elif type == "url_1":
        link_image = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\3. ULR1\\{sku_name} copy.jpg"
    elif type == "url_2":
        link_image = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\4. ULR2\\{sku_name} copy.jpg"

    driver = webdriver.Chrome()
    driver.get("https://postimages.org")

    wait = WebDriverWait(driver, 120)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='expire']")))
    upload_button.click()
    pyautogui.sleep(1)

    pyautogui.press('up')
    pyautogui.sleep(1)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 120)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='uploadFile']")))
    upload_button.click()
    pyautogui.sleep(2)

    pyautogui.write(link_image)
    pyautogui.sleep(2)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 220)
    copy_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-clipboard-target='#code_direct']")))
    copy_button.click()
    pyautogui.sleep(2)

    copied_text = pyperclip.paste()
    pyautogui.sleep(2)
    driver.quit()

    return copied_text

def copy_Bumper_file():
    source_path = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\image_base\\base_data\\BumperStickersAAx3.xlsm"
    destination_path = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\temp_data\\BumperStickersAAx3.xlsm"
    try:
        shutil.copy(source_path, destination_path)
        print(f"Đã sao chép {source_path} tới {destination_path}")
    except Exception as e:
        print(f"Lỗi: {e}")


    source_path = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\image_base\\base_data\\BumperStickersAAx2.xlsm"
    destination_path = "C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\temp_data\\BumperStickersAAx2.xlsm"
    try:
        shutil.copy(source_path, destination_path)
        print(f"Đã sao chép {source_path} tới {destination_path}")
    except Exception as e:
        print(f"Lỗi: {e}")



def move_temp_excel_form():
    # Đường dẫn đến tệp cần di chuyển
    source_file = r"C:\Users\Cong Dinh\Documents\GitHub\sticker\temp_form.xlsx"

    # Đường dẫn đến thư mục đích
    destination_directory = r"C:\Users\Cong Dinh\Desktop\Sticker Image\temp_data"

    # Kiểm tra xem tệp nguồn tồn tại
    if os.path.exists(source_file):
        # Kiểm tra xem thư mục đích tồn tại, nếu không tồn tại thì tạo thư mục đích
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Đường dẫn đầy đủ đến tệp trong thư mục đích
        destination_file = os.path.join(destination_directory, "temp_form.xlsx")

        # Di chuyển tệp từ nguồn sang đích
        shutil.move(source_file, destination_file)


def upload_process():

    name_size_2 = "NameSize_2.csv"
    name_size_2_change = "NameSize_2_change.csv"
    name_size_4 = "NameSize_4.csv"
    name_size_4_change = "NameSize_4_change.csv"



    sku_list = read_csv_file(name_size_4)

    for sku in sku_list:
        sku_temp_main = upload_image_to_postimage(sku, "main")
        sku_temp_url_1 = upload_image_to_postimage(sku, "url_1")
        sku_temp_url_2 = upload_image_to_postimage(sku, "url_2")
        prefix = sku.split('_')[:2]
        result = '_'.join(prefix)
        data_to_write = [result, sku_temp_main, sku_temp_url_1, sku_temp_url_2]
        write_to_excel(data_to_write)

    copy_Bumper_file()
    move_temp_excel_form()
    create_folder_and_copy_data()
    delete_folder_data()




if __name__ == "__main__":
    upload_process()
    #create_folder_and_copy_data()