# Đường dẫn đến file input
input_file_path = "filtered_data.txt"

# Đường dẫn đến file output
output_file_path = "unique_data.txt"

# Tạo một tập hợp để lưu trữ các dòng đã xuất hiện
seen_lines = set()

# Mở file input để đọc và file output để ghi
with open(input_file_path, "r", encoding="utf-8") as input_file, open(output_file_path, "w", encoding="utf-8") as output_file:
    for line in input_file:
        # Kiểm tra xem dòng đã xuất hiện chưa
        if line not in seen_lines:
            # Nếu chưa xuất hiện, thêm vào tập hợp và ghi vào file mới
            seen_lines.add(line)
            output_file.write(line)
