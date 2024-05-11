############
## classes##
############
class Wall:
    def __init__(self, armour, height, width):
        self.armour = armour
        self.height = height
        self.width = width
        self.volume = width * height

    def fortify(self):
        self.armour *= 2

    def get_cost(self):
        cost = self.armour * self.height
        return cost


great_wall = Wall(10, 5, 30)
rose_wall = Wall(30, 15, 60)
maria_wall = Wall(40, 30, 120)

print("----- great wall -----")
print(f"volume: {great_wall.volume}")
great_wall.fortify()
print(f"armour: {great_wall.armour}")
print(f"cost: {great_wall.get_cost()}")

print("----- rose wall -----")
print(f"volume: {rose_wall.volume}")
rose_wall.fortify()
print(f"armour: {rose_wall.armour}")
print(f"cost: {rose_wall.get_cost()}")

print("----- maria wall -----")
print(f"volume: {maria_wall.volume}")
maria_wall.fortify()
print(f"armour: {maria_wall.armour}")
print(f"cost: {maria_wall.get_cost()}")
