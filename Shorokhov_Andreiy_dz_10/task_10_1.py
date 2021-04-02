class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._max_len = 0
        self._number_len = 0

    def __add__(self, other):
        if self.validation(other):
            return Matrix([
                [el_1 + el_2 for el_1, el_2 in zip(row_1, row_2)]
                for row_1, row_2 in zip(self._matrix, other._matrix)
            ])
        raise ValueError('Матрицы имеют разный размер!')

    def __str__(self):
        result = []
        self.max_num_len()
        for row in self._matrix:
            for el in row:
                self.num_len(el)
                result.append(f'{el}')
                for _ in range(self.space_len()):
                    result.append(' ')
            result.pop()
            result.append('\n')
        return ''.join(result)

    def num_len(self, el):
        count = 0
        el_tmp = el
        while el_tmp:
            el_tmp = el_tmp // 10
            count += 1
        self._number_len = count
        return self._number_len

    def max_num_len(self):
        for row in self._matrix:
            for el in row:
                self.num_len(el)
                if self._number_len > self._max_len:
                    self._max_len = self.num_len(el)
        return self._max_len

    def space_len(self):
        return self._max_len - self._number_len + 1

    def validation(self, other):
        return (len(self._matrix) == len(other._matrix)) and \
               (len(self._matrix[0]) == len(other._matrix[0]))


if __name__ == '__main__':
    matrix_1 = Matrix([
        [1, 42, 5],
        [5, 2, 14]
    ])
    matrix_2 = Matrix([
        [2, 12, 24],
        [31, 7, 12]
    ])
    print(matrix_1)
    print(matrix_2)
    print(matrix_1 + matrix_2)
