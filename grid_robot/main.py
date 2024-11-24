import time
from heuristics import *
from grid_robot_solved.search import *

if __name__ == '__main__':
    map = [
        [0, 0, 0, 0],
        [1, 4, 2, -1],
        [0, -1, 0, -1]
    ]
    robot_start_location = (0, 0)
    lamp_h = 6
    lamp_location = (2, 2)

    start_state = grid_robot_state(map=map, robot_location=robot_start_location, lamp_height=lamp_h,
                                   lamp_location=lamp_location)
    start_time = time.time()
    search_result = search(start_state, base_heuristic)
    end_time = time.time() - start_time
    # runtime
    print(end_time)
    # solution cost
    print(search_result[-1].g)