from typing import List
def minCostClimbingStairs(self, cost: List[int]) -> int:
    a = cost[0]
    b = cost[1]
    for stepIndex in range(2, len(cost)):
        new = cost[stepIndex] + min(a, b)
        a = b
        b = new
    return min(a, b)