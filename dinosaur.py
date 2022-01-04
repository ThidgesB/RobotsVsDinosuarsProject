#cool idea: per dino: randomize health through set values, if max health is below 1/2, give bonuses to attack. below 1/4 even greater bonuses



class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.dino_attack_power = attack_power

    def attack(self, robot): # robot_a fight watever dino we pass in when we call the function so example self.fleet.robot_a.attack(dino_a)
        pass