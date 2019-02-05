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
    def add_node(data, children, parent, responses):
        resps = {**parent.get_responses(), **responses}
        new_node = node.Node(data, children, parent, "", resps)
        parent.add_child(new_node)

    add_node = staticmethod(add_node)

    def navigate_tree(self, dictionary, entity, current_node):
        # extract dictionary of entities from main message
        entities_dict = dictionary['entities']

        # determine if entity we are searching for is in our dictionary from wit.ai
        if entity in entities_dict:

            # find value of the given entity
            found_entity_dict = entities_dict[entity][0]   # extract the dictionary for that entity
            new_entity = found_entity_dict['value']

            # child node found, recursively calls navigate_tree to examine child
            if current_node.get_child(new_entity) is not None:
                child = current_node.get_child(new_entity)
                return self.navigate_tree(dictionary, new_entity, child)

        # either there was no entity in the dictionary that matches the given entity or
        # a child matching the new entity was found
        if 'intent' in entities_dict:
            intent_dict = entities_dict['intent'][0]
            intent_value = intent_dict['value']
            if intent_value in current_node.get_responses():
                return current_node.get_responses()[intent_value]
            elif 'unknown' in current_node.get_responses():
                return current_node.get_responses()['unknown']
            else:
                return "I don't understand what you want from me"
        elif 'unknown' in current_node.get_responses():
            return current_node.get_responses()['unknown']
        else:
            return "I don't understand what you want from me"
