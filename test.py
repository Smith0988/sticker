import os
import shutil

# Đường dẫn đến tệp cần di chuyển
source_file = r"C:\Users\Cong Dinh\Documents\GitHub\sticker\temp_form.xlsx"

# Đường dẫn đến thư mục đích
destination_directory = r"C:\Users\Cong Dinh\Desktop\Sticker Image\temp_data"

# Kiểm tra xem tệp nguồn tồn tại
if os.path.exists(source_file):
    # Kiểm tra xem thư mục đích tồn tại, nếu không tồn tại thì tạo thư mục đích
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Đường dẫn đầy đủ đến tệp trong thư mục đích
    destination_file = os.path.join(destination_directory, "temp_form.xlsx")

    # Di chuyển tệp từ nguồn sang đích
    shutil.move(source_file, destination_file)

    print(f"Di chuyển tệp thành công.")
else:
    print(f"Tệp nguồn không tồn tại.")
