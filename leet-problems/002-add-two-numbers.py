class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_ll = ListNode(-1)

        carry = 0
        it_ll = result_ll
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            sum = sum % 10

            it_ll.next = ListNode(sum)
            it_ll = it_ll.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                sum = l1.val + carry
                carry = sum // 10
                sum = sum % 10
                it_ll.next = ListNode(sum)
                l1 = l1.next
        if l2:
            while l2:
                sum = l2.val + carry
                carry = sum // 10
                sum = sum % 10
                it_ll.next = ListNode(sum)
                l2 = l2.next
        if carry:
            it_ll.next = ListNode(1)

        return result_ll.next

