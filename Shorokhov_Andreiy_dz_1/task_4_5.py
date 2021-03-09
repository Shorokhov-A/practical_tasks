from requests import get, utils
from decimal import Decimal
from datetime import date
import sys

CURRENCY_RATE_DICT = {}


def currency_rate(*args):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    current_date = content.split('" name')[0].split('<ValCurs Date="')[1].split('.')
    current_date = date(int(current_date[2]), int(current_date[1]), int(current_date[0]))
    for el in content.split('<CharCode>')[1:]:
        inner_data = el.split('</Value>')[0]
        currency_code = inner_data.split('</CharCode>')[0]
        currency_value = inner_data.split('<Value>')[1].replace(',', '.')
        CURRENCY_RATE_DICT[currency_code.upper()] = Decimal(currency_value)
    value_str = ''
    for item in args:
        value_str += ''.join(f'{CURRENCY_RATE_DICT.get(item.upper())}, ')
    value_str += ''.join(f'{current_date}')
    return value_str


if __name__ == '__main__':

    exit(currency_rate(*sys.argv[1:]))
