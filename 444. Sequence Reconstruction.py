## time - O(mn), space - O(mn)
from collections import defaultdict


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, indegree = defaultdict(list), defaultdict(int)
        nodes = set()

        for seq in seqs:
            nodes |= set(seq)
            if seq:
                indegree[seq[0]] += 0
            for i in range(len(seq) - 1):
                indegree[seq[i + 1]] += 1
                graph[seq[i]].append(seq[i + 1])

        superseq = []
        stack = [node for node in indegree if indegree[node] == 0]
        while len(stack) == 1:
            node = stack.pop()
            superseq.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    stack.append(nei)

        if len(stack) > 1:
            return False
        return len(superseq) == len(nodes) and superseq == org     