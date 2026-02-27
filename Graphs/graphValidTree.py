from typing import List

def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
    adjList = [[] for _ in range(n)]
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    
    def dfs(node, visited, justVisited):
        if node in visited:
            return False
        visited.add(node)
        for child in adjList[node]:
            if child == justVisited :
                continue
            if not dfs(child, visited, node):
                return False
        return True
    
    visited = set()
    if dfs(0, visited, None) and len(visited) == n:
        return True
    else:
        return False
# def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
#     adjList = [[] for _ in range(len(edges))]
#     for edge in edges:
#         adjList[edge[0]].append(edge[1])
    
#     def dfs(node, visited, justVisited):
#         if node in visited:
#             return False
#         visited.add(node)
#         for child in adjList[node]:
#             if not dfs(child, visited):
#                 return False
#         return True