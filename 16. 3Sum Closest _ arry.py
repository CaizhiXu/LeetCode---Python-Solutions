## time - O(n**2), space - O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<=2:
            return -1
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                tmp = nums[i]+nums[left]+nums[right]
                if abs(tmp-target)<abs(res-target):
                    res = tmp
                if tmp < target:
                    left += 1
                elif tmp > target:
                    right -= 1
                else:
                    return tmp
        return res