class Node:
    def __init__(self,d=None):
        self.data = d
        self.next = None
        self.prev = None

# TODO
# - push_front(value)
# - pop_front
# - push_back(value)
# - pop_back
# - insert(index, value)
# - erase(index)

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.size+=1

    def pop_front(self):
        if self.head is not None:
            old = self.head
            self.head = self.head.next
            del old
            if self.head is not None:
                self.head.prev = None
            self.size-=1

    def push_back(self, data):
        if self.head is None:
            self.push_front(data)
        else:
            new_node = Node(data)
            it = self.head
            while it.next is not None:
                it = it.next
            it.next = new_node
            new_node.prev = it
            self.size+=1

    def pop_back(self):
        if self.head is not None:
            if self.head.next is None:
                self.pop_front()
            else:
                prev = None
                it = self.head
                while it.next is not None:
                    prev = it
                    it = it.next
                prev.next = None
                del it
                self.size-=1

    def insert(self, index, data):
        if index < self.size:
            if index == 0:
                self.push_front(data)
            else:
                new_node = Node(data)
                prev = None
                it = self.head
                counter = 0
                while counter < index:
                    counter+=1
                    prev = it
                    it = it.next
                new_node.next = it
                new_node.prev = prev
                it.prev = new_node
                prev.next = new_node
                self.size+=1

    def erase(self, index):
        if index < self.size:
            if index == 0:
                self.pop_front()
            elif index == self.size - 1:
                self.pop_back()
            else:
                counter = 0
                prev = None
                it = self.head
                while counter < index:
                    prev = it
                    it = it.next
                    counter+=1
                prev.next = it.next
                it.next.prev = prev
                del it
                self.size-=1

    def print(self):
        it = self.head
        while it is not None:
            print(it.data, end=' ')
            it = it.next
        print()

