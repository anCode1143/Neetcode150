from collections import defaultdict
import heapq
from typing import List

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = defaultdict(list)
    for node, destination, length in flights:
        adj[node].append((destination, length))
    heap = [(0, src, 0)]
    shortest = {(src, 0) : 0}
    while heap:
        dist, node, steps = heapq.heappop(heap)
        if node == dst:
            return dist
        shortest[(node, steps)] = dist
        if steps <= k:
            for child_dst, child_dist in adj[node]:
                if (child_dst, steps + 1) not in shortest or shortest[(child_dst, steps + 1)] > child_dist + dist:
                    shortest[(child_dst, steps + 1)] = child_dist + dist
                    heapq.heappush(heap, (child_dist + dist, child_dst, steps + 1))
    return -1

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))