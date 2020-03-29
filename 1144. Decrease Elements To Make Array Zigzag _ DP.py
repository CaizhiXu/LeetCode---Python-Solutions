# time - O(N), space - O(1)
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        even_small, odd_small = 0, 0
        nums = [float("inf")] + nums + [float("inf")]
        for i in range(1, len(nums)-1):
            if i%2 == 1:
                odd_small += max(0, nums[i]-min(nums[i-1], nums[i+1])+1)
            else:
                even_small += max(0, nums[i]-min(nums[i-1], nums[i+1])+1)
        return min(odd_small, even_small)