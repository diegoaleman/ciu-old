# ABCDGH
# AEDFHR
# ADH
def LCS_recursive(s1,s2):
    if s1 == '' or s2 == '':
        return 0
    if s1[-1] == s2[-1]:
        return 1 + LCS_recursive(s1[:len(s1)-1],s2[:len(s2)-1])
    else:
        return max(LCS_recursive(s1[:len(s1)-1],s2), LCS_recursive(s1, s2[:len(s2)-1]))


def LCS_dynamic(s1,s2):
    matrix = [[0]*(len(s1)+1)]*(len(s2)+1)
    return matrix

def LCS(s1,s2,option):
    if option == 1:
        return LCS_recursive(s1,s2)
    else:
        return LCS_dynamic(s1,s2)

if __name__ == '__main__':
    s1 = 'aggtab'
    s2 = 'gxtxayb'
    print(LCS(s1,s2,2))
