import heapq
from typing import List
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distanceHeap = []
    for point in points:
        distanceHeap.append([point[0]**2 + point[1]**2, point[0], point[1]])
    heapq.heapify(distanceHeap)
    answer = []
    for _ in range(k):
        z, x, y = heapq.heappop(distanceHeap)
        answer.append([x, y])
    return answer



points = [[1,3],[-2,2]]
k = 1

print(kClosest(points, k))