from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            if not l1.next and not l2.next and (l1.val + l2.val == 0):
                return ListNode()
        
        answer = ListNode()
        head = answer
        carry = 0
        while l1 or l2:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            sum = val1 + val2 + carry
            carry = 0
            if sum > 9:
                carry = 1
                sum = sum % 10
            new_node = ListNode(sum)
            answer.next = new_node
            answer = answer.next
        
        if carry:
            last_one = ListNode(1)
            answer.next = last_one
        return head.next

