import csv
from datetime import datetime
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from write_data_to_excel import *
import chardet


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
    base_directory = r"C:\Users\Cong Dinh\Desktop\Sticker Image\image_base"
    new_folder_name = fd_name

    new_folder_path = os.path.join(base_directory, new_folder_name)
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)

    source_directory = r"C:\Users\Cong Dinh\Desktop\Sticker Image"

    destination_directory = f"C:\\Users\\Cong Dinh\\Desktop\\Sticker Image\\image_base\\{fd_name}"
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


def read_csv_file():
    csv_file = r"C:\Users\Cong Dinh\Desktop\Sticker Image\temp_data\NameSize_2.csv"
    list_1 = []
    # Xác định mã hóa của tệp
    with open(csv_file, 'rb') as file:
        result = chardet.detect(file.read())
    # Sử dụng mã hóa được xác định
    with open(csv_file, 'r', encoding=result['encoding']) as file:
    #with open(csv_file, newline='', encoding='utf-8') as file:
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

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='expire']")))
    upload_button.click()
    pyautogui.sleep(1)

    pyautogui.press('up')
    pyautogui.sleep(1)
    pyautogui.press('down')
    pyautogui.sleep(1)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 60)
    upload_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='uploadFile']")))
    upload_button.click()
    pyautogui.sleep(2)

    pyautogui.write(link_image)
    pyautogui.sleep(2)
    pyautogui.press("enter")

    wait = WebDriverWait(driver, 60)
    copy_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[@data-clipboard-target='#code_direct']")))
    copy_button.click()
    pyautogui.sleep(2)

    copied_text = pyperclip.paste()
    pyautogui.sleep(2)
    driver.quit()

    return copied_text


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
    sku_list = read_csv_file()
    for sku in sku_list:
        sku_temp_main = upload_image_to_postimage(sku, "main")
        sku_temp_url_1 = upload_image_to_postimage(sku, "url_1")
        sku_temp_url_2 = upload_image_to_postimage(sku, "url_2")

        data_to_write = [sku, sku_temp_main, sku_temp_url_1, sku_temp_url_2]
        write_to_excel(data_to_write)

    move_temp_excel_form()
    create_folder_and_copy_data()
    delete_folder_data()


if __name__ == "__main__":
    upload_process()
    #move_temp_excel_form()
    #create_folder_and_copy_data()
    #delete_folder_data()