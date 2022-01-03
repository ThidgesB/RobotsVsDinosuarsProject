from weapon import Weapon
chosen_weapon = Weapon()


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = chosen_weapon

    def attack(self, dinosaur):
        pass