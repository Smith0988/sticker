# Đọc nội dung từ file chua_dung_long_lines_tren_8_tu.txt
with open("unmatched_lines_8_tu.txt", "r", encoding="utf-8") as long_lines_file:
    long_lines = long_lines_file.readlines()

# Lọc và giữ lại chỉ một dòng duy nhất nếu có hàng trùng nhau
unique_lines = list(set(long_lines))

# Ghi vào file mới
with open("unique_short_lines.txt", "w", encoding="utf-8") as unique_file:
    unique_file.write("\n".join(unique_lines))
