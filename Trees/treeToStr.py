from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = []
        def preOrder(node):
            answer.append(str(node.val))
            if not node.left and node.right:
                answer.append("()")
            if node.left:
                answer.append("(")
                preOrder(node.left)
                answer.append(")")
            if node.right:
                answer.append("(")
                preOrder(node.right)
                answer.append(")")
        preOrder(root)
        return "".join(answer)