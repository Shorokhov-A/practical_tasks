from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        def log_formation(item, value, kwarg=None):
            kwarg_name = ''
            if kwarg:
                kwarg_name = f'{kwarg} = '
            return f'{func.__name__}({kwarg_name}{item}: {type(item)}), ' \
                   f'значение функции: {round(value, 3)}, ' \
                   f'тип значения: {type(value)},\n'

        args_type = ''
        result = func(*args, **kwargs)
        func_item_gen = (item for item in result)
        for arg in args:
            func_item = next(func_item_gen)
            args_type += log_formation(arg, func_item)
        if kwargs:
            for key, val in kwargs.items():
                func_item = next(func_item_gen)
                args_type += log_formation(val, func_item, key)
        args_type = args_type.rstrip(',\n')
        return args_type

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    result = []
    for arg in args:
        result.append(arg ** 3)
    if kwargs:
        for key, val in kwargs.items():
            result.append(val ** 3)

    return result


if __name__ == '__main__':
    print(calc_cube(5, 8.5, 3.2, 1.8, x=2, y=1.5))
