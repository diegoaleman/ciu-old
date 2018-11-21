class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        slow = head
        fast = head.next


        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
                del fast
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
        return head

