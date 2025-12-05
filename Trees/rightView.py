from collections import deque
def rightSideView(root: Optional[TreeNode]) -> List[int]:
    # level order traversal where you append the last appended node to the answer
    if not root:
        return []
    level = deque()
    answer = []
    level.append(root)
    while level:
        parentNum = len(level)
        node = level[0]
        for _ in range(parentNum):
            node = level.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        answer.append(node.val)

    return answer