## time, space - O(mn)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        for j in range(n):
            if p[j] == '*':
                dp[0][j + 1] = dp[0][j - 1]  # edge case easy to omit

        for i in range(m):
            for j in range(n):
                if p[j] == '*':
                    if p[j - 1] != '.' and p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i + 1][j] or dp[i][j + 1]
                elif p[j] == '.' or p[j] == s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
        return dp[-1][-1]