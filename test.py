def tach_theo_tu(text, gioi_han=130):
    if len(text) > 130:
        words = text.split()
        result = ''
        current_length = 0

        for word in words:
            word_length = len(word) + 1  # Cộng thêm 1 để tính cả khoảng trắng sau mỗi từ
            if current_length + word_length <= gioi_han:
                result += word + ' '
                current_length += word_length
            else:
                break
        return result.rstrip() + '...'
    else:
        return text

# Ví dụ sử dụng
text_input = "Security is mostly a superstition. It does not exist in nature, nor do the children of men as a whole experience it. Avoiding danger is no safer in the long run than outright exposure. Life is either a daring adventure or nothing."
text_output = tach_theo_tu(text_input)
print(text_output)
