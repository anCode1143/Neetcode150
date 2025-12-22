from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def treeTravsersal(node):
            
            leftBalance, leftHeight = treeTravsersal(node.left) if node.left else (True, 1)
            rightBalance, rightHeight = treeTravsersal(node.right) if node.right else (True, 1)
            height = 1 + max(leftHeight, rightHeight)
            balance = leftBalance and rightBalance and abs(leftHeight - rightHeight) <= 1
            return balance, height
        
        if not root:
            return True
        answer, _ = treeTravsersal(root)
        return answer
            