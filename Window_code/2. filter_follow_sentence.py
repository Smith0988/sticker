with open("unmatched_data.txt", "r", encoding="utf-8") as input_file:
    with open("filtered_data.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            # Kiểm tra xem cụm từ "Please Be Patien" có xuất hiện trong hàng không
            if "sorry i'm late" in line.lower():
                # Nếu không xuất hiện, ghi hàng vào file mới
                output_file.write(line)
