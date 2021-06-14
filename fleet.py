from robots import Robots
from weapons import Weapons

class Fleet:
    def __init__(self):
        self.robots = []
        self.weapons = []
        self.create_fleet()

    def create_fleet(self):
        megatron = Robots("Megatron", 100, 100, self.weapons[0])
        self.robots.append(megatron)

    def create_weapons(self):
        weapon1 = Weapons("Plasma Cannon", 100)
        self.weapons.append(weapon1)
