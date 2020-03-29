## time, space - O(2**N)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(path, arr):
            if not arr:
                res.append(path)
                return
            for i, num in enumerate(arr):
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                helper(path + [num], arr[:i] + arr[i + 1:])

        nums.sort()
        res = []
        helper([], nums)
        return res


## time, space - O(n!)
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cnts = Counter(nums)
        res = []

        def helper(x, path, length):
            cnts[x] -= 1
            if length == 0:
                res.append(path)
            for y in cnts:
                if cnts[y]:
                    helper(y, path + [y], length - 1)
            cnts[x] += 1

        for x in cnts:
            helper(x, [x], len(nums) - 1)
        return res