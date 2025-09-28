from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        copy = head
        log = {}
        while copy:
            log[copy] = Node(copy.val)
            copy = copy.next

        answer = head
        while answer:
            copied_node = log[answer]
            if answer.next:
                copied_node.next = log[answer.next]
            if answer.random:
                copied_node.random = log[answer.random]
            answer = answer.next

        return log[head]
    
    