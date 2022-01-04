from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinos = []
        self.create_herd()

    def create_herd(self):
        dino_a = Dinosaur('T-Rex', 50)
        dino_b = Dinosaur('Utahraptor', 25)
        dino_c = Dinosaur('Carcharodontosaurus', 25)

        self.dinos.append(dino_a)
        self.dinos.append(dino_b)
        self.dinos.append(dino_c)