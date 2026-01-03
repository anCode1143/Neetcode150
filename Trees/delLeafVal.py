def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    def inOrderDel(node, parent, isLeft):
        if node.left:
            inOrderDel(node.left, node, True)
        if node.right:
            inOrderDel(node.right, node, False)
        if node.val == target and not node.left and not node.right and parent:
            if isLeft:
                parent.left = None
            else:
                parent.right = None
    if root.left or root.right:
        inOrderDel(root, None, None)
    if not root.left and not root.right and root.val == target:
        return None
    else:
        return root