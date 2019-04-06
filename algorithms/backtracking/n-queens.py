def isValid(partial_result):
    row_id = len(partial_result) - 1
    for x in range(row_id):
        diff = abs(partial_result[x] - partial_result[row_id])
        if diff == 0 or diff == row_id - x:
            return False
    return True

def n_queens(n,row,partial_solution,solution):
    if row==n:
        solution.append(partial_solution)
    else:
        for col in range(n):
            partial_solution.append(col)
            if isValid(partial_solution):
                n_queens(n,row+1,partial_solution[:],solution)
            partial_solution.pop()

if __name__ == '__main__':
    n = 4
    solution = []
    n_queens(n,0,[],solution)
    print(solution)
