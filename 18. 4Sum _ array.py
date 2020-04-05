## time - O(n**3), space - O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                tmp = target - nums[i] - nums[j]
                left, right = j+1, n-1
                while left < right:
                    if nums[left]+nums[right] < tmp:
                        left += 1
                    elif nums[left]+nums[right] > tmp:
                        right -= 1
                    else:
                        candidate = [nums[i], nums[j], nums[left], nums[right]]
                        if not res or res[-1] != candidate:
                            res.append(candidate)
                        left += 1
                        right -= 1
        return res