# Quick sort
# best case -> O(nlogn)
# worst case -> O(n^2)
def quicksort(list,start,end):
    if start<end:
        index = partition(list,start,end)
        quicksort(list,start,index-1)
        quicksort(list,index+1,end)

def partition(list,start,end):
    pivot = list[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and list[left] <= pivot:
            left+=1

        while left <= right and list[right] >= pivot:
            right-=1

        if left < right:
            list[left],list[right] = list[right],list[left]
        else:
            done = True
    list[start],list[right] = list[right],list[start]
    return right
