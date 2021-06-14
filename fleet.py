from robots import Robots


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_herd(self):
        megatron = Robots("Megatron")
        self.robots.append(megatron)
