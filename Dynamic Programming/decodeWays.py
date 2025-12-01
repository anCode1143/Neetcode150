def numDecodings(self, s: str) -> int:
    dp = {len(s):1}
    for index in range(len(s)-1, -1, -1):
        if s[index] == "0":
            dp[index] = 0
        else:
            dp[index] =dp[index+1]

        if (index < len(s)-1 and 
            (s[index] == "1" or (s[index] == "2" and s[index+1] in "0123456"))):
            dp[index] += dp[index+2]
    return dp[0]