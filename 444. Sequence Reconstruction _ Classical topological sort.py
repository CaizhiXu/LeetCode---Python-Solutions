from collections import defaultdict
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        indegrees = defaultdict(int)
        graph = defaultdict(list)
        nodes = set()

        for arr in seqs:
            nodes |= set(arr)
            for i in range(len(arr)):
                if i == 0:
                    if arr[i] not in indegrees:
                        indegrees[arr[i]] = 0
                if i < len(arr) - 1:
                    graph[arr[i]].append(arr[i + 1])
                    indegrees[arr[i + 1]] += 1

        curr = [node for node in indegrees if indegrees[node] == 0]
        res = []
        while len(curr) == 1:
            first_node = curr.pop()
            res.append(first_node)
            for nei in graph[first_node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    curr.append(nei)

        if len(curr) > 1:
            return False
        return len(res) == len(nodes) and res == org