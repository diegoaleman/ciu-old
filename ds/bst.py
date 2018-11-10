class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# TODO
# - insert
# - get_node_count -> count of values stored
# - print_values -> values in the tree, from min to max
# - delete_tree
# - is_in_tree -> true if given value exist in tree
# - get_height -> height in nodes
# - get_min -> returns min value stored in the tree
# - get_max -> returns max value stored in the tree
# - is_binary_search_tree
# - delete_value
# - get_successor -> returns next-highest value in tree after given value


class BST:
    def __init__(self):
        self.head = None

