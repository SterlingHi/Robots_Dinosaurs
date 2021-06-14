from robots import Robots


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        megatron = Robots("Megatron")
        self.robots.append(megatron)
