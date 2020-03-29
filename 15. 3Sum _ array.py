## two pointers, unique solution.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > 0 - nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < 0 - nums[i]:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
        return res

# Hash map
## time, space - O(n**2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            visited = set()
            for j in range(i+1, len(nums)):
                if 0-nums[i]-nums[j] in visited:
                    if not res or [nums[i], 0-nums[i]-nums[j], nums[j]] != res[-1]:
                        res.append([nums[i], 0-nums[i]-nums[j], nums[j]])
                else:
                    visited.add(nums[j])
        return res