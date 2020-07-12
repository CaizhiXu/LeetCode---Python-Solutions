from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        if not T:
            return ''
        t_cnt = Counter(T)
        res = []

        for c in S:
            if c in t_cnt:
                res.append(c * t_cnt[c])
                t_cnt[c] = 0

        for c in t_cnt:
            if t_cnt[c] != 0:
                res.append(c * t_cnt[c])
                t_cnt[c] = 0
        return ''.join(res)