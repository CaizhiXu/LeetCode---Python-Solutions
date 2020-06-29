## time - O(nlogn), space - O(n)
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        temp = Counter(S)
        cnts = [(v, k) for k, v in temp.items()]
        cnts.sort(reverse=True)
        res = [[] for _ in range(cnts[0][0])]

        if cnts[0][0] > (len(S) + 1) // 2:
            return ""

        idx = 0
        r = len(res)
        for num, c in cnts:
            i = 0
            while i < num:
                res[idx % r].append(c)
                idx += 1
                i += 1

        for i in range(len(res)):
            res[i] = "".join(res[i])
        return "".join(res)