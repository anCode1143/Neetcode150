from typing import List

def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=len)
    dp = {word:1 for word in words}
    for word in reversed(words):
        candidates = set()
        for charIndex in range(len(word)):
            candidate = word[:charIndex] + word[charIndex+1:]
            candidates.add(candidate)
        for key in dp.keys() & candidates:
            dp[key] = max(dp[key], dp[word] + 1)
    return max(dp.values())