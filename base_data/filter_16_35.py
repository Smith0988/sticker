# Mở file unmatched_data_honk_keywork.txt để đọc
with open('unmatched_data_honk_keywork.txt', 'r', encoding='utf-8') as input_file:
    # Đọc từng dòng và kiểm tra độ dài
    for line in input_file:
        # Kiểm tra xem độ dài của câu là lớn hơn hay bằng 4
        if len(line.strip()) >= 4:
            # Nếu câu lớn hơn hoặc bằng 4, in ra file larger_than_4.txt
            with open('larger_than_4.txt', 'a', encoding='utf-8') as larger_file:
                larger_file.write(line)
        else:
            # Nếu câu nhỏ hơn 4, in ra file smaller_than_4.txt
            with open('smaller_than_4.txt', 'a', encoding='utf-8') as smaller_file:
                smaller_file.write(line)
