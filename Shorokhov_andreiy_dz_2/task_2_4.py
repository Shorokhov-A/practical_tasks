employees_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employer in employees_list:

    employer = employer[employer.rindex(' ') + 1:].capitalize()
    print(f'Привет, {employer}!')
