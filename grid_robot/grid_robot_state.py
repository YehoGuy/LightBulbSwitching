class grid_robot_state:
    # you can add global params

    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1)):
        self.robot_location = robot_location
        self.map = map
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location

    @staticmethod
    def is_goal_state(_grid_robot_state):
        pass

    def get_lamp_remaining(self):
        return self.lamp_height - map[self.lamp_location[0]][self.lamp_location[1]]
    
    def get_neighbors(self):
        pass

        # you can change the body of the function if you want
        # def __hash__(self):

        # you can change the body of the function if you want
        # def __eq__(self, other):
        # you can change the body of the function if you want

    def get_state_str(self):
        return self.location



    #you can add helper functions