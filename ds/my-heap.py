# HEAPS
# every parent node is less or equal than its childs

# TODO
# - insert
# - sift_up -> needed for insert
# - get_min -> returns min item, without removing it
# - is_empty -> boolean
# - extract_min -> returns min item
# - sift_down -> needed by extract_min
# - heapify -> create a heap from an array of elements (for heap sort)
# - heap_sort()

class Heap:
    def __init__(self):
        self.heap = []

    def get_left(self,index):
        return (2*index)+1

    def get_right(self,index):
        return (2*index)+2

    def get_parent(self,index):
        return int((index - 1) / 2)


