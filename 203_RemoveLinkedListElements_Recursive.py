# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            if head.val == val:
                return self.removeElements(head.next, val)
            else:
                head.next = self.removeElements(head.next, val)
    
        return head
