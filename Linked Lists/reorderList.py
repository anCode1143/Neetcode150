from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        slow.next = None
        big_head = self.reverseList(second_half)

        small_head = head
        while big_head:
            small_head_next = small_head.next
            big_head_next = big_head.next

            small_head.next = big_head
            big_head.next = small_head_next

            small_head = small_head_next
            big_head = big_head_next
            
        
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            after = current.next
            current.next = prev
            prev = current
            current = after
        return prev


# [1, 2, 3, 4, 5, 6]