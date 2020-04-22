## time - O(n**2), space - O(n)
from collections import Counter


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        cnts = Counter(ages)

        for i in cnts.keys():
            lower = 0.5 * i + 7
            for j in cnts.keys():
                if not (j <= lower or j > i):
                    if i == j:
                        res += cnts[i] * (cnts[i] - 1)
                    else:
                        res += cnts[i] * cnts[j]

        return res