def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    oddRow = True
    top = []
    bottom = []
    top.append(root)
    while top[0].left:
        for parent in top:
            bottom.append(parent.left)
            bottom.append(parent.right)
        if oddRow:
            right = len(bottom)-1
            left = 0
            while left < right:
                bottom[left].val, bottom[right].val = bottom[right].val, bottom[left].val
                left += 1
                right -= 1
        top = bottom
        bottom = []
        oddRow = not oddRow
    return root