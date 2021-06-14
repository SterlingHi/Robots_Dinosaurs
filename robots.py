


class Robots:
    def __init__(self, name, health, power, weapon):
        self.name = name
        self.health = health
        self.power = power
        self.weapon = weapon

    def robot_attack(self, dino):
        dino.health -= self.weapon.attackpower
        self.power -= 20
