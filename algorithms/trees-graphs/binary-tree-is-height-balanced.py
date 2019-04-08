import collections

class Node:
    def __init__(self, v = None):
        self.value = v
        self.left = None
        self.right = None

class BTBalanced:
    def __init__(self,b,l):
        self.balanced = b
        self.level = l

def create_tree():
    root = Node(9)
    root.left = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.left.left.left = Node(1)
    root.left.left.right = Node(5)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.left.right = Node(19)
    root.right.right = Node(30)
    root.right.right.right = Node(35)
    root.right.right.right.right = Node(40)
    return root

def is_tree_balanced(root):
    if root == None:
        return BTBalanced(True,0)

    left_result = is_tree_balanced(root.left)
    if left_result.balanced == False:
        return left_result
    right_result = is_tree_balanced(root.right)
    if right_result.balanced == False:
        return right_result

    m = 1+max(left_result.level, right_result.level)
    if abs(left_result.level - right_result.level) <= 1:
        return BTBalanced(True,m)
    else:
        return BTBalanced(False,m)


if __name__ == '__main__':
    root = create_tree()
    result = is_tree_balanced(root)
    print(result.balanced)

