def count_words(line):
    # Hàm này trả về số từ trong một dòng
    words = line.split()
    return len(words)

def process_file(input_filename, output_large_filename, output_small_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file, \
         open(output_large_filename, 'w', encoding='utf-8') as output_large_file, \
         open(output_small_filename, 'w', encoding='utf-8') as output_small_file:

        for line in input_file:
            word_count = count_words(line)
            if word_count >= 3:
                output_large_file.write(line)
            else:
                output_small_file.write(line)

if __name__ == "__main__":
    input_filename = "unique_data.txt"
    output_large_filename = "large_words.txt"
    output_small_filename = "small_words.txt"

    process_file(input_filename, output_large_filename, output_small_filename)

    print("Xong! Đã phân loại dữ liệu vào hai file.")
