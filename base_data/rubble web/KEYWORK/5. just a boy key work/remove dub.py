# Tạo một tập hợp để theo dõi các dòng đã xuất hiện
seen_lines = set()

# Mở file đầu vào và ghi vào file mới
with open("filtered_sentences.txt", "r", encoding="utf-8") as input_file:
    with open("unique_filtered_sentences.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            # Loại bỏ khoảng trắng và kiểm tra xem dòng đã xuất hiện trước đó chưa
            clean_line = line.strip()
            if clean_line not in seen_lines:
                seen_lines.add(clean_line)
                output_file.write(clean_line + "\n")
