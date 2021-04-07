class MyNotNumber(Exception):
    pass


result = []
while True:
    user_input = input('Введите число (для выхода введите «stop»):\n')

    if user_input == 'stop':
        break

    try:
        if not user_input.isdigit():
            raise MyNotNumber('Вы ввыли не число')
    except MyNotNumber as e:
        print(f'error: {e}')
    else:
        user_input = int(user_input)
        result.append(user_input)

print(result)
