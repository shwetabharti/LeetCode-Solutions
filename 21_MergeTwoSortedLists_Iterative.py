# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        temp = head 

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next 

        if l1 and not l2:
            temp.next = l1
        else:
            temp.next = l2
        
        return head
            