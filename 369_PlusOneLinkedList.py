# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        head, carry = self.helper(head, 0)
        if carry:
            newHead, newHead.next = ListNode(1), head
            head = newHead
        return head
    
    def helper(self, head, carry):
        if not head:
            return None, 1
        head.next, carry = self.helper(head.next, carry)
        if (head.val < 9 and carry == 1):
            head.val += 1
            carry = 0
        elif (head.val == 9 and carry == 1):
            head.val = 0
            carry = 1
        return head, carry
    
            
            
            