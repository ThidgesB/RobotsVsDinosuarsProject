from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.robot_fleet = Fleet()
        self.dinosaur_herd = Herd()
        pass

    def run_game(self): # can call this to run our other methods weve made
        self.display_welcome()
        self.battle()
        pass

    def display_welcome(self):
        print('Welcome to Jurassic Arena')
        pass

    def battle(self): # this may call dino_turn and robo_turn could even call opponent_options below 
        battle_over = False          #boolean flag
        while battle_over == False:  #loop over battle until flag is tripped
            self.robo_turn()
            if len(self.dinosaur_herd.dinos) == 0:   #if there are no dinos left, trip flag
                winning_team = 'Robots'
                battle_over = True
            else:
                self.dino_turn()
                if len(self.robot_fleet.robots) == 0: #if there are no robots left, trip flag
                    winning_team = 'Dinosaurs'
                    battle_over = True
                else:
                    battle_over = False        #Else, continue battle
        if battle_over == True:
            self.display_winners(winning_team)
            
        
    def dino_turn(self): # might include show_dino_opponent_options also remember you have attack logic in class
        self.show_dino_opponent_options()
        dino_index = int(input('Select Dinosaur to Attack with'))
        self.show_robo_opponent_options()
        robot_index = int(input('Select Robot to Attack'))
        self.dinosaur_herd.dinos[dino_index].attack(self.robot_fleet.robots[robot_index], self.robot_fleet.robots)
        

    def robo_turn(self): # might include show_robo_opponent_options  also remember you have attack logic in class
        self.show_robo_opponent_options()
        robot_index = int(input('Select robot to attack with'))
        self.show_dino_opponent_options()
        dino_index = int(input('Select dinosaur to attack'))
        self.robot_fleet.robots[robot_index].attack(self.dinosaur_herd.dinos[dino_index], self.dinosaur_herd.dinos)  #<--,(self.herd.dinos)
        

    def show_dino_opponent_options(self):
        print('Current Dinosaur Herd (Enemies)')
        temp = 0
        for dino in self.dinosaur_herd.dinos:
            print(f'Press {temp} to select {dino.name} ({dino.health} HP)')
            temp += 1
        

    def show_robo_opponent_options(self):
        print('Current Robot Fleet')
        temp = 0
        for robot in self.robot_fleet.robots:
            print(f'Press {temp} to select {robot.name} ({robot.health} HP)')
            temp += 1

    def display_winners(self, winner):
        print(f'{winner} have triumphed!')