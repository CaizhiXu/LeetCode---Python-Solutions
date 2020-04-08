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



## KMP algo
## time - O(m), space - O(n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        lh, ln = len(haystack), len(needle)
        lps = self.get_lps(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        if j == len(needle):
            return i - ln
        else:
            return -1

    def get_lps(self, nums):
        n = len(nums)
        lps = [0] * n
        for j in range(1, n):
            tmp = lps[j - 1]
            while nums[tmp] != nums[j] and tmp > 0:
                tmp = lps[tmp - 1]
            if tmp == 0:
                lps[j] = int(nums[0] == nums[j])
            else:
                lps[j] = tmp + 1
        return lps