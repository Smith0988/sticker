import base64

import requests

# Thông tin kho lưu trữ (repository) trên GitHub
repo_owner = "Smith0988"
repo_name = "sticker_image"

# Tên tệp ảnh bạn muốn tải lên
file_name = "logo_1.png"

# Token truy cập GitHub
access_token = "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"

# Đường dẫn API để tạo một tệp mới
upload_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_name}"

# Đọc dữ liệu tệp ảnh
with open(file_name, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode('utf-8')

# Tạo yêu cầu PUT để tải ảnh lên
headers = {
    "Authorization": f"token {access_token}",
    "Content-Type": "application/json"
}
data = {
    "message": "Upload an image",
    "content": image_data
}
response = requests.put(upload_url, headers=headers, json=data)

if response.status_code == 201:
    print("Tải ảnh lên thành công.")
else:
    print("Lỗi khi tải ảnh lên GitHub.")
    print("Response content:", response.content)
