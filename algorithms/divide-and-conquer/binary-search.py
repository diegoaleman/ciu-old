# Binary Search (recursive)

def binarySearch(target,start,end,arr):
    if start > end:
        return None

    middle = (end + start) // 2
    if arr[middle] == target:
        return middle
    else:
        if target > arr[middle]:
            return binarySearch(target,middle+1,end,arr)
        else:
            return binarySearch(target,start,middle-1,arr)



if __name__ == '__main__':
    l = [1,11,23,49,52,69,73,91]
    print(binarySearch(1234,0,len(l)-1,l))
