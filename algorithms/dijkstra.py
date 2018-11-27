# Dijkstra algorithm
# shortest path in a weighted graph

# Assumptions: no negative weight edges

def find_min(dct, s):
    min_index = None
    min_val = 1000
    for k,v in dct.items():
        if k not in s:
            if v < min_val:
                min_val = v
                min_index = k
    return min_index

def dijkstra(matrix, length):
    s = set()
    master_node = 0
    dct = {}
    dct[master_node] = 0

    while master_node is not None:
        for i in range(length):
            if matrix[master_node][i] > 0 and i not in s:
                sum_val = matrix[master_node][i] + dct[master_node]
                if i in dct:
                    if sum_val < dct.get(i):
                        dct[i] = sum_val
                else:
                    dct[i] = matrix[master_node][i] + dct[master_node]
        s.add(master_node)
        master_node = find_min(dct, s)
        #f = filter(lambda x:x[0] not in s,list(dct.items()))
        #master_node = min(f,key=key=lambda x: x[1])
    return dct

def main():
    matrix = [[0,4,2,-1,-1],[-1,0,3,2,3],[-1,1,0,4,5],[-1,-1,-1,0,-1],[-1,-1,-1,1,0]]
    n = 5
    dct = dijkstra(matrix,n)
    print(dct.items())

if __name__ == "__main__":
    main()
