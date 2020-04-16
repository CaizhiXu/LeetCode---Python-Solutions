## time - O(nk**2), space - O(kn**2)
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = -1
        self.palSuffix = []


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieNode()
        for i, w in enumerate(words):
            node = trie
            w = w[::-1]
            for j, c in enumerate(w):
                if w[j:] == w[j:][::-1]:
                    node.palSuffix.append(i)
                node = node.children[c]
            node.is_word = i

        res = []
        for i, w in enumerate(words):
            node = trie
            for j, c in enumerate(w):
                if w[j:] == w[j:][::-1] and node.is_word != -1:
                    res.append([i, node.is_word])
                if c not in node.children:
                    break
                node = node.children[c]
            else:
                if node.is_word != -1 and node.is_word != i:
                    res.append([i, node.is_word])
                for j in node.palSuffix:
                    res.append([i, j])

        return res