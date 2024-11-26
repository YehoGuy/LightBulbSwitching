from search_node import search_node
from grid_robot_state import grid_robot_state
from queue import PriorityQueue

def create_open_set():
    return list()


def create_closed_set():
    return list()


def add_to_open(vn, open_set):
    open_set.append(vn)
    


def open_not_empty(open_set):
    return len(open_set) > 0
    


def get_best(open_set):
    min_node = open_set[0]
    for node in open_set:
        if node.f < min_node.f:
            min_node = node
    open_set.remove(min_node)
    return min_node
    


def add_to_closed(vn, closed_set):
    closed_set.append(vn)

#returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
#remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    for node in open_set:
        if node == vn:
            if node.g > vn.g:
                open_set.remove(node)
                return False
            return True
    return False
    

    

#returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
#remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    for node in closed_set:
        if node == vn:
            if node.g > vn.g:
                closed_set.remove(node)
                return False
            return True
    return False


# helps to debug sometimes..
def print_path(path):
    for i in range(len(path)-1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)
        #TODO: remove
        print(f"current: {current.state.get_state_str()}")
        if grid_robot_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None




