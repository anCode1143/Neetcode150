from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # init dummyNode, prevLeft node, then left node
        # run next, prev, curr to reverse list from left+1 to right
        # prevLeft.next.next = right.next
        # prevLeft.next = right
        if not head.next or left == right:
            return head
        
        dummy = ListNode(0, head)
        prevLeft = dummy
        for _ in range(left-1):
            prevLeft = prevLeft.next

        prev = None
        curr = prevLeft.next
        for _ in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        prevLeft.next.next = curr
        prevLeft.next = prev

        return dummy.next