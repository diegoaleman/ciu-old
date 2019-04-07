import collections

class Node:
    def __init__(self, v = None):
        self.value = v
        self.left = None
        self.right = None

def create_tree():
    root = Node(8)
    root.left = Node(7)
    root.left.left = Node(3)
    root.left.left.left = Node(1)
    root.left.left.right = Node(5)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.left.right = Node(19)
    root.right.right = Node(30)
    root.right.right.right = Node(35)
    root.right.right.right.right = Node(40)
    return root

def breadth_first_search(root):
    level = 0
    # append, popleft
    queue = collections.deque([])
    queue.append((root,1))

    while len(queue) > 0:
        current = queue.popleft()
        print(current[1], end=' - ')
        print(current[0].value)
        if current[0].left != None:
            queue.append((current[0].left,current[1]+1))
        if current[0].right != None:
            queue.append((current[0].right,current[1]+1))

if __name__ == '__main__':
    root = create_tree()
    breadth_first_search(root)
