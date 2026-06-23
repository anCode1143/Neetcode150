class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    # max passable, max path
    def traverse(node):
        maxPaths = [node.val]
        passables = [node.val]
        rightPassable = 0
        if node.right:
            rightPassable, rightMax = traverse(node.right)
            maxPaths.append(rightMax)
            maxPaths.append(rightPassable)
            passables.append(node.val + rightPassable)
        leftPassable = 0
        if node.left:
            leftPassable, leftMax = traverse(node.left)
            maxPaths.append(leftMax)
            maxPaths.append(leftPassable)
            passables.append(node.val + leftPassable)

        maxPaths.append(node.val + leftPassable + rightPassable)
        maxPassable = max(passables)
        return (maxPassable, max(maxPaths))
    return max(traverse(root))