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
        if head is None:
            return head

        prev = None
        it = head
        while it:
            temp = it.next
            it.next = prev
            prev = it
            it = temp
        return prev

