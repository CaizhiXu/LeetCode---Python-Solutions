## time, space - O(n!)
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(list(tiles))

        def helper(string):
            if not string:
                return 0
            cnt = 0
            for i, ch in enumerate(string):
                if i > 0 and string[i] == string[i - 1]:
                    continue
                cnt += 1 + helper(string[:i] + string[i + 1:])
            return cnt

        return helper(tiles)


## time, space - O(n!)
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnts = Counter(tiles)
        res = 0

        def helper(x):
            cnts[x] -= 1
            res = 1
            for y in cnts:
                if cnts[y]:
                    res += helper(y)
            cnts[x] += 1
            return res

        for c in cnts:
            res += helper(c)
        return res