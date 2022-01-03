from weapon import Weapon
chosen_weapon = Weapon()


class Robot:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.weapon = ()

    def create_robot(self, name, weapon_name, weapon_attack_power):
        self.name = name
        self.weapon = weapon_name, weapon_attack_power



    def attack(self, dinosaur):
        pass