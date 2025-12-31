from typing import List
def numSpecialEquivGroups(self, words: List[str]) -> int:
    specialEquivalentGroups = set()
    for word in words:
        charOccurence = [0] * 52
        for charIndex in range(len(word)):
            charOccurence[ord(word[charIndex]) - ord('a') + 26*(charIndex % 2)] += 1
        specialEquivalentGroups.add(tuple(charOccurence))
    return len(specialEquivalentGroups)

"""
cue for diagnosing pattern - breaking problem down to number of chars

how to implement the solution
    each word becomes two maps counting odd and even indexed chars
    if this pair of maps equates to an existing one of the set, continue
    else, its a new subset

struggled parts
    verbose problem, took some time to fully process information

complexity details
    speed - O(N*L) every character of every word is iterated through, 
        in the nested word loop, theres a constant time comparison of array to set
    memory - O(N), where every word has an array of its characters, and then a set of some words
"""