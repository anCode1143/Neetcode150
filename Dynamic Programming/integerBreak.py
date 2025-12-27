def integerBreak(n: int) -> int:
    dp = {1:1}
    if n > 2:
        dp[2] = 2
    else:
        return 1
    for number in range(2, n+1):
        biggest = number - 1
        for factor in range(1, number):
            biggest = max(biggest, factor * (number - factor), factor * dp[number - factor], dp[factor] * (number - factor))
        dp[number] = biggest
    return dp[n]

    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])

        return dp[n]
