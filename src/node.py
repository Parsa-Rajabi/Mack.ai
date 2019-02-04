class Node(object):
    data = ""
    children = []
    parent = ""     # another node object
    responses = dict()  # dictionary of 10 things Mack can do per topic (ie. getPreference)text = ""
    node_function = None

    # constructor
    def __init__(self, data, children, parent, text, responses):
        self.data = data
        self.children = children
        self.parent = parent
        self.text = text
        self.responses = responses

    def init_root_node(data, children, text, responses):
        node = Node(data, children, None, text, responses)
        return node

    init_root_node = staticmethod(init_root_node)

    def add_child(self, child):
        self.children.append(child)

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children

    def get_child(self, child_data):
        children_list = self.get_children()
        for child in children_list:
            if child.get_data() == child_data:
                return child
        return None

    def get_parent(self):
        return self.parent

    def get_responses(self):
        return self.responses

    def get_node_function(self):
        return self.node_function

    def set_data(self, data):
        self.data = data

    def set_children(self, children_list):
        self.children = children_list

    def set_parent(self, parent):
        self.parent = parent

    def set_text(self, text):
        self.text = text

    def set_node_function(self, method):
        self.node_function = method

    # def find_next_child(self, confidence, value):


Node.init_root_node = staticmethod(Node.init_root_node)
