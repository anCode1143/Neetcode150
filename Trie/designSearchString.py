class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if not curr.children[ord(char) - ord("a")]:
                curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        curr.isWord = True

    def search(self, word: str) -> bool:
        return self._wildDfs(word, 0, self.head)

    def _wildDfs(self, word: str, index: int, curr : TrieNode) -> bool:
        if index == len(word):
            return True if curr.isWord else False
        if word[index] == ".":
            for char in curr.children:
                if char:
                    if self._wildDfs(word, index+1, char):
                        return True
        elif curr.children[ord(word[index]) - ord("a")]:
            return self._wildDfs(word, index+1, curr.children[ord(word[index]) - ord("a")])
        return False
    
class SolutionTrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class SolutionWordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)