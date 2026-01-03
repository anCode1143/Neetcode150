class DLLNode:
    def __init__(self, val, key, next=None, prev=None,):
        self.next = next
        self.prev = prev
        self.key = key
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ptrToNode = {}
        self.amount = 0
        self.lru = DLLNode(None, None)
        self.mru = DLLNode(None, None)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if not self.ptrToNode.get(key):
            return -1
        node = self.ptrToNode[key]
        self._add_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.ptrToNode.get(key):
            node = self.ptrToNode[key]
            node.val = value
            self._add_mru(node)
        elif self.amount < self.capacity:
            node = DLLNode(val = value, key = key)
            self._add_mru(node)
            self.amount += 1
        elif self.amount == self.capacity:
            self._remove(self.lru.next)
            node = DLLNode(val = value, key = key)
            self._add_mru(node)
    
    def _remove(self, node):
        del self.ptrToNode[node.key]
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _add_mru(self, node):
        if self.ptrToNode.get(node.key):
            self._remove(node)
        self.ptrToNode[node.key] = node
        self.mru.prev.next = node
        node.prev = self.mru.prev
        self.mru.prev = node
        self.mru.prev.next = self.mru


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

"""
cue for diagnosing pattern - tracking order of values while doing operations in constant time

how to implement the solution
    use a hashmap of DLLNodes, 
    then implement mru and delete functions

struggled parts - challenge in verbosity without helper functions. understand the repitition of some operations
"""