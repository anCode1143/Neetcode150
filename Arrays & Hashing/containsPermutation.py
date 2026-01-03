from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    s1Map = defaultdict(int)
    for char in s1:
        s1Map[char] += 1
    left = 0
    right = len(s1)-1
    if not right < len(s2):
        return False
    subS2Map = defaultdict(int)
    for char in s2[:right]:
        subS2Map[char] += 1
    while right < len(s2):
        subS2Map[s2[right]] += 1
        if s1Map == subS2Map:
            return True
        subS2Map[s2[left]] -= 1
        if subS2Map[s2[left]] == 0:
            del subS2Map[s2[left]]
        left += 1
        right += 1
    return False

print(checkInclusion("adc", "dcda"))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26