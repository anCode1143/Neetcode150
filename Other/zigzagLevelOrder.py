from collections import deque
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    startLeft = True
    levelNodes = deque()
    levelNodes.append(root)
    answer = []
    while levelNodes:
        level = []
        length =len(levelNodes)
        for _ in range(length):
            current = levelNodes.popleft()
            if current.left:
                levelNodes.append(current.left)
            if current.right:
                levelNodes.append(current.right)	
            level.append(current.val)		
        if startLeft:
            answer.append(level)
        else:
            answer.append(level[::-1])
        startLeft = not startLeft
    return answer