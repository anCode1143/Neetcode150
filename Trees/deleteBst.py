def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root
    if key > root.val:
        root.right = self.deleteNode(root.right, key)
    elif key < root.val:
        root.left = self.deleteNode(root.left, key)
    else: # key == root
        if not root.right and not root.left:
            return None
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        
        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val
        root.right = self.deleteNode(root.right, curr.val)
    return root