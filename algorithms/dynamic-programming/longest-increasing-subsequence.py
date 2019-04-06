def LIS(l):
    acum = [1 for x in range(len(l))]

    for current in range(1,len(l)):
        for prev in range(current):
            if l[current] > l[prev]:
                acum[current] = max(acum[current], 1+acum[prev])

    return max(acum)



if __name__ == '__main__':
    l = [50, 3, 10, 7, 40, 80]
    print(LIS(l))
