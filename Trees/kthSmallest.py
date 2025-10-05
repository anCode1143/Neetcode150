from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []
        def inOrderTraversal(node, k, in_order):
            if not node:
                return

            inOrderTraversal(node.left, k, in_order)
            in_order.append(node.val)
            if len(in_order) == k:
                return
            inOrderTraversal(node.right, k, in_order)

        inOrderTraversal(root, k, in_order)
        return in_order[k-1]