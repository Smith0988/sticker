from PIL import Image

# Mở ảnh
img = Image.open('screenshot.png')

# Lấy kích thước ảnh
width, height = img.size

# Xác định kích thước mới cho phần góc trái dưới cùng (ví dụ, lấy 1/4 ảnh)
new_width = width // 2
new_height = height // 2

# Cắt và chỉ lấy phần góc trái dưới cùng
bottom_left_part = img.crop((0, height - new_height, new_width, height))

# Chuyển đổi sang chế độ màu không chứa kênh Alpha
bottom_left_part = bottom_left_part.convert('RGB')

# Lưu phần góc trái dưới cùng vào một tệp mới
bottom_left_part.save('bottom_left_part.jpg')


