from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(self, head: Optional[ListNode]) -> bool:
    currNode = head
    values = []
    while currNode:
        values.append(currNode.val)
        currNode = currNode.next

    left, right = 0, len(values) - 1
    while left < right:
        if not values[left] == values[right]:
            return False
        left += 1
        right -= 1
    return True