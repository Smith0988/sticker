import re


def split_sentence_2_3_and_3_3(text):
    sentence = re.sub(r'\s+', ' ', text).strip()
    if len(sentence) <= 38:
        words = sentence.split()
        num_words = len(words)
        one_half = num_words // 2
        first_half = ' '.join(words[:one_half])
        second_half = ' '.join(words[one_half:])
        if len(second_half) > len(first_half) + 10:
            word_1 = first_half.split()
            word_2 = second_half.split()
            word_1.append(word_2[0])
            word_2 = word_2[1:]
            first_half = ' '.join(word_1)
            second_half = ' '.join(word_2)
        split = [first_half, second_half]
        product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"

    else:
        words = sentence.split()
        num_words = len(words)
        one_third = num_words // 3
        two_thirds = 2 * one_third
        first_third = ' '.join(words[:one_third])
        second_third = ' '.join(words[one_third:two_thirds])
        last_third = ' '.join(words[two_thirds:])
        split = [first_third, second_third, last_third]
        product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"


    split = [item.upper() for item in split]

    return split, product_name

def split_sentence_4_2_5_2(text):
    sentence = re.sub(r'\s+', ' ', text).strip()

    if len(sentence) <= 130:
        words = sentence.split()
        num_words = len(words)
        one_fourth = num_words // 4
        two_fourths = 2 * one_fourth
        three_fourths = 3 * one_fourth
        first_part = ' '.join(words[:one_fourth])
        second_part = ' '.join(words[one_fourth:two_fourths])
        third_part = ' '.join(words[two_fourths:three_fourths])
        last_part = ' '.join(words[three_fourths:])
        split = [first_part, second_part, third_part, last_part]
        product_name = "2Pcs - 5IN " + first_part + " " + second_part + " Bumper Sticker" + " - " + first_part + " " + second_part + " Sticker"

    else:  # len(sentence) > 69
        words = sentence.split()
        num_words = len(words)
        one_fifth = num_words // 5
        two_fifths = 2 * one_fifth
        three_fifths = 3 * one_fifth
        four_fifths = 4 * one_fifth
        first_part = ' '.join(words[:one_fifth])
        second_part = ' '.join(words[one_fifth:two_fifths])
        third_part = ' '.join(words[two_fifths:three_fifths])
        fourth_part = ' '.join(words[three_fifths:four_fifths])
        last_part = ' '.join(words[four_fifths:])
        split = [first_part, second_part, third_part, fourth_part, last_part]
        product_name = "2Pcs - 5IN " + first_part + " " + second_part + " Bumper Sticker" + " - " + first_part + " " + second_part + " Sticker"

    split = [item.upper() for item in split]

    return split, product_name






if __name__ == "__main__":
    english_sentence = "A new sentence begins with a capital letter A new  sdb e swber swdbesd dern"
    #result, product_name = split_sentence_2_3_and_3_3(english_sentence)
    result, product_name = split_sentence_4_2_5_2(english_sentence)
    print(result)
    print(product_name)
