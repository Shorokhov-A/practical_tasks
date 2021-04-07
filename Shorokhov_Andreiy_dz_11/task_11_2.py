class MyException(Exception):
    pass


def calc(x, y):
    if y == 0:
        raise MyException('Division by zero!')
    return x / y


if __name__ == '__main__':
    try:
        print(calc(100, 0))

    except MyException as e:
        print(f'error: {e}')
