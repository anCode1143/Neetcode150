def numOfWays(self, n: int) -> int:
    curr = [6, 6]
    MOD = 1000000007
    for _ in range(n-1):
        curr = [(curr[0]*3+curr[1]*2) % MOD, (curr[0]*2+curr[1]*2) % MOD]
    return (curr[0] +  curr[1]) % MOD
