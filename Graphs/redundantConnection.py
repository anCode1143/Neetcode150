from typing import List

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    parent = [num for num in range(len(edges))]
    depth = [0 for _ in range(len(edges))]

    def find(node):
        if node != parent[node]:
            node = find(parent[node])
        return node
    
    def union(nodeX, nodeY):
        rootX = find(nodeX)
        rootY = find(nodeY)
        if depth[rootX] > depth[rootY]:
            parent[rootY] = rootX
        elif depth[rootX] < depth[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootX] = rootY
            depth[rootY] += 1
    
    for edge in edges:
        root0 = find(edge[0]) 
        root1 = find(edge[1])
        if root0 == root1:
            return edge
        else:
            union(edge[0], edge[1])
    return []