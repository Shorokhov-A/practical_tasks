class Road:

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asphalt_weight(self, weight, height):
        square_meter_weight = float(weight)
        roadbed_height = float(height)
        result = self._length * self._width * square_meter_weight * roadbed_height

        return result


Road_1 = Road(100, 20)
Road_2 = Road(500, 20)
print(Road_1.asphalt_weight(25, 5))
print(Road_2.asphalt_weight(25, 5))
