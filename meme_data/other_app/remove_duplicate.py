
import pandas as pd

# Đọc tệp CSV
df = pd.read_csv('output_sorted_by_repeat.csv', header=None, names=['Link', 'Value1', 'Value2'])

# Loại bỏ các hàng trùng lặp dựa trên cột thứ 1 (Link) và cột thứ 3 (Value2)
df_deduplicated = df.drop_duplicates(subset=['Link', 'Value2'])

# Ghi DataFrame sau khi loại bỏ các hàng trùng lặp vào một tệp mới
df_deduplicated.to_csv('output_deduplicated.csv', index=False)
