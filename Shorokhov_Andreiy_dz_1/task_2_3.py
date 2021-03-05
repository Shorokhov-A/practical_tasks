example_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
                'была', '+5', 'градусов']

idx = 0

while True:

    if example_list[idx].isdigit():

        example_list.insert(idx, '"')
        example_list[idx + 1] = f'{int(example_list[idx + 1]):02d}'
        idx += 2
        example_list.insert(idx, '"')

    elif example_list[idx].startswith(('+', '-')) \
            and example_list[idx].removeprefix('+').isdigit():

        example_list.insert(idx, '"')
        example_list[idx + 1] = f'+{int(example_list[idx + 1]):02d}'
        idx += 2
        example_list.insert(idx, '"')

    elif example_list[idx].startswith(('+', '-')) \
            and example_list[idx].removeprefix('-').isdigit():

        el_mod = int(example_list[idx]) * -1
        example_list.insert(idx, '"')
        example_list[idx + 1] = f'-{el_mod:02d}'
        idx += 2
        example_list.insert(idx, '"')

    idx += 1

    if idx == len(example_list) - 1:

        break

print(example_list)
result = ' '.join(example_list)
print(result)
