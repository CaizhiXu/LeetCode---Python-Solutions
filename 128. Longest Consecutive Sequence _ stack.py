## time - O(N), space - O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        end_map, start_map = {}, {}
        res = 0
        for num in nums:
            if num in start_map or num in end_map:
                continue
            if num-1 not in start_map and num+1 not in end_map:
                start_map[num] = num
                end_map[num] = num
                res = max(res, 1)
                continue
            if num+1 in end_map:
                val = end_map[num+1]
                del end_map[num+1]
                end_map[num] = val
                start_map[val] = num
                res = max(res, val-num+1)
            if num-1 in start_map:
                val = start_map[num-1]
                del start_map[num-1]
                start_map[num] = val
                end_map[val] = num
                if num in end_map:
                    key, val = start_map[num], end_map[num]
                    del start_map[num]
                    del end_map[num]
                    start_map[val], end_map[key] = key, val
                    num = key
                res = max(res, abs(num-val)+1)
        return res



## based on set, time - O(N), space - O(N)
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        _set = set(nums)
        res = 0
        while _set:
            num = _set.pop()
            count = 1
            temp = num + 1
            while temp in _set:
                count += 1
                _set.remove(temp)
                temp += 1
            temp = num - 1
            while temp in _set:
                count += 1
                _set.remove(temp)
                temp -= 1
            res = max(res, count)
        return res


## union find solution, time - O(N), space - O(N)
class Solution3:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        parent = {i: i for i in range(n)}
        size = {i: 1 for i in range(n)}
        visited = {}

        for i, num in enumerate(nums):
            if num in visited:
                continue
            if num - 1 in visited:
                self.union(i, visited[num - 1], parent, size)
            if num + 1 in visited:
                self.union(i, visited[num + 1], parent, size)
            visited[num] = i
        return max(size.values())

    def find(self, x, parent):
        if x != parent[x]:
            parent[x] = self.find(parent[x], parent)
        return parent[x]

    def union(self, i, j, parent, size):
        rootI = self.find(i, parent)
        rootJ = self.find(j, parent)
        if rootI != rootJ:
            if size[rootI] < size[rootJ]:
                rootI, rootJ = rootJ, rootI
            parent[rootJ] = rootI
            size[rootI] += size[rootJ]