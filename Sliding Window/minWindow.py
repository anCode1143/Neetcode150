from collections import defaultdict
from typing import Counter

def minWindow(self, s: str, t: str) -> str:
    tMap = Counter(t)
    sMap = defaultdict(int)
    left, right = 0, 0
    currLenIdx = (float('inf'),(-1, -1))
    while right < len(s):
        sMap[s[right]] += 1
        while map_match(tMap, sMap) and left <= right:
            if currLenIdx[0] > right - left:
                currLenIdx = (right - left, (left, right))
            sMap[s[left]] -= 1
            left += 1
        right += 1
    if currLenIdx[1][0] == -1: 
        return ""
    answer = (currLenIdx[1][0], currLenIdx[1][1]+1)
    return ''.join(s[answer[0]:answer[1]])
            
        
def map_match(tMap, sMap):
    for char, count in tMap.items():
        if sMap[char] < count:
            return False
    return True