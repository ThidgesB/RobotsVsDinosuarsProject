from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.robot_fleet = Fleet()
        self.dinosaur_herd = Herd()
        pass

    def run_game(self): # can call this to run our other methods weve made
        self.display_welcome()
        pass

    def display_welcome(self):
        pass

    def battle(self): # this may call dino_turn and robo_turn could even call opponent_options below 
        pass

    def dino_turn(self, dinosaur): # might include show_diono_opponent_options also remember you have attack logic in class
        pass

    def robo_turn(self, robot): # might include show_robo_opponent_options  also remember you have attack logic in class
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass