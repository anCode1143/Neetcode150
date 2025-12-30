def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    lowestAncestor = None
    def treeTraversal(node):
        nonlocal lowestAncestor
        rightRes = (False, False)
        leftRes = (False, False)
        if node.right:
            rightRes = treeTraversal(node.right)
        if node.left:
            leftRes = treeTraversal(node.left)
        pFound = node == p or rightRes[0] or leftRes[0]
        qFound = node == q or rightRes[1] or leftRes[1]
        if not lowestAncestor and pFound and qFound:
            lowestAncestor = node
        return pFound, qFound
    treeTraversal(root)
    return lowestAncestor