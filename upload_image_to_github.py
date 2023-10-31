import base64
import os
import sys

import requests

# Thông tin kho lưu trữ (repository) trên GitHub
repo_owner = "Smith0988"
repo_name = "sticker_image"
# Token truy cập GitHub
access_token = ""

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def upload_image(file_name):
    link = []

    # Tên tệp ảnh bạn muốn tải lên

    #file_path = resource_path(f"temp_data\\{file_name}")
    #print(file_path)

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
        link = "https://github.com/Smith0988/sticker_image/blob/main/" + file_name
    if link:
        return link
    else:
        return []

if __name__ == "__main__":
    file_name = "logo_5.png"
    result = upload_image(file_name)
    print(result)
