def show_sale(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            if args and len(args) == 1:
                if line_num >= int(*args):
                    print(line.strip())
            elif args and len(args) == 2:
                range_start, range_end = map(int, args)
                if range_start <= line_num <= range_end:
                    print(line.strip())
            else:
                print(line.strip())


if __name__ == '__main__':
    import sys

    show_sale(sys.argv)
