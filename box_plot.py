import matplotlib.pyplot as plt

class BoxPlot():
    def __init__(self, x1,y1):
        self.x_scale = x1
        self.y_scale = y1

    def boxPlot(self):
        x = []
        y = []
        for num in range(self.x_scale):
            x.append(num * 0.1)
        for num in range(self.y_scale):
            y.append(num * 0.1)
        plt.grid()
        plt.xlim(xmin=0, xmax=(self.x_scale * 0.1))
        plt.ylim(ymin=0, ymax=(self.y_scale * 0.1))
        plt.xticks(x)
        plt.yticks(y)

    def set_x_scale(self,x1):
        self.x_scale = x1

    def set_y_scale(self, y1):
        self.y_scale = y1

    def get_x_scale(self):
        return self.x_scale

    def get_y_scale(self):
        return self.y_scale
