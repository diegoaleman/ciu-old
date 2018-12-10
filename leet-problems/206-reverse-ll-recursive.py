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
        else:
            return self.reverse(head)

    def reverse(self,head,master_head=None):
        if head.next is None:
            return head
        master_head = self.reverse(head.next)
        temp = head.next
        temp.next = head
        head.next = None
        return master_head

