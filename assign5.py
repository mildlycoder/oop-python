###########################
## Heirachial Inheritance##
###########################


class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows <= 0:
            raise Exception("Not enough arrows")
        self.__num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)
        pass

    def triple_shot(self, target):
        super().use_arrows(3)
        print(f"{super().get_name()} shot {target.get_name()}")


cb = Crossbowman("Hunter", 4)
hu = Human("PK")

cb.triple_shot(hu)
print(cb.get_num_arrows())
