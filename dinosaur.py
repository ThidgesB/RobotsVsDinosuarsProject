#cool idea: per dino: randomize health through set values, if max health is below 1/2, give bonuses to attack. below 1/4 even greater bonuses



class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.dino_attack_power = attack_power
        self.health = 0

    def attack(self, robot):
        pass