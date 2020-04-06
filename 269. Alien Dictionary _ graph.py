## time - O(mn), space - O(mn)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c: [] for w in words for c in w}
        indegrees = {c: 0 for w in words for c in w}

        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    graph[first[j]].append(second[j])
                    indegrees[second[j]] += 1
                    break
            if first[j] == second[j] and len(first) > len(second):
                return ""

        res = ''
        stack = [c for c in indegrees if indegrees[c] == 0]
        while stack:
            c = stack.pop()
            res += c
            for nei in graph[c]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    stack.append(nei)
        if len(res) < len(graph):
            return ""
        return res