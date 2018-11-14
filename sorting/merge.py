# Merge sort
# Time -> O(nlog)
# Space -> O(n)
def mergesort(list):
    if len(list) < 2:
        return list
    result = []
    middle = len(list) // 2
    L = mergesort(list[:middle])
    R = mergesort(list[middle:])

    i = j = 0
    while (i < len(L)) and (j < len(R)):
        if L[i] < R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1
    if i == len(L):
        result.extend(R[j:])
    else:
        result.extend(L[i:])

    return result
