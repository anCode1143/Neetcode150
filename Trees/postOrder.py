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

"""
how to implement the solution - traversal type can be configured based on the order of recursion and appending

struggled parts - remembering the meaning of preorder, inorder, postorder

complexity details
    speed - linear
    space - linear
"""