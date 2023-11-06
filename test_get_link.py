import requests
from bs4 import BeautifulSoup

# URL của trang web chứa danh sách hình ảnh
url = "https://postimg.cc/gallery/X1W3Tbr"
# Gửi yêu cầu GET để lấy nội dung của trang
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Tìm tất cả các thẻ a có class "img"
    a_tags = soup.find_all("a", class_="img")

    # Lặp qua danh sách các thẻ a và lấy liên kết
    for a_tag in a_tags:
        style = a_tag["style"]
        url = style.split("(")[1].split(")")[0]
        print(url)
else:
    print("Không thể truy cập trang web.")

