## time - O(n), space - O(n)
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = Counter(p)
        cnt = len(window)
        size = len(p)
        left = 0
        res = []

        for right, c in enumerate(s):
            if c in window:
                window[c] -= 1
                if window[c] == 0:
                    cnt -= 1
            if right - left >= size:
                if s[left] in window:
                    window[s[left]] += 1
                    if window[s[left]] == 1:
                        cnt += 1
                left += 1
            if cnt == 0:
                res.append(left)
        return res