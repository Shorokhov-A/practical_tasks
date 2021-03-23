def add_sales(argv):
    prices = []
    for el in argv:
        prices.extend([el, '\n'])
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(prices)


if __name__ == '__main__':
    import sys

    add_sales(sys.argv[1:])
