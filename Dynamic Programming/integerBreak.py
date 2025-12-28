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

"""
cue for diagnosing pattern - optimising backtracking

how to implement the solution
    establish base cases and build up the running answer until the target
    recurrence relation - understand the possible ways answers can be derived and how to express them

struggled parts - recurrence relation, must understand the possible ways answers can be derived and how to express them

compare my code and to the standard: what I could do differently
    if i understood the solution deeper, the code/solution would be more elegant

complexity details
    speed - quadratic; for every element up until the target, it will iterate within the bounds to find the optimised recurrence relation
    memory - linear; stores a dict for the optimised solution of every element up until the target
"""