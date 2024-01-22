def remove_duplicates(input_file, output_file):
    # Mở file đầu vào để đọc
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Loại bỏ các câu trùng lặp
    unique_lines = list(set(line.lower() for line in lines))

    # Mở file đầu ra để ghi
    with open(output_file, 'w', encoding='utf-8') as file:
        # Ghi các câu không trùng lặp vào file mới
        file.writelines(unique_lines)

# Gọi hàm và truyền tên file đầu vào và tên file đầu ra
remove_duplicates('unique_data.txt', 'unique_data_no_duplicates.txt')
