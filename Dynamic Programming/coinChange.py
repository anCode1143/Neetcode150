def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for dpIndex in range(1, amount+1):
        for coin in coins:
            if dpIndex - coin >= 0:
                dp[dpIndex] = min(dp[dpIndex], 1+dp[dpIndex-coin])
    if dp[amount] <= amount:
        return dp[amount]
    else:
        return -1