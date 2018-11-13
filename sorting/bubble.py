# Bubble sort
def bubble(list):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
