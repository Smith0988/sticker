from split_sentence import *
from export_to_photoshop_form import *

base_data = resource_path("base_data\\sentence_data.txt")
used_data = resource_path("use_data\\sentence_used.txt")


def write_sentence_to_file(filename, sentence):
    try:
        with open(filename, 'a') as file:
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


list_text = find_unmatched_sentences(base_data, used_data)
if list_text:
    i = 1
    for text in list_text:
        i = i + 1
        if i == 3:
            break
        write_sentence_to_file(used_data, text)
        list_split, product_name = split_sentence_by_length(text)
        sku = export_file_to_csv(list_split)


print(sku)
print(product_name)
