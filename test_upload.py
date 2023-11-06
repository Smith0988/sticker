import requests

# Đường dẫn đến tệp ảnh bạn muốn tải lên
image_path = "image_1.png"

# URL của trang tải ảnh trên postimages.org
upload_url = "https://postimages.org/"

# Tạo một phiên làm việc
session = requests.Session()

# Truy cập trang tải ảnh trên postimages.org để nhận cookie
session.get(upload_url)

# Tạo dữ liệu để gửi ảnh
files = {
    'file': (image_path, open(image_path, 'rb')),
}

# Gửi yêu cầu POST để tải ảnh lên
response = session.post(upload_url, files=files)

# Lấy kết quả trả về
response_data = response.json()

# In liên kết để chia sẻ ảnh
print(f"Link to uploaded image: {response_data['data']['url']}")
