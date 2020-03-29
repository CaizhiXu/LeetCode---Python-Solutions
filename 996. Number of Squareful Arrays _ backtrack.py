## time, space - O(n!)
from collections import Counter

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        c = Counter(A)
        self.res = 0

        def helper(num, length):
            c[num] -= 1
            if length == 0:
                self.res += 1
            for nxt in c:
                if c[nxt]:
                    tmp = (num + nxt) ** 0.5
                    if int(tmp) == tmp:
                        helper(nxt, length - 1)
            c[num] += 1

        for num in c:
            helper(num, len(A) - 1)
        return self.res