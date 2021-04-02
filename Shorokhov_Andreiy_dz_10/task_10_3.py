class Cell:
    def __init__(self, cells_number):
        self._cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self._cells_number + other._cells_number)

    def __sub__(self, other):
        if self._cells_number > other._cells_number:
            return Cell(self._cells_number - other._cells_number)
        msg = f'{Cell(self._cells_number)} <= {Cell(other._cells_number)}'
        raise ValueError(msg)

    def __mul__(self, other):
        return Cell(self._cells_number * other._cells_number)

    def __truediv__(self, other):
        return Cell(self._cells_number // other._cells_number)

    def __str__(self):
        return f'{self.__class__.__name__}({self._cells_number})'

    def make_order(self):
        cell_el = '*****'
        cell_rest = '*'
        delimiter = '<>'
        result = []
        for _ in range(self._cells_number // len(cell_el)):
            result.extend([cell_el, delimiter])
        result.pop()
        if self._cells_number % len(cell_el):
            result.append(delimiter)
            for _ in range(self._cells_number % len(cell_el)):
                result.append(cell_rest)
        return ''.join(result)


if __name__ == '__main__':
    cell_1 = Cell(41)
    cell_2 = Cell(5)
    cell_3 = Cell(3)
    print(cell_1 + cell_2 + cell_3)
    print(cell_1 - cell_2 - cell_3)
    print(cell_1 * cell_2 * cell_3)
    print(cell_1 / cell_2 / cell_3)
    print(cell_1.make_order())
