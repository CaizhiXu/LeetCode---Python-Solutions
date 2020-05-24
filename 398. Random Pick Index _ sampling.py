import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def pick(self, target: int) -> int:
        res = 0
        index = 1
        for i in range(len(self.arr)):
            if self.arr[i] == target:
                if random.random() < 1/index:
                    res = i
                index += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)