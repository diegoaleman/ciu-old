class Node:
    def __init__(self,d=None):
        self.data = d
        self.next = None
# TODO
# x size
# x empty
# x value_at_index(index)
# x push_front(value)
# x pop_front()
# x push_back(value)
# x pop_back()
# x front()
# x back()
# x insert(index, value)
# x erase(index)
# - value_n_from_end(n)
# - reverse()
# - remove_value(value)

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def front(self):
        if self.size > 0:
            return self.head.data
        else:
            return None

    def push_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size+=1

    def pop_front(self):
        if self.size > 0:
            old_node = self.head
            self.head = self.head.next
            del old_node
            self.size-=1

    def back(self):
        if self.size > 0:
            it = self.head
            while it.next is not None:
                it = it.next
            return it.data
        else:
            return None

    def push_back(self,data):
        if self.size == 0:
            self.push_front(data)
        else:
            it = self.head
            while it.next is not None:
                it = it.next
            new_node = Node(data)
            it.next = new_node
            self.size+=1

    def pop_back(self):
        if self.size > 0:
            if self.size == 1:
                self.pop_front()
            else:
                it = self.head
                prev = None
                while it.next is not None:
                    prev_it = it
                    it = it.next
                prev_it.next = None
                del it
                self.size-=1

    def value_at_index(self,index):
        if index+1 <= self.size:
            it = self.head
            counter = 0
            while counter is not index:
                counter+=1
                it = it.next
            return it.data

    def insert(self,index,data):
        if index+1 <= self.size:
            if index == 0:
                self.push_front(data)
            else:
                prev = None
                it = self.head
                counter = 0
                while counter is not index:
                    counter+=1
                    prev = it
                    it = it.next
                new_node = Node(data)
                new_node.next = it
                prev.next = new_node

    def erase(self,index):
        if index+1 <= self.size:
            if index == 0:
                self.pop_front()
            elif index == self.size-1:
                self.pop_back()
            else:
                prev = None
                it = self.head
                counter = 0
                while counter is not index:
                    counter+=1
                    prev = it
                    it = it.next
                prev.next = it.next
                del it

    def print(self):
        it = self.head
        while it is not None:
            print(it.data, end=' ')
            it = it.next
        print()


sll = SingleLinkedList()
sll.push_front(4)
sll.push_front(3)
sll.push_front(1)
sll.push_back(5)
sll.print()
sll.insert(1,2)
sll.print()
sll.erase(1)
sll.print()
