# Insertion sort
# worst & average -> O(n^2)
# best case (when ordered) -> O(n)
def insertion(list):
    for i in range(1, len(list)):
        aux = i
        for j in range(i-1, -1, -1):
            if list[aux] < list[j]:
                list[aux], list[j] = list[j], list[aux]
                aux = j
            else:
                break
