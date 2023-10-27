from datetime import datetime

# Lấy ngày và giờ hiện tại
now = datetime.now()

# Lấy ngày
day = now.day

# Lấy tháng
month = now.month

# Lấy năm
year = now.year

# Lấy giờ
hour = now.hour

# Lấy phút
minute = now.minute

# In kết quả
print(f"Ngày: {day}/{month}/{year}")
print(f"Giờ: {hour}:{minute}")
