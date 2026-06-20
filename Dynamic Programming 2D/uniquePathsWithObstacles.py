from typing import List

def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[-1][-1] == 1:
        return 0
    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    dp[-1][-1] = 1

    for col in range(len(dp[0])-2, -1, -1):
        if obstacleGrid[-1][col] == 1:
            dp[-1][col] = 0
        else:
            dp[-1][col] = dp[-1][col+1]

    for row in range(len(dp)-2, -1, -1):
        if obstacleGrid[row][-1] == 1:
            dp[row][-1] = 0
        else:
            dp[row][-1] = dp[row+1][-1]
    
    for row in range(len(dp)-2, -1, -1):
        for col in range(len(dp[0])-2, -1, -1):
            if obstacleGrid[row][col] == 1:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row][col+1] + dp[row+1][col]
    
    return dp[0][0]