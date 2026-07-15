import heapq
from typing import List

def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    adj = {key:[] for key in range(n)}
    for a_node, b_node, dist in times:
        adj[a_node].append([dist, b_node])
    shortest = {}
    heap = [[0, k]]
    while heap:
        dist, node = heapq.heappop(heap)
        if node in shortest:
            continue
        shortest[node] = dist
        for child_dist, child_node in adj[node]:
            heapq.heappush(heap, [child_dist + dist, child_node])
    answer = 0
    for node in range(1, n+1):
        if node not in shortest:
            return -1
        else:
            answer = max(answer, shortest[node])
    return answer