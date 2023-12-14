import re


def split_sentence_2_3_and_3_3(text):
    sentence = re.sub(r'\s+', ' ', text).strip()
    if len(sentence) <= 80:
        words = sentence.split()
        num_words = len(sentence)
        target = num_words // 2
        result_1 = ''
        result_2 = ''
        temp_len = 0
        for word in words:
            temp_len = temp_len + len(word) + 1
            if temp_len <= target + 3:
                result_1 = result_1 + word + ' '
            else:
                result_2 = result_2 + word + ' '
        result_1 = result_1.strip()
        result_2 = result_2.strip()
        split = [result_1, result_2]
        product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"

    else:
        words = sentence.split()
        num_words = len(sentence)
        target_1 = num_words // 3
        target_2 = target_1 * 2
        temp_len = 0
        result_1 = ''
        result_2 = ''
        result_3 = ''
        for word in words:
            temp_len = temp_len + len(word) + 1
            if temp_len <= target_1:
                result_1 = result_1 + word  + ' '
            elif target_1 < temp_len <= target_2 + 3:
                result_2 = result_2 + word  + ' '
            else:
                result_3 = result_3 + word + ' '

        result_1 = result_1.strip()
        result_2 = result_2.strip()
        result_3 = result_3.strip()

        split = [result_1, result_2, result_3]
        product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"

    split = [item.upper() for item in split]

    return split, product_name

def check_len_by_130(text, gioi_han=130):

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


def split_sentence_4_2_5_2(text):

    sentence = re.sub(r'\s+', ' ', text).strip()
    if len(sentence) > 130:
        sentence = check_len_by_130(sentence)

    words = sentence.split()
    num_words = len(sentence)
    target_1 = num_words // 4
    target_2 = target_1 * 2
    target_3 = target_1 * 3

    result_1 = ''
    result_2 = ''
    result_3 = ''
    result_4 = ''
    temp_len = 0

    for word in words:
        temp_len += len(word) + 1
        if temp_len <= target_1 + 1:
            result_1 = result_1 + word + " "
        elif target_1 < temp_len <= target_2 + 3:
            result_2 = result_2 + word + " "
        elif target_2 < temp_len <= target_3 + 5:
            result_3 = result_3 + word + " "
        else:
            result_4 = result_4 + word + " "
        #result_1 = result_1.strip()
        #result_2 = result_2.strip()
        #result_3 = result_3.strip()
        #result_4 = result_4.strip()

    split = [result_1, result_2, result_3, result_4]
    product_name = "2Pcs - 5IN {} {} Bumper Sticker - {} {} Sticker".format(result_1, result_2, result_1, result_2)

    split = [item.upper() for item in split]

    return split, product_name


def split_sentence_chu_de(text, text_base):

    sentence = re.sub(r'\s+', ' ', text_base).strip()

    index = sentence.lower().find(text)

    # Tách chuỗi thành hai phần
    split_result = [
        sentence[:index + len(text)].upper(),
        sentence[index + len(text):].strip()
    ]



    split = [split_result[0], split_result[1], "1", "2", "3"]

    product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"

    split = [item.upper() for item in split]

    return split, product_name



if __name__ == "__main__":
    english_sentence = "don't honk at me im popping my pimples"
    result, product_name = split_sentence_chu_de("please don't honk at me", english_sentence)
    print(result)
    print(product_name)
