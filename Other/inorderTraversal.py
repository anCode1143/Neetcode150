# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def inorderTraversal(root, answer):
            if not root:
                return
            else:
                inorderTraversal(root.left, answer)
                answer.append(root.val)
                inorderTraversal(root.right, answer)
            return
        inorderTraversal(root, answer)
        return answer
