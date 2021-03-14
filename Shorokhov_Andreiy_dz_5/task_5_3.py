tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Анатолий', 'Артём'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

klasses_dict = {
    klass: klasses[klass]
    for klass in range(len(klasses))
}

tutors_gen = (
    (tutors[idx], klasses_dict.get(idx))
    for idx in range(len(tutors))
)

for _ in range(len(tutors) + 1):
    tutors_gen_item = next(tutors_gen)
    print(tutors_gen_item, type(tutors_gen_item))
