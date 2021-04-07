class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b,
                             self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}i'


if __name__ == '__main__':
    complex_number_1 = ComplexNumber(3, 1)
    complex_number_2 = ComplexNumber(2, 5)
    complex_number_3 = ComplexNumber(5, 3)
    print(complex_number_1)
    print(complex_number_2)
    print(complex_number_3)
    print(complex_number_1 + complex_number_2 + complex_number_3)
    print(complex_number_1 * complex_number_2 * complex_number_3)
