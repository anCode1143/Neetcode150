import math
def numSquares(n: int) -> int:
    dp = {num:n+1 for num in range(n+1)}
    dp[0] = 0
    dp[1] = 1
    for curr in range(2, n+1):
        currMin = dp[curr]
        for squareRoot in range(int(math.sqrt(curr))+1):
            currMin = min(currMin, 1 + dp[curr - squareRoot * squareRoot])
        dp[curr] = currMin
    return dp[n]

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]