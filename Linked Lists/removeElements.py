def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return None
    dummy = ListNode(next=head)
    curr = head
    prev = dummy
    while curr:
        if curr.val == val:
            while curr and curr.val == val:
                curr = curr.next
        prev.next = curr
        prev = prev.next
        curr = curr.next if curr else None
    return dummy.next