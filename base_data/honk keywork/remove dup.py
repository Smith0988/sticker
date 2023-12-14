# Thay đổi tên file đầu vào và đầu ra tại đây
input_file_path = 'unique_larger_than_4.txt'
contains_file_path = 'contains_dont_honk.txt'
does_not_contain_file_path = 'does_not_contain_dont_honk.txt'

# Mở file đầu vào với mã hóa 'utf-8' hoặc 'latin-1' hoặc mã hóa khác phù hợp
try:
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Mở hai file đầu ra
        with open(contains_file_path, 'w', encoding='utf-8') as contains_file, \
             open(does_not_contain_file_path, 'w', encoding='utf-8') as does_not_contain_file:
            # Duyệt qua từng dòng trong file đầu vào
            for line in input_file:
                # Kiểm tra xem dòng có chứa cụm từ "don't honk" hay không
                if 'don\'t honk' in line:
                    # Nếu có, ghi vào file chứa
                    contains_file.write(line)
                else:
                    # Nếu không, ghi vào file không chứa
                    does_not_contain_file.write(line)

    print("Quá trình kiểm tra và ghi hoàn thành.")
except UnicodeDecodeError as e:
    print(f"Lỗi UnicodeDecodeError: {e}")
    print("Vui lòng kiểm tra mã hóa đúng cho file của bạn và thay đổi mã hóa ở đoạn mã.")
