class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        num_dct = {}
        for i, num in enumerate(nums_sorted):
            if num not in num_dct:
                num_dct[num] = i

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = num_dct[nums[i]]
        return res