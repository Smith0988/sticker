import pyautogui


pyautogui.sleep(2)  # Chờ 2 giây
# Lấy tọa độ hiện tại của con trỏ chuột
x, y = pyautogui.position()

print(f"Tọa độ hiện tại: ({x}, {y})")
