# For binomial coefficient, the pascal triangle is needed
# Pascal triangle
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#
# The result of the binomial coefficient is the value
# stored in i row and j column of pascal triangle
#
# Original formula:
# n! / (k! * (n-k)!)
#
# n elements
# k size groups

def createMatrix(n):
    m = []

    for x in range(n):
        m.append([0]*(n))

    return m

def binomialCoefficient(n,k):
    matrix = createMatrix(n+1)

    for i in range(n+1):
        j_limit = min(i,k)
        for j in range(j_limit+1):
            if j==0 or j==i:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i-1][j-1]
    return matrix[n][k]

def main():
    n = int(input("N: "))
    k = int(input("K: "))
    bc = binomialCoefficient(n,k)
    print(f'The result is {bc}')

if __name__ == "__main__":
    main()
