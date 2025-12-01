def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # init dp, everything false except len(s)
    # iterate through substring backwards, checking all words in dict
    # if length is good and the substring matches the word, assign dp bool
    # is dp bool is true, break

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for index in range(len(s), -1, -1):
        for word in wordDict:
            if index + len(word) <= len(s) and s[index:index+len(word)] == word:
                dp[index] = dp[index + len(word)]
            if dp[index]:
                break
    return dp[0]