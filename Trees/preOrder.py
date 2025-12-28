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

"""
how to implement the solution - traversal type can be configured based on the order of recursion and appending

struggled parts - remembering the meaning of preorder, inorder, postorder

complexity details
    speed - linear
    space - linear
"""