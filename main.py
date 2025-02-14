import time
import matplotlib.pyplot as plt
import random

from inputs import Inputs
from box_plot import BoxPlot
from update_grid import UpdateGrid

def grid(x_scale, y_scale):
    list1 = []
    a = random.randint(1, (x_scale - 1))  # row number
    b = random.randint(1, (y_scale - 1))  # column number
    list1.append((a,b))
    for num in list1:
        if num == (a,b):
            a = random.randint(1, (x_scale - 1))
            b = random.randint(1, (y_scale - 1))
    updategrid = UpdateGrid(a, b)

    with plt.ion():
        updategrid.updateGrid()

        plt.pause(0.05)


def main():
    plt.figure()
    # plt.ion()
    inputs = Inputs()
    n = inputs.get_number_of_robots()
    t_or_p = inputs.get_t_or_p()
    x_scale = inputs.get_x_scale()
    y_scale = inputs.get_y_scale()

    total_grids = x_scale * y_scale

    boxplot=BoxPlot(x_scale,y_scale)
    boxplot.boxPlot()


    if t_or_p == 't':
        time_given = int(input("How much time would you like to run the robot for?"))
        total_time = 0
        i = 0

        for num in range(total_grids):
            if time_given > total_time:
                start = time.time()
                for z in range(n):
                    grid(x_scale,y_scale)

                    i += 1
                time.sleep(2)
                end = time.time()
                time_taken = end - start
                total_time += time_taken

        percentage_completed = 100 - (((total_grids - i) / total_grids) * 100)
        print(f"percentage_completed: {percentage_completed}%")
    elif t_or_p == 'p':
        percentage_given = int(input("How much percentage of the room do you want cleaned?"))
        total_percentage = 0
        total_time = 0
        i = 0
        for num in range(total_grids):
            if percentage_given > total_percentage:
                start = time.time()
                for z in range(n):
                    grid(x_scale,y_scale)
                    i += 1
                time.sleep(2)
                end = time.time()
                time_taken = end - start
                total_time += time_taken

                total_percentage = 100 - (((total_grids - i) / total_grids) * 100)
        print(f"Robots ran for {round(total_time, 2)} seconds to clean {percentage_given}% of room")

    plt.show()


main()

