## time, space - O(mn)
from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])

        dq = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dq.append((i, j, 0))
                    visited.add((i, j))

        while dq:
            i, j, dep = dq.pop()
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited \
                        and rooms[ni][nj] != -1:
                    visited.add((ni, nj))
                    dq.appendleft((ni, nj, dep + 1))
                    if dep + 1 < rooms[ni][nj]:
                        rooms[ni][nj] = dep + 1

        return


## time - O(mn), space - O(mn)
from collections import deque


class Solution2:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        dq = deque()
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dq.append((i, j, 0))

        while dq:
            x, y, dist = dq.pop()
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and \
                        rooms[nx][ny] > dist + 1:
                    rooms[nx][ny] = dist + 1
                    dq.appendleft((nx, ny, dist + 1))
