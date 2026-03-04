from typing import List
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        head = TrieNode()
        for word in wordDict:
            curr = head
            for charIndex in range(len(word)):
                if not curr.children[ord(word[charIndex]) - ord('a')]:
                    curr.children[ord(word[charIndex]) - ord('a')] = TrieNode()
                curr = curr.children[ord(word[charIndex]) - ord('a')]
                if charIndex == len(word) - 1:
                    curr.isWord = True
        
        answer = []
        def traverseTrie(charIndex, words, trieNode, currWord):
            if not trieNode:
                return
            if charIndex == len(s):
                if trieNode.isWord:
                    words.append(currWord)
                    answer.append(" ".join(words))
                    words.pop()
                return
            if trieNode.isWord:
                words.append(currWord)
                traverseTrie(charIndex, words, head, "")
                words.pop()
            currWord += s[charIndex]
            traverseTrie(charIndex+1, words, trieNode.children[ord(s[charIndex]) - ord('a')], currWord)
        traverseTrie(0, [], head, "")
        return answer
    

