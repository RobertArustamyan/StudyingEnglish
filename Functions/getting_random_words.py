import random

def get_word(data, mode=1):
    '''
    Func that returns word from given data
    :param data: Json format data
    :param mode: 1 For English to Armenian, 2 For Armenian to English
    :return: pair of words to be displayed
    '''
    words_to_give = list(data.keys())
    word_to_give = random.choice(words_to_give)
    word_to_give_translated = data[word_to_give]

    return [word_to_give, word_to_give_translated] if mode else [word_to_give_translated, word_to_give]


if __name__ == "__main__":
    test_data = {
        "hello": "Բարև",
        "world": "Աշխարհ",
        "python": "Փայթոն",
        "code": "Կոդ",
        "learning": "Ուսում"
    }
    for i in range(5):
        print(get_word(test_data, mode=0))
