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

    sku = "ST" + str(year) + formatted_month + formatted_day + "_" + formatted_hour + formatted_minute + formatted_second
    return sku


def export_file_to_csv(list_text):

    list2 = ['SKU', 'Name1', 'Name2']
    list3 = ['SKU', 'Name1', 'Name2', 'Name3']
    result_list =[]

    sku = create_sku_code()
    result_list.append(sku)

    for list in list_text:
        result_list.append(list)

    if len(list_text) == 2:
        with open(name_size_2, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Ghi hàng 1 từ list1
            #writer.writerow(list2)
            # Ghi hàng 2 từ list2
            writer.writerow(result_list)
    if len(list_text) == 3:
        with open(name_size_3, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            # Ghi hàng 1 từ list1
            #writer.writerow(list3)
            # Ghi hàng 2 từ list2
            writer.writerow(result_list)
    return sku

if __name__ == "__main__":

    list = ["toi","day", "HAHA"]
    export_file_to_csv(list)

