def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    insertNode = Node(val)
    if not root:
        return insertNode
    
    def travserseToPointer(node):
        if node.val > val:
            if node.left:
                travserseToPointer(node.left)
            else:
                node.left = insertNode
                return
        else:
            if node.right:
                travserseToPointer(node.right)
            else:
                node.right = insertNode
                return

    travserseToPointer(root)
    return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root