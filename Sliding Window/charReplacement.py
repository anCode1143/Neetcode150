def characterReplacement(s: str, k: int) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    left = 0
    right = 1
    charCount = {}
    charCount[s[left]] = 1
    if s[right] in charCount:
        charCount[s[right]] += 1
    else:
        charCount[s[right]] = 1

    commonChar = s[right]
    answer = 1
    while right < len(s):
        commonChar = max(charCount, key=charCount.get)
        if (right - left + 1) <= (k + charCount[commonChar]):
            answer = max(answer, right - left + 1)
            right += 1
            if right < len(s):
                if s[right] in charCount:
                    charCount[s[right]] += 1
                else:
                    charCount[s[right]] = 1
        else:
            if right - left == 1:
                right += 1
                if right < len(s):
                    if s[right] in charCount:
                        charCount[s[right]] += 1
                    else:
                        charCount[s[right]] = 1
            charCount[s[left]] -= 1
            left += 1

    return answer

print(characterReplacement("AABA", 0))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
    
"""
cue for diagnosing pattern - iterating through an array checking for certain conditions in linear time

how to implement the solution
    init left and right pointer, hashmap for the count of elements in range
    if most common character in window + k >= windwo size, update answer to window size and extend window to the right
    else, shrink from left
        if window size is 1, move both pointers

struggled parts - trying to figure out the solution with sliding windows

improvement from standard solution - heavily overcomplicated the code

complexity details
    speed - linear, iterate through array with window, never rechecking anything and saving values in a hashmap
    memory - constant, hashap to save counts of max 26 values
"""