def max_subarray_sum(l):
    if len(l) == 0:
        return None

    sub = l.copy()

    for i in range(1,len(sub)):
        if sub[i-1] + sub[i] > sub[i]:
            sub[i] += sub[i-1]
    return max(sub)

if __name__ == '__main__':
    l = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray_sum(l))
