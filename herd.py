from dinosaurs import Dinosaurs


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        titan = Dinosaurs("Titan")
        self.dinosaurs.append(titan)
