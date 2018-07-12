# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        h1 = head
        t1 = h1.next
        t2 = t1.next
        while t1:
            t1.next = h1
            h1 = t1
            t1 = t2
            if t2:
                t2 = t2.next
        head.next = None
        head = h1
        return head
        