from random import choice


def get_jokes(jokes_number):

    """
    Generates n jokes formed with three random words taken from three lists
    :param jokes_number: number of jokes
    :return: joke list
    """

    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

    jokes_list = []

    for idx in range(jokes_number):

        first_word = choice(nouns)
        second_word = choice(adverbs)
        third_word = choice(adjectives)

        jokes_list.append(f'{first_word} {second_word} {third_word}')

    return jokes_list


print(get_jokes(3))
