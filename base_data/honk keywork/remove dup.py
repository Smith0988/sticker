# Mở file larger_than_4.txt để đọc
with open('larger_than_4.txt', 'r', encoding='utf-8') as larger_file:
    # Đọc nội dung của file và tạo một tập hợp (set) để loại bỏ các hàng trùng lặp
    unique_lines = set(larger_file.read().splitlines())

# In các hàng không trùng lặp ra file mới (ví dụ: unique_larger_than_4.txt)
with open('unique_larger_than_4.txt', 'w', encoding='utf-8') as unique_file:
    for line in unique_lines:
        unique_file.write(line + '\n')
