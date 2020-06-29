## time, space - O(mn)
from collections import defaultdict


class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0
        combo_dict = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                bucket = w[:i] + '_' + w[i + 1:]
                combo_dict[bucket].append(w)

        dq = deque([(beginWord, 1)])
        visited = set([beginWord])
        while dq:
            w, dep = dq.pop()
            if w == endWord:
                return dep
            for i in range(len(w)):
                bucket = w[:i] + '_' + w[i + 1:]
                for word in combo_dict[bucket]:
                    if word not in visited:
                        dq.appendleft((word, dep + 1))
                        visited.add(word)
        return 0



## this function returns the shortest path
from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        bucket = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[:i] + '_' + w[i + 1:]
                bucket[key].append(w)

        print('t')
        dq = deque([beginWord])
        visited = set([beginWord])
        parent = {}

        while dq:
            node = dq.popleft()
            print(node)

            if node == endWord:
                res = self.findPath(parent, endWord)
                print('T')
                return res
            for i in range(len(node)):
                key = node[:i] + '_' + node[i + 1:]
                for nei in bucket[key]:
                    if nei not in visited:
                        visited.add(nei)
                        dq.append(nei)
                        parent[nei] = node
        return -1

    def findPath(self, parent, end):
        res = [end]
        node = end
        while node in parent:
            node = parent[end]
            res.append(node)
        return res


b = "hit"
e = "cog"
wordlist = ["hot","dot","dog","lot","log","cog"]
print(Solution().)