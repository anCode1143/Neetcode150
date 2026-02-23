from typing import Optional
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
def flatten(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return head
    def recursionTraverse(node,  upperNext):
        curr = node
        while curr:
            if curr.child:
                # if this is the last one, next = upperNext of previous layer
                afterChildren = curr.next
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None
                recursionTraverse(curr.next, afterChildren)
            if curr.next:
                curr = curr.next
            else: break
        if upperNext:
            upperNext.prev = curr
        curr.next = upperNext

    recursionTraverse(head, None)
    return head