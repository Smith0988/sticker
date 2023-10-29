import requests
from bs4 import BeautifulSoup

# URL của trang web bạn muốn trích xuất
url = "https://www.reddit.com/r/MemeTemplatesOfficial/comments/16i38ch/amber_heard_mercy_cosplay_elon_musk/"  # Thay URL của trang web thực tế bạn muốn trích xuất

# Gửi yêu cầu GET để lấy nội dung trang web
response = requests.get(url)

# Kiểm tra xem yêu cầu có thành công không
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích nội dung trang web
    soup = BeautifulSoup(response.text, "html.parser")

    # Tìm thẻ <div> với class tương ứng
    div_tag = soup.find("div", class_="hciOr5UGrnYrZxB11tX9s")

    # Kiểm tra xem thẻ đã tìm thấy chưa
    if div_tag:
        text = div_tag.get_text()
        print("Nội dung của thẻ <div>:", text)
    else:
        print("Không tìm thấy thẻ <div> với class tương ứng.")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
