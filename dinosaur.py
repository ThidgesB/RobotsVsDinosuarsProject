#cool idea: per dino: randomize health through set values, if max health is below 1/2, give bonuses to attack. below 1/4 even greater bonuses



class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.dino_attack_power = attack_power

    def attack(self, robot, robot_list): # robot_a fight watever dino we pass in when we call the function so example self.fleet.robot_a.attack(dino_a)
        robot.health = robot.health - self.dino_attack_power
        print(f'{robot.name} has been attacked by {self.name} and took {self.dino_attack_power} damage. ')
        print(f'{robot.name} has {robot.health} HP')
        if robot.health <= 0:
            robot_list.remove(robot)
            print(f'{robot.name} has been defeated!')
            if robot.health < 0:
                print('OVERKILL')