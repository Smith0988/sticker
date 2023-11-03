import pyautogui
import subprocess
import time

# Mở Photoshop bằng lệnh thực thi
subprocess.Popen("C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe")

# Đợi một khoảng thời gian để Photoshop khởi động (thời gian này có thể cần điều chỉnh)
time.sleep(3)

# Sử dụng pyautogui để thực hiện các thao tác nhấn phím và chuột
# Ví dụ: mở một tệp ảnh
pyautogui.hotkey("ctrl", "o")
time.sleep(2)
pyautogui.typewrite("D:\\1.Github\\sticker\\logo_5.png")
pyautogui.press("enter")

time.sleep(10)

# Sau đó bạn có thể thực hiện các thao tác khác trên Photoshop bằng cách sử dụng pyautogui

# Để đảm bảo tính ổn định, bạn có thể cân nhắc sử dụng thư viện khác như AutoIt
