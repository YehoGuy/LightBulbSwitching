import time
from heuristics import *
from search import search

if __name__ == '__main__':
    map = [
        [0, 0, 0, 0],
        [1, 4, 2, -1],
        [0, -1, 0, -1]
    ]
    #map[Y][X]
    robot_start_location = (0, 0)
    lamp_h = 2
    lamp_location = (2, 2)

    start_state = grid_robot_state(map=map, robot_location=robot_start_location, lamp_height=lamp_h,
                                   lamp_location=lamp_location)
    start_time = time.time()
    print(start_time)
    #choose between base_heuristic and advanced_heuristic
    search_result = search(start_state, advanced_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)
    for node in search_result:
        print(node.state.robot_location)