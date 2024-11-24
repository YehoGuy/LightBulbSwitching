
class search_node():
    def __init__(self, state, g=0, h=0, prev=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.prev = prev


    def __lt__(self, other):
        return (self.f < other.f) or (self.f == other.f and self.h < other.h)

    def get_neighbors(self):
        return self.state.get_neighbors()

