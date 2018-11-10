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

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            inserted = False
            it = self.head
            while not inserted:
                if data > it.data:
                    if it.right is None:
                        it.right = new_node
                        inserted = True
                    else:
                        it = it.right
                elif data < it.data:
                    if it.left is None:
                        it.left = new_node
                        inserted = True
                    else:
                        it = it.left
                else:   # if inserted value already exists
                    return 0

    def print(self, option):
        if option == 1:
            self.preorder(self.head)
        elif option == 2:
            self.inorder(self.head)
        else:
            self.postorder(self.head)
        print()

    # used to create copy of a tree
    def preorder(self,node):
        if node is not None:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    # list elements from min to max
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    # used to delete tree
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

