def climbStairs(self, n: int) -> int:
    one, two = 1, 1
    for _ in range(n):
        temp = one
        one += two
        two = temp
    return one