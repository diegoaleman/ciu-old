# creation
a = [[1,2,3],[4,5,6]]

r = 4
c = 5
# method 1
b = [0] * r
for i in range(r):
    b[i] = [0] * c

# method 2
d = []
for i in range(r):
    d.append([0] * c)

# method 3
e = [[0] * c for i in range(r)]

# method 4: input by the user
# the first line of input is the number of rows of the array
n = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    a.append(row)


# access
column = a[1]
element = a[1][1]



# iteration
# method 1
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# method 2
for row in a:
    for elem in row:
        print(elem, end=' ')
