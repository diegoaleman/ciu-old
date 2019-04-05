class Node:
    def __init__(self,v=None,n=None):
        self.value = v
        self.next = n

def create_ll():
    head = Node(-1)
    it   = head
    for i in range(10):
        it.next = Node(i)
        it = it.next

    return head.next

def print_ll(head):
    it = head
    while it:
        print(it.value,end=' - ')
        it = it.next
    print()

def reverse_ll_iter(head):
    it = head
    current = None
    while it:
        next_node = it.next
        it.next = current
        current = it
        if next_node == None:
            return current
        else:
            it = next_node

def reverse_ll_recursive(head):
    if head.next == None:
        return head
    reverse_head = reverse_ll_recursive(head.next)
    head.next.next = head
    head.next = None
    return reverse_head

def reverse_ll(head,option):
    if option == 1:
        return reverse_ll_iter(head)
    else:
        return reverse_ll_recursive(head)

h = create_ll()
print_ll(h)
h2 = reverse_ll(h,2)
print_ll(h2)


