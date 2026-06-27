from collections import deque
from typing import List

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    visited = set(beginWord)
    processing = deque()
    processing.append((beginWord, 1))
    while processing:
        word, steps = processing.popleft()
        for currIndex in range(len(beginWord)):
            for letter in range(26):
                new = word[0:currIndex] + chr(ord('a') + letter) + word[currIndex+1:]
                if new == endWord:
                    return steps + 1
                if new in wordSet and new not in visited:
                    processing.append((new, steps+1))
                    visited.add(new)
    return 0