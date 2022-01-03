from weapon import Weapon
chosen_weapon = Weapon()


class Robot:
    def __init__(self, name):
        self.name = name

    def attack(self, dinosaur):
        pass

    def health(self, robot_hp):
        self.robot_health = robot_hp

    def weapon(self):
        weapon = chosen_weapon.__init__('Damocles', 25)

    # def robot_name(self, robot_name):
    #     self.name = robot_name
