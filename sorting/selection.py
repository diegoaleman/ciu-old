def selection(list):
    length = len(list)
    for i in range(len(list[:-1])):
        for j in range(i+1, length):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
