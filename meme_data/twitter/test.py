from bs4 import BeautifulSoup

# HTML của thẻ a
html = """
<a href="/Kettavan__Memes/status/1722167673935843685/analytics" aria-label="3138 views. View post analytics" role="link" class="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1777fci r-bt1l66 r-1ny4l3l r-bztko3 r-lrvibr">
    <div dir="ltr" class="css-901oao r-1awozwy r-14j79pv r-6koalj r-37j5jr r-a023e6 r-16dba41 r-1h0z5md r-rjixqe r-bcqeeo r-o7ynqc r-clp7b1 r-3s2u2q r-qvutc0" style="text-overflow: unset;">
        <div class="css-1dbjc4n r-xoduu5">
            <div class="css-1dbjc4n r-1niwhzg r-sdzlij r-1p0dtai r-xoduu5 r-1d2f490 r-xf4iuw r-1ny4l3l r-u8s1d r-zchlnj r-ipm5af r-o7ynqc r-6416eg"></div>
            <svg viewBox="0 0 24 24" aria-hidden="true" class="r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-1hdv0qi">
                <g>
                    <path d="M8.75 21V3h2v18h-2zM18 21V8.5h2V21h-2zM4 21l.004-10h2L6 21H4zm9.248 0v-7h2v7h-2z"></path>
                </g>
            </svg>
        </div>
        <div class="css-1dbjc4n r-xoduu5 r-1udh08x">
            <span data-testid="app-text-transition-container" style="transform: translate3d(0px, 0px, 0px); transition-property: transform; transition-duration: 0.3s;">
                <span class="css-901oao css-16my406 r-poiln3 r-n6v787 r-1cwl3u0 r-1k6nrdp r-1pn2ns4 r-qvutc0" style="text-overflow: unset;">
                    <span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0" style="text-overflow: unset;">3.1K</span>
                </span>
            </span>
        </div>
    </div>
</a>
"""

# Phân tích HTML
soup = BeautifulSoup(html, 'html.parser')

# Tìm thẻ span chứa giá trị "3.1K"
span_element = soup.find('span', class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')

# Lấy giá trị
value = span_element.get_text()
print(value)
