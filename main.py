import time

from split_sentence import *
from export_to_photoshop_form import *
from upload_image_to_github import *

base_data = resource_path("base_data\\sentence_data.txt")
used_data = resource_path("use_data\\sentence_used.txt")
temp_used_data = resource_path("use_data\\temp_sentence_used.txt")

import shutil
import os

# Đường dẫn tới tệp ảnh ban đầu
source_path = resource_path("temp_data/logo.png")


def write_sentence_to_file(filename, sentence):
    try:
        with open(filename, 'a') as file:
            file.write(sentence + '\n')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def write_sentence_to_file_temp(filename, sentence):
    try:
        with open(filename, 'w') as file:
            file.write(sentence + '\n')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def read_sentences_from_file(filename):
    try:
        with open(filename, 'r') as file:
            sentences = file.read().splitlines()
        return sentences
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def find_unmatched_sentences(data_filename, used_filename):
    data_sentences = read_sentences_from_file(data_filename)
    used_sentences = read_sentences_from_file(used_filename)

    unmatched_sentences = []

    for sentence in data_sentences:
        if sentence not in used_sentences:
            unmatched_sentences.append(sentence)

    return unmatched_sentences

def create_csv_to_photo():

    sku_csv = create_sku_code()
    sku_csv_2 = sku_csv + "_2.csv"
    sku_csv_3 = sku_csv + "_3.csv"
    list_text = find_unmatched_sentences(base_data, used_data)
    if list_text:
        list2 = ['SKU', 'Name1', 'Name2']
        list3 = ['SKU', 'Name1', 'Name2', 'Name3']
        with open(name_size_2, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(list2)
        with open(name_size_3, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(list3)


        write_sentence_to_file_temp(temp_used_data, "")

    if list_text:
        sku_list = []
        product_name_list = []
        i = 1
        for text in list_text:
            i = i + 1
            if i == 200:
                break

            write_sentence_to_file(used_data, text)
            write_sentence_to_file(temp_used_data, text)
            list_split, product_name = split_sentence_by_length(text)
            sku = export_file_to_csv(list_split)
            time.sleep(1)
            sku_list.append(sku)
            product_name_list.append(product_name)

    new_name_2 = resource_path(f"temp_data\\{sku_csv_2}.csv")
    os.rename(name_size_2, new_name_2)

    new_name_3 = resource_path(f"temp_data\\{sku_csv_3}.csv")
    os.rename(name_size_3, new_name_3)

    return sku_list, product_name_list







if __name__ == "__main__":
    sku_list, product_name_list = create_csv_to_photo()
    print(sku_list)
    print(product_name_list)


