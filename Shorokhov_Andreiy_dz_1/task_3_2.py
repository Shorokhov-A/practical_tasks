WORDS = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}


def num_translate(text):
    if text.istitle():
        return WORDS.get(text.lower()).capitalize()
    return WORDS.get(text)


print(num_translate('seven'))
