# Selection sort
# O(n^2)
def selection(list):
    for i in range(len(list[:-1])):
        min_position = i
        for j in range(i+1, len(list)):
            if list[min_position] > list[j]:
                min_position = j
        list[i], list[min_position] = list[min_position], list[i]
