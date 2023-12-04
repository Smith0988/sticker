input_file_path = "output_diff.txt"
output_filtered_large_path = "output_filtered_large.txt"

# Đọc nội dung từ file input
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# Lọc các câu có số từ lớn hơn hoặc bằng 10
filtered_large_lines = [line for line in lines if len(line.split()) >= 10]

# Ghi kết quả ra file output_filtered_large
with open(output_filtered_large_path, 'w', encoding='utf-8') as output_filtered_large_file:
    output_filtered_large_file.writelines(filtered_large_lines)

print("Các dòng có số từ lớn hơn hoặc bằng 10 đã được ghi vào", output_filtered_large_path)
