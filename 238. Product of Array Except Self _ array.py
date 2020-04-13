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


## time - O(n), space - O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        running_product = 1
        for i in range(len(nums) - 2, -1, -1):
            running_product *= nums[i + 1]
            ans[i] = ans[i] * running_product
        return ans