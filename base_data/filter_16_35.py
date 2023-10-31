# Đọc nội dung từ tệp "lines_without_person_remove_sticker&quotes.txt"
with open('lines_without_person_remove_sticker&quotes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Tạo tệp mới để ghi các hàng thỏa điều kiện
output_file = 'selected_lines.txt'

# Mở tệp mới để ghi
with open(output_file, 'w', encoding='utf-8') as output:
    for line in lines:
        # Loại bỏ khoảng trắng và ký tự xuống dòng từ đầu và cuối chuỗi
        cleaned_line = line.strip()

        # Kiểm tra số lượng ký tự của hàng
        char_count = len(cleaned_line)

        if 16 <= char_count <= 35:
            # Nếu số lượng ký tự từ 16 đến 35, ghi vào tệp mới
            output.write(cleaned_line + '\n')
