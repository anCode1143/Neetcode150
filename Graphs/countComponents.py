from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:
    parent = [num for num in range(n)]
    depth = [0 for _ in range(n)]
    
    def find(node):
        if node != parent[node]:
            node = find(parent[node])
        return node
    
    def union(nodeX, nodeY):
        rootX = find(nodeX)
        rootY = find(nodeY)

        if depth[rootY] > depth[rootX]:
            parent[rootX] = rootY
        elif depth[rootY] < depth[rootX]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            depth[rootY] += 1
    
    for edge in edges:
        union(edge[0], edge[1])

    groups = set()
    for node in parent:
        leader = find(node)
        if leader not in groups:
            groups.add(leader)

    return len(groups)