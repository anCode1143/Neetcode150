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

"""

how to implement the solution
    write recursive tree traversal function, 
    tracking when nodes are found with return values
    when both are found, assign a global variable the first time it is the case

struggled parts - 
    defining base case and structure for recursion. 
    base case is not always if the node is empty

complexity details
    speed - linear, goes through all nodes once
    memory - height, recursive stack
"""