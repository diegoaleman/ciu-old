def LCS_recursive(s1,s2):
    if s1 == '' or s2 == '':
        return 0
    if s1[-1] == s2[-1]:
        return 1 + LCS_recursive(s1[:len(s1)-1],s2[:len(s2)-1])
    else:
        return max(LCS_recursive(s1[:len(s1)-1],s2), LCS_recursive(s1, s2[:len(s2)-1]))

def LCS_dynamic(s1,s2,matrix):
    for row in range(1,len(s2)+1):
        for col in range(1,len(s1)+1):
            if s1[col-1] == s2[row-1]:
                matrix[row][col] = 1 + matrix[row-1][col-1]
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])
    return matrix[len(s2)][len(s1)]

def LCS(s1,s2,option):
    if option == 1:
        return LCS_recursive(s1,s2)
    else:
        matrix = [[0 for x in range(len(s1)+1)] for y in range(len(s2)+1)]
        return LCS_dynamic(s1,s2,matrix)

if __name__ == '__main__':
    s1 = 'aggtab'
    s2 = 'gxtxayb'
    print(LCS(s1,s2,2))
