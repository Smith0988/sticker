import spacy

# Load model ngôn ngữ tiếng Anh
nlp = spacy.load("en_core_web_sm")

# Đọc nội dung từ tệp raw_sentence_data.txt với mã hóa UTF-8
with open('raw_sentence_data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Tạo danh sách để lưu trữ các hàng có tên riêng và các hàng không có tên riêng
lines_with_person = []
lines_without_person = []

# Duyệt qua từng hàng và kiểm tra
for line in lines:
    doc = nlp(line)
    # Kiểm tra xem có tên riêng trong hàng hay không
    if any(ent.label_ == "PERSON" for ent in doc.ents):
        lines_with_person.append(line)
    else:
        lines_without_person.append(line)

# Ghi kết quả vào các tệp riêng biệt
with open('lines_with_person.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines_with_person)

with open('lines_without_person.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines_without_person)
