from time import sleep


class TrafficLight:
    def __init__(self, __color=None):
        self.__color = __color
        self.switching_time = {
            'red': 7.0,
            'yellow': 2.0,
            'green': 10.0
        }

    def switching(self):
        if self.__color == 'red':
            self.__color = 'yellow'
        elif self.__color == 'yellow':
            self.__color = 'green'
        else:
            self.__color = 'red'

    def running(self):
        for _ in range(4):
            TrafficLight.switching(self)
            print(self.__color)
            sleep(self.switching_time[self.__color])


traffic_light = TrafficLight('red')
traffic_light.running()
