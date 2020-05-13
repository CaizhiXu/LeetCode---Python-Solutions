## time - O(m**2), space - O(1)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        i, j = 0, 0
        minLen = float('inf')
        start = -1
        while i < len(S):
            if S[i] == T[j]:
                j += 1
                if j == len(T):  ## T is matched in S
                    end = i + 1
                    j -= 1
                    while j >= 0:  ## find minimum window in S
                        while S[i] != T[j]:
                            i -= 1
                        j -= 1
                        i -= 1
                    j += 1
                    i += 1

                    if end - i < minLen:
                        minLen = end - i
                        start = i
            i += 1
        return S[start:start + minLen] if start != -1 else ''