# Kruskal algorithm
import heapq

def initialValues(matrix,length,h):
    for i in range(length):
        for j in range(length):
            val = matrix[i][j]
            if val > 0:
                heapq.heappush(h,(val,[i,j]))

def kruskal(matrix, length):
    h = []
    heapq.heapify(h)
    initialValues(matrix,length,h)
    visited = set()
    result = []
    node = heapq.heappop(h)

    while len(h) > 0:
        while node[1][1] in visited and len(h) > 0:
            node = heapq.heappop(h)

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
