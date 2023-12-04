file1_path = "sticker_data.txt"
file2_path = "sticker_data_part1.txt"
output_file_path = "output_diff.txt"

# Đọc nội dung từ file1 và file2
with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
    lines_file1 = set(file1.readlines())
    lines_file2 = set(file2.readlines())

# Tìm sự khác biệt giữa hai tập hợp dòng
difference = lines_file1 - lines_file2

# Ghi kết quả ra file output
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(difference)

print("Các dòng chỉ xuất hiện trong", file1_path, "mà không xuất hiện trong", file2_path, "đã được ghi vào", output_file_path)
