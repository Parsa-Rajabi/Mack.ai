class Node(object):
    data = ""
    children = []
    # parent = ""

    #constructor
    def __init__(self, data, children):
        self.data = data
        self.children = children
        # self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_data(self, data):
        self.data = data

   # def find_next_child(self, confidence, value):


