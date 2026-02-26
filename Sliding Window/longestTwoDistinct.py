from collections import defaultdict
def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    # sliding windows, keep track of the two chars and their occurences
    if len(s) == 1: return 1
    chars = defaultdict(int)
    left, right = 0, 1
    chars[s[left]] += 1
    answer = 0
    while right < len(s):
        chars[s[right]] += 1
        if len(chars) > 2:
            while len(chars) > 2 and right < len(s):
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1
                if left == right:
                    right += 1
                    chars[s[right]] += 1
        answer = max(answer, sum(chars.values()))
        right += 1
    return answer