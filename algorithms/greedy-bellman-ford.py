# Bellman Ford algorithm

def bellmanFord(matrix, length):
    L = [0]
    L.extend([999] * (length-1))
    visited = {0}
    counter = 0
    changes = True

    while counter < length and changes:
        counter+=1
        changes = not changes

        for row in range(length):
            if row not in visited:
                continue
            for col in range(length):
                val = matrix[row][col]

                if val == 0:
                    continue
                visited.add(col)
                min_val = min(L[col], val + L[row])
                if min_val != L[col]:
                    changes = True
                    L[col] = min_val
    return L



def main():
    matrix =[
        [0,10,0,0,0,8],
        [0,0,0,2,0,0,],
        [0,1,0,0,0,0],
        [0,0,-2,0,0,0],
        [0,-4,0,-1,0,0],
        [0,0,0,0,1,0]
    ]
    n = 6
    res = bellmanFord(matrix,n)
    print(res)


if __name__ == "__main__":
    main()
