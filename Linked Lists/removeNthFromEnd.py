from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        placeholder = ListNode()
        placeholder.next = head
        end = placeholder
        slow = placeholder

        for _ in range(n):
            end = end.next

        while end.next:
            end = end.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return placeholder.next