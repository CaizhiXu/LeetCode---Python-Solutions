## time, space - O(mn)
from collections import defaultdict


class Solution:
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