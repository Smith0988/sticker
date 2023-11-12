import pandas as pd
from datetime import datetime

# Đường dẫn đến file CSV
csv_path = 'base_data_instagram.csv'

# Đọc dữ liệu từ file CSV
df = pd.read_csv(csv_path, header=None, names=['Link', 'Views'])

# Thêm cột thời gian
df['Timestamp'] = datetime.now()

# Ghi vào file tổng
total_file_path = 'total_data.csv'
df.to_csv(total_file_path, mode='a', header=False, index=False)
