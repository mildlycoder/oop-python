class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        unit_hit = []

        x_1 = x - self.__fire_range
        y_1 = y - self.__fire_range
        y_2 = y + self.__fire_range
        x_2 = y + self.__fire_range

        for unit in units:
            if unit.in_area(x_1, y_1, x_2, y_2):
                unit_hit.append(unit.name)

        return unit_hit


u1 = Unit("1", 1, 1)
u2 = Unit("2", 2, 2)
u3 = Unit("3", 3, 3)
u4 = Unit("4", 4, 4)
u5 = Unit("5", 4, 5)

units = [u1, u2, u3, u5, u4]
dragon1 = Dragon("Dragon", 2, 2, 2)

print(dragon1.breathe_fire(4, 4, units))
