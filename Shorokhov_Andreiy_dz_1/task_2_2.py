example_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
                'была', '+5', 'градусов']
list_processed = []

for element in example_list:

    list_processed.append(element)

    if element.isdigit():

        list_processed.pop()
        list_processed.extend(['"', f'{int(element):02d}', '"'])

    elif element.startswith(('+', '-')) \
            and element.removeprefix('+').isdigit():

        list_processed.pop()
        list_processed.extend(['"', f'+{int(element):02d}', '"'])

    elif element.startswith(('+', '-')) \
            and element.removeprefix('-').isdigit():

        el_mod = int(element) * -1
        list_processed.pop()
        list_processed.extend(['"', f'-{el_mod:02d}', '"'])

print(list_processed)
result = ' '.join(list_processed)
print(result)
