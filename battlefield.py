from dinosaurs import Dinosaurs
from robots import Robots
from herd import Herd
from fleet import Fleet

class Battlefield:
# herd = Herd()
# print(herd.dinosaurs[0].type)
#
# fleet = Fleet()
# print(fleet.robots[0].name)
    def __init__(self):
        self.herd = Herd()
        self.fleet = Fleet()

    def battle(self):
        self.fleet.robots[0].robot_attack(self.herd.dinosaurs[0])
        self.herd.dinosaurs[0].dino_attack(self.fleet.robots[0])

#
#     def choose_char():
#         Dinosaurs
#
#         Robots
#
#         playerChoice = input("Would you like to be robot or dinosaur? ")
#         if playerChoice == "Dinosaur":
#             player = Dinosaurs()
#         elif playerChoice == "Robot":
#             player == Robots()
#
#     return player
#
#
# def fight_club():
#     player = choose_char()
#



