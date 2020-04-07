## time - O(m*n), space - O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        lh, ln = len(haystack), len(needle)
        for i in range(lh):
            if haystack[i] != needle[0]:
                continue
            j = 0
            while j < ln and j+i< lh:
                if haystack[j+i] == needle[j]:
                    j += 1
                else:
                    break
            if j == ln:
                return i
            elif j + i == lh:
                return -1
        return -1