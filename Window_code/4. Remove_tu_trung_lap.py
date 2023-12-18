# Tạo một list chứa các cụm từ cần kiểm tra
phrases_to_check = ["my teacher voice"]

# Tạo một tập hợp để theo dõi các câu đã xuất hiện
seen_phrases = set()

# Mở file đầu vào và ghi vào file mới
with open("unique_data.txt", "r", encoding="utf-8") as input_file:
    with open("filtered_sentences.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            # Kiểm tra xem câu có chứa ít nhất một trong những cụm từ cần kiểm tra không
            if any(phrase.lower() in line.lower() for phrase in phrases_to_check):
                # Chỉ ghi câu vào file mới nếu chưa xuất hiện trước đó
                if not any(phrase.lower() in seen_phrases for phrase in phrases_to_check):
                    seen_phrases.update(phrase.lower() for phrase in phrases_to_check)
                    output_file.write(line)
            else:
                # Nếu câu không chứa cụm từ cần kiểm tra, ghi vào file mới
                output_file.write(line)
