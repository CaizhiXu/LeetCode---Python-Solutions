## time, space - O(mn)
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for s in strings:
            key = 0
            for c in s:
                key = 10*key + (ord(c) - ord(s[0]))%26 + 1
            dct[key].append(s)
        res = dct.values()
        return res