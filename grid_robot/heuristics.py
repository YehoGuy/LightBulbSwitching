from grid_robot_state import grid_robot_state



# manhattan-distance heuristic
def base_heuristic(_grid_robot_state):
    return abs(_grid_robot_state.robot_location[0] - _grid_robot_state.lamp_location[0]) + abs(
        _grid_robot_state.robot_location[1] - _grid_robot_state.lamp_location[1])

# improved heuristic: manhattan-distance * (1+needed-stairs)
def advanced_heuristic(_grid_robot_state):
    return base_heuristic(_grid_robot_state)*(1+_grid_robot_state.get_lamp_remaining())
