import re

def split_sentence_by_length(text):


    sentence = re.sub(r'\s+', ' ', text).strip()
    if len(sentence) <= 35:
        words = sentence.split()
        num_words = len(words)
        one_half = num_words // 2
        first_half = ' '.join(words[:one_half])
        second_half = ' '.join(words[one_half:])
        if len(second_half) > len(first_half) +10:
            word_1 = first_half.split()
            word_2 = second_half.split()
            word_1.append(word_2[0])
            word_2 = word_2[1:]
            first_half = ' '.join(word_1)
            second_half = ' '.join(word_2)
        split = [first_half, second_half]
        product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"
    elif len(sentence) > 35 and len(sentence) <= 52:
        words = sentence.split()
        num_words = len(words)
        one_third = num_words // 3
        two_thirds = 2 * one_third
        first_third = ' '.join(words[:one_third])
        second_third = ' '.join(words[one_third:two_thirds])
        last_third = ' '.join(words[two_thirds:])
        split = [first_third, second_third, last_third]
        product_name = "2Pcs - 5IN " + sentence + " Bumper Sticker" + " - " + sentence + " Sticker"
    else:
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



    split = [item.upper() for item in split]

    return split, product_name


if __name__ == "__main__":

    english_sentence = "A new sentence begins with a capital letter A new sentence begins"
    result, product_name = split_sentence_by_length(english_sentence)

    print(result)
    print(product_name)
