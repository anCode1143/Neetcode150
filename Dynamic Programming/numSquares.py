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

"""
cue for diagnosing pattern - lots of choices, answer builds off previous instance

how to implement the solution
    iterate through perfect squares for every number up to target
    find the min for dp[curr - squareRoot * squareRoot]
    return dp[n]

struggled parts - getting the pointers for the answer right and ensuring iteration is correct

complexity details
    speed - n*sqrt(n), iterates through square root of n for every element n, 
        doing constant time comparison
    memory -  linear, keeps an array of n length
"""