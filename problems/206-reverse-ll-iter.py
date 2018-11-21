class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        prev = None
        it = head
        next = it.next
        while next:
            it.next = prev
            prev = it
            it = next
            next = next.next
        if it:
            it.next = prev

        return it

