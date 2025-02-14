import matplotlib.pyplot as plt

class UpdateGrid():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def updateGrid(self):
        particularBox_xCoord = [(self.b - 1) * 0.1, (self.b - 1) * 0.1, (self.b) * 0.1, (self.b) * 0.1, (self.b - 1) * 0.1]
        particularBox_yCoord = [(self.a - 1) * 0.1, (self.a) * 0.1, (self.a) * 0.1, (self.a - 1) * 0.1, (self.a - 1) * 0.1]
        plt.fill(particularBox_xCoord, particularBox_yCoord)

    def set_a(self,a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b