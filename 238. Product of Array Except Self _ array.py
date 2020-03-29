# time, space - O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        preProduct = 1
        for i in range(n):
            res[i] = preProduct
            preProduct *= nums[i]
        sufProduct = 1
        for i in range(n-1, -1, -1):
            res[i] *= sufProduct
            sufProduct *= nums[i]
        return res