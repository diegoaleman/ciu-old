class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getLinkedLength(self, head):
        count = 0
        while head:
            count+=1
            head = head.next
        return count


    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        length = self.getLinkedLength(head)
        k = k%length

        if k == 0:
            return head

        end = head
        for _ in range(k-1):
            end = end.next

        prev = None
        start = head
        while end.next is not None:
            prev = start
            start = start.next
            end = end.next

        end.next = head
        prev.next = None
        head = start

        return head


