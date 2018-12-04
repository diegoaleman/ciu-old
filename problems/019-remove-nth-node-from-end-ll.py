# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        it = head
        for _ in range(n):
            it = it.next

        slow = head
        if it is None:
            return head.next
        fast = it

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head

