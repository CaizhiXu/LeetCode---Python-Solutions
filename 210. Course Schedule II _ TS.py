# time, space - O(E+V)
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = {i: 0 for i in range(numCourses)}

        for cour, pre in prerequisites:
            graph[pre].append(cour)
            indegrees[cour] += 1

        res = []
        curr = [i for i in indegrees if indegrees[i] == 0]
        while curr:
            temp = curr.pop()
            res.append(temp)
            for nei in graph[temp]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    curr.append(nei)
        return res if len(res) == numCourses else []