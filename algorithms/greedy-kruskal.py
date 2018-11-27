# Kruskal algorithm
import heapq

def initHeap(matrix,length,h):
    for i in range(length):
        for j in range(length):
            val = matrix[i][j]
            if val > 0:
                heapq.heappush(h,(val,[i,j]))

def setUnion(parent,x,y):
    x_set = findParent(parent,x)
    y_set = findParent(parent,y)

    parent[x_set] = y_set

def findParent(parent, index):
    if parent[index] == -1:
        return index
    if parent[index] != -1:
        return findParent(parent,parent[index])

def validNode(parent,x,y):
    x_set = findParent(parent,x)
    y_set = findParent(parent,y)

    if x_set == y_set:
        return False
    else:
        setUnion(parent,x,y)
        return True

def kruskal(matrix, length):
    h = []
    result = []
    visited = set()
    initHeap(matrix,length,h)
    node = heapq.heappop(h)
    valid_node = True
    parent = [-1] * length
    setUnion(parent,node[1][0], node[1][1])

    while len(h) > 0:
        while not valid_node and len(h) > 0:
            node = heapq.heappop(h)
            valid_node = validNode(parent,node[1][0],node[1][1])
        valid_node = not valid_node

        if len(h) == 0 and node[1][1] in visited:
            return result

        visited.add(node[1][0])
        visited.add(node[1][1])
        result.append(node)

    return result

def main():
    matrix = [
        [0,2,3,3,-1,-1,-1],
        [2,0,4,-1,3,-1,-1],
        [3,4,0,5,1,6,-1],
        [3,-1,5,0,-1,7,-1],
        [-1,3,1,-1,0,8,-1],
        [-1,-1,6,7,8,0,9],
        [-1,-1,-1,-1,-1,9,0]]
    n = 7
    res = kruskal(matrix,n)
    print(res)


if __name__ == "__main__":
    main()
