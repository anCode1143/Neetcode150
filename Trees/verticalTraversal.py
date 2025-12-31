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

"""
how to implement the solution
    do bfs, right to left, keeping track of column, 
    then adding it into a dedicated column map

struggled parts - realising my initial solution with dfs is wrong, failed to foresee wrong ordering

complexity details
    speed - linear, all nodes iterates through once
    memory - linear, store all nodes for answer
"""