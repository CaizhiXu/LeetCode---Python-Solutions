## time - O(n), space - O(n)
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnts = Counter(p)
        s_cnts = {}
        left, right = 0, 0
        res = []
        match = 0

        while right < len(s):
            s_cnts[s[right]] = s_cnts.get(s[right], 0) + 1
            if s_cnts[s[right]] == p_cnts[s[right]]:
                match += 1
            while s_cnts[s[right]] > p_cnts[s[right]]:
                s_cnts[s[left]] -= 1
                if s_cnts[s[left]] < p_cnts[s[left]]:
                    match -= 1
                left += 1

            if match == len(p_cnts):
                res.append(left)
                s_cnts[s[left]] -= 1
                match -= 1
                left += 1

            right += 1
        return res