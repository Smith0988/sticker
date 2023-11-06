def sort_urls_by_number(urls):
    # Hàm tự tạo để trích xuất số từ phần đầu tiên của URL
    def extract_number(url):
        parts = url.split("-")
        if len(parts) > 1:
            first_part = parts[1]
            try:
                number = int(first_part)
                return number
            except ValueError:
                return 0
        return 0

    # Sắp xếp danh sách các URL theo số tăng dần
    sorted_urls = sorted(urls, key=extract_number)

    return sorted_urls

# Ví dụ sử dụng hàm
urls = [
    "https://i.postimg.cc/L6HGt8MM/ST20231105-102612-copy.jpg",
    "https://i.postimg.cc/KvzJck24/ST20231105-102613-copy.jpg",
    "https://i.postimg.cc/BvgK1p53/ST20231105-102608-copy.jpg",
    "https://i.postimg.cc/6QjCmz80/ST20231105-102609-copy.jpg",
    "https://i.postimg.cc/J0W06B5x/ST20231105-102610-copy.jpg",
    "https://i.postimg.cc/fTzTVs2V/ST20231105-102611-copy.jpg"
]

sorted_urls = sort_urls_by_number(urls)

# In danh sách đã sắp xếp
for url in sorted_urls:
    print(url)
