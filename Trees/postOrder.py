def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    answer = []
    def appendPostOrder(node):
        if not node:
            return
        appendPostOrder(node.left)
        appendPostOrder(node.right)
        answer.append(node.val)
    appendPostOrder(root)
    return answer