def max_subarray_sum(l):
    max_val = prev_max = -9999

    for i in range(len(l)):
        if l[i] > prev_max + l[i]:
            prev_max = l[i]
        else:
            prev_max += l[i]

        if prev_max > max_val:
            max_val = prev_max 

    return max_val

if __name__ == '__main__':
    l = [-2,1,-3,4,-1,2,1,-5,4]
    print(max_subarray_sum(l))
