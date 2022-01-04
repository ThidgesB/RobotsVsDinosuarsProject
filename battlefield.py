from herd import Herd
from fleet import Fleet
import random

def random_selection(selection):
    random_index = random.randint(0,len(selection)-1)
    result = selection[random_index]
    #print(result)
    return result

class Battlefield:
    def __init__(self):
        self.robot_fleet = Fleet()
        self.dinosaur_herd = Herd()
        pass

    def run_game(self): # can call this to run our other methods weve made
        self.display_welcome()
        self.robo_turn()
        pass

    def display_welcome(self):
        pass

    def battle(self): # this may call dino_turn and robo_turn could even call opponent_options below 
        pass

    def dino_turn(self, dinosaur): # might include show_diono_opponent_options also remember you have attack logic in class
        dino_index = random_selection(self.dinosaur_herd.dinos)
        pass

    def robo_turn(self): # might include show_robo_opponent_options  also remember you have attack logic in class
        self.show_robo_opponent_options()
        robot_index = int(input("Select robot to attack with"))
        self.show_dino_opponent_options()
        dino_index = int(input("Select dinosaur to attack"))
        self.robot_fleet.robots[robot_index].attack(self.dinosaur_herd.dinos[dino_index])  #<--,(self.herd.dinos)
        pass

    def show_dino_opponent_options(self):
        print('Current Dinosaur Herd (Enemies)')
        temp = 0
        for dino in self.dinosaur_herd.dinos:
            print(f'Press {temp} to select {dino.name} ({dino.health} HP)')
            temp += 1
        pass

    def show_robo_opponent_options(self):
        print("Current Robot Fleet")
        temp = 0
        for robot in self.robot_fleet.robots:
            print(f'Press {temp} to select {robot.name} ({robot.health} HP)')
            temp += 1

    def display_winners(self):
        pass