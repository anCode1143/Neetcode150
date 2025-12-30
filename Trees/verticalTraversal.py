from collections import defaultdict, deque
def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    colArrays = defaultdict(list)
    queue = deque()
    queue.append((root, 0))
    while queue:
        parents = len(queue)
        for _ in range(parents):
            currNode, column = queue.popleft()
            colArrays[column].append(currNode.val)
            if currNode.left:
                queue.append((currNode.left, column-1))
            if currNode.right:
                queue.append((currNode.right, column+1))

    minKey = min(colArrays.keys())
    maxKey = max(colArrays.keys())
    answer = []
    for column in range(minKey, maxKey+1):
        answer.append(colArrays[column])
    return answer