def goodNodes(self, root: TreeNode) -> int:
    goodCount = 0
    def traversal(node, max):
        nonlocal goodCount
        if not node:
            return
        if node.val >= max:
            max = node.val
            goodCount += 1
        traversal(node.left, max)
        traversal(node.right, max)
    traversal(root, -10001)
    return goodCount

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

"""
how to implement the solution
    init maxvalue as -inf, pass dfs traversal
    if node is higher than maxvalue, update it and the answer

complexity details
    speed - linear, traverses down every node in order to check if its a good node
    memory - linear, height of the recursion stack
"""