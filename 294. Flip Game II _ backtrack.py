## time, space - O(2**N)
class Solution:
    def canWin(self, s: str) -> bool:
        memo = {}
        def helper(s):
            if s not in memo:
                for i in range(len(s)-1):
                    if s[i:i+2] == '++' and not helper(s[:i] + '-' + s[i+2:]):
                        memo[s] = True
                        return memo[s]
                memo[s] = False
            return memo[s]
        return helper(s)