## time - O(nlogn), space - O(n)
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        root = [i for i in range(len(s))]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX

        for start, end in pairs:
            union(start, end)

        res, ch_dict = '', defaultdict(list)
        for i in range(len(s)):
            ch_dict[find(i)].append(s[i])
        for k in ch_dict.keys():
            ch_dict[k].sort(reverse=True)
        for i in range(len(s)):
            res += ch_dict[find(i)].pop()

        return res