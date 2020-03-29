## time, space - O(m*2**n)
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[-1] * (1 << n) for _ in range(m + 1)]
        maskToCnt = {0: 0}
        for i in range(1, 1 << n):
            maskToCnt[i] = maskToCnt[i >> 1] + int(i % 2 == 1)

        legal = [0] * m
        for i in range(m):
            temp = 0
            for j in range(n):
                if seats[i][j] == '.':
                    temp += 1 << j
            legal[i] = temp

        dp[0][0] = 0
        for i in range(1, m + 1):
            for j in range(1 << n):
                if (j & legal[i - 1] == j) and not j & (j >> 1):
                    for k in range(1 << n):
                        if not j & (k >> 1) and not (j >> 1) & k and dp[i - 1][k] != -1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][k] + maskToCnt[j])
        return max(dp[m])