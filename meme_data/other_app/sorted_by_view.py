import pandas as pd
import numpy as np
import re



# Hàm chuyển đổi lượt xem từ dạng 'K' hoặc 'M' sang số nguyên
def convert_views(view_str):
    if pd.notna(view_str):
        view_str = str(view_str)
        matches = re.findall(r'(\d+)([KM])', view_str)
        total_views = 0
        for match in matches:
            value, unit = match
            if unit == 'K':
                total_views += int(value) * 1000
            elif unit == 'M':
                total_views += int(value) * 1000000
        return total_views
    else:
        return np.nan

# Hàm thực hiện sắp xếp và ghi ra tệp mới
def sort_and_save_csv(input_file, output_file):
    # Đọc tệp CSV
    df = pd.read_csv(input_file, header=None)

    # Chuyển đổi lượt xem sang số nguyên
    df[1] = df[1].apply(convert_views)

    # Loại bỏ các giá trị không hợp lệ
    df = df.dropna(subset=[1])

    # Sắp xếp theo số lượt xem giảm dần
    df_sorted = df.sort_values(by=1, ascending=False)

    # Ghi vào tệp CSV mới
    df_sorted.to_csv(output_file, header=False, index=False)

# Sử dụng hàm để thực hiện sắp xếp và ghi ra tệp mới
sort_and_save_csv('output.csv', 'output_sorted_by_view.csv')
