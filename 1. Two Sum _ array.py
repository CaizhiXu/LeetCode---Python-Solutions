## time, space - O(N)
## Caizhi Xu
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre = {}
        for i, num in enumerate(nums):
            if target - num in pre:
                return [pre[target - num], i]
            else:
                pre[num] = i