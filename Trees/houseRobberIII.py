from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> tuple[int, int]: # tuple[0] is the head included, tuple[1] is head not included
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            withHead = max(node.val + left[1] + right[1], left[0] + right[0])
            withoutHead = max(left) + max(right)
            return (withHead, withoutHead)
        
        finalEval = dfs(root)
        return max(finalEval)