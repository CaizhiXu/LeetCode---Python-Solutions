## time - O(n), space - O(1)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        if len(t) - len(s) > 1:
            return False

        diff = False
        i, j = 0, 0
        while i < len(s):
            if s[i] != t[j]:
                if diff:
                    return False
                else:
                    diff = True
                    if len(s) < len(t):
                        i -= 1
            i += 1
            j += 1
        if len(s) == len(t):
            return diff
        return True