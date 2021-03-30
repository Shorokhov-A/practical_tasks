class Car:
    is_police = False

    def __init__(self, color, name):
        self.police_id = ''
        if self.is_police:
            self.police_id = '(ПОЛИЦИЯ) '
        self.speed = 0
        self.color = color
        self.name = name
        self.direction = None

    def go(self, speed):
        self.speed = speed
        print(f'Транспортное средство {self.name} {self.color} {self.police_id}двигается.')

    def stop(self):
        self.speed = 0
        print(f'Транспортное средство {self.name} {self.color} {self.police_id}остановилось.')

    def turn(self, direction=None):
        self.direction = direction
        if self.direction:
            print(f'Транспортное средство {self.name} {self.color} {self.police_id}'
                  f'повернуло {self.direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.name} {self.color} {self.police_id}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'ВНИМАНИЕ! <<{self.name} {self.color}>>: ПРЕВЫШЕНИЕ СКОРОСТНОГО РЕЖИМА {speed_limit} км/ч')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'ВНИМАНИЕ! <<{self.name} {self.color}>>: ПРЕВЫШЕНИЕ СКОРОСТНОГО РЕЖИМА {speed_limit} км/ч')
        super().show_speed()


class PoliceCar(Car):
    is_police = True


car_1 = TownCar('white', 'Hyundai')
car_2 = SportCar('red', 'Lamborghini')
car_3 = WorkCar('green', 'DAF')
car_4 = PoliceCar('blue', 'Ford')

car_1.go(70)
car_1.show_speed()
car_1.turn()
car_1.stop()

car_2.go(120)
car_2.show_speed()
car_2.turn('направо')
car_2.stop()

car_3.go(40)
car_3.show_speed()
car_3.turn('налево')
car_3.stop()

car_4.go(100)
car_4.show_speed()
car_4.turn()
car_4.stop()
