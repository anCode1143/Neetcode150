class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.wordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if currNode.children[ord(char) - ord('a')] == None:
                currNode.children[ord(char) - ord('a')] = TrieNode()
            currNode = currNode.children[ord(char) - ord('a')]
        currNode.wordEnd = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            if currNode.children[ord(char) - ord('a')] == None:
                return False
            currNode = currNode.children[ord(char) - ord('a')]
        return currNode.wordEnd

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            if currNode.children[ord(char) - ord('a')] == None:
                return False
            currNode = currNode.children[ord(char) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True