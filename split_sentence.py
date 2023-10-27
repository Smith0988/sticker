import re


def split_sentence_by_length(text):

    sentence = re.sub(r'\s+', ' ', text).strip()

    if len(sentence) <= 50:
        words = sentence.split()
        num_words = len(words)
        one_half = num_words // 2
        first_half = ' '.join(words[:one_half])
        second_half = ' '.join(words[one_half:])
        split = [first_half, second_half]
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


if __name__ == "__main__":

    english_sentence = "Grow Through What You Go Through"
    result = split_sentence_by_length(english_sentence)

    for i, sentence in enumerate(result):
        print(f"Sentence {i + 1}: {sentence}")
