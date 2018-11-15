# HEAPS
# min heap
# every parent node is less or equal than its childs

# TODO
# x insert
# x sift_up -> needed for insert
# x get_min -> returns min item, without removing it
# x extract_min -> returns min item
# x sift_down -> needed by extract_min
# x heapify -> create a heap from an array of elements (for heap sort)
# - heap_sort()

class Heap:
    def __init__(self,list=None):
        self.heap = []
        if list is not None:
            self.heapify(list)

    def get_left(self,index):
        return (2*index)+1

    def get_right(self,index):
        return (2*index)+2

    def get_parent(self,index):
        return int((index - 1) / 2)

    def swap(self,i1,i2):
        self.heap[i1], self.heap[i2] = self.heap[i2], self.heap[i1]


    def sift_up(self,index):
        parent = self.get_parent(index)
        if parent >= 0 and self.heap[index] < self.heap[parent]:
            self.swap(index,parent)
            self.sift_up(parent)

    def insert(self,data):
        self.heap.append(data)
        self.sift_up(len(self.heap)-1)

    def min_child(self,index):
        left = self.get_left(index)
        right = self.get_right(index)

        if left > len(self.heap)- 1:
            return 0
        elif right > len(self.heap)-1:
            return left
        else:
            if self.heap[left] < self.heap[right]:
                return left
            else:
                return right

    def sift_down(self,index):
        min = self.min_child(index)

        if min > 0 and self.heap[index] > self.heap[min]:
            self.swap(index,min)
            self.sift_down(min)

    def extract_min(self):
        self.swap(0,len(self.heap)-1)
        min = self.heap.pop()
        self.sift_down(0)
        return min

    def heapify(self,list):
        for i in list:
            self.insert(i)

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
