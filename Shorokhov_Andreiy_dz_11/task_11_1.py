import re


class Date:
    re_date = re.compile(r'(?P<day>\d*)-(?P<month>\d*)-(?P<year>\d*)')

    @classmethod
    def get_numbers(cls, date_str):
        result = {}
        txt = str(date_str)
        result.update(*map(lambda x: x.groupdict(), cls.re_date.finditer(txt)))
        for key, val in result.items():
            val = int(val)
            result[key] = val
        return result

    @staticmethod
    def validator(date_list):
        for key, val in date_list.items():
            msg = f'{key}: {val}'
            if key == 'day' and val > 31 or key == 'month' and val > 12:
                raise ValueError(msg)
        return 'Validation successful.'


if __name__ == '__main__':
    cur_date = Date.get_numbers('03-04-2021')
    print(cur_date)
    try:
        print(Date.validator(cur_date))
    except ValueError as e:
        print(f'ERROR: {e}')
