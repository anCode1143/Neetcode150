def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.answer = 0
    def dfs(node) -> int:
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)

        self.answer = max(self.answer, left + right)

        return 1 + max(left, right)
    dfs(root)
    return self.answer