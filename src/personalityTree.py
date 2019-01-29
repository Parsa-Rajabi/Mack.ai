import node
class Tree(object):
    root = None

    def __init__(self, root):
        self.root = root
        #add in child nodes here


    #when i add this new node, i have to add it to the children's list in its parent node
    def add_node(self, data, children, parent, text, node_function):
        new_node = node.Node(data, children, parent, text, node_function)
        parent.add_child(new_node)

    