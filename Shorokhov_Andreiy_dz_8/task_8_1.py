import re


def email_parse(arg):
    result = {}
    re_mail = re.compile(r'(?P<username>([\w.-]+))@(?P<domain>([\w-]+\.'
                         r'(ru$|com$|org$|net$)))')
    if not re_mail.match(arg):
        msg = f'wrong email: {arg}'
        raise ValueError(msg)

    result.update(*map(lambda x: x.groupdict(), re_mail.finditer(arg)))
    return result


if __name__ == '__main__':
    print(email_parse('example@geekbrains.ru'))
