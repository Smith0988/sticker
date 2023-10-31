# Đọc tệp văn bản và xóa các dòng trùng nhau
def remove_duplicate_lines(input_file, output_file):
    lines_seen = set()  # Tạo một tập hợp để lưu trữ các dòng đã xuất hiện
    with open(output_file, 'w', encoding='utf-8') as output, open(input_file, 'r', encoding='utf-8') as input:
        for line in input:
            if line not in lines_seen:
                output.write(line)
                lines_seen.add(line)

# Tệp gốc chứa các dòng trùng nhau
input_file = "selected_lines_16_35.txt"

# Tạo tệp mới chứa các dòng không trùng nhau
output_file = "lines_without_duplicates.txt"

remove_duplicate_lines(input_file, output_file)

print("Các dòng trùng nhau đã được xóa và lưu trong tệp mới.")
