## time, space - O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start, end = 0, 0
        pos = {}
        maxLen = 0
        while end < len(s):
            while s[end] in seen:
                maxLen = max(maxLen, end-start)
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            end += 1
        maxLen = max(maxLen, end-start)
        return maxLen