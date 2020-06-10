## time, space - O(mn)
from collections import deque


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        visited_pac, visited_atl = set(), set()
        dq_pac, dq_atl = deque(), deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    dq_pac.append((i, j))
                    visited_pac.add((i, j))
                if i == len(matrix) - 1 or j == len(matrix[0]) - 1:
                    dq_atl.append((i, j))
                    visited_atl.add((i, j))
        self.bfs(dq_pac, visited_pac, matrix)
        self.bfs(dq_atl, visited_atl, matrix)
        return list(visited_pac & visited_atl)

    def bfs(self, dq, visited, matrix):
        while dq:
            x, y = dq.pop()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) \
                        and (nx, ny) not in visited and matrix[nx][ny] >= matrix[x][y]:
                    visited.add((nx, ny))
                    dq.appendleft((nx, ny))
