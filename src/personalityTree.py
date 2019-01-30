import node


class Tree(object):
    root = None

    # constructor method
    def __init__(self, root):
        self.root = root

    # getter for root of tree
    def get_root(self):
        return self.root

    # adds a new node to the tree
    def add_node(self, data, children, parent, responses):
        new_node = node.Node(data, children, parent, responses)
        parent.add_child(new_node)

    def navigate_tree(self, dictionary, entity, current_node):
        # extract dictionary of entities from main message
        entities_dict = dictionary[1]

        # determine if entity we are searching for is in our dictionary from wit.ai
        if entity in entities_dict:

            # find value of the given entity
            found_entity_dict = entities_dict[entity]   # extract the dictionary for that entity
            new_entity = found_entity_dict['value']

            # child node found, recursively calls navigate_tree to examine child
            if current_node.get_child(new_entity) is not None:
                child = current_node.get_child(new_entity)
                self.navigate_tree(dictionary, new_entity, child)

        # either there was no entity in the dictionary that matches the given entity or
        # a child matching the new entity was found
        intent_dict = entities_dict['intent']
        intent_value = intent_dict['value']
        if intent_value in current_node.get_responses():
            return current_node.get_responses()[intent_value]
        else:
            return "I don't understand what you want from me"