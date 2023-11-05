import pyautogui
import subprocess
import time

# Mở Photoshop bằng lệnh thực thi
subprocess.Popen("E:\\0.Sticker\\0. Phan Mem\\Photoshop CS6x64Portable\\App\\Ps\\Photoshop.exe")

# Đợi một khoảng thời gian để Photoshop khởi động (thời gian này có thể cần điều chỉnh)
time.sleep(10)

# Sử dụng pyautogui để thực hiện các thao tác nhấn phím và chuột
# Ví dụ: mở một tệp ảnh
pyautogui.hotkey("ctrl", "o")
time.sleep(2)
pyautogui.typewrite("C:\\Users\\Cong Dinh\\Desktop\\BumperSticker_2x2.psd")
pyautogui.press("enter")

time.sleep(10)

# Sau đó bạn có thể thực hiện các thao tác khác trên Photoshop bằng cách sử dụng pyautogui

# Để đảm bảo tính ổn định, bạn có thể cân nhắc sử dụng thư viện khác như AutoIt
