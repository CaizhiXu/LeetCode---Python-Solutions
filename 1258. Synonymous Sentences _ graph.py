from collections import defaultdict, deque


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        for a, b in synonyms:
            graph[a].append(b)
            graph[b].append(a)

        text = text.split(' ')
        res = []
        self.dfs(0, '', res, text, graph)
        return res

    ## time - O(n+a**b), space - O(a**b)
    def dfs(self, idx, path, res, text, graph):
        if idx == len(text):
            res.append(path)
            return
        if path != '':
            path += ' '
        if text[idx] not in graph:
            self.dfs(idx + 1, path + text[idx], res, text, graph)
            return
        syns = self.bfs(text[idx], graph)
        for w in syns:
            self.dfs(idx + 1, path + w, res, text, graph)

    def bfs(self, v, graph):  ## time - O(V+E), space - O(V)
        res, visited = [], set()
        dq = deque()
        dq.append(v)
        visited.add(v)
        while dq:
            node = dq.popleft()
            res.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dq.append(nei)
        return sorted(res)