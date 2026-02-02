from typing import Optional

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def leavesTraversal(node, answer):
        if not node.left and not node.right:
            answer.append(node.val)
        elif node.left:
            leavesTraversal(node.left, answer)
        elif node.right:
            leavesTraversal(node.right, answer)

    leaves1 = []
    leavesTraversal(root1, leaves1)

    leaves2 = []
    leavesTraversal(root2, leaves2)

    return True if leaves1 == leaves2 else False