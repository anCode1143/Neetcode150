def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    answer = 100001
    def traverse(parent, left, right):
        nonlocal answer
        answer = min(answer, abs(parent.val - left), abs(parent.val - right))
        if parent.left:
            traverse(parent.left, left, parent.val)
        if parent.right:
            traverse(parent.right, parent.val, right)
    traverse(root, float('inf'), float('inf'))
    return answer