## time - O(n), space - O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) <= k:
            return len(s)

        window = {}
        cnt, res = 0, 0
        left = 0
        for right, c in enumerate(s):
            if c not in window or window[c] == 0:
                cnt += 1
                window[c] = 0
            window[c] += 1
            if cnt <= k:
                res = max(res, right - left + 1)
            while cnt > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    cnt -= 1
                left += 1
        return res