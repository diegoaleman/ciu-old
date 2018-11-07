# Implementation uses a normal List

class Stack:
    def __init__(self):
        self.stack = []

    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)

    def remove(self):
        if len(self.stack) >= 0:
            return self.stack.pop()

    def peek(self):
        l = len(self.stack)
        if l > 0:
            return self.stack[l-1]

s = Stack()
s.add(4)
s.add(3)
print(s.peek())
print(s.stack)
s.add(2)
s.add(1)
print(s.peek())
print(s.stack)
s.remove()
s.remove()
print(s.stack)
