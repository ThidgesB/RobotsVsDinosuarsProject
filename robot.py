from weapon import Weapon



class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon()


    def attack(self, dino): # dinosaur.name or dinosaur.health   dino_list
        dino.health = dino.health - self.weapon.weapon_attack_power
        print(f'Dinosaur {dino.name} has been attacked by robot {self.name} with {self.weapon.weapon_name} and did {self.weapon.weapon_attack_power} damage ') # this is where the math happens to subtract the robot attack power from the dino health
        print(f'{dino.name} has {dino.health} remaining')
            # think about adding an if statment "if" dino heath is 0 or less than he can be removed from the list in this step.
        pass