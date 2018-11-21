# Floyd-Warshall algorithm
# shortest path in a weighted graph

# Assumptions: no negative weight edges

def floydWarshall(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k or j == i:
                    continue
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

def main():
    matrix = [[0,2,999,10,999],[999,0,9,999,5],[12,999,0,6,999],[999,999,999,0,7],[999,999,3,999,0]]
    floydWarshall(matrix)

if __name__ == "__main__":
    main()
