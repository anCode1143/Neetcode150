from collections import deque
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root.right and not root.left:
        return True
    left = []
    right = []
    def bfs(node, output):
        queue = deque()
        queue.append(node)
        output.append([node.val])
        while queue:
            parents = len(queue)
            level = []
            for _ in range(parents):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                    level.append(currNode.left.val)
                else:
                    level.append(None)
                if currNode.right:
                    queue.append(currNode.right)
                    level.append(currNode.right.val)
                else:
                    level.append(None)
            output.append(level)
    if root.left:
        bfs(root.left, left)
    if root.right:
        bfs(root.right, right)
    left = [level[::-1] for level in left]
    return left == right

"""
how to implement the solution
    take care of edge cases
    do level order traversal on each sie of root appending None childs
    reverse every level of one side before comparing

struggled parts
    what specifically to reverse (each individual level)

compare my code and to the standard: what I could do differently
    over complicated, space inefficiency
    could just do it recursively comparing nodes at the same time without storing

complexity details
    speed - linear
    space - linear

"""