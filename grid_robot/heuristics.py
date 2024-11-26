from grid_robot_state import grid_robot_state



# manhattan-distance heuristic |h(x)| = |x1-x2| + |y1-y2|
def base_heuristic(_grid_robot_state):
    return abs(_grid_robot_state.robot_location[0] - _grid_robot_state.lamp_location[0]) + abs(
        _grid_robot_state.robot_location[1] - _grid_robot_state.lamp_location[1])

#improved heuristic: manhattan-Distance-1 + picking up weight + one step with weight + putting down weight
def advanced_heuristic(_grid_robot_state):
    if _grid_robot_state.get_lamp_remaining() == 0:
        return base_heuristic(_grid_robot_state)
    #manhattan-Distance-1 + picking up weight + one step with weight + putting down weight
    return base_heuristic(_grid_robot_state)-1 + 1 + (1+_grid_robot_state.get_lamp_remaining())+1
