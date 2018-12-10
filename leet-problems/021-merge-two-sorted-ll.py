class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_ll = ListNode(-1)
        it = result_ll

        while l1 and l2:
            if l1.val <= l2.val:
                it.next = l1
                l1 = l1.next
            else:
                it.next = l2
                l2 = l2.next
            it = it.next

        if l1:
            it.next = l1
        if l2:
            it.next = l2

        return result_ll.next

