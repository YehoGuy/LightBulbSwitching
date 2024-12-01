from grid_robot_state import grid_robot_state

def distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

# manhattan-distance heuristic |h(x)| = |x1-x2| + |y1-y2|
def base_heuristic(_grid_robot_state):
    return abs(_grid_robot_state.robot_location[0] - _grid_robot_state.lamp_location[0]) + abs(
        _grid_robot_state.robot_location[1] - _grid_robot_state.lamp_location[1])

#improved heuristic: manhattan-Distance-1 + picking up weight + one step with weight + putting down weight
def advanced_heuristic(_grid_robot_state):
    if _grid_robot_state.get_lamp_remaining() == 0:
        return base_heuristic(_grid_robot_state)
    return min(distance(_grid_robot_state.robot_location, _grid_robot_state.closest_stairs_loc) + 1 + distance(_grid_robot_state.closest_stairs_loc, _grid_robot_state.lamp_location)*_grid_robot_state.get_lamp_remaining() + 1,
               base_heuristic(_grid_robot_state)*_grid_robot_state.get_lamp_remaining())
    #manhattan-Distance-1 + picking up weight + one step with weight + putting down weight
    #return base_heuristic(_grid_robot_state)-1 + 1 + (1+_grid_robot_state.get_lamp_remaining())+1
