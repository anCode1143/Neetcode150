def minimumTotal(triangle: List[List[int]]) -> int:
    dp = [[10001] * subArray for subArray in range(1, len(triangle)+1)]
    dp[0][0] = triangle[0][0]
    if len(triangle) == 1:
        return dp[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]

    for levelIndex in range(2, len(dp)+1):
        for elementIndex in range(len(dp[levelIndex])):
            if elementIndex == len(dp[levelIndex])-1:
                dp[levelIndex][elementIndex] = dp[levelIndex-1][elementIndex-1] + triangle[levelIndex][elementIndex]
            elif elementIndex == 0:
                dp[levelIndex][elementIndex] = dp[levelIndex-1][elementIndex] + triangle[levelIndex][elementIndex]
            else:
                dp[levelIndex][elementIndex] = min(dp[levelIndex-1][elementIndex-1], dp[levelIndex-1][elementIndex]) + triangle[levelIndex][elementIndex]
    return min(dp[-1])

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]