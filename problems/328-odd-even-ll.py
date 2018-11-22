# This solution can be implemented in way shorter code (leetcode)
# but idea is the same
# Keep odds in one ll and evens in other ll, then merge the ll
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head

        prev = None

        odd = head
        odd_it = odd

        even = ListNode(-1)
        even_it = even

        while odd_it and odd_it.next:
            even_it.next = odd_it.next
            odd_it.next = odd_it.next.next
            even_it = even_it.next
            even_it.next = None
            prev = odd_it
            odd_it = odd_it.next
        if odd_it:
            odd_it.next = even.next
        else:
            prev.next = even.next

        return odd

# OTHER WAY OF IMPLEMENTING
#        oddHead = odd = ListNode(0)
#        evenHead = even = ListNode(0)
#
#        isOdd = True
#
#        while head:
#            if isOdd:
#                odd.next = head
#                odd = odd.next
#            else:
#                even.next = head
#                even = even.next
#
#            isOdd = not isOdd
#            head = head.next
#
#        even.next = None
#        odd.next = evenHead.next
#
#        return oddHead.next
