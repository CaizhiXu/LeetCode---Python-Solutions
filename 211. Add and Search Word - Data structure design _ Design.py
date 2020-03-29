class TrieNode:
    def __init__(self):
        self.next = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:  ## time - O(n), space - O(n)
        """
        Adds a word into the data structure.
        """
        root = self.root
        for c in word:
            if c not in root.next:
                root.next[c] = TrieNode()
            root = root.next[c]
        root.is_end = True

    def search(self, word):  ## DFS, time, space - O(n-N)
        return self.find(word, self.root)

    def find(self, word, node):
        if not word:
            return node.is_end
        if word[0] == '.':
            for c in node.next:
                if self.find(word[1:], node.next[c]):
                    return True
            return False
        else:
            if word[0] in node.next:
                return self.find(word[1:], node.next[word[0]])
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)