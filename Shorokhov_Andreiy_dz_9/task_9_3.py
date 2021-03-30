from decimal import Decimal


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


class Position(Worker):
    pass

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        total_income = 0
        for val in self._income.values():
            total_income += Decimal(val)

        return total_income


employer_1 = Position('Игорь', 'Иванов', 'Старший мастер', 16000, 1000)
employer_2 = Position('Сергей', 'Петров', 'Начальник участка', 20000, 3000)
print(employer_1.get_full_name())
print(employer_1.get_total_income())
print(employer_2.get_full_name())
print(employer_2.get_total_income())
