import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # keep one element of (value, listIndex, nodeObject) for every list
    # push min into answer, then add next element from respective list
    heap = []
    for lListIndex in range(len(lists)):
        if lists[lListIndex]:
            heap.append((lists[lListIndex].val, lListIndex, lists[lListIndex]))
    heapq.heapify(heap)

    head = curr = ListNode()
    while heap:
        _, nodeIndex, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, nodeIndex, node.next))
    
    return head.next
