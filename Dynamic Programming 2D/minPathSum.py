from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    dp = [[-1] * len(grid[0]) for _  in range(len(grid))]
    dp[0][0] = grid[0][0]
    for col in range(1, len(grid[0])):
        dp[0][col] = dp[0][col-1] + grid[0][col]
    for row in range(1, len(grid)):
        dp[row][0] = dp[row-1][0] + grid[row][0]
    
    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            dp[row][col] = min(dp[row][col-1], dp[row-1][col]) + grid[row][col]
    return dp[-1][-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))