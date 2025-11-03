def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
    def dfs(node, prev):
        if node in visit:
            return False
        visit.add(node)
        for neighbour in neighbourList[node]:
            if neighbour == prev:
                continue
            if not dfs(neighbour, node):
                return False
        return True

    if not n:
        return True
    
    neighbourList = {i:[] for i in range(n)}
    for n1, n2 in edges:
        neighbourList[n1].append(n2)
        neighbourList[n2].append(n1)
    
    visit = set()
    if dfs(0, -1):
        return len(visit) == n
    return False