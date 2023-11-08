import spacy

# Nạp mô hình ngôn ngữ spaCy
nlp = spacy.load("en_core_web_sm")

# Tên tệp đầu vào và tên tệp đầu ra
input_file = "lines_without_duplicates16_35.txt"

# Tạo tên tệp đầu ra cho hàng có tên riêng và hàng không có tên riêng
output_file_with_named_entity = "lines_with_named_entity.txt"
output_file_without_named_entity = "lines_without_named_entity.txt"

# Mở tệp đầu vào và tạo tệp đầu ra
with open(input_file, "r", encoding="utf-8") as input_f, open(output_file_with_named_entity, "w", encoding="utf-8") as output_with_ne, open(output_file_without_named_entity, "w", encoding="utf-8") as output_without_ne:
    # Duyệt từng dòng trong tệp đầu vào
    for line in input_f:
        line = line.strip()  # Loại bỏ khoảng trắng ở đầu và cuối dòng

        # Xử lý văn bản bằng spaCy
        doc = nlp(line)

        contains_named_entity = False

        # Kiểm tra xem dòng có chứa thực thể định danh không
        for ent in doc.ents:
            contains_named_entity = True
            break

        # Ghi dòng vào tệp đầu ra tương ứng
        if contains_named_entity:
            output_with_ne.write(line + "\n")
        else:
            output_without_ne.write(line + "\n")
