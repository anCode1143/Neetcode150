# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        oldToNew = {}
        def dfs(node):
            if node not in oldToNew:
                copy = Node(node.val)
                oldToNew[node] = copy
                for neighbour in node.neighbors:
                    copy.neighbors.append(dfs(neighbour))
            return oldToNew[node]
        
        return dfs(node)
