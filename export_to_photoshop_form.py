import csv
import os
import sys
from datetime import datetime


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


name_size_2 = resource_path("temp_data\\NameSize_2.csv")
name_size_3 = resource_path("temp_data\\NameSize_3.csv")
name_size_4 = resource_path("temp_data\\NameSize_4.csv")


def create_name_size_2():
    list_2 = ['SKU', 'Name1', 'Name2']
    with open(name_size_2, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list_2)


def create_name_size_3():
    list_3 = ['SKU', 'Name1', 'Name2', 'Name3']
    with open(name_size_3, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list_3)


def create_name_size_4():
    list_4 = ['SKU', 'Name1', 'Name2', 'Name3', 'Name4']
    with open(name_size_4, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(list_4)


def create_sku_code():
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


def export_file_to_csv(list_text):
    result_list = []
    sku = create_sku_code()
    result_list.append(sku)

    for list in list_text:
        result_list.append(list)

    if len(list_text) == 2:
        if not os.path.exists(name_size_2):
            create_name_size_2()

        with open(name_size_2, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(result_list)

    elif len(list_text) == 3:
        if not os.path.exists(name_size_3):
            create_name_size_3()

        with open(name_size_3, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(result_list)

    else:
        if not os.path.exists(name_size_4):
            create_name_size_4()

        with open(name_size_4, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(result_list)
    return sku


if __name__ == "__main__":
    list = ["toi", "day", "nhe", "ban"]
    export_file_to_csv(list)
