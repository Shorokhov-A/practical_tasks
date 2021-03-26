from functools import wraps


def val_checker(val):
    def _val_checker(func):
        @wraps(func)
        def wrapper(arg):
            result = func(arg)
            if val(result):
                return result
            msg = f'wrong val: {arg}'
            raise ValueError(msg)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(9))
