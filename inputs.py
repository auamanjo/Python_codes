class Inputs():
    def __init__(self):
        self.y_scale = int(input("How much tiles are there in y direction of the room?"))
        self.x_scale = int(input("How much tiles are there in x direction of the room?"))
        self.number_of_robots = int(input("How many robots are there in the room?"))
        print("Would you like to provide with time or percentage of tiles cleaned? ")
        self.t_or_p = (input("Enter t for time or p for percentage of tiles?")).lower()


    def get_number_of_robots(self):
        return self.number_of_robots

    def get_t_or_p(self):
        return self.t_or_p

    def get_y_scale(self):
        return self.y_scale

    def get_x_scale(self):
        return self.x_scale
