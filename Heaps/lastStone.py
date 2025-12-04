import heapq
def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [-x for x in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        newStone = y - x
        if newStone > 0:
            heapq.heappush(stones, -newStone)
    return -stones[0] if stones else 0