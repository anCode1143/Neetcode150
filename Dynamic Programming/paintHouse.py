from typing import List
def minCost(costs: List[List[int]]) -> int:
    dp = [0, 0, 0]
    for house in range(len(costs)):
        dp0 = costs[house][0] + min(dp[1], dp[2])
        dp1 = costs[house][1] + min(dp[0], dp[2])
        dp2 = costs[house][2] + min(dp[1], dp[0])
        dp = [dp0, dp1, dp2]
    return min(dp)