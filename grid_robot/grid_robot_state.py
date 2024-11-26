# for deep copying the map
import copy

class grid_robot_state:
    # you can add global params

    def __init__(self, robot_location, map=None, lamp_height=-1, lamp_location=(-1, -1), carried_stairs=0):
        self.robot_location = robot_location
        self.map = map
        self.lamp_height = lamp_height
        self.lamp_location = lamp_location
        self.carried_stairs = carried_stairs

    @staticmethod
    def is_goal_state(_grid_robot_state):
        condition = _grid_robot_state.robot_location[0] == _grid_robot_state.lamp_location[0] and _grid_robot_state.robot_location[1] == _grid_robot_state.lamp_location[1] and _grid_robot_state.get_lamp_remaining() == 0
        return condition

    # returns the remaining height needed to reach the lamp
    def get_lamp_remaining(self):
        return self.lamp_height - self.map[self.lamp_location[1]][self.lamp_location[0]]
    
    def get_neighbors(self):
        list_of_neighbours = []
        # pick stairs
        if self.map[self.robot_location[1]][self.robot_location[0]] > 0 and self.carried_stairs == 0:
            stairs_picked = self.map[self.robot_location[1]][self.robot_location[0]]
            new_map = copy.deepcopy(self.map)
            new_map[self.robot_location[1]][self.robot_location[0]] = 0
            list_of_neighbours.append(
                (grid_robot_state(map=new_map, 
                                  robot_location=self.robot_location, 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=stairs_picked),
                                   
                                    1)
                )
        # place stairs
        if self.carried_stairs > 0 and self.map[self.robot_location[1]][self.robot_location[0]] == 0:
            new_map = copy.deepcopy(self.map)
            new_map[self.robot_location[1]][self.robot_location[0]] = self.carried_stairs
            list_of_neighbours.append(
                (grid_robot_state(map=new_map, 
                                  robot_location=self.robot_location, 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=0),
                                   
                                    1)
                )
        # combine stairs
        # TODO go over extra check
        # also checks that the robot wont pick up more stairs then needed
        if self.carried_stairs > 0 and self.map[self.robot_location[1]][self.robot_location[0]] > 0 and self.map[self.robot_location[1]][self.robot_location[0]]+self.carried_stairs<=self.lamp_height:
            new_map = copy.deepcopy(self.map)
            new_map[self.robot_location[1]][self.robot_location[0]] = 0
            list_of_neighbours.append(
                (grid_robot_state(map=new_map, 
                                  robot_location=self.robot_location, 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=self.carried_stairs+self.map[self.robot_location[1]][self.robot_location[0]]),
                                   
                                    1)
                )
        # move right
        if self.robot_location[0] < len(self.map[self.robot_location[1]]) - 1 and self.map[self.robot_location[1]][self.robot_location[0]+1] != -1:
            list_of_neighbours.append(
                (grid_robot_state(map=self.map, 
                                  robot_location=(self.robot_location[0]+1, self.robot_location[1]), 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=self.carried_stairs),
                                   
                                    1+self.carried_stairs)
                )
        # move left
        if self.robot_location[0] > 0 and self.map[self.robot_location[1]][self.robot_location[0]-1] != -1:
            list_of_neighbours.append(
                (grid_robot_state(map=self.map, 
                                  robot_location=(self.robot_location[0]-1, self.robot_location[1]), 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=self.carried_stairs),
                                   
                                    1+self.carried_stairs)
                )
        # move up
        if self.robot_location[1] > 0 and self.map[self.robot_location[1]-1][self.robot_location[0]] != -1:
            list_of_neighbours.append(
                (grid_robot_state(map=self.map, 
                                  robot_location=(self.robot_location[0], self.robot_location[1]-1), 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=self.carried_stairs),
                                   
                                    1+self.carried_stairs)
                )
        # move down
        if self.robot_location[1] < len(self.map) - 1 and self.map[self.robot_location[1]+1][self.robot_location[0]] != -1:
            list_of_neighbours.append(
                (grid_robot_state(map=self.map, 
                                  robot_location=(self.robot_location[0], self.robot_location[1]+1), 
                                  lamp_height=self.lamp_height, 
                                  lamp_location=self.lamp_location, 
                                  carried_stairs=self.carried_stairs),
                                   
                                    1+self.carried_stairs)
                )
        return list_of_neighbours
            
        

        # you can change the body of the function if you want
    
    #   grid_robot_states are compared by data, not by address:

    def __hash__(self):
        #python list is not hashable
        return hash((self.robot_location, str(self.map), self.lamp_height, self.lamp_location, self.carried_stairs))

        # you can change the body of the function if you want
    def __eq__(self, other):
        return self.robot_location == other.robot_location and self.map == other.map and self.lamp_height == other.lamp_height and self.lamp_location == other.lamp_location and self.carried_stairs == other.carried_stairs
        
        # you can change the body of the function if you want
    def get_state_str(self):
        return f"({self.robot_location}, {self.get_lamp_remaining()}, {self.lamp_location}, {self.carried_stairs})"



    #you can add helper functions