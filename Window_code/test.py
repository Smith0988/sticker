# Đọc dữ liệu từ file sticker_data.txt với encoding utf-8
with open('sticker_data.txt', 'r', encoding='utf-8') as sticker_file:
    sticker_data = set(sticker_file.read().splitlines())

# Kiểm tra từng hàng trong sticker_data
for line in sticker_data:
    # Kiểm tra xem hàng có trong raw_data_from_web.txt hay không
    if line not in open('raw_data_from_web.txt', encoding='utf-8').read():
        # Nếu không trùng, thêm hàng vào file mới (ví dụ: unmatched_data.txt)
        with open('unmatched_data.txt', 'a', encoding='utf-8') as unmatched_file:
            unmatched_file.write(line + '\n')
