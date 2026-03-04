from collections import deque
from typing import Optional
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None): # type: ignore
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root
    queue = deque()
    queue.append(root)
    while queue:
        parentLen = len(queue)
        for parentIndex in range(parentLen):
            parent = queue.popleft()
            if not parentIndex == parentLen - 1:
                parent.next = queue[0]
            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)
    return root