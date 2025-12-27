def rangeSumBST(root: Optional[TreeNode], low: int, high: int) -> int:
    answer = 0
    def dfs(node):
        nonlocal answer
        if not node:
            return
        if low <= node.val <= high:
            answer += node.val
        if low < node.val:
            dfs(node.left)
        if high > node.val:
            dfs(node.right)
    dfs(root)
    return answer