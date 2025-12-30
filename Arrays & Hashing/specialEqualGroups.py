from typing import List
def numSpecialEquivGroups(self, words: List[str]) -> int:
    specialEquivalentGroups = set()
    for word in words:
        charOccurence = [0] * 52
        for charIndex in range(len(word)):
            charOccurence[ord(word[charIndex]) - ord('a') + 26*(charIndex % 2)] += 1
        specialEquivalentGroups.add(tuple(charOccurence))
    return len(specialEquivalentGroups)