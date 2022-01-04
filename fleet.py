from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
        
    def create_fleet(self):
        robot_a = Robot('CL4P-TP')
        robot_b = Robot('Damocles')
        robot_c = Robot('Nexus-6')

        self.robots.append(robot_a)
        self.robots.append(robot_b)
        self.robots.append(robot_c)