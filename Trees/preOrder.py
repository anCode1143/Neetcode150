def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    answer = []
    def appendPreOrder(node):
        if not node:
            return
        answer.append(node.val)
        appendPreOrder(node.left)
        appendPreOrder(node.right)
    appendPreOrder(root)
    return answer