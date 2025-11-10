from typing import List

def count_components(self, n: int, edges: List[List[int]]) -> int:
    adjList = [[] for _ in range(n)]
    answer = 0
    visited = set()
    for edge in edges:
        adjList[edge[0]].append(edge[1])
        adjList[edge[1]].append(edge[0])
    
    def dfs(node):
        if node in visited:
            return
        else:
            visited.add(node)
            for adjNode in adjList[node]:
                dfs(adjNode)
            return
        
    for node in range(n):
        if not node in visited:
            answer += 1
            dfs(node)
    return answer

