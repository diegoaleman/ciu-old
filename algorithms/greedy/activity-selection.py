import operator

def activity_order(arr):
    i = 0
    print(0,end=' ')

    for j in range(1,len(arr)):
        if arr[j][0] >= arr[i][1]:
            print(j, end=' ')
            i = j
    print()

if __name__ == '__main__':
    start = [0, 5, 3, 8, 5, 1]
    finish = [6, 7, 4, 9, 9, 2]
    arr = list(zip(start,finish))
    arr.sort(key = operator.itemgetter(1))
    activity_order(arr)
