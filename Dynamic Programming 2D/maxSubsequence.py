def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

    for index1 in range(len(text1)-1, -1, -1):
        for index2 in range(len(text2)-1, -1, -1):
            if text1[index1] == text2[index2]:
                dp[index2][index1] = 1 + dp[index2+1][index1+1]
            else:
                dp[index2][index1] = max(dp[index2+1][index1], dp[index2][index1+1])
    return dp[0][0]

print(longestCommonSubsequence("abcde", "ace"))