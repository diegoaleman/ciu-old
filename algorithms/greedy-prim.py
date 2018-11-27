# Prim algorithm

import heapq

def addNodes(matrix, length, row, visited, h):
    for i in range(length):
        val = matrix[row][i]
        if val > 0 and i not in visited:
            heapq.heappush(h,(val,[row,i]))

def prim(matrix, length):
    result = []
    visited = set()
    h = []
    heapq.heapify(h)
    addNodes(matrix,length,0,visited,h)
    visited.add(0)
    node = heapq.heappop(h)

    while len(h) > 0 and len(visited) < length:
        while node[1][1] in visited and len(h) > 0:
            node = heapq.heappop(h)

        if len(h) == 0 and node[1][1] in visited:
            return result

        result.append(node)
        addNodes(matrix,length,node[1][1],visited,h)
        visited.add(node[1][1])

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
    res = prim(matrix,n)
    print(res)

if __name__ == "__main__":
    main()
