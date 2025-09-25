def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    while current:
        after = current.next
        current.next = prev
        prev = current
        current = after
    return prev