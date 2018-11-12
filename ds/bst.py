import collections

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

    def breadth_first_print(self):
        queue = collections.deque()
        queue.append(self.head)
        while len(queue) > 0:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            print(node.data, end=' ')
        print()

    def find_deleted_node(self,data):
        prev = None
        it = self.head

        # iterate until node is found or None is found
        while it.data is not data and it is not None:
            prev = it
            if data > it.data:
                it = it.right
            else:
                it = it.left

        return [prev, it]

    def number_of_childs(self,node):
        left = node.left
        right = node.right

        if left and right:
            return 2
        elif (left and not right) or (right and not left):
            return 1
        else:
            return 0

    def delete_value(self,data):
        find_node = self.find_deleted_node(data)
        prev_node = find_node[0]
        node = find_node[1]
        num_of_childs = self.number_of_childs(node)

        if num_of_childs == 0:
            if prev_node is None:
                self.head = None
            else:
                if node.data > prev_node.data:
                    prev_node.right = None
                else:
                    prev_node.left = None
            del node





bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(20)
bst.insert(1)
bst.insert(6)

bst.breadth_first_print()

bst.delete_value(7)

bst.breadth_first_print()


