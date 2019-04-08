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

def get_parents(root):
    h = {}
    queue = collections.deque([])
    queue.append(root)
    h[root.value] = None

    while len(queue) > 0:
        current = queue.popleft()
        if current.left != None:
            queue.append(current.left)
            h[current.left.value] = current
        if current.right != None:
            queue.append(current.right)
            h[current.right.value] = current
    return h



def k_distance_from_node(n, root, k):
    parents = get_parents(root)
    queue = collections.deque([(n,1)])
    seen = set([n.value])

    while len(queue) > 0:
        current = queue.popleft()
        node = current[0]
        level = current[1]

        print(node.value)

        if level == k:
            queue.append(current)
            return list(queue)

        if parents[node.value] is not None and parents[node.value].value not in seen:
            queue.append((parents[node.value] ,level + 1))
            seen.add(parents[node.value].value)
        if node.left is not None and node.left.value not in seen:
            queue.append((node.left, level + 1))
            seen.add(node.left.value)
        if node.right is not None and node.right.value not in seen:
            queue.append((node.right, level + 1))
            seen.add(node.right.value)



def print_nodes(lst):
    for x in lst:
        print(x[0].value, end=' ')
    print()

if __name__ == '__main__':
    root = create_tree()
    k = 3
    result = k_distance_from_node(root.left, root, k)
    print_nodes(result)
