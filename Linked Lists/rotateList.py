from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # find length of list
    # if k > len, k = k % len
    # slow, fast = list[k], list[-1]
    # slow.next = null, fast.next = head
    if not head: return head
    length = 0
    counter = head
    while counter:
        counter = counter.next
        length += 1
    if k >= length:
        k %= length
    if k == 0: return head

    end = head
    kNode = head
    index = 0
    while end.next:
        end = end.next
        if index >= k:
            kNode = kNode.next
        index += 1
    end.next = head
    head = kNode.next
    kNode.next = None

    return head