# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next

        if not head:
            return head
        
        ptr1 = head
        ptr2 = head.next
  
        while ptr2:
            if ptr2.val != val:
                ptr1.next = ptr2
                ptr1 = ptr2
            ptr2 = ptr2.next
        
        ptr1.next = None
        return head